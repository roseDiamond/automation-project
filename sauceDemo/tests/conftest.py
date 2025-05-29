from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver


@pytest.fixture(scope='function')
def browserInstance():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # ✅ Open browser in incognito mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(3)

    yield  driver
    driver.close()