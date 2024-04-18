from typing import Optional

import types


def name_callback(value: str):
    print("Validating name")
    if value != "Camila":
        raise types.BadParameter("Only Camila is allowed")
    return value


def main(name: Optional[str] = types.Option(default=None, callback=name_callback)):
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
