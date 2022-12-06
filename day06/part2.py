from collections import deque
from pathlib import Path

import pytest

FILE = Path(__file__)
TEST_RESULT = 29
TEST_INPUT = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""


def solve(puzzle_input: str) -> int:
    message = deque["str"]([], maxlen=14)
    for idx, c in enumerate(puzzle_input):
        message += c
        if len(message) == 14 == len(set(message)):
            return idx + 1
    return 0


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
