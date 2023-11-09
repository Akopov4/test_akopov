import pytest
from allure_commons._allure import step
from typing import Union
from constants import EMAIL, PASSWORD
from pages.log_in_form.loginform import LogInForm
from pages.my_events_page.my_events_page import MyEventsPage
from tests.ui_tests import TestBase


class TestLogin(TestBase):

    @pytest.mark.parametrize('email,password', [(EMAIL,PASSWORD),('erwrwer', 'asdsadada')])
    def test_log_in(self, log_in_fixture, email, password):

        if email == EMAIL and password == PASSWORD:
            assert log_in_fixture.get_text_of_top_bar() == 'My Events'
            log_in_fixture.log_out()
        if email == 'sadsad@dsas.com' and password == 'asdsadada':
            assert log_in_fixture.get_wrong_email_or_pass() == 'Wrong email or password.'
        if email == 'asdsadcom':
            assert log_in_fixture.get_invalid_email_error() == 'Please provide a valid email address'



@pytest.fixture(scope='function')
def log_in_fixture(email, password, driver) -> Union[LogInForm, MyEventsPage]:
        "actions necessary to login"
        yield MyEventsPage()
        "actions needed to log out"

