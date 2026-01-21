# S1_MC_03.py

def calc(a, op, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        return None
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        return None

    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return None
            return a / b
        case _:
            return None


def main():
    tests = [
        (2, "+", 3),
        (2, "-", 3),
        (2, "*", 3),
        (6, "/", 2),
        (6, "/", 0),
        ("2", "+", 3),
        (2, "?", 3),
    ]
    for a, op, b in tests:
        print(f"{a!r} {op} {b!r} -> {calc(a, op, b)!r}")


if __name__ == "__main__":
    main()
