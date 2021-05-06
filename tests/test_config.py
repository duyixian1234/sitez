import pytest

from sitez.config import ProjectSettings


@pytest.fixture
def settings():
    yield ProjectSettings(name="site", author="author", email="author@example.com")


@pytest.fixture
def raw_toml():
    yield 'name = "site"\nauthor = "author"\nemail = "author@example.com"\n'


def test_dumps(settings: ProjectSettings, raw_toml: str) -> None:
    assert settings.dumps() == raw_toml
