from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME :str
    APP_VERSION :str
    GEMINI_KEY : str
    FILE_ALLOWED_TYPES :list
    FILE_MAX_SIZE :int
    FILE_DEFAULT_SIZE:int
    MONGO_URL :str
    MONGO_DATABASE:str
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()