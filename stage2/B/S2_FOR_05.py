# S2_FOR_05.py

def main():
    for r in range(1, 11):
        for c in range(1, 11):
            print(f"{r * c:4}", end="")
        print()


if __name__ == "__main__":
    main()
