from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_until_element_is_present(self, locator: tuple, timeout: float = 5, attempts:int =3):
        for i in range(attempts):
            try:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
                break
            except (TimeoutException, StaleElementReferenceException):
                raise NoSuchElementException(
                f'Element "{locator}" not present in DOM after {timeout*attempts} seconds or it has been changed')


    def find_element(self, locator: tuple, timeout: float = 5) -> WebElement:
        self.wait_until_element_is_present(locator, timeout)
        return self.driver.find_element(*locator)


    def is_element_visible(self, locator: tuple, timeout: float = 5) -> bool:
        try:
            self.wait_until_element_is_visible(locator, timeout=timeout)
        except NoSuchElementException:
            return False
        return True


    def wait_until_element_is_visible(self, locator: tuple, timeout: float = 5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Element "{locator}" not visible after {timeout} seconds')


    def find_elements(self, locator: tuple, timeout: float = 5, wait: bool = True) -> List[WebElement]:
        if wait:
            self.wait_until_element_is_present(locator, timeout)
        return self.driver.find_elements(*locator)


    def is_element_enabled(self, locator: tuple, timeout: float = 5) -> bool:
        element = self.find_element(*locator, timeout=timeout)
        return element.is_enabled()
