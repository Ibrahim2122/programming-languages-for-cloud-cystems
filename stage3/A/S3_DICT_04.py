# S3_DICT_04.py

def omit(d, keys):
    keys = list(keys)
    out = {}
    for k, v in d.items():
        if k not in keys:
            out[k] = v
    return out


def main():
    d = {"a": 1, "b": 2, "c": 3}
    print(omit(d, ["b"]))
    print(omit(d, ["x", "c"]))


if __name__ == "__main__":
    main()

