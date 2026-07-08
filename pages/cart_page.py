from selenium.webdriver.common.by import By
from utils.waits import Waits


class CartPage:

    CART_LINK = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    CART_ITEM = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):

        Waits.clickable(
            self.driver,
            self.CART_LINK
        ).click()

    def get_cart_item_name(self):

        return Waits.visible(
            self.driver,
            self.CART_ITEM
        ).text