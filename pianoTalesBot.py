from PIL import ImageGrab,Image
from pynput.mouse import Controller, Button
import cv2, time
import numpy as np

raton = Controller()

time.sleep(4)

pos1 = 340,raton.position[1]
pos2 = 430,raton.position[1]
pos3 = 520,raton.position[1]
pos4 = 620, raton.position[1]
print(pos1)

while True:
    screen = np.array(ImageGrab.grab(bbox=None))
    gris = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
    #cv2.imshow('Python Window', gris)



    color1 = gris[pos1[0],pos1[1]]
    color2 = gris[pos2[0],pos2[1]]
    color3 = gris[pos3[0], pos3[1]]
    color4 = gris[pos4[0], pos4[1]]

    if color1 == 0:
        print("Negro")
        raton.position = (pos1)
        raton.press(Button.left)
        raton.release(Button.left)

    if color2 == 0:
        print("Negro")
        raton.position = (pos2)
        raton.press(Button.left)
        raton.release(Button.left)

    if color3 == 0:
        print("Negro")
        raton.position = (pos3)
        raton.press(Button.left)
        raton.release(Button.left)

    if color4 == 0:
        print("Negro")
        raton.position = (pos4)
        raton.press(Button.left)
        raton.release(Button.left)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break