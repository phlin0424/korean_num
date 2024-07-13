from pathlib import Path

from config import conf
from pydantic import BaseModel


class CreateNumResponseSchema(BaseModel):
    current_number: int


class CreateAudioSchema(BaseModel):
    input_number: int
    output_path: Path = conf.data_path


class KoreanNumResponseSchema(BaseModel):
    display_knum: str
