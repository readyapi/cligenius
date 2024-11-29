import cligenius
import pytest
from cligenius.testing import CliRunner

runner = CliRunner()


def test_warns_when_callback_is_not_supported():
    app = cligenius.Cligenius()

    sub_app = cligenius.Cligenius()

    @sub_app.callback()
    def callback():
        """This help text is not used."""

    app.add_cligenius(sub_app)

    with pytest.warns(
        match="The 'callback' parameter is not supported by Cligenius when using `add_cligenius` without a name"
    ):
        try:
            app()
        except SystemExit:
            pass


def test_warns_when_callback_is_not_supported_added_after_add_cligenius():
    app = cligenius.Cligenius()

    sub_app = cligenius.Cligenius()
    app.add_cligenius(sub_app)

    @sub_app.callback()
    def callback():
        """This help text is not used."""

    with pytest.warns(
        match="The 'callback' parameter is not supported by Cligenius when using `add_cligenius` without a name"
    ):
        try:
            app()
        except SystemExit:
            pass
