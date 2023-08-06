from typing import Protocol, TypeVar
from typing import Callable

T = TypeVar("T")
U = TypeVar("U")

class Result(Protocol[T]):
    pass

    def get(self) -> T:
        ...
    
    def flatmap(self, func: Callable[[T], "Result[U]"]) -> "Result[U]":
        ...
    
    def map_error(self, func: Callable[[Exception], T]) -> "Result[T]":
        ...
    
    def fold(self, fa: Callable[[Exception], U], fb: Callable[[T], U]) -> U:
        ...
    
    def __bool__(self) -> bool:
        ...

class Success(Result[T]):

    def __init__(self, value: T):
        self._value = value
    
    def get(self) -> T:
        return self._value

    def flatmap(self, func: Callable[[T], "Result[U]"]) -> "Result[U]":
        return func(self._value)

    def map_error(self, _: Callable[[Exception], T]) -> "Result[T]":
        return self

    def fold(self, _: Callable[[Exception], U], fb: Callable[[T], U]) -> U:
        return fb(self._value)

    def __bool__(self) -> bool:
        return True

class Failure(Result[T]):
    
    def __init__(self, exception: Exception):
        self._exception = exception
    
    def get(self) -> T:
        raise self._exception

    def flatmap(self, _: Callable[[T], "Result[U]"]) -> "Result[U]":
        return self

    def map_error(self, func: Callable[[Exception], T]) -> "Result[T]":
        return Failure(func(self._exception))

    def fold(self, fa: Callable[[Exception], U], _: Callable[[T], U]) -> U:
        return fa(self._exception)

    def __bool__(self) -> bool:
        return False
