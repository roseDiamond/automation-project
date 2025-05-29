import time

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.success_text =(By.CSS_SELECTOR,'.app_logo')
        # self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")


    def login(self, username, password):
        self.driver.find_element(*self.user_name).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)

    def success_message(self):
        x= self.driver.find_element(*self.success_text).text
        return x

