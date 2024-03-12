from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# options to keep browser open
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get("https://thetestingworld.com/testings")

# Maximize browser
driver.maximize_window()


# Fetching title
print("Title of the page is: " + driver.title)

# # Fetch URL of page
print("Page URL is: " + driver.current_url)

# # Fetch complete Page HTML
print("**************************************************************")
# print(driver.page_source)

# # Fetching text from link
print("Text on link is: " + driver.find_element(By.CLASS_NAME, "displayPopup").text)

# # Fetching attribute value of element
print("Attribute of the element is: " + driver.find_element(By.XPATH, "//input[@type='submit']")
.get_attribute("value"))

# # Fetching data from dropdown menu selecting by visible text
obj = Select(driver.find_element(By.NAME, "sex"))
obj.select_by_visible_text("Male")
print(obj.first_selected_option.text)
print("****************************")
for op in obj.options:
    print(op.text)

obj = Select(driver.find_element(By.NAME, "country"))
obj.select_by_visible_text("Slovakia")

time.sleep(2)
driver.close()
