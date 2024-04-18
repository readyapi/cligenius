import types
from types.testing import CliRunner

from .main import main

app = types.Types()
app.command()(main)

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["--name", "Camila"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.stdout
