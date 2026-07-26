from selenium.webdriver.common.by import By

from config.settings import BASE_URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    SIGNUP_NAME = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    LOGIN_ERROR = (By.CSS_SELECTOR, "form[action='/login'] p")
    LOGGED_IN_AS = (By.CSS_SELECTOR, "li a i.fa-user + b")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    def open_login_page(self):
        self.open(f"{BASE_URL}/login")

    def login(self, email, password):
        self.type_text(self.LOGIN_EMAIL, email)
        self.type_text(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def start_signup(self, name, email):
        self.type_text(self.SIGNUP_NAME, name)
        self.type_text(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BUTTON)

    def is_login_error_visible(self):
        return self.is_visible(self.LOGIN_ERROR)

    def get_login_error_text(self):
        return self.get_text(self.LOGIN_ERROR)

    def is_logged_in_as(self, name):
        if not self.is_visible(self.LOGGED_IN_AS):
            return False
        return name in self.get_text(self.LOGGED_IN_AS)

    def logout(self):
        self.click(self.LOGOUT_LINK)
