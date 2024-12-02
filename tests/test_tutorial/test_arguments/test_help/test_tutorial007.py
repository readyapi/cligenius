import subprocess
import sys

import cligenius
import cligenius.core
from cligenius.testing import CliRunner

from docs_src.arguments.help import tutorial007 as mod

runner = CliRunner()

app = cligenius.Cligenius()
app.command()(mod.main)


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Say hi to NAME very gently, like Dirk." in result.output
    assert "Arguments" in result.output
    assert "Secondary Arguments" in result.output


def test_call_arg():
    result = runner.invoke(app, ["Camila"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
