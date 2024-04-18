from typing import List

import types
from typing_extensions import Annotated


def main(number: Annotated[List[float], types.Option()] = []):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    types.run(main)
