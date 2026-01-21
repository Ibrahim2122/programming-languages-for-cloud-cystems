# S1_VAR_03.py

def main():
    lst = [1, 2, 3]
    lst[1] = 99
    print("lst after modification:", lst)

    tup = (1, 2, 3)
    try:
        tup[1] = 99  # type: ignore[misc]
    except TypeError as e:
        print("tuple modification error:", e)

    # Lists are mutable (their contents can change), while tuples are immutable (their contents cannot be reassigned).
    # So item assignment works for lists but raises TypeError for tuples.


if __name__ == "__main__":
    main()
