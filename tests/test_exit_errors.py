import errno

import types
import types.completion
from types.testing import CliRunner

runner = CliRunner()


def test_eoferror():
    # Mainly for coverage/completeness
    app = types.Types()

    @app.command()
    def main():
        raise EOFError()

    result = runner.invoke(app)
    assert result.exit_code == 1


def test_oserror():
    # Mainly for coverage/completeness
    app = types.Types()

    @app.command()
    def main():
        e = OSError()
        e.errno = errno.EPIPE
        raise e

    result = runner.invoke(app)
    assert result.exit_code == 1


def test_oserror_no_epipe():
    # Mainly for coverage/completeness
    app = types.Types()

    @app.command()
    def main():
        raise OSError()

    result = runner.invoke(app)
    assert result.exit_code == 1
