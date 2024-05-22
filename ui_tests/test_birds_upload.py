from identity_page import BirdsIdentity


def test_upload_bird(driver):
    upload_page = BirdsIdentity(driver)
    upload_page.navigate_to_identity()
