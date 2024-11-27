import pytest
from pagini.login_page import LoginPage
from utils.test_data import TestData

@pytest.mark.login
def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate_to()
    login_page.login(TestData.VALID_EMAIL, TestData.VALID_PASSWORD)
    assert page.url == "https://www.codecademy.com/learn"

#@pytest.mark.invalidlogin
def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.navigate_to()
    login_page.login(TestData.INVALID_EMAIL, TestData.INVALID_PASSWORD)
    #assert "Invalid credentials" in login_page.get_error_message()