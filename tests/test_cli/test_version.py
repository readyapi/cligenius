import subprocess
import sys


def test_script_help():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", "-m", "types", "--version"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Types version:" in result.stdout
