# S1_VAR_10.py

def inspect(v):
    type_name = type(v).__name__
    is_none = v is None
    is_callable = callable(v)

    try:
        iter(v)
        is_iterable = True
    except TypeError:
        is_iterable = False

    truthy = bool(v)

    return {
        "type_name": type_name,
        "is_none": is_none,
        "is_callable": is_callable,
        "is_iterable": is_iterable,
        "truthy": truthy,
    }


def sample_fn():
    return 123


def main():
    values = [
        0,
        1,
        3.14,
        "",
        "0",
        [],
        [0],
        (),
        {"a": 1},
        {1, 2},
        None,
        sample_fn,
        range(3),
    ]

    for v in values:
        info = inspect(v)
        print(f"value={v!r}")
        for k, val in info.items():
            print(f"  {k}: {val!r}")
        print()


if __name__ == "__main__":
    main()
