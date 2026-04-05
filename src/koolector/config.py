"""Manage configuration for the application."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    paperless_api_url: str
    paperless_api_token: str
