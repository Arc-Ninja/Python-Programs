#CREATOR: ARC NINJA // 20 OCT 2021
from os import truncate
import schedule as sc
import time
import pyautogui as pg

def openzoom():
    pg.moveTo(171, 859) #app shortcut location on desktop
    pg.doubleClick()
    pg.moveTo(741, 435, duration=15) #join meeting button location
    pg.click()
    pg.moveTo(745, 435, duration=5) #just to put some time delay 
    pg.write('85219852778', interval=0.25) #put zoom id here
    pg.keyDown('enter')
    pg.keyUp('enter')
    pg.moveTo(741, 438, duration=15) #again just for time delay
    pg.write('Study', interval=0.5) #put zoom password
    pg.keyDown('enter')
    pg.keyUp('enter')

sc.every().day.at("21:42").do(openzoom) #time of meeting

while True:
    sc.run_pending()
    time.sleep(1)

#thats it enjoy your sleep while you automatically get connected to your zoom meeting.

#SET-UP FOR AUTO START :-

#set the program file shortcut on the desktop > right click > properties > shortcut > run > minimised > apply > ok

#open RUN > type "shell:startup" > ok > the startup folder will open > copy the desktop shortcut > paste it in this startup folder.


#you are ready to go, now the program will start running automatically when u turn on ur computer.


#NOTE: THE PROGRAM MIGHT FAIL SOMETIMES IF YOU'R INTERNET SPEED IS TOO SLOW