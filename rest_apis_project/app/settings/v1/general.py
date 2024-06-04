"""General settings."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class GeneralSettings(BaseSettings):
    """General configuration settings."""

    HASH_KEY: str
    MONGO_CONNECTION_STRING: str

    model_config = SettingsConfigDict(env_file="app/env/v1/general.env")
