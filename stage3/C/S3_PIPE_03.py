# S3_PIPE_03.py

import re

def pipe(*fns):
    def run(x):
        for fn in fns:
            x = fn(x)
        return x
    return run


def collapse_spaces(s: str) -> str:
    return re.sub(r"\s+", " ", s)


def main():
    normalize = pipe(
        lambda s: s.strip(),
        lambda s: s.lower(),
        collapse_spaces,
    )

    text = " Ala Ma   Kota "
    print(normalize(text))


if __name__ == "__main__":
    main()
