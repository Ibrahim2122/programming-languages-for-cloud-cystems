# S1_MC_01.py

def day_name(n: int):
    match n:
        case 1: return "Monday"
        case 2: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"
        case 7: return "Sunday"
        case _: return None


def main():
    for n in [0, 1, 2, 6, 7, 8]:
        print(f"{n} -> {day_name(n)!r}")


if __name__ == "__main__":
    main()
