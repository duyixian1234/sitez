from pathlib import Path

from sitez.io import read_text, write_text


def test_read_text(tmp_path: Path):
    path = tmp_path / "temp.txt"
    path.write_text("Hello, World.")
    assert read_text(str(path)) == "Hello, World."


def test_write_text(tmp_path: Path):
    path = tmp_path / "temp.txt"
    write_text("Hello, World.", str(path))
    assert path.read_text() == "Hello, World."
