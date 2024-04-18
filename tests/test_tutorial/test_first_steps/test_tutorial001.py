import subprocess
import sys

import types
from types.testing import CliRunner

from docs_src.first_steps import tutorial001 as mod

runner = CliRunner()


def test_cli():
    app = types.Types()
    app.command()(mod.main)
    result = runner.invoke(app, [])
    assert result.output == "Hello World\n"


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
