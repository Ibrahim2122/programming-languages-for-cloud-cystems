# S2_FOR_02.py

def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None


def main():
    tests = [
        [1, 3, 5, 7],
        [1, 3, 4, 6],
        [],
        [2],
    ]
    for t in tests:
        print(f"{t!r} -> {find_first_even(t)!r}")


if __name__ == "__main__":
    main()
