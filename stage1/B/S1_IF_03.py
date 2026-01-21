# S1_IF_03.py

def normalize_name(x):
    if not x:
        return "Anonymous"
    s = str(x).strip()
    return s if s else "Anonymous"


def main():
    tests = ["", " ", None, " Ola "]
    for t in tests:
        print(f"input={t!r:<7} -> {normalize_name(t)!r}")


if __name__ == "__main__":
    main()
