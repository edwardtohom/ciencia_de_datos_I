from _typeshed import Incomplete
from typing import Any

log: Any

class Bakery:
    cls: Any
    cache: Any
    def __init__(self, cls_, cache) -> None: ...
    def __call__(self, initial_fn, *args): ...

class BakedQuery:
    steps: Any
    def __init__(self, bakery, initial_fn, args=...) -> None: ...
    @classmethod
    def bakery(cls, size: int = ..., _size_alert: Incomplete | None = ...): ...
    def __iadd__(self, other): ...
    def __add__(self, other): ...
    def add_criteria(self, fn, *args): ...
    def with_criteria(self, fn, *args): ...
    def for_session(self, session): ...
    def __call__(self, session): ...
    def spoil(self, full: bool = ...): ...
    def to_query(self, query_or_session): ...

class Result:
    bq: Any
    session: Any
    def __init__(self, bq, session) -> None: ...
    def params(self, *args, **kw): ...
    def with_post_criteria(self, fn): ...
    def __iter__(self): ...
    def count(self): ...
    def scalar(self): ...
    def first(self): ...
    def one(self): ...
    def one_or_none(self): ...
    def all(self): ...
    def get(self, ident): ...

def bake_lazy_loaders() -> None: ...
def unbake_lazy_loaders() -> None: ...

baked_lazyload: Any
baked_lazyload_all: Any
bakery: Any
