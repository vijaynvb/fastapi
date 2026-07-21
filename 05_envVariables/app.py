from python_dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()  # Load environment variables from .env file

import os

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    DEBUG: bool = os.getenv("DEBUG")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    API_KEY: str = os.getenv("API_KEY")

settings = Settings()

secret_key = settings.SECRET_KEY
debug = settings.DEBUG
database_url = settings.DATABASE_URL
api_key = settings.API_KEY