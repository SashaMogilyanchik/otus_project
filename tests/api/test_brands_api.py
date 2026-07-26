import allure
import pytest

from api import endpoints
from api.client import ApiClient


@pytest.mark.api
class TestBrandsApi:
    @allure.title("Список брендов")
    def test_get_brands_list(self, api_client):
        response = api_client.get(endpoints.BRANDS_LIST)
        data = response.json()

        assert data["responseCode"] == 200
        assert len(data["brands"]) > 0

    @allure.title("Структура бренда")
    def test_brand_structure(self, api_client):
        response = api_client.get(endpoints.BRANDS_LIST)
        brand = ApiClient.parse_json(response)["brands"][0]

        assert "id" in brand
        assert "brand" in brand

    @allure.title("Количество брендов больше 5")
    def test_brands_count(self, api_client):
        response = api_client.get(endpoints.BRANDS_LIST)
        brands = ApiClient.parse_json(response)["brands"]

        assert ApiClient.get_response_code(response) == 200
        assert len(brands) > 5
