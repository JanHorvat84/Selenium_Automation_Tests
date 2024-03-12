from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Action chains import for using actions preformed by mouse
from selenium.webdriver.common.action_chains import ActionChains
import time

# necessary to keep Chrome browser open
options = Options()
options.add_experimental_option("detach", True)

driver = Chrome(options=options)
driver.get("https://thetestingworld.com")
act = ActionChains(driver)

# context click on element found by Xpath
quickdemo = driver.find_element(By.XPATH, "//a[text()='Quick Demo']")
act.click(quickdemo).perform()

# hover mouse on element found by Xpath
tutorial = driver.find_element(By.XPATH, "//span[contains(text(), 'TUTORIAL')]")
act.move_to_element(tutorial)


# left click, double click and right click anywhere on site (right click opens options)
act.click().perform()
act.double_click().perform()
act.context_click().perform()
