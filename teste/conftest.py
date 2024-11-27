# import pytest
# from playwright.sync_api import Page, sync_playwright, Browser
#
# @pytest.fixture(scope="function")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()
#
# @pytest.fixture
# def page(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     page.close()
#     context.close()

