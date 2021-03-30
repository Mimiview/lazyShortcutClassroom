import time
import pyautogui

web_http = ["https://moodle.unive.it/course/view.php?id=5616", "https://moodle.unive.it/course/view.php?id=5641",
            "https://moodle.unive.it/course/view.php?id=5647", "https://moodle.unive.it/course/view.php?id=5694",
            "https://moodle.unive.it/course/view.php?id=7306"]

pixel_lessons = [[-1460, 455], [-1396, 658], [-1444, 872], [-1464, 469], [-1444, 538]]

pixel_zoom_lesson = []


# debugger per la posizione
def positioning():
    for i in range(10):
        time.sleep(1)
        print(pyautogui.position())


# questo è duro, ognuno ha il link per entrare sul portale zoom in posti diversi di moodle
def findLinkLesson(i, j):
    pyautogui.keyDown('ctrl')
    pyautogui.press('f')
    pyautogui.keyUp('ctrl')
    pyautogui.typewrite(j)
    pyautogui.click(pixel_lessons[i][0], pixel_lessons[i][1])


# apre chrome, nel mio caso si trova nella barra delle applicazioni
def open_chrome():
    pyautogui.click(-1562, 1076)
    time.sleep(1)
    pyautogui.click(-1596, 52)


# sorta di main momentaneo
def open_windows():
    i = input("Scegliere tra 1. Basi di dati 2. IUM 3.SO 4.ASD Pelillo 5.PO2")
    i = int(i)

    open_chrome()
    web_links(i)
    login_page()
    # search di lezioni da cambiare posizione per ognuna, a indice dei siti web corrisponderà la propria posizione
    findLinkLesson(1, "lesson")


# scrive sulla barra di nav. i link delle lezioni
def web_links(i):
    pyautogui.typewrite(web_http[i])
    pyautogui.press('enter')


# utilizzare per fare il login in moodle (le credenziali salvale)
def login_page():
    time.sleep(4)
    pyautogui.click(-1536, 434)
    time.sleep(2)
    pyautogui.click(-1043, 585)


# dentro il link di zoom, but TODO AMMA FINI
def zoom_in(i):
    pyautogui.click(-132, 377)
    findLinkLesson(i, "PASS")


# positioning()


# open_windows()


positioning()
