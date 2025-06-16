from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.checkout = (By.ID,"checkout")
        self.shopping = (By.ID,"continue-shopping")
        self.cart_product =(By.CLASS_NAME,"cart_item_label")
        self.first_name =(By.ID,"first-name")
        self.last_name =(By.ID,"last-name")
        self.post_code =(By.ID,"postal-code")
        self.conti = (By.ID,"continue")



    def click_checkout(self):
        self.driver.find_element(*self.checkout).click()

    def click_contionue_shoping(self):
        self.driver.find_element(*self.shopping).click()

    def remove_product_by_name(self,product_name):
        products = self.driver.find_elements(*self.cart_product)
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                button = product.find_element(By.CLASS_NAME, "cart_button")
                button.click()
                break

    def fill_form_click_continue(self):
        self.driver.find_element(*self.first_name).send_keys("Sun")
        self.driver.find_element(*self.last_name).send_keys("Singh")
        self.driver.find_element(*self.post_code).send_keys("1234")
        self.driver.find_element(*self.conti).click()

    def click_finsh(self):
        self.driver.find_element(By.ID,"finish").click()

    def verify_checkout_complete(self):
        return self.driver.find_element(By.CLASS_NAME,"complete-header").text
