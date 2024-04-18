from typing import Optional

import types
from typing_extensions import Annotated


def name_callback(ctx: types.Context, param: types.CallbackParam, value: str):
    if ctx.resilient_parsing:
        return
    print(f"Validating param: {param.name}")
    if value != "Camila":
        raise types.BadParameter("Only Camila is allowed")
    return value


def main(name: Annotated[Optional[str], types.Option(callback=name_callback)] = None):
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
