import pyautogui
import sys
import time

print("Enter number of times to run commands")
print()
count =int(input())
print("Please switch to the screen you want automated")

time.sleep(2)

for i in range(count):
    pyautogui.hotkey("altleft", "r")
    time.sleep(0.5)
    pyautogui.hotkey("altleft", "y")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.write("Hello")
    time.sleep(0.5)
    pyautogui.hotkey("altleft", "o")
    time.sleep(0.5)