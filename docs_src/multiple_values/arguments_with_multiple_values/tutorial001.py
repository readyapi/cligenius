from pathlib import Path
from typing import List

import types


def main(files: List[Path], celebration: str):
    for path in files:
        if path.is_file():
            print(f"This file exists: {path.name}")
            print(celebration)


if __name__ == "__main__":
    types.run(main)