import os
from pathlib import Path

from pydantic_settings import BaseSettings

DIR_PATH = Path(__file__).resolve().parent.parent
HOST = os.getenv("HOST", "localhost")


class Config(BaseSettings):
    root_path: Path = DIR_PATH
    data_path: Path = DIR_PATH / "src" / "data"
    backend_url: str = f"http://{HOST}:80"


conf = Config()


if __name__ == "__main__":
    print(conf)
