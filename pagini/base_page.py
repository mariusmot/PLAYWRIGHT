class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        self.page.goto(url)

    def get_element(self, selector):
        return self.page.locator(selector)

    def click(self, selector):
        self.get_element(selector).click()

    def fill(self, selector, text):
        self.get_element(selector).fill(text)

    def get_text(self, selector):
        return self.get_element(selector).text_content()