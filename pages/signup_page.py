from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class SignupPage(BasePage):
    TITLE_MR = (By.ID, "id_gender1")
    PASSWORD = (By.ID, "password")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")
    NEWSLETTER = (By.ID, "newsletter")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED_HEADING = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def fill_account_info(self, user_data):
        self.click(self.TITLE_MR)
        self.type_text(self.PASSWORD, user_data["password"])
        Select(self.find(self.DAYS)).select_by_value(str(user_data["birth_date"]))
        Select(self.find(self.MONTHS)).select_by_value(str(user_data["birth_month"]))
        Select(self.find(self.YEARS)).select_by_value(str(user_data["birth_year"]))
        if user_data.get("newsletter"):
            self.click(self.NEWSLETTER)
        self.type_text(self.FIRST_NAME, user_data["firstname"])
        self.type_text(self.LAST_NAME, user_data["lastname"])
        self.type_text(self.COMPANY, user_data["company"])
        self.type_text(self.ADDRESS1, user_data["address1"])
        self.type_text(self.ADDRESS2, user_data["address2"])
        Select(self.find(self.COUNTRY)).select_by_visible_text(user_data["country"])
        self.type_text(self.STATE, user_data["state"])
        self.type_text(self.CITY, user_data["city"])
        self.type_text(self.ZIPCODE, user_data["zipcode"])
        self.type_text(self.MOBILE, user_data["mobile_number"])

    def create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created(self):
        return self.is_visible(self.ACCOUNT_CREATED_HEADING)

    def continue_after_signup(self):
        self.click(self.CONTINUE_BUTTON)
