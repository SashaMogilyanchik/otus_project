from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    LOGO = (By.CSS_SELECTOR, "img[alt='Website for automation practice']")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "a[href='/products']")
    CART_LINK = (By.CSS_SELECTOR, "a[href='/view_cart']")
    SUBSCRIPTION_TEXT = (By.CSS_SELECTOR, "#footer .single-widget h2")

    def is_logo_visible(self):
        return self.is_visible(self.LOGO)

    def go_to_products(self):
        self.click(self.PRODUCTS_LINK)

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def is_subscription_section_visible(self):
        return self.is_visible(self.SUBSCRIPTION_TEXT)
