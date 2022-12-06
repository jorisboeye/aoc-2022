from pathlib import Path

import pytest

FILE = Path(__file__)
TEST_RESULT = 15
TEST_INPUT = """\
A Y
B X
C Z
"""

SHAPES = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
SHAPE_SCORE = {"Rock": 1, "Paper": 2, "Scissors": 3}
BEATS = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}


def score(_round: str) -> int:
    villain, hero = (SHAPES[x] for x in _round.split())
    if villain == hero:
        score = 3
    elif BEATS[hero] == villain:
        score = 6
    else:
        score = 0
    return score + SHAPE_SCORE[hero]


def solve(puzzle_input: str) -> int:
    return sum(score(x) for x in puzzle_input.splitlines())


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
