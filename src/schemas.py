from pathlib import Path

from config import conf
from pydantic import BaseModel


class CreateNumResponseSchema(BaseModel):
    current_number: int


class CreateAudioSchema(BaseModel):
    input_text: str
    output_path: Path = conf.data_path


class KoreanNumResponseSchema(BaseModel):
    display_knum: str


class CreateDateResponseSchema(BaseModel):
    date: str


class CreatePplNumResponseSchema(BaseModel):
    ppl_num: str
