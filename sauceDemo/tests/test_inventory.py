import time

import pytest

from sauceDemo.pages.inventory_page import InventoryPage
from sauceDemo.pages.login_page import LoginPage

# @pytest.mark.usefixtures("browserInstance","login")
# class TestInventory:
#
#     def test_inventory(self, browserInstance):
#         driver = browserInstance
#         inventory = InventoryPage(driver)
#         var = inventory.click_menu()
#         print("fghjkl",var)
#
#         assert "Logout" ==var," failed not match"
#         time.sleep(1)
#
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

@pytest.mark.smoke
def test_sort_product_high_to_low(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    inventory.select_sort_option("Price (high to low)")
    actual =inventory.get_product_prices()
    expected = sorted(actual,reverse=True)
    assert actual == expected,f"expected prices high to low {expected}, but got {actual}"

# @pytest.mark.smoke
@pytest.mark.parametrize("option_text, criteria", [
    ("Name (A to Z)", "name_asc"),
    ("Name (Z to A)", "name_desc"),
    ("Price (low to high)", "price_asc"),
    ("Price (high to low)", "price_desc")
])
def test_product_sorting(browserInstance,login,option_text,criteria):
    driver = browserInstance
    page = InventoryPage(driver)

    page.select_sort_option(option_text)

    if "name" in criteria:
        actual = page.get_product_names()
        expected = sorted(actual) if "asc" in criteria else sorted(actual, reverse=True)
        assert actual == expected, f"❌ Name sorting failed for {option_text}. Actual: {actual}, Expected: {expected}"

    elif "price" in criteria:
        actual = page.get_product_prices()
        expected = sorted(actual) if "asc" in criteria else sorted(actual, reverse=True)
        assert actual != expected, f"❌ Price sorting failed for {option_text}. Actual: {actual}, Expected: {expected}"
