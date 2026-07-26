import allure
import pytest

from pages.cart_page import CartPage
from pages.products_page import ProductsPage


@pytest.mark.ui
class TestCart:
    @allure.title("Товар в корзине")
    def test_cart_shows_added_product(self, driver):
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)

        products_page.open_products_page()
        products_page.add_first_product_to_cart()
        products_page.go_to_cart_from_modal()

        assert cart_page.get_cart_items_count() == 1

    @allure.title("Удаление товара из корзины")
    def test_remove_product_from_cart(self, driver):
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)

        products_page.open_products_page()
        products_page.add_first_product_to_cart()
        products_page.go_to_cart_from_modal()
        assert cart_page.get_cart_items_count() == 1

        cart_page.delete_first_item()
        assert cart_page.is_cart_empty()

    @allure.title("Пустая корзина")
    def test_empty_cart_page(self, driver):
        cart_page = CartPage(driver)
        cart_page.open_cart_page()
        assert cart_page.is_cart_empty()

    @allure.title("Checkout без авторизации")
    def test_checkout_without_login_shows_login_prompt(self, driver):
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)

        products_page.open_products_page()
        products_page.add_first_product_to_cart()
        products_page.go_to_cart_from_modal()
        cart_page.proceed_to_checkout()

        assert "/login" in cart_page.get_current_url() or cart_page.is_login_prompt_visible()
