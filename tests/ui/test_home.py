import allure
import pytest

from pages.home_page import HomePage


@pytest.mark.ui
class TestHomePage:
    @allure.title("Главная страница открывается")
    def test_home_page_opens_with_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home()
        assert home_page.is_logo_visible()

    @allure.title("Переход на Products")
    def test_navigate_to_products(self, driver):
        home_page = HomePage(driver)
        home_page.open_home()
        home_page.go_to_products()
        assert "/products" in home_page.get_current_url()

    @allure.title("Переход в корзину")
    def test_navigate_to_cart(self, driver):
        home_page = HomePage(driver)
        home_page.open_home()
        home_page.go_to_cart()
        assert "/view_cart" in home_page.get_current_url()

    @allure.title("Блок подписки на главной")
    def test_subscription_section_visible(self, driver):
        home_page = HomePage(driver)
        home_page.open_home()
        assert home_page.is_subscription_section_visible()
