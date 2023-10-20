from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_DIR: Path = Path(__file__).resolve(strict=True).parent.parent
    BOT_TOKEN: str

    model_config = SettingsConfigDict(env_file='../.env')


settings = Settings()
print(settings.APP_DIR)
