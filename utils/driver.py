from playwright.sync_api import sync_playwright

def get_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        return browser