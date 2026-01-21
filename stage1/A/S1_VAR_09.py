# S1_VAR_09.py

def add(a: int, b: int) -> int:
    return a + b


def main():
    print("add(2, 3) =", add(2, 3))

    result = add("2", "3")  # type: ignore[arg-type]
    print('add("2", "3") =', result)

    # Type hints are for tooling/readability, not automatic runtime checks.


if __name__ == "__main__":
    main()
