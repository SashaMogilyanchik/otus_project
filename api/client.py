import requests

from api import endpoints
from config.settings import API_BASE_URL


class ApiClient:
    def __init__(self, base_url=API_BASE_URL):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params, timeout=30)

    def post(self, endpoint, data=None):
        return requests.post(f"{self.base_url}{endpoint}", data=data, timeout=30)

    def put(self, endpoint, data=None):
        return requests.put(f"{self.base_url}{endpoint}", data=data, timeout=30)

    def delete(self, endpoint, data=None):
        return requests.delete(f"{self.base_url}{endpoint}", data=data, timeout=30)

    def create_account(self, user_data):
        return self.post(endpoints.CREATE_ACCOUNT, data=user_data)

    def delete_account(self, email, password):
        return self.delete(
            endpoints.DELETE_ACCOUNT,
            data={"email": email, "password": password},
        )

    def update_account(self, user_data):
        return self.put(endpoints.UPDATE_ACCOUNT, data=user_data)

    def verify_login(self, email, password):
        return self.post(
            endpoints.VERIFY_LOGIN,
            data={"email": email, "password": password},
        )

    def get_user_by_email(self, email):
        return self.get(endpoints.GET_USER_BY_EMAIL, params={"email": email})

    @staticmethod
    def parse_json(response):
        return response.json()

    @staticmethod
    def get_response_code(response):
        return ApiClient.parse_json(response)["responseCode"]
