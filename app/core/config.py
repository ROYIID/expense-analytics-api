from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Expense Analytics API"
    debug: bool = True
    secret_key: str = "default-secret"

    model_config = {"env_file": ".env"}

settings = Settings()
