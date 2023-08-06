from pathlib import Path

from visual_novel_toolkit.speller.interfaces import Words
from visual_novel_toolkit.speller.words import ConfigWords
from visual_novel_toolkit.speller.words import FileWords


def sort_words(files: list[Path]) -> bool:
    affected = False
    json_files: list[Words] = [ConfigWords(), *[FileWords(path) for path in files]]
    for json_file in json_files:
        dictionary = json_file.loads()
        sorted_dictionary = sorted(set(dictionary))
        if dictionary != sorted_dictionary:
            json_file.dumps(sorted_dictionary)
            affected = True
    return affected
