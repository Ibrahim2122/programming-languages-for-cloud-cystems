# S3_LAM_03.py

def make_adder(x):
    return lambda n: n + x


def main():
    add10 = make_adder(10)
    add3 = make_adder(3)

    print("add10:", add10(0), add10(5), add10(-2))
    print("add3: ", add3(0), add3(5), add3(-2))


if __name__ == "__main__":
    main()
