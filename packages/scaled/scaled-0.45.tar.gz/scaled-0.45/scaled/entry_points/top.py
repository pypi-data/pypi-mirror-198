import argparse
import curses
import functools
import json
import logging
from typing import Callable, List

import zmq

from scaled.protocol.python.message import MessageType, PROTOCOL, SchedulerStatus
from scaled.utility.zmq_config import ZMQConfig

SORT_BY_OPTIONS = {
    ord("n"): "worker",
    ord("c"): "cpu",
    ord("m"): "rss",
    ord("f"): "free",
    ord("w"): "working",
    ord("q"): "queued",
}


def get_args():
    parser = argparse.ArgumentParser(
        "poke scheduler for monitoring information", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--timeout", type=int, default=5, help="timeout seconds")
    parser.add_argument("address", help="scheduler address to connect to")
    return parser.parse_args()


def main():
    curses.wrapper(poke)


def poke(screen):
    args = get_args()

    screen.nodelay(1)
    config = {"sort_by": "cpu"}

    try:
        subscribe_status(
            address=ZMQConfig.from_string(args.address),
            callback=functools.partial(show_status, screen=screen, config=config),
            timeout=args.timeout
        )
    except zmq.Again:
        raise TimeoutError(f"Cannot connect to monitoring address {args.address} after {args.timeout} seconds")
    except KeyboardInterrupt:
        pass


def subscribe_status(address: ZMQConfig, callback: Callable[[SchedulerStatus], None], timeout: int):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt(zmq.RCVTIMEO, timeout * 1000)
    socket.connect(address.to_address())
    socket.subscribe("")

    while frames := socket.recv_multipart():
        if len(frames) < 2:
            logging.error(f"received unexpected frames {frames}")
            continue

        if frames[0] not in {member.value for member in MessageType}:
            logging.error(f"received unexpected message type: {frames[0]}")
            return

        message_type_bytes, *payload = frames
        message_type = MessageType(message_type_bytes)
        message = PROTOCOL[message_type_bytes].deserialize(payload)

        if message_type != message_type.SchedulerStatus:
            raise ValueError(f"unknown message type: {message_type}")

        assert isinstance(message, SchedulerStatus)
        callback(message)



def show_status(status: SchedulerStatus, screen, config):
    data = json.loads(status.data)

    option = screen.getch()
    if option in SORT_BY_OPTIONS:
        config["sort_by"] = SORT_BY_OPTIONS[option]

    data["scheduler"]["cpu"] = __format_percentage(data["scheduler"]["cpu"])
    data["scheduler"]["rss"] = __format_bytes(data["scheduler"]["rss"])
    scheduler_table = __generate_keyword_data("scheduler", data["scheduler"])
    task_manager_table = __generate_keyword_data("task_manager", data["task_manager"])
    sent_table = __generate_keyword_data("scheduler_sent", data["binder"]["sent"])
    received_table = __generate_keyword_data("scheduler_received", data["binder"]["received"])
    # client_table = __generate_keyword_data("client_manager", data["client_manager"])
    function_id_to_tasks = __generate_keyword_data(
        "function_id_to_tasks", data["function_manager"]["function_id_to_tasks"], truncate_number=24
    )
    worker_manager_table = __generate_worker_manager_table(
        data["worker_manager"], truncate_number=24, sort_by=config["sort_by"]
    )

    table1 = __merge_tables(scheduler_table, task_manager_table)
    table1 = __merge_tables(table1, sent_table)
    table1 = __merge_tables(table1, received_table)
    # table = __merge_tables(table, client_table)

    table2 = __merge_tables(worker_manager_table, function_id_to_tasks, padding=4)

    screen.clear()
    try:
        new_row = __print_table(screen, 0, table1, padding=2)
    except curses.error:
        __print_too_small(screen)
        return

    try:
        screen.addstr(new_row + 1, 0, "Shortcuts: " + " ".join([f"{v}[{chr(k)}]" for k, v in SORT_BY_OPTIONS.items()]))
        _ = __print_table(screen, new_row + 2, table2)
    except curses.error:
        pass

    screen.refresh()


def __generate_keyword_data(title, data, truncate_number: int = 0):
    table = [[title, ""]]
    if truncate_number:
        table.extend([[f"{k[:-truncate_number]}+", v] for k, v in data.items()])
    else:
        table.extend([[k, v] for k, v in data.items()])
    return table


def __generate_worker_manager_table(wm_data, truncate_number: int, sort_by: str):
    if not wm_data:
        return []

    wm_data = sorted(wm_data, key=lambda item: item[sort_by], reverse=True)

    for row in wm_data:
        row["worker"] = f"{row['worker'][:-truncate_number]}+" if truncate_number else row["worker"]
        row["cpu"] = __format_percentage(row["cpu"])
        row["rss"] = __format_bytes(row["rss"])
        row["free"] = __format_integer(row["free"])
        row["working"] = __format_integer(row["working"])
        row["queued"] = __format_integer(row["queued"])

    worker_manager_table = [[f"*{v}" if v == sort_by else v for v in wm_data[0].keys()]]
    worker_manager_table.extend([list(worker.values()) for worker in wm_data])
    return worker_manager_table


def __print_table(screen, line_number, data, padding=1):
    if not data:
        return

    col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

    for i, header in enumerate(data[0]):
        screen.addstr(line_number, sum(col_widths[:i]) + i + (padding * i), str(header).rjust(col_widths[i]))

    for i, row in enumerate(data[1:], start=1):
        for j, cell in enumerate(row):
            screen.addstr(line_number + i, sum(col_widths[:j]) + j + (padding * j), str(cell).rjust(col_widths[j]))

    return line_number + len(data)


def __format_bytes(number) -> str:
    for unit in ["B", "KiB", "MiB", "GiB", "TiB"]:
        if number >= 1024.0:
            number /= 1024.0
            continue

        return f"{number:.1f} {unit}"


def __format_integer(number):
    return f"{number:,}"


def __format_percentage(number):
    return f"{number:.1%}"


def __merge_tables(left: List[List], right: List[List], padding: int = 0) -> List[List]:
    if not left:
        return right

    if not right:
        return left

    result = []
    for i in range(max(len(left), len(right))):
        if i < len(left):
            left_row = left[i]
        else:
            left_row = [""] * len(left[0])

        if i < len(right):
            right_row = right[i]
        else:
            right_row = [""] * len(right[0])

        if padding:
            padding_column = [" " * padding]
            result.append(left_row + padding_column + right_row)
        else:
            result.append(left_row + right_row)

    return result


def __print_too_small(screen):
    screen.clear()
    screen.addstr(0, 0, "Your terminal is too small to show")
    screen.refresh()
