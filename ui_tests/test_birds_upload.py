import pytest
from ui_tests.identity_page import BirdsIdentity, get_all_images

image_paths_positive = get_all_images()
image_paths_negative = get_all_images(directory="negative")


@pytest.mark.parametrize("image_path", image_paths_positive)
def test_upload_bird_positive(driver, image_path):
    upload_page = BirdsIdentity(driver)
    upload_page.navigate_to_identity()
    upload_page.send_images(image_path)
    upload_page.submit_search()
    upload_page.submit_search()
    assert upload_page.get_the_match_result() >= 90, "result is less than 90%"


@pytest.mark.parametrize("image_path", image_paths_negative)
def test_upload_bird_negative(driver, image_path):
    upload_page = BirdsIdentity(driver)
    upload_page.navigate_to_identity()
    upload_page.send_images(image_path)
    upload_page.submit_search()
    upload_page.submit_search()
    assert upload_page.get_the_match_result() == 0, "Non bird is recognized as bird"

# upload button + asserts
