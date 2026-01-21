# S2_FOR_04.py

def count_occurrences(values):
    counts = {}
    for v in values:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    return counts


def main():
    tests = [
        ["a", "b", "a", "c", "b", "a"],
        [1, 2, 2, 3, 3, 3],
        [],
    ]
    for t in tests:
        print(f"{t!r} -> {count_occurrences(t)!r}")


if __name__ == "__main__":
    main()
