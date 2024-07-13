import random

from navertts import NaverTTS
from schemas import CreateAudioSchema


def create_audio(create_audio_params: CreateAudioSchema) -> str:
    """Create an audio file (.mp3) for the input korean word. Based on Naver TTS API."""

    # Create the directory if not exist:
    if not create_audio_params.output_path.exists():
        create_audio_params.output_path.mkdir(parents=True, exist_ok=True)

    # # Check the file existence:
    # audio_filename = (
    #     create_audio_params.output_path
    #     / f"naver_num_{ str(create_audio_params.input_number).zfill(6)}.mp3"
    # )
    # if audio_filename.exists():
    #     return str(audio_filename)
    audio_filename = create_audio_params.output_path / "temp.mp3"

    # Generate the audio file (.mp3):
    text = str(create_audio_params.input_number)
    tts = NaverTTS(text)
    tts.save(audio_filename)
    return str(audio_filename)


def generate_number(digit: int) -> int:
    current_number = random.randint(10 ** (digit - 1), 10**digit - 1)
    return current_number


def number_to_korean(number):
    units = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    tens = ["", "십", "백", "천", "만"]

    if number == 0:
        return "영"

    if number < 10:
        return units[number]

    # Split the number into individual digits
    digits = list(map(int, str(number)))
    length = len(digits)
    result = ""

    for i, digit in enumerate(digits):
        if digit != 0:
            # Add the unit and tens part
            result += units[digit] + tens[length - 1 - i]

    # Remove any leading "일" before "십", "백", "천"
    result = result.replace("일십", "십").replace("일백", "백").replace("일천", "천")

    return result


if __name__ == "__main__":
    # create_audio(text="21")
    # print(generate_number())
    print(number_to_korean(800))
    print(number_to_korean(8000))
