import pyautogui
import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

allchars = list(chars)

pwd = pyautogui.password("Enter password:")

samplepwd = ""

while(samplepwd != pwd):
    samplepwd = random.choices(allchars, k=len(pwd))

    print("<========" + str(samplepwd) + "========>")

    if(samplepwd == list(pwd)):
        print("The password is: " + "".join(samplepwd))
        break