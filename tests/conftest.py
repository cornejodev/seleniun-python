import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    # setup before running test function that is using fixture
    driver = webdriver.Chrome()
    driver.maximize_window()
    # execute anything that has to happen
    yield driver
    # once everything above has finished execution then quit the driver
    driver.quit()
