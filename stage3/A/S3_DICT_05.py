# S3_DICT_05.py

def invert(d):
    out = {}
    for k, v in d.items():
        if v in out:
            if isinstance(out[v], list):
                out[v].append(k)
            else:
                out[v] = [out[v], k]
        else:
            out[v] = k
    return out


def main():
    d = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    print(invert(d))


if __name__ == "__main__":
    main()

