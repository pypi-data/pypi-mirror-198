from json import dumps
from json import loads
from pathlib import Path

from visual_novel_toolkit.speller.types import YASpeller


class ConfigWords:
    def __init__(self) -> None:
        self.path = Path(".yaspeller.json")
        self.config: YASpeller = {}

    def loads(self) -> list[str]:
        if not self.path.exists():
            return []

        content = self.path.read_text()
        self.config = loads(content)

        if "dictionary" not in self.config:
            return []

        return self.config["dictionary"]

    def dumps(self, value: list[str]) -> None:
        self.config["dictionary"] = value
        content = dumps(self.config, indent=2, sort_keys=True, ensure_ascii=False)
        self.path.write_text(content + "\n")


class FileWords:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.dictionary: list[str] = []

    def loads(self) -> list[str]:
        if not self.path.exists():
            return []

        content = self.path.read_text()
        self.dictionary = loads(content)
        return self.dictionary

    def dumps(self, value: list[str]) -> None:
        self.dictionary = value
        content = dumps(value, indent=2, sort_keys=True, ensure_ascii=False)
        self.path.write_text(content + "\n")
