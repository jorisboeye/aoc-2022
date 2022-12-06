def main(path: str) -> int:
    with open(path) as file:
        print(max(sum(map(int, e.splitlines())) for e in file.read().split("\n\n")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main("./day01/input.txt"))
