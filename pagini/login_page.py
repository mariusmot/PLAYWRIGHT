from utils.base import BasePage
from playwright.sync_api import Page
from utils.test_data import TestData


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    LOGIN_LINK = "[data-testid='header-sign-in']"
    ACCEPT_COOKIES_BUTTON = "#onetrust-accept-btn-handler"
    EMAIL_INPUT = "input[name='user[login]']"
    PASSWORD_INPUT = "input[name='user[password]']"
    LOGIN_BUTTON = "button[type='submit']:has-text('Log in')"
    AVATAR_DROPDOWN = "div[data-testid='avatar-container']"
    LOG_OUT = "a[href='/sign_out']"
    error_message = ".error-message"

    def navigate_to(self):
        self.page.goto(TestData.BASE_URL)
        self.accept_cookies()
        #self.page.locator(self.LOG_IN_LINK).first.click()

    def accept_cookies(self):
        self.page.locator(self.ACCEPT_COOKIES_BUTTON).click()

    def login(self, username, password):
        self.page.wait_for_selector(self.EMAIL_INPUT, state="attached").fill(username)
        self.page.wait_for_selector(self.PASSWORD_INPUT, state="attached").fill(password)
        self.page.wait_for_selector(self.LOGIN_BUTTON).click()
        self.page.wait_for_load_state('networkidle')

    def logout(self):
        self.page.wait_for_selector(self.AVATAR_DROPDOWN, state="attached").click()
        self.page.wait_for_selector(self.LOG_OUT, state="attached").click()


