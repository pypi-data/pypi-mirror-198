from ..base import base
from loguru import logger


class Home(base):
    def __init__(self, token: str):
        super().__init__(token)

    def schoolnum(
        self,
        officeId=0,
        officeType=0,
    ):
        api_name = "sports/analysis/schoolnum"
        data = {"officeId": officeId, "officeType": officeType}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def levelrate(
        self,
        officeId=0,
        officeType=0,
        gradeType=10,
        dataType=1,
    ):
        api_name = "sports/analysis/levelrate"
        data = {"officeId": officeId, "officeType": officeType,
                "gradeType": gradeType, "dataType": dataType}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def levelrate_years(
        self,
        officeId=0,
        officeType=0,
        gradeCode="2001",
        dataType=1,
    ):
        api_name = "sports/analysis/levelrate/years"
        data = {"officeId": officeId, "officeType": officeType,
                "gradeCode": gradeCode, "dataType": dataType}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def levelrate_detail(
        self,
        levelId=1,
        officeId=0,
        officeType=0,
        gradeCode="3001",
        dataType=1,
    ):
        api_name = "sports/analysis/levelrate/detail"
        data = {"levelId": levelId, "officeId": officeId, "officeType": officeType,
                "gradeCode": gradeCode, "dataType": dataType}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def levelrate_weight(
        self,
        officeId=0,
        officeType=0,
        gradeCode="3001",
    ):
        api_name = "sports/analysis/levelrate/weight"
        data = {
            "officeId": officeId,
            "officeType": officeType,
            "gradeCode": gradeCode,
        }
        response = self.request(api_name=api_name, method="post", json=data,)
        return response
