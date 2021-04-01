import time
import pyautogui
from selenium import webdriver

driver = webdriver.Chrome("driver/chromedriver")
web_http = ["https://moodle.unive.it/mod/lti/launch.php?id=286767",  # BD
            "https://moodle.unive.it/mod/lti/launch.php?id=298281",  # IUM
            "https://moodle.unive.it/mod/lti/launch.php?id=301935",  # SO
            "https://moodle.unive.it/mod/lti/launch.php?id=229445",  # ASD
            "https://moodle.unive.it/mod/lti/launch.php?id=297564"]  # PO2


# sorta di main momentaneo
def open_windows():
    i = input("Scegliere tra \n1.Basi di dati \n2.IUM \n3.SO \n4.ASD Pelillo \n5.PO2\n")
    i = int(i)-1
    driver.get(i)
    # j = input("Hai già effettuato il login a moodle? Y/n ")
    assert "moodle" in driver.title
    # problema todo vedere per quale motivo si apre un nuovo ambiente di google


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


# open_windows()


positioning()
