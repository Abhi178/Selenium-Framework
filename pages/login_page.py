from selenium.webdriver.common.by import By
from utils.waits import Waits




class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver


    def enter_username(self, username):

        Waits.visible(
            self.driver,
            self.USERNAME
        ).send_keys(username)

    def enter_password(self, password):

        Waits.visible(
            self.driver,
            self.PASSWORD
        ).send_keys(password)

    def click_login(self):

        Waits.clickable(
            self.driver,
            self.LOGIN
        ).click()

    def login(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()