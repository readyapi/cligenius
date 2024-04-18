import time

import types


def main():
    total = 0
    with types.progressbar(range(100), label="Processing") as progress:
        for value in progress:
            # Fake processing time
            time.sleep(0.01)
            total += 1
    print(f"Processed {total} things.")


if __name__ == "__main__":
    types.run(main)
