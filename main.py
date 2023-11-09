import getpixelcolor
from pyautogui import moveTo, click
from win32api import GetSystemMetrics

x = int(GetSystemMetrics(0)/2)
y = int(GetSystemMetrics(1)*0.936)

print("MAKE SURE TO RUN ME AS ADMINISTRATOR :3")

while(True):
    px = getpixelcolor.average(x-1, y, x+1, y+2)
    print(px)
    if (px == (3, 3, 3)):
        moveTo(x, y)
        click()
        print("Dialogue skipped!")