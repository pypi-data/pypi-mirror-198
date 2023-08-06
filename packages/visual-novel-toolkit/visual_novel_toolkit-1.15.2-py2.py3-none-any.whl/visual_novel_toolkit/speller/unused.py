from pathlib import Path
from string import punctuation

from visual_novel_toolkit.speller.interfaces import Words
from visual_novel_toolkit.speller.words import ConfigWords
from visual_novel_toolkit.speller.words import FileWords


punctuation = punctuation + "“”’…"


def find_unused_words(files: list[Path]) -> bool:
    affected = False
    json_files: list[Words] = [ConfigWords(), *[FileWords(path) for path in files]]
    words_cloud = get_words_cloud()
    for json_file in json_files:
        dictionary = set(json_file.loads())
        unused = dictionary - words_cloud
        if unused:
            json_file.dumps(sorted(dictionary - unused))
            affected = True
    return affected


def get_words_cloud() -> set[str]:
    words_cloud = set()
    docs = Path("docs")
    for md_file in docs.glob("**/*.md"):
        content = md_file.read_text()
        words_cloud |= {
            word.strip(punctuation)
            for token in content.split()
            for word in token.split("-")
        }
    return words_cloud
