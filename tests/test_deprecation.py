from typing import Optional

import cligenius
import pytest
from cligenius.testing import CliRunner

runner = CliRunner()


def test_deprecation():
    app = cligenius.Cligenius()

    def add_command():
        @app.command()
        def cmd(
            opt: Optional[float] = cligenius.Option(
                3.14,
                is_flag=True,
                flag_value="42",
                help="Some wonderful number",
            ),
        ): ...  # pragma: no cover

    with pytest.warns(
        match="The 'is_flag' and 'flag_value' parameters are not supported by Cligenius"
    ):
        add_command()
