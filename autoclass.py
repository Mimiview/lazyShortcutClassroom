import time
import pyautogui

web_http = ["https://moodle.unive.it/course/view.php?id=5616", "https://moodle.unive.it/course/view.php?id=5641",
            "https://moodle.unive.it/course/view.php?id=5647", "https://moodle.unive.it/course/view.php?id=5694",
            "https://moodle.unive.it/course/view.php?id=7306"]

pixel_lessons = [[-1460, 455], [-1396, 658], [-1444, 872], [-1464, 469], [-1444, 538]]

# TODO vedere tempo di responsing della pagina, mini problemi

# sorta di main momentaneo
def open_windows():
    i = input("Scegliere tra \n1.Basi di dati \n2.1IUM \n3.SO \n4.ASD Pelillo \n5.PO2\n")
    i = int(i)-1
    j = input("Hai già effettuato il login a moodle? Y/n ")
    open_chrome()
    web_links(i)
    if (j != "Y") or (j != "y"):  # TODO capire in che modo risolvere il fatto se si è collegati o meno
        print('flaggone matto')
        login_page()
    else:
        time.sleep(1)
    # search di lezioni da caFebbraio mbiare posizione per ognuna, a indice dei siti web corrisponderà la propria
    # posizione
    crtl_shortcut('f')
    findLinkLesson(i, "lezioni")
    zoom_in(i)


# debugger per la posizione
def positioning():
    for i in range(10):
        time.sleep(1)
        print(pyautogui.position())


# questo è duro, ognuno ha il link per entrare sul portale zoom in posti diversi di moodle
def findLinkLesson(i, j):
    pyautogui.typewrite(j)
    pyautogui.click(pixel_lessons[i][0], pixel_lessons[i][1])  # click Calendario lezioni
    time.sleep(1)


# apre chrome, nel mio caso si trova nella barra delle applicazioni
def open_chrome():
    pyautogui.click(-1562, 1076)  # click la barra delle applicazioni
    time.sleep(1)


# scrive sulla barra di nav. i link delle lezioni
def web_links(i):
    pyautogui.click(-1596, 52)  # barra di navigazione
    pyautogui.typewrite(web_http[i])
    pyautogui.press('enter')


# utilizzare per fare il login in moodle (le credenziali salvale)
def login_page():
    time.sleep(4)
    pyautogui.click(-1536, 434)  # prima del login
    time.sleep(2)
    pyautogui.click(-1043, 585)  # login


# dentro il link di zoom TODO mini problema per quanto riguarda il copying del passcode, vedere bene, e problema sul joi
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
