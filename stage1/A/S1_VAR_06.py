# S1_VAR_06.py

def to_int_or_none(s):
    if s is None:
        return None
    try:
        return int(s)
    except (ValueError, TypeError):
        return None


def main():
    tests = ["12", " 12 ", "12x", "", None]
    for t in tests:
        print(f"input={t!r:<6} -> {to_int_or_none(t)!r}")


if __name__ == "__main__":
    main()
