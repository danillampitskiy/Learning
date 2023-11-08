import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait



def test_login(driver):
    driver.get("https://www.demoblaze.com/")


    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    login_button.click()

    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "loginusername"))
    )
    username_field.send_keys("danil666")

    password_field = driver.find_element(By.ID, "loginpassword")
    password_field.send_keys("Qwerty123")

    login_button1 = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
    login_button1.click()

    time.sleep(5)

    logout_button = driver.find_element(By.ID, "logout2")

    assert logout_button.is_displayed()
    assert "Welcome danil666" in driver.find_element(By.XPATH, "/html/body").text

def test_add_to_cart(driver):
    driver.get("https://www.demoblaze.com/")


    wait = WebDriverWait(driver, timeout=5)

    login_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    login_button.click()

    username_field = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "loginusername"))
    )
    username_field.send_keys("danil666")

    password_field = driver.find_element(By.ID, "loginpassword")
    password_field.send_keys("Qwerty123")

    login_button1 = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
    login_button1.click()

    monitors_element_found = False
    while not monitors_element_found:
        try:
            monitors_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@onclick=\"byCat('monitor')\"]"))
            )
            monitors_element.click()
            monitors_element_found = True
        except StaleElementReferenceException:
            pass

    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card h-100']")))

    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    max_price = 0
    max_price_elem = None
    for product in products:
        try:
            price_elem = product.find_element(By.XPATH, ".//h5")

            if price_elem.text.startswith('$'):
                price = int(price_elem.text[1:])

                if price > max_price:
                    max_price = price
                    max_price_elem = product
        except Exception as e:
            print(f"Error while finding elements or parsing: {e}")

    if max_price_elem:
        max_price_product = max_price_elem.find_element(By.XPATH, ".//h4/a")
        product_name = max_price_product.text
        product_price = max_price_elem.find_element(By.XPATH, ".//h5").text[1:]
        max_price_product.click()
    else:
        pytest.fail("Couldn't locate the highest price product element")

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@onclick='addToCart(10)']")))

    assert product_name is not None and product_name in driver.page_source, "Product name not found on the product page"
    assert product_price in driver.find_element(By.XPATH, "/html/body").text

    add_to_cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Add to cart')]")
    add_to_cart_button.click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    driver.switch_to.default_content()

    cart_button = driver.find_element(By.ID, "cartur")
    cart_button.click()

    time.sleep(5)

    assert product_name in driver.find_element(By.XPATH, "/html/body").text
    assert product_price in driver.find_element(By.XPATH, "/html/body").text

if __name__ == "__main__":
    pytest.main()