# S3_PIPE_02.py

def pipe(*fns):
    def run(x):
        for fn in fns:
            x = fn(x)
        return x
    return run


def compose(*fns):
    def run(x):
        for fn in reversed(fns):
            x = fn(x)
        return x
    return run


def main():
    f = lambda x: x + 1
    g = lambda x: x * 2
    h = lambda x: x - 3

    p = pipe(f, g, h)       # h(g(f(x)))
    c = compose(f, g, h)    # f(g(h(x)))

    for n in [0, 1, 10]:
        print(f"x={n}  pipe -> {p(n)}   compose -> {c(n)}")


if __name__ == "__main__":
    main()
