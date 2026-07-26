import pytest

from api.client import ApiClient
from utils.data_generator import generate_user_data


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def test_user(api_client):
    user_data = generate_user_data()
    response = api_client.create_account(user_data)
    assert ApiClient.get_response_code(response) == 201
    yield user_data
    api_client.delete_account(user_data["email"], user_data["password"])
