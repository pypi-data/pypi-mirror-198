from typing import Protocol


class Words(Protocol):
    def loads(self) -> list[str]:
        raise RuntimeError

    def dumps(self, value: list[str]) -> None:
        raise RuntimeError
