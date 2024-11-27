import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    """Lanseaza o singura instanta Playwright pentru intreaga sesiune."""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Lanseaza o singura instanta de browser pentru intreaga sesiune."""
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Lanseaza o pagina noua de browser pentru fiecare functie din test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

