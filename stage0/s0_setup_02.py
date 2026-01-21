from pathlib import Path

base = Path(".")

structure = {
    "stage1": {
        "A": [f"S1_VAR_{i:02d}.py" for i in range(1, 11)],
        "B": [f"S1_IF_{i:02d}.py" for i in range(1, 4)],
        "C": [f"S1_MC_{i:02d}.py" for i in range(1, 4)],
    },
    "stage2": {
        "A": [f"S2_LIST_{i:02d}.py" for i in range(1, 7)],
        "B": [f"S2_FOR_{i:02d}.py" for i in range(1, 7)],
        "C": [],  # reserved
    },
    "stage3": {
        "A": [f"S3_DICT_{i:02d}.py" for i in range(1, 7)],
        "B": [f"S3_LAM_{i:02d}.py" for i in range(1, 7)],
        "C": [f"S3_PIPE_{i:02d}.py" for i in range(1, 7)],
    },
}

for stage, groups in structure.items():
    for group, files in groups.items():
        folder = base / stage / group
        folder.mkdir(parents=True, exist_ok=True)
        for filename in files:
            (folder / filename).touch(exist_ok=True)
