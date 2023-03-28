import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver(request) -> WebDriver:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    yield browser
    browser.quit()
