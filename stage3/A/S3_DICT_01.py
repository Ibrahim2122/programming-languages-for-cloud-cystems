# S3_DICT_01.py

def get_path(obj, path, fallback=None):
    if not isinstance(obj, dict) or not isinstance(path, str):
        return fallback

    cur = obj
    for part in path.split("."):
        if not isinstance(cur, dict):
            return fallback
        if part not in cur:
            return fallback
        cur = cur[part]
    return cur


def main():
    data = {"a": {"b": {"c": 123}}, "x": 5}
    tests = [
        ("a.b.c", "NOPE"),
        ("a.b", "NOPE"),
        ("a.b.c.d", "NOPE"),
        ("a.x.c", "NOPE"),
        ("x.y", "NOPE"),
    ]
    for p, fb in tests:
        print(f"path={p!r} -> {get_path(data, p, fb)!r}")


if __name__ == "__main__":
    main()

