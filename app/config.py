from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Loads application settings from the .env file.
    """
    BREAD_API_BASE_URL: str
    BREAD_API_BASE_URL_PROCESSOR: str # <-- Add this line

    # Pydantic-settings configuration
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

# Create a single, importable instance of the settings
settings = Settings()