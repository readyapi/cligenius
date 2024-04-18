from enum import Enum
from typing import List

import types
from typing_extensions import Annotated


class Food(str, Enum):
    food_1 = "Eggs"
    food_2 = "Bacon"
    food_3 = "Cheese"


def main(groceries: Annotated[List[Food], types.Option()] = [Food.food_1, Food.food_3]):
    print(f"Buying groceries: {', '.join([f.value for f in groceries])}")


if __name__ == "__main__":
    types.run(main)
