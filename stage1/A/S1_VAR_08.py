# S1_VAR_08.py

def main():
    big_int = 10**100
    print("big_int type:", type(big_int).__name__)
    print("big_int digits:", len(str(big_int)))

    big_float = float(big_int)
    print("big_float type:", type(big_float).__name__)
    print("big_float value:", big_float)

    # Floats have limited precision (about 16 decimal digits), so very large integers can't be represented exactly as float.
    # You can see this by converting the float back to int and comparing (it often won't match).
    print("int(big_float) == big_int:", int(big_float) == big_int)


if __name__ == "__main__":
    main()
