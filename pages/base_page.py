from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import BASE_URL, DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, url):
        self.driver.get(url)

    def open_home(self):
        self.open(BASE_URL)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def is_visible(self, locator):
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
