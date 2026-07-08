from datetime import datetime
import os


def take_screenshot(driver):

    os.makedirs(
        "screenshots",
        exist_ok=True
    )

    filename = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    path = f"screenshots/{filename}.png"

    driver.save_screenshot(path)

    return path
