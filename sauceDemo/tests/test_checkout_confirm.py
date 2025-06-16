import time

import pytest

from sauceDemo.pages.checkout_confirm_page import CheckoutPage
from sauceDemo.pages.inventory_page import InventoryPage
from sauceDemo.utils.base import Base


@pytest.mark.usefixtures("browserInstance","login")
class TestCheckout:
    def test_checkout_functionality(self,browserInstance):
        driver = browserInstance
        inventory = InventoryPage(driver)

        product_name = "Sauce Labs Backpack"
        inventory.add_product_to_cart_by_name(product_name)
        checkout =inventory.go_to_cart()
        time.sleep(1)
        checkout.click_checkout()
        time.sleep(1)
        print(f"checkout is present{driver.current_url}")
        assert "checkout" in driver.current_url, f"checkout is not present{driver.current_url}"


    def test_continoue_shopping(self,browserInstance):
        driver = browserInstance
        inventory = InventoryPage(driver)

        product_name = "Sauce Labs Backpack"
        inventory.add_product_to_cart_by_name(product_name)
        checkout = inventory.go_to_cart()
        time.sleep(1)
        checkout.click_contionue_shoping()
        time.sleep(1)
        print("inventory.htm is present:",driver.current_url)
        assert "inventory.html" in driver.current_url,"Not ptesent inventory.html"


    def test_removing_products(self,browserInstance):
        driver = browserInstance
        base = Base(driver)
        products = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
        for product in products:
            base.add_product_to_cart_by_name(product)
        len_prod = base.get_cart_count()
        print(f"cart count is equal product len {len(products)} equal cart count:{len_prod}")
        assert len(products) == base.get_cart_count(),f"cart count is not{len_prod}"
        base.go_to_cart()
        time.sleep(1)
        product_name = "Sauce Labs Backpack"
        cart = CheckoutPage(driver)
        cart.remove_product_by_name(product_name)
        time.sleep(2)
        print(f"cart count is equal product len {len(products)-1} equal cart count:{base.get_cart_count()}")
        assert len(products)-1 == base.get_cart_count(), f"cart count is not{base.get_cart_count()}"

    def test_complete_checkout_flow_successfully(self, browserInstance):
        driver = browserInstance
        base = Base(driver)
        checkout = CheckoutPage(driver)
        base.add_product_to_cart_by_name("Sauce Labs Backpack")
        base.go_to_cart()
        checkout.click_checkout()
        checkout.fill_form_click_continue()
        checkout.click_finsh()
        time.sleep(1)
        print("checkout complete; ", checkout.verify_checkout_complete())
        time.sleep(1)
        assert 'Thank you' in checkout.verify_checkout_complete()



