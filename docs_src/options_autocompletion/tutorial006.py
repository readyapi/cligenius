from typing import List

import types

app = types.Types()


@app.command()
def main(name: List[str] = types.Option(["World"], help="The name to say hi to.")):
    for each_name in name:
        print(f"Hello {each_name}")


if __name__ == "__main__":
    app()
