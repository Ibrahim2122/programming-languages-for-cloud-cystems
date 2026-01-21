# S3_LAM_05.py

def at_least(min_value):
    return lambda x: x >= min_value


def main():
    nums = [1, 5, 10, 2, 7, 0]
    pred = at_least(5)
    kept = list(filter(pred, nums))

    print("nums:", nums)
    print("kept:", kept)


if __name__ == "__main__":
    main()
