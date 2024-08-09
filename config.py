from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_name: str = "db.sqlite3"
    SECRET_KEY: str
    DEBUG: bool = True
    ALLOWED_HOSTS: list[str] = []

    TEST_login: str = "TEST"
    TEST_password: str = "<PASSWORD>"

    model_config = SettingsConfigDict(env_file=".config.env")


settings = Settings()
