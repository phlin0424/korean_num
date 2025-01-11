from fastapi import APIRouter, HTTPException
from schemas import (
    CreateAudioSchema,
    CreateNumResponseSchema,
    KoreanNumResponseSchema,
    CreateDateResponseSchema,
    CreatePplNumResponseSchema,
)
from utils import (
    create_audio,
    generate_number,
    number_to_korean,
    generate_date,
    generate_ppl_num,
)

routers = APIRouter()


@routers.get("/get_number", response_model=CreateNumResponseSchema)
def generate_num(digit: int = 4):
    if digit > 5:
        raise HTTPException(
            status_code=403, detail="not available number (must be smaller than 100k)"
        )
    current_number = generate_number(digit)
    print(current_number)
    return CreateNumResponseSchema(current_number=current_number)


@routers.post("/play_audios")
def play_audio(create_audio_request: CreateAudioSchema):
    audio_filename = create_audio(create_audio_request)
    return audio_filename


@routers.get("/display_knum", response_model=KoreanNumResponseSchema)
def display_knum(input_number: int):
    if input_number > 10**5:
        raise HTTPException(
            status_code=403, detail="not available number (must be smaller than 100k)"
        )
    number_display = number_to_korean(input_number)
    return {"display_knum": number_display}


@routers.get("/get_date", response_model=CreateDateResponseSchema)
def get_date():
    return {"date": generate_date()}


@routers.get("/get_ppl_num", response_model=CreatePplNumResponseSchema)
def get_ppl_num():
    return {"ppl_num": generate_ppl_num()}
