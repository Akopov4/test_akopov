import pytest
from typing import Union
from constants import EMAIL, PASSWORD
from pages.log_in_form.loginform import LogInForm
from pages.my_events_page.my_events_page import MyEventsPage
from tests.ui_tests import TestBase

class TestSignup(TestBase):

    pytest.mark.parametrize()
    def test_signup(self, signup_fixture):
        pass






def signup_fixture(frist_and_last_name:str, email:str,password:str):
    pass
