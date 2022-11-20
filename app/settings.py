import os
from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8080
    database_url: str = os.getenv("DATABASE_URL")

settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8',
)

print(f"Connected to: {settings}")
