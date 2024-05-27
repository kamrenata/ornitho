from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.fake: Faker = Faker()

    def find_element(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def open_url(self, url):
        self.driver.get(url)

    def wait_element_is_present(self, locator: tuple, timeout=10):
        WebDriverWait(driver=self.driver, timeout=timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_elements_are_present(self, locator: tuple, timeout=10):
        WebDriverWait(driver=self.driver, timeout=timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
