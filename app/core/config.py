from datetime import date
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

    historic_path: str = "./input/historic/"
    historic_file_download: bool = False
    historic_download_url: str = (
        "https://www.bcv.org.ve/sites/default/files/EstadisticasGeneral/"
    )
    historic_base_file_format: str = "2_1_{date}_smc.xls"
    historic_download_from_date: date | None = None


@lru_cache
def get_settings():
    return Settings()
