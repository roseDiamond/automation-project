from selenium.webdriver.common.by import By

class Base:
    def __init__(self,driver):
        self.driver = driver
        self.products_locator = (By.CLASS_NAME, "inventory_item")
        self.button_locator = (By.CLASS_NAME,"btn_secondary")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def go_to_cart(self):  # Clicks the cart icon and opens the cart page
        self.driver.find_element(*self.cart_badge).click()

    def get_cart_count(self):
        try:
            return int(self.driver.find_element(*self.cart_badge).text)
        except:
            return 0

    def add_product_to_cart_by_name(self, target_name):
        products = self.driver.find_elements(*self.products_locator)
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == target_name:
                product.find_element(By.CLASS_NAME, "btn_inventory").click()
                break
