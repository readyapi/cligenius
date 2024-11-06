import os
import subprocess
import sys

from cligenius.testing import CliRunner

from docs_src.options_autocompletion import tutorial003 as mod

runner = CliRunner()


def test_completion_zsh():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL003.PY_COMPLETE": "complete_zsh",
            "_CLIGENIUS_COMPLETE_ARGS": "tutorial003.py --name Sul",
        },
    )
    assert "Camila" not in result.stdout
    assert "Carlos" not in result.stdout
    assert "Sulaiman" in result.stdout


def test_completion_powershell():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL003.PY_COMPLETE": "complete_powershell",
            "_CLIGENIUS_COMPLETE_ARGS": "tutorial003.py --name Sul",
            "_CLIGENIUS_COMPLETE_WORD_TO_COMPLETE": "Sul",
        },
    )
    assert "Camila" not in result.stdout
    assert "Carlos" not in result.stdout
    assert "Sulaiman" in result.stdout


def test_1():
    result = runner.invoke(mod.app, ["--name", "Camila"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
