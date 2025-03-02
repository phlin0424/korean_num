import requests
from requests import Response

from korean_num.config import conf


# a client to request apis
class Client:
    def __init__(self, conf=conf):
        self.backend_url = conf.backend_url

    def get(self, path: str, params: dict = {}):
        url = f"{self.backend_url}/{self.clean_path(path)}"
        with requests.get(url, params=params) as r:
            return self._get_json_result(url, r)

    def post(self, path: str, json: dict = {}):
        url = f"{self.backend_url}/{self.clean_path(path)}"
        with requests.post(url, json=json) as r:
            return self._get_json_result(url, r)

    def clean_path(self, path: str):
        if path.startswith("http"):
            raise Exception(
                f"Wrong path {path}, use with api path directly (no http://xxx..xxx)."
            )
        path = path.removeprefix("/")
        return path

    def _get_json_result(self, url: str, r: Response, print_auth_error=True):
        if r.status_code > 400 and r.status_code < 500:
            if print_auth_error:
                print(
                    f"Unauthorized call. Check your PAT token {r.text} - {r.url} - {url}"
                )
        try:
            return r.json()
        except Exception as e:
            print(
                f"API CALL ERROR - can't read json. status: {r.status_code} {r.text} - URL: {url} - {e}"
            )
            raise e
