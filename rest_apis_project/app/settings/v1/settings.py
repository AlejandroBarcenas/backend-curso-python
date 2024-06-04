"""Global settings."""

from app.settings.v1.general import GeneralSettings
# from pydantic_settings import BaseSettings
from pydantic import BaseModel


class Settings(BaseModel):
    """Global configuration settings.

    Args:
        GENERAL (GeneralSettings): General configuration.
    """

    GENERAL: GeneralSettings


SETTINGS = Settings(
    GENERAL=GeneralSettings(),
)
