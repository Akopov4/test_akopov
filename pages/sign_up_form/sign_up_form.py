import allure
import string
import random
from typing import Union
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page.base_page import BasePage
from pages.sign_up_form.sign_up_locators import SignUpFormLocators


class SignUpForm(BasePage):

    def get_first_last_field(self) -> WebElement:
        return self.driver.find_element(SignUpFormLocators.FIRST_NAME_LAST_NAME)

    def get_password_field(self) -> WebElement:
        return self.driver.find_element(SignUpFormLocators.SING_UP_PASS_FIELD)

    @allure.step('Fill "First and Last Name" text field')
    def fill_first_lats_field(self):
        name_field = self.get_first_last_field()
        name_field.send_keys(f"{generate_random_letters()} {generate_random_letters()}")

    @allure.step('Is "First and Last Name" highlighted in red')
    def first_last_red(self) -> bool:
        first_last = self.get_first_last_field()
        if first_last.get_attribute("class") == "error":
            return True
        else:
            return False

    @allure.step("Fill password text field")
    def fill_sign_up_password_field(self, password: str):
        sign_up_pass = self.get_password_field()
        sign_up_pass.send_keys(password)

    @allure.step('Is "Password" field highlighted in red')
    def pass_field_red(self):
        pass_filed = self.get_password_field()
        if pass_filed.get_attribute("class") == "error":
            return True
        else:
            return False

    @allure.title('Get Sign up error')
    def get_sign_up_error(self) -> str:
        return self.driver.find_element(SignUpFormLocators.SIGN_UP_ERROR).text

    @allure.step('Get description of allowed passwords')
    def get_allowed_pass_desc(self) -> str:
        paragraphs = self.find_elements(SignUpFormLocators.PARAGRAPHS_OF_PASS_DESC)
        description = ''
        for _ in paragraphs:
            description = '\n'.join(_.text)
        return description


def generate_random_letters(length: int = 5) -> str:
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for i in range(length))


def generate_password(length: int = 8) -> str:
    characters = string.ascii_letters.upper() + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))
