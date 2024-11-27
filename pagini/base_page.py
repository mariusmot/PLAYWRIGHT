from config.config import Config
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page





    # def get_text(self, selector):
    #     return self.get_element(selector).text_content()