import allure
import pytest

from api import endpoints
from api.client import ApiClient


@pytest.mark.api
class TestProductsApi:
    @allure.title("Список товаров")
    def test_get_products_list(self, api_client):
        response = api_client.get(endpoints.PRODUCTS_LIST)
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 200
        assert len(payload["products"]) > 0

    @allure.title("Структура товара")
    def test_product_structure(self, api_client):
        response = api_client.get(endpoints.PRODUCTS_LIST)
        product = ApiClient.parse_json(response)["products"][0]

        assert "id" in product
        assert "name" in product
        assert "price" in product

    @allure.title("Количество товаров больше 30")
    def test_products_count(self, api_client):
        response = api_client.get(endpoints.PRODUCTS_LIST)
        products = response.json()["products"]

        assert len(products) > 30
