import pytest

from sauceDemo.pages.inventory_page import InventoryPage
from sauceDemo.tests.conftest import browserInstance



# @pytest.mark.smoke
def test_cart_badge_not_visible_when_cart_is_empty(browserInstance,login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    badge_count = inventory.get_cart_count()
    # Check if badge count is NOT present
    assert badge_count ==0,f"Expected no badge, but got count:{badge_count}"

def test_cart_badge_count_for_multiple_items(browserInstance, login):
    driver = browserInstance
    inventory = InventoryPage(driver)
    products = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    for product in products:
        inventory.add_product_to_cart_by_name(product)
    count = inventory.get_cart_count()
    print(f'cart count should {len(products)} and actual {count}')
    assert len(products) ==inventory.get_cart_count(),f"Expected cart badge count {len(products)}, got {count}"
# @pytest.mark.smoke
def test_cart_badge_updates_after_multiple_item_removed(browserInstance,login):
    """Verifies that the cart badge count updates correctly after removing multiple item item."""
    inventory = InventoryPage(browserInstance)
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Fleece Jacket"]
    for product in products_to_add:
        inventory.add_product_to_cart_by_name(product)

    removing_product = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    for product in removing_product:
        inventory.remove_product_by_name(product)
    inventory.remove_product_by_name(removing_product)
    print(inventory.get_cart_count())

    expected = len(products_to_add) - len(removing_product)
    actual = inventory.get_cart_count()
    assert expected == actual, f"expected{expected} but got {actual}"

# @pytest.mark.smoke
def test_cart_badge_updates_after_single_item_removed(browserInstance,login):
    """Verifies that the cart badge count updates correctly after removing one item."""
    inventory = InventoryPage(browserInstance)
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light","Sauce Labs Fleece Jacket"]
    for product in products_to_add:
        inventory.add_product_to_cart_by_name(product)

    removing_product = "Sauce Labs Backpack"
    inventory.remove_product_by_name(removing_product)
    print(inventory.get_cart_count())

    expected = len(products_to_add) -1
    print("prd len", len(products_to_add))
    actual = inventory.get_cart_count()
    assert expected == actual,f"expected{expected} but got {actual}"





