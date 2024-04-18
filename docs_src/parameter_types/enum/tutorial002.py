from enum import Enum

import types


class NeuralNetwork(str, Enum):
    simple = "simple"
    conv = "conv"
    lstm = "lstm"


def main(
    network: NeuralNetwork = types.Option(NeuralNetwork.simple, case_sensitive=False),
):
    print(f"Training neural network of type: {network.value}")


if __name__ == "__main__":
    types.run(main)
