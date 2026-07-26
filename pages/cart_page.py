from selenium.webdriver.common.by import By

from config.settings import BASE_URL
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ROWS = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.check_out")
    DELETE_BUTTONS = (By.CSS_SELECTOR, ".cart_quantity_delete")
    LOGIN_TO_CHECKOUT = (By.CSS_SELECTOR, "a[href='/login'] u")

    def open_cart_page(self):
        self.open(f"{BASE_URL}/view_cart")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ROWS))

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def delete_first_item(self):
        initial_count = self.get_cart_items_count()
        buttons = self.driver.find_elements(*self.DELETE_BUTTONS)
        if not buttons:
            raise AssertionError("В корзине нечего удалять")
        buttons[0].click()
        self.wait.until(
            lambda driver: len(driver.find_elements(*self.CART_ROWS)) == initial_count - 1
        )

    def is_cart_empty(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements(*self.CART_ROWS)) == 0)
            return True
        except Exception:
            return self.get_cart_items_count() == 0

    def is_login_prompt_visible(self):
        return self.is_visible(self.LOGIN_TO_CHECKOUT)
