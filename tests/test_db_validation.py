from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from database.db_utils import DatabaseUtils


def test_product_price_matches_database(driver):

    driver.get(
        "https://www.saucedemo.com"
    )

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    ui_price = inventory.get_first_product_price()

    db_price = DatabaseUtils.get_product_price(
        "Sauce Labs Backpack"
    )

    assert ui_price == f"${db_price}"