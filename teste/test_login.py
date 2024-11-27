import pytest
from playwright.sync_api import expect
from pagini.login_page import LoginPage
from utils.test_data import TestData

@pytest.mark.login
def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate_to()
    login_page.login(TestData.VALID_EMAIL, TestData.VALID_PASSWORD)
    expect(page).to_have_url(TestData.LOGGED_IN_URL)
    login_page.logout()
    assert "Signed out successfully." in page.wait_for_selector(TestData.ERROR_MESSAGE).text_content(), "Delogarea nu a reusit!"

# @pytest.mark.invalidlogin
# def test_invalid_login(page):
#     login_page = LoginPage(page)
#
#     login_page.navigate_to()
#     login_page.login(TestData.INVALID_EMAIL, TestData.INVALID_PASSWORD)
    #assert "Invalid credentials" in login_page.get_error_message()