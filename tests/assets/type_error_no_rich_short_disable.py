import types
import types.main

types.main.rich = None


app = types.Types(pretty_exceptions_short=False)


@app.command()
def main(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    app()
