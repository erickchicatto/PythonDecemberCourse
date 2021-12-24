#https://pyautogui.readthedocs.io/en/latest/mouse.html

import pyautogui, sys

def moveMouse():
    pyautogui.moveTo(1107, 749) 
    pyautogui.click()
    print("This is ok ")


print('Press Ctrl-C to quit')

try:
    while True:
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)  
except KeyboardInterrupt:
    print('\n')
    moveMouse()

#main
