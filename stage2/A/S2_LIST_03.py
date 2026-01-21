# S2_LIST_03.py

def chunk(lst, size):
    if size <= 0:
        return None
    out = []
    for i in range(0, len(lst), size):
        out.append(lst[i:i + size])
    return out


def main():
    tests = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 3),
        ([], 3),
        ([1, 2], 0),
    ]
    for lst, size in tests:
        print(f"lst={lst!r}, size={size} -> {chunk(lst, size)!r}")


if __name__ == "__main__":
    main()
