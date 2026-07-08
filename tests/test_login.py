from pages.login_page import LoginPage

from utils.config_reader import BASE_URL

#from utils.json_reader import read_login_data
import pytest

#test_data = read_login_data()


#@pytest.mark.parametrize("user", test_data)
def test_valid_login(driver):


    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory" in driver.current_url