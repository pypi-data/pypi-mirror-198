from ..base import base
from loguru import logger


class TestStandard(base):
    def __init__(self, token: str):
        super().__init__(token)

    def findAll(
        self,
        pageNum=1,
        pageSize=10,
    ):
        api_name = "sports/platform/testStandard/findAll"
        data = {"pageNum": pageNum, "pageSize": pageSize}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def info(
        self,
        standardId,
        gender='',
        itemId='',
    ):
        api_name = "sports/platform/testStandard/findStandardInfo"
        data = {"standardId": standardId, "gender": gender, "itemId": itemId}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response
