from typing import Any, Generic, List, TypeVar


class sessionmaker:

    def __init__(self, bind) -> None:
        ...

    def __call__(self) -> Session:
        ...


T = TypeVar('T')


class Query(Generic[T]):

    def filter(self, *criterion) -> Query:
        ...

    def order_by(self, *criterion) -> Query:
        ...

    def offset(self, offset) -> Query:
        ...

    def having(self, *criterion) -> Query:
        ...

    def group_by(self, *criterion) -> Query:
        ...

    def limit(self, *criterion) -> Query:
        ...

    def first(self) -> T:
        ...

    def scalar(self) -> T:
        ...

    def all(self) -> List[T]:
        ...


class Session:

    def add(self, instance) -> None:
        ...

    def query(self, table: T, **kwargs) -> Query[T]:
        ...

    def execute(self, query: str) -> None:
        ...

    bind = ...  # type: Any
