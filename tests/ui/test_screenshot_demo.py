import allure
import pytest

from pages.home_page import HomePage


@pytest.mark.ui
class TestScreenshotDemo:
    @allure.title("Демо: падение для проверки скриншота в Allure")
    def test_always_fails_with_screenshot(self, driver):
        home_page = HomePage(driver)
        home_page.open_home()
        assert home_page.is_logo_visible(), "Страница должна открыться перед падением"
        assert False, "Намеренное падение для проверки скриншота"
