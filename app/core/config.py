from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Legislation Monitor"
    DEBUG: bool = True
    SECRET_KEY: str = "change_me"
    DATABASE_URL: str = "sqlite:///legislation.db"
    LOG_LEVEL: str = "INFO"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
