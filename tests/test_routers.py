import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from korean_num.app import app

# Create a test client
client = TestClient(app)


@pytest.fixture
def current_path() -> Path:
    return Path(__file__).resolve().parent


def test_get_number():
    """TESTCASE1: test endpoint /get_number"""
    digit = 5  # digit =5 -> a number between 10000~99999
    response = client.get(
        "/get_number",
        params={"digit": digit},
    )
    assert response.status_code == 200
    assert response.json()["current_number"] < 10**5
    assert response.json()["current_number"] >= 10**4


def test_play_audios(current_path):
    """TESTCASE2: test endpoint /play_audios."""
    response = client.post(
        "/play_audios",
        json={"input_text": "1234", "output_path": current_path.__str__()},
    )
    filename = response.text.strip('"')
    assert os.path.isfile(filename)
    os.remove(filename)
    assert response.status_code == 200


def test_display_knum() -> None:
    """TESTCASE 3: test endpoint /display_knum."""
    response = client.get(
        "/display_knum",
        params={"input_number": 1234},
    )
    assert response.status_code == 200
    assert response.json()["display_knum"] == "천이백삼십사"


def test_display_knum_digiterror() -> None:
    """TESTCASE 4: test endpoint /display_knum with a number greater than 10**6."""
    response = client.get(
        "/display_knum",
        params={"input_number": 999999},
    )
    assert response.status_code == 403
    assert response.json()["detail"] == "not available number (must be smaller than 100k)"
