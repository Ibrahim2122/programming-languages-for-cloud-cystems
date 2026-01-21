# index.py

def eq(actual, expected):
    if actual != expected:
        raise AssertionError(f"Expected {expected!r}, got {actual!r}")


def main():
    print("It works")


if __name__ == "__main__":
    main()
