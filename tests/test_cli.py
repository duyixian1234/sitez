from pathlib import Path

import pytest
from typer.testing import CliRunner

from sitez.cli import app


@pytest.fixture
def runner():
    yield CliRunner()


def test_version(runner: CliRunner):
    result = runner.invoke(app, "version")
    assert result.exit_code == 0
    assert result.stdout == "Sitez version: 0.1.0\n"


def test_init(runner: CliRunner, tmp_path: Path):

    result = runner.invoke(app, ["init", str(tmp_path)])
    assert result.exit_code == 0
    assert result.stdout == f"Init sitez project at {tmp_path}\n"
    assert (tmp_path / "sitez.toml").read_text() == 'name = "My Site"\n'
