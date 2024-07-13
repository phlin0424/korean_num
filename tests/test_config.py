from pathlib import Path

from src.config import conf


def test_conf():
    root_path = Path(__file__).resolve().parent.parent
    port = 80
    assert conf.root_path == root_path
    assert conf.backend_url == f"http://localhost:{port}"
