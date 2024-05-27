import pytest
from ui_tests import identity_page
from ui_tests.identity_page import BirdsIdentity, get_all_images

image_paths_positive = get_all_images()
image_paths_negative = get_all_images(directory="negative")


class TestBirdsImagesUpload:
    def test_upload_button_is_present(self, driver):
        """To verify that upload button is present on the page"""
        upload_page = BirdsIdentity(driver)
        upload_page.open_url(identity_page.BirdsIdentity.identity_url)
        upload_page.wait_element_is_present(identity_page.BirdsIdentity.submit_button)

    @pytest.mark.parametrize("image_path", image_paths_positive)
    def test_upload_bird_positive(self, driver, image_path):
        """To verify that images are uploaded and to check a percentage match result"""
        upload_page = BirdsIdentity(driver)
        upload_page.navigate_to_identity()
        upload_page.send_images(image_path)
        upload_page.submit_search()
        upload_page.submit_search()
        assert upload_page.get_the_match_result() >= 90, (
            "Result is less than 90%, try uploading a better quality image "
            "or an image from a different angle")

    @pytest.mark.parametrize("image_path", image_paths_negative)
    def test_upload_bird_negative(self, driver, image_path):
        """To verify that images with no birds does not have a percentage match result"""
        upload_page = BirdsIdentity(driver)
        upload_page.navigate_to_identity()
        upload_page.send_images(image_path)
        upload_page.submit_search()
        upload_page.submit_search()
        assert upload_page.get_the_match_result() == 0, "Non bird is recognized as bird"
