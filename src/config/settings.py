from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App settings"""

    # Telegram Bot
    telegram_bot_token: str = Field(..., description="Telegram Bot Token")
    telegram_bot_polling_timeout: int = Field(default=30, description="Polling timeout")

    # OpenDota API
    opendota_base_url: str = "https://api.opendota.com/api"
    opendota_timeout: int = 30
    opendota_max_retries: int = 3
    opendota_api_token: str | None = None  

    # Stratz API
    stratz_api_token: str = Field(..., description="Stratz API Token")
    stratz_base_url: str = Field(
        default="https://api.stratz.com/graphql", description="Stratz API URL"
    )

    stratz_timeout: int = Field(default=30, description="Request timeout")
    stratz_max_retries: int = Field(default=3, description="Max retry attempts")

    # Logging
    log_level: str = Field(default="INFO", description="Logging level")

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )
