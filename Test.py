import pyautogui
import time

time.sleep(2)
iml = pyautogui.screenshot(region=(660,350,600,400))
iml.save(r"D:\Programfile\Programcode\aimbooster\saveimage.png")