from selenium.webdriver.common.by import By

from config.settings import BASE_URL
from pages.base_page import BasePage


class ProductsPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".productinfo")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "a.add-to-cart")
    VIEW_CART_MODAL = (By.CSS_SELECTOR, "a[href='/view_cart'] u")
    PAGE_HEADING = (By.CSS_SELECTOR, ".features_items h2.title")

    def open_products_page(self):
        self.open(f"{BASE_URL}/products")

    def search_product(self, query):
        self.type_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)

    def get_products_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def is_page_heading_visible(self):
        return self.is_visible(self.PAGE_HEADING)

    def add_first_product_to_cart(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if not buttons:
            raise AssertionError("Не нашёл товары на странице")
        buttons[0].click()

    def go_to_cart_from_modal(self):
        self.click(self.VIEW_CART_MODAL)
