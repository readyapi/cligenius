from typing import Optional

import types


def name_callback(ctx: types.Context, param: types.CallbackParam, value: str):
    if ctx.resilient_parsing:
        return
    print(f"Validating param: {param.name}")
    if value != "Camila":
        raise types.BadParameter("Only Camila is allowed")
    return value


def main(name: Optional[str] = types.Option(default=None, callback=name_callback)):
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
