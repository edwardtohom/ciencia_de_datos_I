from _typeshed import Incomplete
from typing import Any

from ..config import PyPIRCCommand

class register(PyPIRCCommand):
    description: str
    sub_commands: Any
    list_classifiers: int
    strict: int
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def check_metadata(self) -> None: ...
    def classifiers(self) -> None: ...
    def verify_metadata(self) -> None: ...
    def send_metadata(self) -> None: ...
    def build_post_data(self, action): ...
    def post_to_server(self, data, auth: Incomplete | None = ...): ...
