import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.settings import DEFAULT_TIMEOUT, HEADLESS
from utils.screenshot import capture_screenshot


def _attach_failure_artifacts(driver):
    try:
        allure.attach(
            capture_screenshot(driver),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception as exc:
        allure.attach(
            str(exc),
            name="screenshot_on_failure_error",
            attachment_type=allure.attachment_type.TEXT,
        )
        try:
            allure.attach(
                driver.page_source,
                name="page_source_on_failure",
                attachment_type=allure.attachment_type.HTML,
            )
        except Exception:
            pass


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)

    if report.when == "call" and report.failed:
        driver = getattr(item, "_driver", None)
        if driver is not None:
            _attach_failure_artifacts(driver)


@pytest.fixture
def driver(request):
    options = Options()
    options.page_load_strategy = "eager"
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--force-device-scale-factor=1")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    driver.implicitly_wait(DEFAULT_TIMEOUT)
    driver.set_page_load_timeout(DEFAULT_TIMEOUT * 3)
    driver.set_script_timeout(DEFAULT_TIMEOUT)

    request.node._driver = driver
    yield driver
    driver.quit()
    request.node._driver = None
