from typing import List

import types


def main(number: List[float] = types.Option([])):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    types.run(main)
