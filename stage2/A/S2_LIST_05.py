# S2_LIST_05.py

def stats(nums):
    if not nums:
        return None

    total = 0
    mn = nums[0]
    mx = nums[0]
    for n in nums:
        total += n
        if n < mn:
            mn = n
        if n > mx:
            mx = n

    return {
        "min": mn,
        "max": mx,
        "avg": total / len(nums),
        "sum": total,
    }


def main():
    tests = [
        [1, 2, 3, 4],
        [-5, -1, -10, 0, 2],
        [],
    ]
    for t in tests:
        print(f"{t!r} -> {stats(t)!r}")


if __name__ == "__main__":
    main()
