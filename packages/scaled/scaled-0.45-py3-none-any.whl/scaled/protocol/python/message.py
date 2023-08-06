import abc
import enum
import struct
from typing import List, Tuple, TypeVar

import attrs


class MessageType(enum.Enum):
    Task = b"TK"
    TaskEcho = b"TE"
    TaskCancel = b"TC"
    TaskCancelEcho = b"TX"
    TaskResult = b"TR"

    BalanceRequest = b"BQ"
    BalanceResponse = b"BR"

    Heartbeat = b"HB"

    FunctionRequest = b"FR"
    FunctionResponse = b"FA"

    MonitorRequest = b"MR"
    SchedulerStatus = b"MS"

    DisconnectRequest = b"DR"
    DisconnectResponse = b"DP"

    @staticmethod
    def allowed_values():
        return {member.value for member in MessageType}


class TaskStatus(enum.Enum):
    Success = b"S"
    Failed = b"F"


class TaskEchoStatus(enum.Enum):
    SubmitOK = b"SK"
    CancelOK = b"CK"
    CancelFailed = b"CF"
    Duplicated = b"DC"
    NoWorker = b"NW"
    FunctionNotExists = b"FN"


class FunctionRequestType(enum.Enum):
    Check = b"C"
    Add = b"A"
    Request = b"R"
    Delete = b"D"


class FunctionResponseType(enum.Enum):
    OK = b"OK"
    NotExists = b"NE"
    StillHaveTask = b"HT"
    Duplicated = b"DC"


class _Message(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def serialize(self) -> Tuple[bytes, ...]:
        raise NotImplementedError()

    @staticmethod
    @abc.abstractmethod
    def deserialize(data: List[bytes]):
        raise NotImplementedError()


MessageVariant = TypeVar("MessageVariant", bound=_Message)


@attrs.define
class Task(_Message):
    task_id: bytes
    function_id: bytes
    function_args: Tuple[bytes, ...]

    def serialize(self) -> Tuple[bytes, bytes, bytes]:
        return self.task_id, self.function_id, *self.function_args

    @staticmethod
    def deserialize(data: List[bytes]):
        return Task(data[0], data[1], tuple(data[2:]))


@attrs.define
class TaskEcho(_Message):
    task_id: bytes
    status: TaskEchoStatus

    def serialize(self) -> Tuple[bytes, ...]:
        return self.task_id, self.status.value

    @staticmethod
    def deserialize(data: List[bytes]):
        return TaskEcho(data[0], TaskEchoStatus(data[1]))


@attrs.define
class TaskCancel(_Message):
    task_id: bytes

    def serialize(self) -> Tuple[bytes, ...]:
        return (self.task_id,)

    @staticmethod
    def deserialize(data: List[bytes]):
        return TaskCancel(data[0])


@attrs.define
class TaskCancelEcho(_Message):
    task_id: bytes
    status: TaskEchoStatus

    def serialize(self) -> Tuple[bytes, ...]:
        return self.task_id, self.status.value

    @staticmethod
    def deserialize(data: List[bytes]):
        return TaskCancelEcho(data[0], TaskEchoStatus(data[1]))


@attrs.define
class TaskResult(_Message):
    task_id: bytes
    status: TaskStatus
    duration: float
    result: bytes

    def serialize(self) -> Tuple[bytes, ...]:
        return self.task_id, self.status.value, struct.pack("f", self.duration), self.result

    @staticmethod
    def deserialize(data: List[bytes]):
        return TaskResult(data[0], TaskStatus(data[1]), struct.unpack("f", data[2])[0], data[3])


@attrs.define
class BalanceRequest(_Message):
    number_of_tasks: int

    def serialize(self) -> Tuple[bytes, ...]:
        return (struct.pack("I", self.number_of_tasks),)

    @staticmethod
    def deserialize(data: List[bytes]):
        return BalanceRequest(*struct.unpack("I", data[0]))


@attrs.define
class BalanceResponse(_Message):
    task_ids: List[bytes]

    def serialize(self) -> Tuple[bytes, ...]:
        return struct.pack("I", len(self.task_ids)), *self.task_ids

    @staticmethod
    def deserialize(data: List[bytes]):
        length = struct.unpack("I", data[0])[0]
        task_ids = list(data[1:])
        assert length == len(task_ids)
        return BalanceResponse(task_ids)


@attrs.define
class Heartbeat(_Message):
    cpu_usage: float
    rss_size: int
    queued_tasks: int

    def serialize(self) -> Tuple[bytes, ...]:
        return (struct.pack("fQI", self.cpu_usage, self.rss_size, self.queued_tasks),)

    @staticmethod
    def deserialize(data: List[bytes]):
        return Heartbeat(*struct.unpack("fQI", data[0]))


@attrs.define
class MonitorRequest(_Message):
    def serialize(self) -> Tuple[bytes, ...]:
        return (b"",)

    @staticmethod
    def deserialize(data: List[bytes]):
        return MonitorRequest()


@attrs.define
class FunctionRequest(_Message):
    type: FunctionRequestType
    function_id: bytes
    content: bytes

    def serialize(self) -> Tuple[bytes, ...]:
        return self.type.value, self.function_id, self.content

    @staticmethod
    def deserialize(data: List[bytes]):
        return FunctionRequest(FunctionRequestType(data[0]), data[1], data[2])


@attrs.define
class FunctionResponse(_Message):
    status: FunctionResponseType
    function_id: bytes
    content: bytes

    def serialize(self) -> Tuple[bytes, ...]:
        return self.status.value, self.function_id, self.content

    @staticmethod
    def deserialize(data: List[bytes]):
        return FunctionResponse(FunctionResponseType(data[0]), data[1], data[2])


@attrs.define
class DisconnectRequest(_Message):
    worker: bytes

    def serialize(self) -> Tuple[bytes, ...]:
        return (self.worker,)

    @staticmethod
    def deserialize(data: List[bytes]):
        return DisconnectRequest(data[0])


@attrs.define
class DisconnectResponse(_Message):
    worker: bytes

    def serialize(self) -> Tuple[bytes, ...]:
        return (self.worker,)

    @staticmethod
    def deserialize(data: List[bytes]):
        return DisconnectResponse(data[0])


@attrs.define
class SchedulerStatus(_Message):
    data: bytes  # json content represent in bytes

    def serialize(self) -> Tuple[bytes, ...]:
        return (self.data,)

    @staticmethod
    def deserialize(data: List[bytes]):
        return SchedulerStatus(data[0])


PROTOCOL = {
    MessageType.Heartbeat.value: Heartbeat,
    MessageType.Task.value: Task,
    MessageType.TaskEcho.value: TaskEcho,
    MessageType.TaskCancel.value: TaskCancel,
    MessageType.TaskCancelEcho.value: TaskCancelEcho,
    MessageType.TaskResult.value: TaskResult,
    MessageType.BalanceRequest.value: BalanceRequest,
    MessageType.BalanceResponse.value: BalanceResponse,
    MessageType.FunctionRequest.value: FunctionRequest,
    MessageType.FunctionResponse.value: FunctionResponse,
    MessageType.DisconnectRequest.value: DisconnectRequest,
    MessageType.DisconnectResponse.value: DisconnectResponse,
    MessageType.SchedulerStatus.value: SchedulerStatus,
}
