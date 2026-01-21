# S1_IF_02.py

def grade(score):
    if not isinstance(score, (int, float)) or isinstance(score, bool):
        return None
    if score < 0 or score > 100:
        return None

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    tests = [59, 60, 69, 70, 89, 90, 100, 101]
    for s in tests:
        print(f"score={s:<3} -> {grade(s)!r}")


if __name__ == "__main__":
    main()
