# S2_FOR_03.py

def sum_until(nums, threshold):
    total = 0
    for n in nums:
        if total + n > threshold:
            break
        total += n
    return total


def main():
    tests = [
        ([1, 2, 3, 4], 6),
        ([5, 5, 5], 9),
        ([10, -3, 2], 7),
        ([], 10),
    ]
    for nums, th in tests:
        print(f"nums={nums!r}, threshold={th} -> {sum_until(nums, th)!r}")


if __name__ == "__main__":
    main()
