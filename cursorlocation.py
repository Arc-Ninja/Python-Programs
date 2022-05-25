import pyautogui as pg

x, y = pg.position()
x = str(x)
y = str(y)
with open("points.txt", "a") as f:
            f.write(x)
            f.write(",")
            f.write(y)
            f.write("\n")
