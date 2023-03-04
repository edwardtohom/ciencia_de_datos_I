from collections.abc import Iterable, Sequence
from socket import AddressFamily
from typing_extensions import Literal

from netaddr.core import INET_PTON as INET_PTON, ZEROFILL as ZEROFILL

width: Literal[32]
word_size: Literal[8]
word_fmt: Literal["%d"]
word_sep: Literal["."]
family: Literal[AddressFamily.AF_INET]
family_name: Literal["IPv4"]
version: Literal[4]
word_base: Literal[10]
max_int: int
num_words: Literal[4]
max_word: int
prefix_to_netmask: dict[int, int]
netmask_to_prefix: dict[int, int]
prefix_to_hostmask: dict[int, int]
hostmask_to_prefix: dict[int, int]

def valid_str(addr: str, flags: int = ...) -> bool: ...
def str_to_int(addr: str, flags: int = ...) -> int: ...
def int_to_str(int_val: int, dialect: object | None = ...) -> str: ...
def int_to_arpa(int_val: int) -> str: ...
def int_to_packed(int_val: int) -> bytes: ...
def packed_to_int(packed_int: bytes) -> int: ...
def valid_words(words: Iterable[int]) -> bool: ...
def int_to_words(int_val: int) -> tuple[int, ...]: ...
def words_to_int(words: Sequence[int]) -> int: ...
def valid_bits(bits: str) -> bool: ...
def bits_to_int(bits: str) -> int: ...
def int_to_bits(int_val: int, word_sep: str | None = ...) -> str: ...
def valid_bin(bin_val: str) -> bool: ...
def int_to_bin(int_val: int) -> str: ...
def bin_to_int(bin_val: str) -> int: ...
def expand_partial_address(addr: str) -> str: ...
