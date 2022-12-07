from pathlib import Path
from typing import Iterable, Protocol, Union

import pytest

FILE = Path(__file__)
TEST_RESULT = 95437
TEST_INPUT = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class Content(Protocol):
    @property
    def size(self) -> int:
        ...


class Directory:
    def __init__(
        self, name: str, parent: Union["Directory", None], contents: list[Content]
    ):
        self.name = name
        self.parent = parent
        self.contents = contents

    @property
    def size(self) -> int:
        return sum(c.size for c in self.contents)

    @property
    def subdirectories(self) -> Iterable["Directory"]:
        for content in self.contents:
            if isinstance(content, self.__class__):
                yield content

    @property
    def path(self) -> str:
        if self.parent is None:
            return self.name
        else:
            return self.parent.path + "/" + self.name

    def __repr__(self) -> str:
        return self.path


class File:
    def __init__(self, name: str, size: int, directory: Directory):
        self.name = name
        self.size = size
        self.directory = directory

    @property
    def path(self) -> str:
        return self.directory.path + "/" + self.name


class FileSystem:
    def __init__(self) -> None:
        root = Directory(name="/", parent=None, contents=[])
        self.directory: Directory = root
        self.directories: list[Directory] = [root]

    def cd(self, location: str) -> None:
        if location == "..":
            if self.directory.parent is None:
                raise ValueError(f"Directory {self.directory} has no parent.")
            self.directory = self.directory.parent
        elif location == self.directory.path:
            pass
        else:
            self.directory = next(
                c for c in self.directory.subdirectories if c.name == location
            )


def solve(puzzle_input: str) -> int:
    fs = FileSystem()
    for command in puzzle_input.split("$ "):
        if command.startswith("ls"):
            for line in command.splitlines()[1:]:
                a, name = line.split()
                if a == "dir":
                    directory = Directory(name=name, parent=fs.directory, contents=[])
                    fs.directory.contents.append(directory)
                    fs.directories.append(directory)
                else:
                    fs.directory.contents.append(
                        File(name=name, size=int(a), directory=fs.directory)
                    )
        elif command:
            _, location = command.strip().split()
            fs.cd(location=location)
    return sum(d.size for d in fs.directories if d.size <= 100000)


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT, TEST_RESULT),),
)
def test(test_input: str, expected: int) -> None:
    assert solve(test_input) == expected


if __name__ == "__main__":
    test_answer = solve(puzzle_input=TEST_INPUT)
    print(test_answer)
    if test_answer == TEST_RESULT:
        with open(FILE.parent / "input.txt") as file:
            answer = solve(puzzle_input=file.read())
        print(answer)
