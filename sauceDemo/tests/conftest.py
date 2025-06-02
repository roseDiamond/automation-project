from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver

from sauceDemo.pages.login_page import LoginPage


@pytest.fixture(scope='function')
def browserInstance():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # ✅ Open browser in incognito mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield  driver
    driver.close()

@pytest.fixture(scope='function')
def login(browserInstance):
    """Logs in before each test using the Login Page."""
    # driver.get("https://www.saucedemo.com/")
    # driver.get(BASE_URL)
    driver = browserInstance
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")