import allure
import pytest

from api import endpoints
from api.client import ApiClient


@pytest.mark.api
class TestLoginApi:
    @allure.title("Логин с валидными данными")
    def test_verify_login_valid_credentials(self, api_client, test_user):
        response = api_client.verify_login(test_user["email"], test_user["password"])
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 200
        assert payload["message"] == "User exists!"

    @allure.title("Логин без email")
    def test_verify_login_without_email(self, api_client):
        response = api_client.post(
            endpoints.VERIFY_LOGIN,
            data={"password": "password123"},
        )
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 400
        assert "parameter is missing" in payload["message"].lower()

    @allure.title("Логин без password")
    def test_verify_login_without_password(self, api_client):
        response = api_client.post(
            endpoints.VERIFY_LOGIN,
            data={"email": "test@example.com"},
        )
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 400
        assert "parameter is missing" in payload["message"].lower()

    @allure.title("Логин с неверными данными")
    def test_verify_login_invalid_credentials(self, api_client):
        response = api_client.verify_login("invalid@example.com", "WrongPassword123!")
        data = response.json()

        assert data["responseCode"] == 404
        assert "not found" in data["message"].lower()
