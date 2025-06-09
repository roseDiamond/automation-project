import time

import pytest

from sauceDemo.pages.inventory_page import InventoryPage

# @pytest.mark.smoke
def test_navigation_to_about_page(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    inventory.open_sidemenu()
    inventory.click_about()
    print(driver.current_url)
    assert "saucelabs.com"in driver.current_url,"Failed"

# @pytest.mark.smoke
def test_logout_functionality(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    inventory.open_sidemenu()
    inventory.click_logout()
    print(inventory.is_login_displayed())
    assert inventory.is_login_displayed(),"Logout failed: login button not visible"
# @pytest.mark.smoke
def test_add_single_product(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(browserInstance)
    product_name = "Sauce Labs Backpack"
    inventory.add_product_to_cart_by_name(product_name)
    count = inventory.get_cart_count()
    assert count ==1, f" product count must be 1 but got {count}"
    inventory.go_to_cart()
    assert "cart.html" in driver.current_url,"failed"

@pytest.mark.smoke
def test_rest_functionality(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    product_name = "Sauce Labs Backpack"
    inventory.add_product_to_cart_by_name(product_name)
    inventory.open_sidemenu()
    inventory.click_reset()
    print(f"cartcount:",inventory.get_cart_count())
    assert 0 == inventory.get_cart_count(),f"Reset failed: cart count{inventory.get_cart_count()}"









def test_add_multiple_products(self, browserInstance):
    inventory = InventoryPage(browserInstance)
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Onesie"]
    inventory.add_multiple_products_to_cart(products_to_add)
    badge_count = inventory.get_cart_count()
    assert len(products_to_add) == badge_count,f"❌ Expected {len(products_to_add)} items, but  {badge_count} in badge"

# @pytest.mark.smoke
def test_add_single_product_to_cart(browserInstance,login):
    driver =browserInstance
    inventory = InventoryPage(driver)
    inventory.add_first_n_products_to_cart(n=1)
    # Verify cart badge shows 3
    count = inventory.get_cart_count()
    print("verhgj",count)
    assert count == 1, f"❌ Expected 1 items in cart but found {count}"

    inventory.click_on_shopping_cart()
    url = "https://www.saucedemo.com/cart.html"
    print(driver.current_url)
    assert url == driver.current_url, f"assertions failed expected{url},got {driver.current_url}"

    # print("sfg",inventory.verify_add_to_cart())
    # assert 1 == inventory.verify_add_to_cart(),"not 1"

def test_sidemenu(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    sidbar_text = inventory.open_sidemenu()
    print("match", sidbar_text)
    assert "Logout" == sidbar_text, " failed not match"





def test_sort_name_z_to_a(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    inventory.verify_sort("Name (Z to A)")

def test_sort_name_a_to_z(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    inventory.verify_sort("Name (A to Z)")

# @pytest.mark.smoke
def test_sort_product_low_to_high(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    inventory.select_sort_option("Price (low to high)")
    actual = inventory.get_product_prices()
    expected = sorted(actual)
    # print("prices high to low actual",expected)
    assert actual == expected, f"expected prices low to high  {expected}, but got {actual}"

# @pytest.mark.smoke
def test_sort_product_high_to_low(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    inventory.select_sort_option("Price (high to low)")
    actual =inventory.get_product_prices()
    expected = sorted(actual,reverse=True)
    assert actual == expected,f"expected prices high to low {expected}, but got {actual}"

# @pytest.mark.smoke
# @pytest.mark.parametrize("option_text, criteria", [
#     ("Name (A to Z)", "name_asc"),
#     ("Name (Z to A)", "name_desc"),
#     ("Price (low to high)", "price_asc"),
#     ("Price (high to low)", "price_desc")
# ])
# def test_product_sorting(browserInstance,login,option_text,criteria):
#     driver = browserInstance
#     page = InventoryPage(driver)
#
#     page.select_sort_option(option_text)
#
#     if "name" in criteria:
#         actual = page.get_product_names()
#         expected = sorted(actual) if "asc" in criteria else sorted(actual, reverse=True)
#         assert actual == expected, f"❌ Name sorting failed for {option_text}. Actual: {actual}, Expected: {expected}"
#
#     elif "price" in criteria:
#         actual = page.get_product_prices()
#         expected = sorted(actual) if "asc" in criteria else sorted(actual, reverse=True)
#         assert actual != expected, f"❌ Price sorting failed for {option_text}. Actual: {actual}, Expected: {expected}"
