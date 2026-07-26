import allure
import pytest

from api.client import ApiClient
from utils.data_generator import generate_user_data


@pytest.mark.api
class TestAccountApi:
    @allure.title("Создание нового пользователя")
    def test_create_account(self, api_client):
        user_data = generate_user_data()
        response = api_client.create_account(user_data)
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 201
        assert payload["message"] == "User created!"

        api_client.delete_account(user_data["email"], user_data["password"])

    @allure.title("Создание пользователя с существующим email")
    def test_create_account_duplicate_email(self, api_client, test_user):
        duplicate_data = generate_user_data(email=test_user["email"])
        response = api_client.create_account(duplicate_data)
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 400
        assert "already exist" in payload["message"].lower()

    @allure.title("Получение пользователя по email")
    def test_get_user_by_email(self, api_client, test_user):
        response = api_client.get_user_by_email(test_user["email"])
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 200
        assert payload["user"]["email"] == test_user["email"]

    @allure.title("Получение несуществующего пользователя")
    def test_get_user_by_nonexistent_email(self, api_client):
        response = api_client.get_user_by_email("nonexistent_user_12345@example.com")
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 404
        assert "not found" in payload["message"].lower()

    @allure.title("Обновление данных пользователя")
    def test_update_account(self, api_client, test_user):
        updated_data = dict(test_user)
        updated_data["firstname"] = "UpdatedFirst"
        updated_data["city"] = "UpdatedCity"

        response = api_client.update_account(updated_data)
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 200
        assert payload["message"] == "User updated!"

        user_response = api_client.get_user_by_email(test_user["email"])
        user_payload = ApiClient.parse_json(user_response)
        assert user_payload["user"]["first_name"] == "UpdatedFirst"

    @allure.title("Удаление пользователя")
    def test_delete_account(self, api_client):
        user_data = generate_user_data()
        create_response = api_client.create_account(user_data)
        assert ApiClient.get_response_code(create_response) == 201

        delete_response = api_client.delete_account(user_data["email"], user_data["password"])
        delete_payload = ApiClient.parse_json(delete_response)

        assert ApiClient.get_response_code(delete_response) == 200
        assert delete_payload["message"] == "Account deleted!"

        get_response = api_client.get_user_by_email(user_data["email"])
        get_payload = ApiClient.parse_json(get_response)
        assert ApiClient.get_response_code(get_response) == 404
        assert get_payload["responseCode"] == 404

    @pytest.mark.parametrize("missing_field", ["name", "email", "password"])
    @allure.title("Создание аккаунта без поля {missing_field}")
    def test_create_account_missing_required_field(self, api_client, missing_field):
        user_data = generate_user_data()
        user_data.pop(missing_field)

        response = api_client.create_account(user_data)
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 400
        assert "parameter is missing" in payload["message"].lower()
