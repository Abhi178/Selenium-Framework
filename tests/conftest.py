import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
    # ✅ Disable proxy (corporate environment fix)
    os.environ["HTTP_PROXY"] = ""
    os.environ["HTTPS_PROXY"] = ""
    os.environ["NO_PROXY"] = "localhost,127.0.0.1"

    # ✅ Use local chromedriver
    service = Service(r"C:\Pytest_Projects\selenium_framework\drivers\chromedriver.exe")

    options = Options()
    options.add_argument("--no-proxy-server")
    options.add_argument("--proxy-server=direct://")
    options.add_argument("--proxy-bypass-list=*")

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    yield driver
    driver.quit()