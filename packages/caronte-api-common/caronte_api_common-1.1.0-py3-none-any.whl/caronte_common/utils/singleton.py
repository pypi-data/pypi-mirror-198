from threading import Lock
from typing import Any, Dict, Generic, TypeVar

T = TypeVar("T")


class Singleton(Generic[T]):
    instances: Dict[str, T] = {}
    _lock: Lock = Lock()

    def __init__(self, callable: Any):  # pylint: disable=W0622
        self.callable = callable

    def __call__(self, *args: Any, **kwargs: Any) -> T:
        with self._lock:
            try:
                instance = self.instances[self.callable.__name__]
            except KeyError:
                instance = self.callable(*args, **kwargs)
                self.instances.update({self.callable.__name__: instance})
            return instance
