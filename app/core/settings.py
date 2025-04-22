from pydantic_settings import BaseSettings
import os

class SilkyConf(BaseSettings):
    github_token: str

    class Config:
        # Поднимаемся на два уровня вверх от app/core/ к корню проекта
        env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
        env_file_encoding = "utf-8"  # На всякий случай указываем кодировку

settings = SilkyConf()