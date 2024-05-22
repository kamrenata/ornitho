from pages.base_page import BasePage, By


class BirdsIdentity(BasePage):
    """Class which reflects locators on the ui_tests identity page"""

    def __init__(self, driver):
        super().__init__(driver)

    url = "https://www.oiseaux.net/identifier/"
    identity_url = "https://www.ornitho.com/"

    bird_image_upload = (By.CSS_SELECTOR, f"h4 > [href='{identity_url}']")

    def navigate_to_identity(self):
        self.open_url(self.url)
        self.find_element(self.bird_image_upload).click()
