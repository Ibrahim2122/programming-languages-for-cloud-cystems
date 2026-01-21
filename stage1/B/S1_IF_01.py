# S1_IF_01.py

def shipping_cost(weight_kg, is_member):
    if not isinstance(weight_kg, (int, float)) or isinstance(weight_kg, bool):
        return None
    if weight_kg <= 0:
        return None

    if weight_kg <= 1:
        cost = 10
    elif weight_kg <= 5:
        cost = 20
    else:
        cost = 30

    if is_member:
        cost *= 0.8

    return cost


def main():
    tests = [
        (0, False),
        (-1, True),
        ("2", False),
        (1, False),
        (1, True),
        (5, False),
        (5, True),
        (5.01, False),
    ]
    for w, m in tests:
        print(f"weight={w!r:<6} member={m!s:<5} -> {shipping_cost(w, m)!r}")


if __name__ == "__main__":
    main()
