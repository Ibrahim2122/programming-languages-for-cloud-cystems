# S1_VAR_04.py

def main():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print("a == b:", a == b)  # same contents
    print("a is b:", a is b)  # different objects

    c = a
    print("a == c:", a == c)
    print("a is c:", a is c)  # same object

    x = None
    print("x is None:", x is None)     # correct None check
    print("x == None:", x == None)     # works, but not the recommended style

    # Use is for identity, == for equality.


if __name__ == "__main__":
    main()
