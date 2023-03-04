from subprocess import Popen
from typing import Any

from paramiko.util import ClosingContextManager

class ProxyCommand(ClosingContextManager):
    cmd: list[str]
    process: Popen[Any]
    timeout: float | None
    def __init__(self, command_line: str) -> None: ...
    def send(self, content: bytes) -> int: ...
    def recv(self, size: int) -> bytes: ...
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def settimeout(self, timeout: float) -> None: ...
