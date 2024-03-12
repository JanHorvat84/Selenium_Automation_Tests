from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = Firefox()
driver.get("https://thetestingworld.com/testings")

# Maximize browser
driver.maximize_window()

# Enter data to the textbox by name
driver.find_element(By.NAME, "fld_username").send_keys("Hello World")

# Enter data to the textbox by Xpath
driver.find_element(By.XPATH, "//input[@name='fld_email']").send_keys("johan@gaymail.com")

# Enter password by name
driver.find_element(By.NAME, "fld_password").send_keys("password")

# Confirm password by name
driver.find_element(By.NAME, "fld_cpassword").send_keys("password")

# Append test, clear first text and append new one
driver.find_element(By.NAME, "fld_username").clear()
driver.find_element(By.NAME, "fld_username").send_keys("and hello world")

# Working with radio button
driver.find_element(By.XPATH, "//input[@value='office']").click()

# Working on the checkbox
driver.find_element(By.NAME, "terms").click()

# # Working on the button
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Working with link
driver.find_element(By.LINK_TEXT, "Read Detail").click()

# 1. working with dropdown menu select by index
obj = Select(driver.find_element(By.NAME, "sex"))
obj.select_by_index(1)

# 2. working with dropdown menu select by value (value is in apostrophes)
obj = Select(driver.find_element(By.NAME, "sex"))
obj.select_by_value("2")

# 3. working with dropdown menu select by visible text
obj = Select(driver.find_element(By.NAME, "sex"))
obj.select_by_visible_text("Choose Gender")

obj = Select(driver.find_element(By.NAME, "country"))
obj.select_by_visible_text("Slovakia")

# closes after delay
time.sleep(3)
driver.close()
