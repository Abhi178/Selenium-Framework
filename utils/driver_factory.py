import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_driver():

    options = Options()

    if os.getenv("HEADLESS", "false").lower() == "true":

        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # CI Mode
        driver = webdriver.Chrome(
            options=options
        )

    else:

        # Local Mode
        service = Service(
            r"C:\Pytest_Projects\selenium_framework\drivers\chromedriver.exe"
        )

        driver = webdriver.Chrome(
            service=service,
            options=options
        )

    driver.maximize_window()

    return driver