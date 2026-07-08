from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_to_cart(driver):

    driver.get(
        "https://www.saucedemo.com"
    )

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack_to_cart()

    assert inventory.get_cart_count() == "1"

    cart = CartPage(driver)

    cart.open_cart()

    assert (
        cart.get_cart_item_name()
        == "Sauce Labs Backpack"
    )