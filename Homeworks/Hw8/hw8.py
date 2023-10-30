from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")


password_field = driver.find_element(By.XPATH, "//input[@type='password']")
password_field.send_keys("secret_sauce")


login_button = driver.find_element(By.ID, "login-button")
login_button.click()


current_url = driver.current_url


expected_url = "https://www.saucedemo.com/inventory.html"

if current_url == expected_url:
    print("Login successful. Current URL matches the expected URL.")
else:
    print(f"Login failed. Current URL is {current_url}, expected URL is {expected_url}")


driver.quit()
