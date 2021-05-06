from typing import Optional

import toml
from pydantic import BaseSettings, EmailStr


class ProjectSettings(BaseSettings):
    name: str
    author: Optional[str]
    email: Optional[EmailStr]

    @classmethod
    def loads(cls, content: str) -> "ProjectSettings":
        kw = toml.loads(content)
        return cls(**kw)

    def dumps(self) -> str:
        return toml.dumps(self.dict())
