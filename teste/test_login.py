import pytest
from config.config import Config
from pagini.login_page import LoginPage
from utils.test_data import TestData

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate_to(Config.BASE_URL)
    login_page.login(TestData.VALID_EMAIL, TestData.VALID_PASSWORD)
    # Add assertions here

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate_to(Config.BASE_URL)
    login_page.login(TestData.INVALID_EMAIL, TestData.INVALID_PASSWORD)
    assert "Invalid credentials" in login_page.get_error_message()