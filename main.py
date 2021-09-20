from time import sleep
import pyautogui as auto
import schedule
import webbrowser

link = "meet.google.com/abc123"

time = str(input("Time: ")) # hr:min      24hr format


def join():
    webbrowser.open_new_tab('https://' + link)
    sleep(7)
    #auto.hotkey('ctrl', 'd')
    #auto.hotkey('ctrl', 'e')
    auto.hotkey('command', 'd')
    auto.hotkey('command', 'e')
    auto.click(x, y) # change "x" & "y"
                     # go to locate.py

schedule.every().day.at(time).do(join)

while True:
    schedule.run_pending()
    sleep(1)