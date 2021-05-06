from pathlib import Path


def read_text(raw_path: str) -> str:
    path = Path(raw_path)
    assert path.exists()
    return path.read_text()


def write_text(content: str, raw_path: str) -> None:
    path = Path(raw_path)
    path.write_text(content)
