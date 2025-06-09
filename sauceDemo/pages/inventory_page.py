import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self,driver):
        self.driver = driver
        self.product_sort_dropdown=(By.CLASS_NAME,"product_sort_container")
        self.name_locator = (By.CLASS_NAME, "inventory_item_name")
        self.price_locator = (By.CLASS_NAME, "inventory_item_price")
        self.products_locator =(By.CLASS_NAME,"inventory_item")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.remove_buttons =(By.CLASS_NAME, "btn_inventory")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.about =(By.ID,"about_sidebar_link")
        self.logout =(By.ID,"logout_sidebar_link")
        self.login_button = (By.ID, "login-button")
        self.reset =(By.ID, "reset_sidebar_link")


    def click_logout(self):
        self.driver.find_element(*self.logout).click()

    def click_reset(self):
        self.driver.find_element(*self.reset).click()

    def is_login_displayed(self):
        return self.driver.find_element(*self.login_button).is_displayed()


    def click_about(self):
        self.driver.find_element(*self.about).click()

    def remove_product_by_name(self,product_name):
        products = self.driver.find_elements(*self.products_locator)
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                product.find_element(*self.remove_buttons).click()
                break
        time.sleep(1)
    def add_product_to_cart_by_name(self,target_name):
        products = self.driver.find_elements(*self.products_locator)
        for product in products:
            name = product.find_element(By.CLASS_NAME,"inventory_item_name").text
            if name == target_name:
                product.find_element(By.CLASS_NAME,"btn_inventory").click()
                break

    def add_multiple_products_to_cart(self, product_list):
        """
                Click 'Add to cart' for a list of products.
                """
        for product in product_list:
            self.add_product_to_cart_by_name(product)

    def get_cart_count(self):
        """ when cart is empty, the badge element doesn’t exist at all in the DOM
        it is not just empty (""), it is not present.
        Without Try-Except?
        badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        If the badge doesn't exist (cart is empty), the above line will raise:
        selenium.common.exceptions.NoSuchElementException
        Which will make your test crash unexpectedly
        Without try-except, this will crash your test when the cart is empty — even though it's correct behavior
        (because empty cart = no badge = 0 items
        """
        try:
            return int(self.driver.find_element(*self.cart_badge).text)
        except:
            return 0

    def go_to_cart(self): #Clicks the cart icon and opens the cart page
        self.driver.find_element(*self.cart_badge).click()

    def select_sort_option(self,option_value):
        """
                Selects a sort option from the dropdown.
                Example: "Price (low to high)", "Name (Z to A)"
                """
        select = Select(self.driver.find_element(*self.product_sort_dropdown))
        select.select_by_visible_text(option_value)
        # print(self.driver.find_element(*self.price_low_high).text)
        # return self.driver.find_element(*self.price_low_high).text

    def get_product_names(self):
        l= [elem.text for elem in self.driver.find_elements(*self.name_locator)]
        print(l)
        return [elem.text for elem in self.driver.find_elements(*self.name_locator)]

    def get_product_prices(self):
        product_prices= [elm.text for elm in self.driver.find_elements(*self.price_locator)]
        print(product_prices)
        return [float(elem.text.replace("$", "")) for elem in self.driver.find_elements(*self.price_locator)]

    def open_sidemenu(self):
        self.driver.find_element(By.ID,"react-burger-menu-btn").click()
        return self.driver.find_element(By.ID, "logout_sidebar_link").text





