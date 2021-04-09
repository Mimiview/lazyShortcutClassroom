import time
import pyautogui
import requests as req
from selenium import webdriver

driver = webdriver.Chrome("driver/chromedriver.exe")
web_http = ["https://moodle.unive.it/mod/lti/launch.php?id=286767",  # BD
            "https://moodle.unive.it/mod/lti/launch.php?id=298281",  # IUM
            "https://moodle.unive.it/mod/lti/launch.php?id=301935",  # SO
            "https://moodle.unive.it/mod/lti/launch.php?id=229445",  # ASD
            "https://moodle.unive.it/mod/lti/launch.php?id=297564"]  # PO2

username = '882483@stud.unive.it'  # big problem about the @
password = ''  # one time with a gui we can manage it with a text field


def main_fun():
    driver.get(web_http[0])
    # todo  require a condition to verify if login is required
    login_fun()
    extract_pass()
    time.sleep(10)
    driver.close()


def extract_pass():
    # driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/textarea').click()
    resp = req.get("https://applications.zoom.us/api/v1/lti/rich/meeting/88578281421/invitation?lti_scid=ad82b86c546f32146d3c989ec16e8f1a0bfff43c5bbc111fa07dc0d91de9738c")
    resp = resp.text
    print(resp)


def login_fun():
    # click of the login unive main page, modify with a condition about the login. Used xpath because couldn't find his class name
    driver.find_element_by_xpath('//*[@id="region-main"]/div[1]/div/div/div/div/div/div/div[1]/a').click()
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("_eventId_proceed").click()


# position debugger
def positioning():
    for i in range(10):
        time.sleep(1)
        print(pyautogui.position())


# find shortcut
def crtl_shortcut(letter):
    pyautogui.keyDown('ctrl')
    pyautogui.press(letter)
    pyautogui.keyUp('ctrl')


main_fun()

# positioning()
