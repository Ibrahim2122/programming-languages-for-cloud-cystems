# S3_DICT_03.py

def pick(d, keys):
    out = {}
    for k in keys:
        if k in d:
            out[k] = d[k]
    return out


def main():
    d = {"a": 1, "b": 2, "c": 3}
    print(pick(d, ["a", "c", "x"]))
    print(pick(d, []))


if __name__ == "__main__":
    main()

# S3_DICT_04.py