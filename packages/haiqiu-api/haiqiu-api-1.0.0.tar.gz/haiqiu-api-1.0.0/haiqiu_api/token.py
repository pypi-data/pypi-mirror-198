from .base import base
from loguru import logger
import datetime


class Token(base):
    def __init__(self, username: str, password: str, accountType: int = 0) -> None:
        self.username = username
        self.password = password
        self.accountType = accountType
        response = self.get()
        self.data = response.get("data")
        self.token = self.data.get("token")
        self.message = response.get("message")
        self.code = response.get("code")
        logger.debug(dict(msg="请求的token", token=self.token))

    def get(self):
        api_name = "sports/login"
        params = {
            "username": self.username,
            "password": self.password,
            "accountType": self.accountType,
        }
        response = self.request(api_name=api_name, json=params)
        return response

    def cache_in(self):
        pass

    def cache_out(self):
        pass
