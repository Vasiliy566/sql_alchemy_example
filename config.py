from pydantic import BaseSettings


class DatabaseConfig(BaseSettings):
    login: str = "admin"
    password: str = "admin"
    host: str = "postgres"
    port: str = "5432"
    database: str = "db1"


config = DatabaseConfig()
