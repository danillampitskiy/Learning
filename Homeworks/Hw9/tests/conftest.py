import pytest
from config import user_name, user_password
from selenium import webdriver

from cart_page import CartPage
from demoblaze_page import DemoBlazePage
from item_page import ItemPage


# To initialize WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# To initialize DemoBlaze page
@pytest.fixture
def demo_blaze_page(driver):
    page = DemoBlazePage(driver)
    page.open_url()
    yield page


# To initialize page with item
@pytest.fixture
def item_page(driver):
    page = ItemPage(driver)
    yield page


# To initialize page with cart
@pytest.fixture
def cart_page(driver):
    page = CartPage(driver)
    yield page

@pytest.fixture(scope="function")
def login_fixture(driver):
    home_page = DemoBlazePage(driver)
    home_page.click_login_button()
    home_page.setup_login_and_password(user_name, user_password)
    return home_page