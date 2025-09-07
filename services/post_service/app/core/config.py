from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database settings
    database_hostname: str
    database_port: int
    database_username: str
    database_password: str
    database_name: str

    # JWT settings
    jwt_secret_key: str
    jwt_algorithm: str
    access_token_expiration_minutes: int

    # User service URL for API calls
    user_service_url: str = "http://user_service:8000"

    class Config:
        env_file = ".env"

settings = Settings()
