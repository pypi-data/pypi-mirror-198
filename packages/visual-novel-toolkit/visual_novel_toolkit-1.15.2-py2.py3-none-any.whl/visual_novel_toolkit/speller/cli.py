# mypy: disable-error-code = misc
from asyncio import run
from pathlib import Path

from typer import Argument
from typer import echo
from typer import Exit
from typer import Typer

from visual_novel_toolkit.speller.check import check_words
from visual_novel_toolkit.speller.exceptions import SpellerError
from visual_novel_toolkit.speller.proofread import proofread_words
from visual_novel_toolkit.speller.sort import sort_words
from visual_novel_toolkit.speller.unused import find_unused_words


speller = Typer()


is_argument = Argument(None)


@speller.command()
def sort(files: list[Path] = is_argument) -> None:
    if sort_words(files):
        raise Exit(code=1)


@speller.command()
def unused(files: list[Path] = is_argument) -> None:
    if find_unused_words(files):
        raise Exit(code=1)


@speller.command()
def proofread() -> None:
    run(proofread_words())


@speller.command()
def check() -> None:
    try:
        if check_words():
            raise Exit(code=1)
    except SpellerError as error:
        echo(error)
        raise Exit(code=1)
