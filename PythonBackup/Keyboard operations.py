from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# necessary to keep Chrome browser open
option = Options()
option.add_experimental_option("detach", True)

driver = Chrome(options=option)
driver.get("https://thetestingworld.com/testings")

# finds element on website by name and writes text to textfield
driver.find_element(By.NAME, "fld_username").send_keys("Sign in")

# creates object for using key caps
act = ActionChains(driver)

# automatically presses Tab key
act.send_keys(Keys.TAB).perform()

# select all data from textbox and copies it to next textfield
act.key_down(Keys.CONTROL)\
    .send_keys("a")\
    .send_keys("c")\
    .key_up(Keys.CONTROL)\
    .send_keys(Keys.TAB)\
    .key_down(Keys.CONTROL)\
    .send_keys("v").perform()
