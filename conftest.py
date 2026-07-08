import pytest
from utils.screenshot import take_screenshot
from utils.driver_factory import get_driver


@pytest.fixture
def driver():

    driver = get_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            take_screenshot(driver)
