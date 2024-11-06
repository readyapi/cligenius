from __future__ import annotations

import cligenius
from cligenius.testing import CliRunner
from typing_extensions import Annotated

runner = CliRunner()


def test_annotated():
    app = cligenius.Cligenius()

    @app.command()
    def cmd(force: Annotated[bool, cligenius.Option("--force")] = False):
        if force:
            print("Forcing operation")
        else:
            print("Not forcing")

    result = runner.invoke(app)
    assert result.exit_code == 0, result.output
    assert "Not forcing" in result.output

    result = runner.invoke(app, ["--force"])
    assert result.exit_code == 0, result.output
    assert "Forcing operation" in result.output
