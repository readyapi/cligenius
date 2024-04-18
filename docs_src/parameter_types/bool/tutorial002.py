from typing import Optional

import types


def main(accept: Optional[bool] = types.Option(None, "--accept/--reject")):
    if accept is None:
        print("I don't know what you want yet")
    elif accept:
        print("Accepting!")
    else:
        print("Rejecting!")


if __name__ == "__main__":
    types.run(main)
