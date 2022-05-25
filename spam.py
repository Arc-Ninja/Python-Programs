import pyautogui as pg
import time
text = "~Cocky cock~"
time.sleep(2)
for i in range (0,100):
        pg.write(text, interval = 0.0000000000000000001)
        pg.press('enter')