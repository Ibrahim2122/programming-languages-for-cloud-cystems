# S1_VAR_05.py

def is_truthy(v):
    return bool(v)


def main():
    tests = [
        0,
        1,
        "",
        "0",
        [],
        [0],
        {},
        None,
    ]

    for v in tests:
        print(f"value={v!r:<8} type={type(v).__name__:<8} truthy={is_truthy(v)}")


if __name__ == "__main__":
    main()
