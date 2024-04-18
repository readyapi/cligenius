from typing import Optional

import types

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise types.Exit()


def name_callback(name: str):
    if name != "Camila":
        raise types.BadParameter("Only Camila is allowed")


def main(
    name: str = types.Option(..., callback=name_callback),
    version: Optional[bool] = types.Option(
        None, "--version", callback=version_callback
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
