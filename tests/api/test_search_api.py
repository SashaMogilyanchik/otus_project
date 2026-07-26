import allure
import pytest

from api import endpoints
from api.client import ApiClient


@pytest.mark.api
class TestSearchApi:
    @pytest.mark.parametrize(
        "query,expected_min_count",
        [
            ("top", 1),
            ("dress", 1),
            ("jean", 1),
            ("tshirt", 1),
            ("nonexistentxyz123", 0),
        ],
    )
    @allure.title("Поиск товара: {query}")
    def test_search_product(self, api_client, query, expected_min_count):
        response = api_client.post(
            endpoints.SEARCH_PRODUCT,
            data={"search_product": query},
        )
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 200
        assert len(payload["products"]) >= expected_min_count

    @allure.title("Поиск без параметра search_product")
    def test_search_product_without_parameter(self, api_client):
        response = api_client.post(endpoints.SEARCH_PRODUCT)
        payload = ApiClient.parse_json(response)

        assert ApiClient.get_response_code(response) == 400
        assert "search_product parameter is missing" in payload["message"]
