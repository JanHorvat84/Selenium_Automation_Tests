from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# import selenium.webdriver.support.expected_conditions as ec
import pytest
import time
# import Take_Screenshot
import logging


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
    time.sleep(2)
    driver.close()


def test_verify_registration(environment_setup):
    # ENTER DATA TO THE TEXTBOX BY NAME
    driver.find_element(By.NAME, "fld_username").send_keys("Hello World")
    
    # ENTER DATA TO THE TEXTBOX FIND BY XPATH
    driver.find_element(By.XPATH, "//input[@name='fld_email']").send_keys("johan@gaymail.com")
    
    # ENTER PASSWORD FIND BY NAME
    driver.find_element(By.NAME, "fld_password").send_keys("password")
    
    # CONFIRM PASSWORD FIND BY NAME
    driver.find_element(By.NAME, "fld_cpassword").send_keys("password")
    
    # # APPEND TEST, CLEAR FIRST TEXT AND APPEND NEW ONE
    # driver.find_element(By.NAME, "fld_username").clear()
    # driver.find_element(By.NAME, "fld_username").send_keys("and hello world")
    #
    # # WORKING WITH RADIO BUTTON FIND BY XPATH
    # driver.find_element(By.XPATH, "//input[@value='office']").click()
    #
    # # WORKING ON THE CHECKBOX FIND BY NAME
    # driver.find_element(By.NAME, "terms").click()
    #
    # # WORKING ON THE BUTTON FIND BY XPATH
    # driver.find_element(By.XPATH, "//input[@type='submit']").click()
    #
    # # WORKING WITH LINK FIND BY LINK TEXT
    # driver.find_element(By.LINK_TEXT, "Read Detail").click()
    #
    # # 1. working with dropdown menu select by index
    # obj = Select(driver.find_element(By.NAME, "sex"))
    # obj.select_by_index(1)
    #
    # # 2. working with dropdown menu select by value (value is in apostrophes)
    # obj = Select(driver.find_element(By.NAME, "sex"))
    # obj.select_by_value("2")
    #
    # # 3. working with dropdown menu select by visible text
    # obj = Select(driver.find_element(By.NAME, "sex"))
    # obj.select_by_visible_text("Choose Gender")
    #
    # # EXPLICIT TIMEOUT
    # wait = WebDriverWait(driver, 10)
    # wait.until(ec.text_to_be_present_in_element((By.ID, "countryId"), "Slovakia"))
    # obj = Select(driver.find_element(By.ID, "countryId"))
    #
    # obj.select_by_visible_text("Slovakia")
    #
    # wait = WebDriverWait(driver, 10)
    # wait.until(ec.text_to_be_present_in_element((By.ID, "stateId"), "Banskobystricky"))
    # obj = Select(driver.find_element(By.ID, "stateId"))
    #
    # obj.select_by_visible_text("Banskobystricky")
    #
    # # TAKE SCREENSHOT AT RUNTIME AFTER FILLING FORM BY SEPARATED METHOD
    # Take_Screenshot.take_page_screenshot(driver, "End_Test_Screenshot")
    #
    # USING JAVASCRIPT (for example - scrollbar is not part of page, no HTML content..., lines are separated by ;)
    # driver.execute_script("window.scrollTo(0,5000);")
    #
    # MULTI WINDOW HANDLING (NOT WORKING - PAGE ACCESS DENIED, JUST EXAMPLE)
    # driver.get("https://www.naukri.com")
    # allwindow = driver.window_handles
    # for win in allwindow:
    #     driver.switch_to.window(win)
    #     print(driver.current_url)

    # MULTI WINDOW HANDLING - TABS HANDLING
    # driver.find_element(By.XPATH, "//label[text()='Login']").click()
    # driver.find_element(By.NAME, "_txtUserName").send_keys("test")
    # driver.find_element(By.NAME, "_txtPassword").send_keys("test")
    # driver.find_element(By.XPATH, "//img[@src='banner/64625f639e847.png']").click()
    #
    # all_tabs = driver.window_handles
    # print(all_tabs)
    #
    # for tab in all_tabs:
    #     driver.switch_to.window(tab)
    #     if driver.current_url == "https://t.me/joinchat/GgRlDbOsbSzkJElL":
    #         driver.find_element(By.XPATH, "//a[@class = 'tgme_head_right_btn']").click()

    # CHECKS IF EXPECTED CONDITIONS MET RESULTS
    assert driver.current_url == "https://thetestingworld.com/testings/"

    # CREATING LOG FILES
    # log = logging.getLogger(__name__)
    # log.setLevel(logging.DEBUG)

    # warn = logging.FileHandler('Warning_logs.txt')
    # warn.setLevel(logging.WARNING)

    # info = logging.FileHandler('Info_logs.txt')
    # info.setLevel(logging.INFO)

    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # warn.setFormatter(formatter)
    # info.setFormatter(formatter)

    # log.info("[My URL is opened]")
    # log.warning("[There is a delay in opening of browser")
