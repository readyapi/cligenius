from typing import List

import cligenius

app = cligenius.Cligenius()


@app.command()
def main(name: List[str] = cligenius.Option(["World"], help="The name to say hi to.")):
    for each_name in name:
        print(f"Hello {each_name}")


if __name__ == "__main__":
    app()
