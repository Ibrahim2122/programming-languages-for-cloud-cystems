# S2_FOR_06.py

def sum_nested(matrix):
    total = 0
    for row in matrix:
        if not isinstance(row, list):
            return None
        for n in row:
            total += n
    return total


def main():
    tests = [
        [[1, 2], [3, 4], [5]],
        [[-1, 1], [10]],
        [],
        [1, [2, 3]],  # invalid: first "row" isn't a list
    ]
    for t in tests:
        print(f"{t!r} -> {sum_nested(t)!r}")


if __name__ == "__main__":
    main()
