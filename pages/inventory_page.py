from selenium.webdriver.common.by import By
from utils.waits import Waits


class InventoryPage:

    TITLE = (By.CLASS_NAME, "title")

    BACKPACK = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):

        return Waits.visible(
            self.driver,
            self.TITLE
        ).text

    def add_backpack_to_cart(self):

        Waits.clickable(
            self.driver,
            self.BACKPACK
        ).click()

    def get_cart_count(self):

        return Waits.visible(
            self.driver,
            self.CART_BADGE
        ).text
    
    PRODUCT_PRICE = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    def get_first_product_price(self):

        return Waits.visible(
        self.driver,
        self.PRODUCT_PRICE
    ).text