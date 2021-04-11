import time
import pyautogui
from selenium import webdriver

driver = webdriver.Chrome("driver/chromedriver.exe")
web_http = ["https://moodle.unive.it/mod/lti/launch.php?id=286767",  # BD
            "https://moodle.unive.it/mod/lti/launch.php?id=298281",  # IUM
            "https://moodle.unive.it/mod/lti/launch.php?id=301935",  # SO
            "https://moodle.unive.it/mod/lti/launch.php?id=229445",  # ASD
            "https://moodle.unive.it/mod/lti/launch.php?id=297564"]  # PO2

username = '882483@stud.unive.it'
password = ''  # one time with a gui we can manage it with a text field

list_password = ['rt3xxq', ['4r643d', '0g008t'], 'SO2021', '6n413q']


def auto_fun(x):
    driver.get(web_http[x])
    login_fun()
    zoom_opening()
    time.sleep(1)
    passcode_zoom(x)
    driver.close()


def passcode_zoom(x):  # todo fammi sto typewrite bonu
    if x == 1:
        pyautogui.typewrite(web_http[x][0])
    else:
        pyautogui.typewrite(web_http[x])
    time.sleep(1)
    pyautogui.click(924, 651)


def zoom_opening():  # todo vedere in che modo con locateScreen riuscire a gettare il passcode e accedere a zoom
    time.sleep(0.5)
    pyautogui.moveTo(759, 404)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(574, 244)
    pyautogui.click()


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


auto_fun(0)

