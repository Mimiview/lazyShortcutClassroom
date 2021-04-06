import time
import pyautogui
from selenium import webdriver


driver = webdriver.Chrome("driver/chromedriver.exe")
web_http = ["https://moodle.unive.it/mod/lti/launch.php?id=286767",  # BD
            "https://moodle.unive.it/mod/lti/launch.php?id=298281",  # IUM
            "https://moodle.unive.it/mod/lti/launch.php?id=301935",  # SO
            "https://moodle.unive.it/mod/lti/launch.php?id=229445",  # ASD
            "https://moodle.unive.it/mod/lti/launch.php?id=297564"]  # PO2


# sorta di main momentaneo
def open_windows():
    driver.get(web_http[0])
    driver.find_element_by_class_name('//*[@id="region-main"]/div[1]/div/div/div/div/div/div/div[1]/a').click()
    # problema per quanto riguarda il click dell'elemnto per entrare nel moodle
    driver.close()
    # j = input("Hai già effettuato il login a moodle? Y/n ")
    # todo completare tutto ciò


# debugger per la posizione
def positioning():
    for i in range(10):
        time.sleep(1)
        print(pyautogui.position())


# utilizzare per fare il login in moodle (le credenziali salvale)
def login_page():
    time.sleep(4)
    pyautogui.click(-1536, 434)  # prima del login
    time.sleep(2)
    pyautogui.click(-1043, 585)  # login


def zoom_in(i):
    pyautogui.click(-124, 377)  # invitation
    time.sleep(2)
    crtl_shortcut('f')
    pyautogui.typewrite("")
    time.sleep(1)
    pyautogui.doubleClick(-1129, 487)  # posizione del passcode
    time.sleep(2)
    crtl_shortcut('c')
    time.sleep(2)
    pyautogui.click(-216, 376)  # posizione del join
    time.sleep(0.5)
    pyautogui.click(-216, 376)  # posizione del join
    time.sleep(8)
    pyautogui.click(828, 481)  # posizione della password
    crtl_shortcut('v')
    pyautogui.click(945, 657)  # poszione bottone per entrare


# shortucut find
def crtl_shortcut(letter):
    pyautogui.keyDown('ctrl')
    pyautogui.press(letter)
    pyautogui.keyUp('ctrl')


open_windows()


# positioning()
