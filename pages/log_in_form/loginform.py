import allure
from typing import Union
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.base_page.base_page import BasePage
from pages.sign_up_form.sign_up_form import SignUpForm
from pages.log_in_form.log_in_locators import LoginFormLocators

from constants import LOG_IN_PAGE


class LogInForm(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Navigate to Log in page')
    def navigate_to_log_in_form(self):
        self.driver.get(LOG_IN_PAGE)

    @allure.step('Fill e-mail text field')
    def fill_email_text_field(self, email: str):
        email_field = self.find_element(LoginFormLocators.EMAIL_TEXT_FIELD)
        if not self.find_element(LoginFormLocators.EMAIL_TEXT_FIELD):
            self.click_change_email()
        email_field.send_keys(email)

    @allure.step('Click on Log in Button')
    def click_on_log_in_button(self):
        self.find_element(LoginFormLocators.LOG_IN_BUTTON).click()

    @allure.step('Fill password tests field')
    def fill_password_field(self, password: str):
        pass_field = self.find_element(LoginFormLocators.PASSWORD_FIELD)
        if pass_field.is_displayed():
            pass_field.clear()
            pass_field.send_keys(password)

    @allure.step('Click change e-mail link')
    def click_change_email(self):
        change_email_link = self.find_element(LoginFormLocators.CHANGE_EMAIL_LINK)
        if change_email_link.is_displayed():
            change_email_link.click()

    @allure.step('Click Submit button')
    def click_submit_button(self):
        submit_button = self.find_element(LoginFormLocators.SUBMIT_BUTTON)
        if submit_button.is_displayed():
            submit_button.click()

    @allure.step('Get invalid email error')
    def get_invalid_email_error(self) -> Union[str, None]:
        invalid_email =self.find_element(LoginFormLocators.INVALID_EMAIL_ERROR)
        if self.is_element_visible(LoginFormLocators.INVALID_EMAIL_ERROR):
            return invalid_email.text
        return None

    @allure.step('Get wrong email or password error is displayed')
    def get_wrong_email_or_pass(self) -> Union[str, None]:
        self.wait_until_element_is_present(LoginFormLocators.USER_PASSWORD_ERROR)
        wrong_email_or_pass = self.find_element(LoginFormLocators.USER_PASSWORD_ERROR, timeout=10)
        if self.is_element_visible(LoginFormLocators.USER_PASSWORD_ERROR):
            return wrong_email_or_pass.text
        return None

    @allure.step('Click on Sign Up link')
    def click_on_sing_up(self):
        self.find_element(LoginFormLocators.SIGN_UP_LINK).click()
        return SignUpForm(self.driver)
