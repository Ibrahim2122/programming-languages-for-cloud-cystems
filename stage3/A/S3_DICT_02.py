# S3_DICT_02.py

def merge_defaults(defaults, overrides):
    return {**defaults, **overrides}


def main():
    defaults = {"timeout": 10, "retries": 3, "cfg": {"mode": "safe", "level": 1}}
    overrides = {"timeout": 5, "cfg": {"level": 99}}

    merged = merge_defaults(defaults, overrides)
    print("merged:", merged)

    # Shallow merge example: nested dict is replaced, not merged key-by-key.
    # Notice cfg.mode is lost because overrides["cfg"] replaces defaults["cfg"] entirely.
    print("cfg in merged:", merged["cfg"])


if __name__ == "__main__":
    main()

