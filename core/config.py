# core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    """
    Centralized Configuration Management.
    """
    
    # Environment URLs (No hardcoded defaults here, they come from .env)
    base_ui_url: str
    base_api_url: str
    
    # Test User Credentials
    admin_email: str
    admin_password: str
    customer_email: str
    customer_password: str
    
    # Database Settings
    db_connection_string: str = Field(default="sqlite:///:memory:")
    
    # Playwright Settings
    headless: bool = Field(default=True, description="Run browser in headless mode")
    browser_timeout: int = Field(default=30000, description="Timeout for Playwright actions in milliseconds")

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

settings = Settings()