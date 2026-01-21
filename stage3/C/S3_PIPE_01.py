# S3_PIPE_01.py

def pipe(*fns):
    def run(x):
        for fn in fns:
            x = fn(x)
        return x
    return run


def main():
    f = lambda x: x + 1
    g = lambda x: x * 2
    h = lambda x: x - 3

    p = pipe(f, g, h)
    for n in [0, 1, 10]:
        print(f"pipe(f,g,h)({n}) -> {p(n)}")


if __name__ == "__main__":
    main()
