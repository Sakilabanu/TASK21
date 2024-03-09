from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the WebDriver (assuming Chrome)
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.saucedemo.com/")

# Display cookies before login
print("Cookies before login:")
for cookie in driver.get_cookies():
    print(cookie)

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait for the inventory page to load
WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))

# Display cookies after login
print("\nCookies after login:")
for cookie in driver.get_cookies():
    print(cookie)

# Logout
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

# Close the browser
driver.quit()