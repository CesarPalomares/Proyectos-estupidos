from pynput.mouse import Controller
import time

time.sleep(3)

raton = Controller()

pos = raton.position

print(pos)