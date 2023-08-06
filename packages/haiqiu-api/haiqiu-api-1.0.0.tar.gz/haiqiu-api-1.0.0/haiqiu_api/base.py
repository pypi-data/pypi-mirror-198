import requests
import datetime
from loguru import logger


class base:
    host_name = "https://sshcloud.haiqiu.cn:8443"
    token = None

    def __init__(self, token: str):
        self.token = token

    def request(self, api_name, method="POST", **kwargs):
        url = f"{self.host_name}/{api_name}"
        headers = kwargs.get("headers", {})
        if self.token:
            headers["authorization"] = self.token
        kwargs["headers"] = headers

        logger.debug(dict(msg="正在请求的url:", url=url))
        logger.debug(dict(msg="正在请求的参数:", kwargs=kwargs))

        response = requests.request(method=method, url=url, **kwargs,)
        if response.status_code == 200:
            return self.response(response.json())
        logger.error(
            {"msg": "请求错误", "data": response.json(),}
        )

    def response(self, data):
        logger.debug(dict(msg="返回值", response=data))
        return data
