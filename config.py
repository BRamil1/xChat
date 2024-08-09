from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_name: str | None = None
    database_engime: str | None = None

    SECRET_KEY: str = "TEST_KEY"
    DEBUG: bool = True
    ALLOWED_HOSTS: list[str] = []

    TEST_login: str = "TEST"
    TEST_password: str = "<PASSWORD>"

    model_config = SettingsConfigDict(env_file=".config.env")


settings = Settings()
