from _future_ import annotations
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel

class ModelConfig(BaseModel):
    name: str = Field(default="gpt-4o-mini")
    temperature: float = Field(default=0.4)
    top_p: float = Field(default=0.9)
    max_output_tokens: int = Field(default=1000)


class DebuggingAppConfig(BaseModel):
    explanation_language: str = Field(default="en")
    max_code_chars: int = Field(default=1000)


class AppConfig(BaseModel):
    model: ModelConfig
    debuggingApp: DebuggingAppConfig


def load_config(path: Optional[Path | str] = None) -> AppConfig:
    if path is None:
        root_dir = Path(__file__).resolve().parent.parent
        path = root_dir / "config" / "config.yaml"
        path = path(path)

        if not path.exists():
            raise FileNotFoundError(f"Config file not found at {path}")

    with open(path, "r") as f:
        config = yaml.safe_load(f)

    return AppConfig(**config)