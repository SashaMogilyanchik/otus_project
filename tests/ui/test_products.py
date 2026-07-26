import allure
import pytest

from pages.products_page import ProductsPage


@pytest.mark.ui
class TestProducts:
    @allure.title("Страница Products открывается")
    def test_products_page_opens(self, driver):
        products_page = ProductsPage(driver)
        products_page.open_products_page()
        assert products_page.is_page_heading_visible()
        assert products_page.get_products_count() > 0

    @pytest.mark.parametrize("query", ["dress", "top"])
    @allure.title("Поиск товара: {query}")
    def test_search_product(self, driver, query):
        products_page = ProductsPage(driver)
        products_page.open_products_page()
        products_page.search_product(query)
        assert products_page.get_products_count() > 0

    @allure.title("Добавление товара в корзину")
    def test_add_first_product_to_cart(self, driver):
        products_page = ProductsPage(driver)
        products_page.open_products_page()
        products_page.add_first_product_to_cart()
        assert products_page.is_visible(products_page.VIEW_CART_MODAL)
