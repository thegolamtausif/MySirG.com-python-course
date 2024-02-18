import pyautogui
import time 
time.sleep(8)
count=0
while count<=50:
    pyautogui.typewrite(" hello ,miss koyel .\n how are you ?")
    pyautogui.press("enter")
    count=count+1