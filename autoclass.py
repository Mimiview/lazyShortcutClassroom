import time
import pyautogui

web_http = ["https://moodle.unive.it/course/view.php?id=5616", "https://moodle.unive.it/course/view.php?id=5641",
            "https://moodle.unive.it/course/view.php?id=5647", "https://moodle.unive.it/course/view.php?id=5694",
            "https://moodle.unive.it/course/view.php?id=7306"]

pixel_lessons = [[-1460, 455], [-1396, 658], [-1444, 872], [-1464, 469], [-1444, 538]]


def positioning():
    for i in range(10):
        time.sleep(1)
        print(pyautogui.position())


def press_search():
    pyautogui.keyDown('ctrl')
    pyautogui.press('f')
    pyautogui.keyUp('ctrl')


def open_windows():
    pyautogui.click(-1562, 1076)
    time.sleep(0.5)
    pyautogui.click(-1596, 52)
    pyautogui.typewrite(web_http[2])
    pyautogui.press('enter')
    # login page
    time.sleep(3)
    pyautogui.click(-1536, 434)
    time.sleep(2)
    pyautogui.click(-1043, 585)
    # search di lezioni da cambiare posizione per ognuna, a indice dei siti web corrisponderà la propria posizione
    press_search()
    pyautogui.typewrite("lezioni")
    pyautogui.click(pixel_lessons[2][0], pixel_lessons[2][1])  # qui bisogna cambiare

    # TODO da completare la parte di zoom e ricordarsi di fare una lista per la posizone del passcode


# positioning()


open_windows()


positioning()

