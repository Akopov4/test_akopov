import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.base_page.base_page import BasePage
from pages.my_events_page.my_events_locators import MyEventsLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyEventsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Get text of top bar')
    def get_text_of_top_bar(self) -> str:
        return self.find_element(MyEventsLocators.MY_EVENTS_TOP_BAR).text



    @allure.step('Click on Log out button')
    def log_out(self):
        self.click_on_profile_button()
        self.find_element(MyEventsLocators.LOG_OUT_BUTTON).click()


    @allure.step('Click on profile button')
    def click_on_profile_button(self):
        self.find_element(MyEventsLocators.MY_PROFILE_BUTTON,timeout=10).click()


