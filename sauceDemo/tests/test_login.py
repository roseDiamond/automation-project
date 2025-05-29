from sauceDemo.pages.login_page import LoginPage


def test_valid_login(browserInstance):
    driver = browserInstance
    login_page = LoginPage(driver)
    login_page.login("standard_user","secret_sauce")
    print("login", login_page.success_message())
    assert "Swag Labs" == login_page.success_message(), "failed"