# S2_LIST_06.py

def active_names_sorted(users):
    return sorted([u["name"].upper() for u in users if u.get("active")])


def main():
    users = [
        {"id": 1, "name": "Ola", "active": True},
        {"id": 2, "name": "Ala", "active": False},
        {"id": 3, "name": "Zenek", "active": True},
        {"id": 4, "name": "bartek", "active": True},
        {"id": 5, "name": "Ewa", "active": False},
    ]
    print(active_names_sorted(users))


if __name__ == "__main__":
    main()
