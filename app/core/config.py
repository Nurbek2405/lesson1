from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import SettingsConfigDict, BaseSettings


ROOT_DIR_PATH = Path(__file__).parent
ENV_FILE_PATH = ROOT_DIR_PATH.joinpath(".env")


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=ENV_FILE_PATH,
        env_nested_delimiter="__",
    )
    db: DatabaseConfig


settings = Setting()