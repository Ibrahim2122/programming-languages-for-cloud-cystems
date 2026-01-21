# S1_MC_02.py

def run_command(cmd):
    match cmd:
        case "start":
            return "STARTED"
        case "stop":
            return "STOPPED"
        case "status":
            return "STATUS_OK"
        case _:
            return "UNKNOWN_COMMAND"


def main():
    tests = ["start", "stop", "status", "restart", "", None]
    for t in tests:
        print(f"{t!r} -> {run_command(t)!r}")


if __name__ == "__main__":
    main()
