from config.config import Config
from pagini.base_page import BasePage

class LoginPage(BasePage):
    #def __init__(self, page: Page):
    #     self.page = page
        #super().__init__(page)

    LOG_IN_LINK = "[data-testid='header-sign-in']"
    ACCEPT_COOKIES_BUTTON = "#onetrust-accept-btn-handler"
    EMAIL_INPUT = "input[name='user[login]']"
    PASSWORD_INPUT = "input[name='user[password]']"
    LOGIN_BUTTON = "button[type='submit']:has-text('Log in')"
    error_message = ".error-message"

    def navigate_to(self):
        self.page.goto(Config.BASE_URL)
        self.accept_cookies()
        self.page.locator(self.LOG_IN_LINK).first.click()

    def accept_cookies(self):
        self.page.locator(self.ACCEPT_COOKIES_BUTTON).click()

    def login(self, username, password):
        self.page.locator(self.EMAIL_INPUT).fill(username)
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()
        self.page.wait_for_load_state('networkidle')
