# S2_LIST_02.py

def unique(values):
    out = []
    for v in values:
        if v not in out:
            out.append(v)
    return out


def main():
    tests = [
        [1, 2, 1, 3, 2, 4, 4],
        ["a", "b", "a", "a", "c"],
        [],
    ]
    for t in tests:
        print(f"{t!r} -> {unique(t)!r}")


if __name__ == "__main__":
    main()
