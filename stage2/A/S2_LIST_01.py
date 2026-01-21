# S2_LIST_01.py

def clean_numbers(values):
    out = []
    for s in values:
        try:
            out.append(float(s.strip()))
        except (ValueError, AttributeError):
            pass
    return out


def main():
    tests = [
        [" 1 ", "x", "2"],
        [" 3.5", " -2 ", "nan", "oops", ""],
    ]
    for t in tests:
        print(f"{t!r} -> {clean_numbers(t)!r}")


if __name__ == "__main__":
    main()
