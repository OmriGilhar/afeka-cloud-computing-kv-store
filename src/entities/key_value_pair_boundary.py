from typing import Any


class KeyValuePairBoundary:
    def __init__(self, key: str = '', value: Any = None):
        self._key: str = key
        self._value: Any = value

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, key: str) -> None:
        self._key = key

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        self._value = value

    def __str__(self) -> str:
        return f"KeyValuePairBoundary [key={self._key}, value={self._value}]"
