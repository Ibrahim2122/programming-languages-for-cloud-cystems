# S3_PIPE_06.py

def pipe_safe(*fns):
    def run(x):
        try:
            for fn in fns:
                x = fn(x)
            return {"ok": True, "value": x}
        except Exception as e:
            return {"ok": False, "error": str(e)}
    return run


def main():
    def must_be_int(x):
        if not isinstance(x, int):
            raise ValueError("expected int")
        return x

    safe = pipe_safe(
        must_be_int,
        lambda n: n * 2,
        lambda n: n + 1,
    )

    print(safe(10))
    print(safe("10"))


if __name__ == "__main__":
    main()
