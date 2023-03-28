import pytest


class TestBase:
    @classmethod
    @pytest.fixture(scope="module", autouse=True)
    def setup_class(cls, driver):
        cls.driver = driver
