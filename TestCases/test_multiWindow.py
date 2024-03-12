from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture()
def environment_setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    global driver
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    # DEFAULT PAGE LOAD TIMEOUT IS 30 SEC
    # driver.set_page_load_timeout(5)

    # GIVE DRIVER ADDITIONAL TIME TO FIND ELEMENT (IMPLICIT IS APPLIED TO EXISTENCE OF ELEMENT)
    # driver.implicitly_wait(20)

    driver.get("https://thetestingworld.com/testings")
    driver.maximize_window()

    # TAKING SCREENSHOT AT RUNTIME
    # driver.get_screenshot_as_file("C:/Users/johnny7sk/Desktop/Temp/Start_Test_Screenshot.png")
    yield
    # time.sleep(2)
    # driver.close()


def test_verify_registration(environment_setup):
    driver.find_element(By.XPATH, "//label[text()='Login']").click()

    # NOT WORKING, SITE BROKEN
    # driver.find_element(By.NAME, '_txtUserName').send_keys("test")
    # driver.find_element(By.NAME, '_txtPassword').send_keys('test')
    # driver.find_element(By.XPATH, "//input[@type='submit' and @value='Login']").click()

    driver.find_element(By.CSS_SELECTOR, "img[src='banner/5c33a68c8a29f.jpg']").click()
    two_windows = driver.window_handles
    driver.switch_to.window(two_windows[1])
    driver.find_element(By.ID, "W0wltc").click()

    pictures = driver.find_element(By.CLASS_NAME, "GKS7s")
    ActionChains(driver) \
        .key_down(Keys.LEFT_CONTROL) \
        .click(pictures) \
        .key_up(Keys.LEFT_CONTROL) \
        .perform()

    three_windows = driver.window_handles

    # closes windows in reversed order from higher list index
    for x in reversed(range(len(three_windows))):
        driver.switch_to.window(three_windows[x])
        time.sleep(2)
        driver.close()


