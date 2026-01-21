# S1_VAR_02.py

def main():
    # Dynamic typing in practice: a variable name can be rebound to values of different types at runtime.
    x = 10
    print(x, type(x).__name__)

    x = 2.5
    print(x, type(x).__name__)

    x = "hello"
    print(x, type(x).__name__)

    x = [1, 2, 3]
    print(x, type(x).__name__)


if __name__ == "__main__":
    main()
