# S3_LAM_06.py

def map_values(d, fn):
    return {k: fn(v) for k, v in d.items()}


def main():
    d = {"a": 1, "b": 2, "c": 3}
    doubled = map_values(d, lambda v: v * 2)
    as_str = map_values(d, lambda v: f"v={v}")

    print("original:", d)
    print("doubled: ", doubled)
    print("as_str:  ", as_str)


if __name__ == "__main__":
    main()
