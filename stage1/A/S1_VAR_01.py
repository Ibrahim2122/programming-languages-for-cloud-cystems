# S1_VAR_01.py

def sample_function():
    return "hello"


def main():
    values = {
        "an_int": 42,
        "a_float": 3.14,
        "a_str": "Python",
        "a_bool": True,
        "a_none": None,
        "a_list": [1, 2, 3],
        "a_tuple": (1, 2, 3),
        "a_dict": {"x": 1, "y": 2},
        "a_set": {1, 2, 3},
        "a_function": sample_function,
    }

    headers = ("name", "value", "type(x)", "type(x).__name__")
    rows = []
    for name, val in values.items():
        rows.append((name, repr(val), str(type(val)), type(val).__name__))

    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))

    def fmt_row(row):
        return " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))

    print(fmt_row(headers))
    print("-+-".join("-" * w for w in col_widths))
    for row in rows:
        print(fmt_row(row))


if __name__ == "__main__":
    main()
