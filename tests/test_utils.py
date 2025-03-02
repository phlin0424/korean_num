from korean_num.utils import generate_number, number_to_korean


def test_number_to_korean():
    assert number_to_korean(800) == "팔백"
    assert number_to_korean(8000) == "팔천"


def test_generate_number():
    assert generate_number(4) < 10**5
