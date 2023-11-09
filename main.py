import getpixelcolor
from pyautogui import moveTo, click
from win32api import GetSystemMetrics

x = int(GetSystemMetrics(0)/2)
y = int(GetSystemMetrics(1)*0.9375)

print("MAKE SURE TO RUN ME AS ADMINISTRATOR :3")

while(True):
    px = getpixelcolor.pixel(x, y)
    if (px == (206, 190, 145)):
        moveTo(x, y)
        click()
        print("Dialogue skipped!")