import os
from pathlib import Path
from pydantic_settings import BaseSettings


PROFILE = os.environ.get("PROFILE", "dev")


class Settings(BaseSettings):
    segment_file_path: str
    source_file_path: str


    class Config:
        env_file = f'{Path(os.path.dirname(__file__))}/{PROFILE}.env'
        env_file_encoding = 'utf-8'
        case_sensitive = False


config = Settings()