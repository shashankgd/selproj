import pytest
from selenium import webdriver

# Define browser fixture to start and close the browser.
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()  # Using Chrome as an example
    yield driver
    driver.quit()
