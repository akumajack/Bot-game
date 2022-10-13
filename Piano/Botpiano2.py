from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#Tile 1 Position x: 364 y: 500 RGB:(0, 0, 0)
#Tile 2 Position x: 455 y: 500 RGB:(0, 0, 0)
#Tile 3 Position x: 629 y: 500 RGB:(0, 0, 0)
#Tile 4 Position x: 552 y: 500 RGB:(0, 0, 0)
print("Ready")
#pyautogui.click(x=100, y=200) move to 100,200,then lick the left mouse butoon.
# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#     time.sleep(0.01) #This pauses the script for 0.001 seconds
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click(x,y):

    pyautogui.click()

while keyboard.is_pressed('q') == False:
    

    if pyautogui.pixel(365, 400)[0] == 0:
        click(365, 400)
    if pyautogui.pixel(455, 400)[0] == 0:
        click(455, 400)
    if pyautogui.pixel(522, 400)[0] == 0:
        click(545, 400)
    if pyautogui.pixel(629, 400)[0] == 0:
        click(630, 400)

print("Exit")