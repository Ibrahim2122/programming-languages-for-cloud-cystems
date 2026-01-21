# S3_DICT_06.py

def group_by(items, key):
    grouped = {}
    for item in items:
        if not isinstance(item, dict):
            continue
        val = item.get(key)
        grouped.setdefault(val, []).append(item)
    return grouped


def main():
    items = [
        {"id": 1, "team": "A", "name": "Ola"},
        {"id": 2, "team": "B", "name": "Ala"},
        {"id": 3, "team": "A", "name": "Zenek"},
        {"id": 4, "name": "NoTeam"},
    ]
    print(group_by(items, "team"))


if __name__ == "__main__":
    main()
