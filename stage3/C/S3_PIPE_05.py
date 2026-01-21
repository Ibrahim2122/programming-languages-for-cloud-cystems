# S3_PIPE_05.py

def parse_line(line: str):
    line = line.strip()
    if ":" not in line:
        return None

    level, rest = line.split(":", 1)
    level = level.strip()
    rest = rest.strip()

    data = {"level": level}
    for part in rest.split():
        if "=" in part:
            k, v = part.split("=", 1)
            data[k] = v
    return data


def main():
    lines = [
        "INFO: user=42 action=login",
        "DEBUG: user=7 action=ping",
        "INFO: user=abc action=login",
        "INFO: action=logout",
        "WARN: user=99 action=oops",
        "INFO user=123 action=login",  # invalid format (no ':')
    ]

    parsed = [parse_line(l) for l in lines]
    info_only = [d for d in parsed if isinstance(d, dict) and d.get("level") == "INFO"]

    user_ids = []
    for d in info_only:
        try:
            user_ids.append(int(d.get("user")))
        except (TypeError, ValueError):
            continue

    print(user_ids)


if __name__ == "__main__":
    main()
