import types
from typing_extensions import Annotated


def main(
    project_name: Annotated[str, types.Option(prompt=True, confirmation_prompt=True)],
):
    print(f"Deleting project {project_name}")


if __name__ == "__main__":
    types.run(main)
