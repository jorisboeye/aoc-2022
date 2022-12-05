def main(path: str) -> int:
    with open(path) as file:
        txt = file.read()
    print(max(sum(map(int, e.strip().split("\n"))) for e in txt.split("\n\n")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main("./day01/input-1.txt"))
