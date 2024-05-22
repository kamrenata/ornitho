import os
import pytest

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from scripts.cft_management import ROOT, get_chrome_paths


@pytest.fixture(autouse=True)
def driver():
    """Create chrome driver for Selenium"""
    chrome_path, chromedriver_path = get_chrome_paths()
    options = ChromeOptions()
    options.binary_location = str(
        os.path.join(
            ROOT,
            chrome_path
        )
    )

    driver = Chrome(
        options=options,
        service=Service(
            executable_path=str(
                os.path.join(ROOT, chromedriver_path)
            )
        ),
    )
    yield driver
    driver.quit()
