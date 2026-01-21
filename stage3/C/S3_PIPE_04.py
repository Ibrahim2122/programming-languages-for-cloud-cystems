# S3_PIPE_04.py

def iter_floats(values):
    for s in values:
        try:
            yield float(s.strip())
        except (ValueError, AttributeError):
            continue


def main():
    raw = [" 1 ", "x", " 2.5", "", None, "3"]
    doubled_sum = 0.0

    for n in iter_floats(raw):   # generator: converts + skips failures
        doubled_sum += (n * 2)   # double then sum

    print("raw:", raw)
    print("sum of doubled floats:", doubled_sum)


if __name__ == "__main__":
    main()
