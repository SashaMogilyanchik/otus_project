import allure
import pytest

from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.data_generator import generate_user_data


@pytest.mark.ui
class TestAuth:
    @allure.title("Успешный вход")
    def test_successful_login(self, driver, test_user):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(test_user["email"], test_user["password"])
        assert login_page.is_logged_in_as(test_user["name"])

    @allure.title("Логин с неверным паролем")
    def test_login_with_invalid_password(self, driver, test_user):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(test_user["email"], "WrongPassword123!")
        assert login_page.is_login_error_visible()
        assert "incorrect" in login_page.get_login_error_text().lower()

    @allure.title("Выход из аккаунта")
    def test_logout_after_login(self, driver, test_user):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(test_user["email"], test_user["password"])
        assert login_page.is_logged_in_as(test_user["name"])
        login_page.logout()
        assert not login_page.is_logged_in_as(test_user["name"])

    @allure.title("Регистрация нового пользователя")
    def test_signup_new_user(self, driver, api_client):
        user_data = generate_user_data()
        login_page = LoginPage(driver)
        signup_page = SignupPage(driver)

        login_page.open_login_page()
        login_page.start_signup(user_data["name"], user_data["email"])
        signup_page.fill_account_info(user_data)
        signup_page.create_account()

        assert signup_page.is_account_created()
        signup_page.continue_after_signup()
        assert login_page.is_logged_in_as(user_data["name"])

        api_client.delete_account(user_data["email"], user_data["password"])
