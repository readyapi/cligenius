from typing import Optional

import types


def name_callback(ctx: types.Context, value: str):
    if ctx.resilient_parsing:
        return
    print("Validating name")
    if value != "Camila":
        raise types.BadParameter("Only Camila is allowed")
    return value


def main(name: Optional[str] = types.Option(default=None, callback=name_callback)):
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
