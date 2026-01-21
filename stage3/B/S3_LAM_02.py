# S3_LAM_02.py

def main():
    people = [
        {"name": "Ola", "age": 30},
        {"name": "Ala", "age": 22},
        {"name": "Zenek", "age": 45},
        {"name": "Bartek", "age": 22},
    ]

    print("before:", people)
    sorted_people = sorted(people, key=lambda p: p["age"])
    print("after: ", sorted_people)


if __name__ == "__main__":
    main()
