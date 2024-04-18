from typing import Optional

import types


def main(name: Optional[str] = types.Argument(default=None)):
    if name is None:
        print("Hello World!")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
