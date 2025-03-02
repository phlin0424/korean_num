from pathlib import Path

from pydantic import BaseModel

from korean_num.config import conf


class CreateNumResponseSchema(BaseModel):
    current_number: int


class CreateAudioSchema(BaseModel):
    input_text: str
    output_path: Path = conf.data_path


class KoreanNumResponseSchema(BaseModel):
    display_knum: str


class CreateDateResponseSchema(BaseModel):
    date: str
