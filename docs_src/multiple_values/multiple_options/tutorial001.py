from typing import List, Optional

import types


def main(user: Optional[List[str]] = types.Option(None)):
    if not user:
        print(f"No provided users (raw input = {user})")
        raise types.Abort()
    for u in user:
        print(f"Processing user: {u}")


if __name__ == "__main__":
    types.run(main)
