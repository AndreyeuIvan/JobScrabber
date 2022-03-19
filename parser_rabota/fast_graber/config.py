from pydantic import BaseSettings


class Setting(BaseSettings):
    db_host: str
    db_port: str
    db_name: str
    db_user: str

    class Config:
        env_file = ".env"


setting = Setting()
