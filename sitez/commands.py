from pathlib import Path

from .config import ProjectSettings


def init_project(raw_path: str):
    path = Path(raw_path) / "sitez.toml"
    if path.exists():
        raise ValueError(f"{path} exists.")
    settings = ProjectSettings(name="My Site")
    text = settings.dumps()
    path.write_text(text)
