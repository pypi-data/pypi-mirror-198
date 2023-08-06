import json
import requests
from typing import Dict, List


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.header = {}

    def set_header_param(self, header_key: str, header_val: str):
        self.header[header_key] = header_val

    def get_and_set_jwt_token_in_auth_header(self, token_path: str, username: str, password: str):
        token = requests.post(f"{self.base_url}{token_path}", { "username": username, "password": password })
        self.set_header_param("Authorization", f"Bearer {token}")

    def get_data(self, path: str) -> List[Dict]:
        url = f"{self.base_url}{path}"
        response = requests.get(url, headers=self.header)
        return json.loads(response.text)
