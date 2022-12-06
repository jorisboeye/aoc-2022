from pathlib import Path

import pytest

FILE = Path(__file__)
TEST_RESULT = 12
TEST_INPUT = """\
A Y
B X
C Z
"""

SHAPES = {"A": "Rock", "B": "Paper", "C": "Scissors"}
SHAPE_SCORE = {"Rock": 1, "Paper": 2, "Scissors": 3}
BEATS = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
WINS = {v: k for k, v in BEATS.items()}


def score(_round: str) -> int:
    villain, result = _round.split()
    villain = SHAPES[villain]
    if result == "Y":
        return 3 + SHAPE_SCORE[villain]
    elif result == "X":
        return 0 + SHAPE_SCORE[BEATS[villain]]
    else:
        return 6 + SHAPE_SCORE[WINS[villain]]


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
