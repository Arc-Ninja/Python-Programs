import pyautogui as pg
import time
def spam():
        text = input("Enter text to spam: ")
        try:
            amt = int(input("Enter number of times to spam: "))
            time.sleep(2)
            while amt>0:
                pg.write(text, interval= 0.000001)
                pg.press('enter')
                amt -= 1
        except:
            print("Enter integer as the amount to spam")
    
