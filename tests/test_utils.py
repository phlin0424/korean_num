from src.utils import number_to_korean


def test_number_to_korean():
    assert number_to_korean(800) == "팔백"
    assert number_to_korean(8000) == "팔천"
