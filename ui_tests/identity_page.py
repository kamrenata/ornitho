import os
from pages.base_page import BasePage, By

project_root = os.path.dirname(os.path.dirname(__file__))


def get_all_images(directory="positive"):
    images = []
    for i in os.listdir(os.path.join(project_root, "resources", directory)):
        images.append(os.path.join(project_root, "resources", directory, i))
    return images


class BirdsIdentity(BasePage):
    """Class which reflects locators on the ui_tests identity page"""

    def __init__(self, driver):
        super().__init__(driver)

    url = "https://www.oiseaux.net/identifier/"
    identity_url = "https://www.ornitho.com/"

    bird_image_upload = (By.CSS_SELECTOR, f"h4 > [href='{identity_url}']")
    drop_image = (By.ID, "NOM_DE_FICHIER")
    submit_button = (By.CLASS_NAME, "validez")
    match_percentage = (By.CLASS_NAME, "pour100esp")

    def navigate_to_identity(self):
        self.open_url(self.url)
        self.find_element(self.bird_image_upload).click()

    def send_images(self, file_path):
        self.find_element(self.drop_image).send_keys(file_path)

    def submit_search(self):
        self.find_element(self.submit_button).click()

    def get_the_match_result(self):
        self.wait_elements_are_present(self.match_percentage)
        result = self.find_elements(self.match_percentage)
        percentage = result[1].text
        return int(percentage.split(".")[0])
