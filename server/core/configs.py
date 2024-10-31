from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "mysql+aiomysql://root:amgartendev@localhost:3306/iText"
    DBBaseModel: ClassVar = declarative_base()

    model_config = SettingsConfigDict(case_sensitive=True)


settings: Settings = Settings()
