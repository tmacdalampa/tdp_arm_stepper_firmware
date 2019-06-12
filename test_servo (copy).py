import time
from time import sleep
import sys
sys.path.insert(0,"/home/tmacdalampa/Downloads")

from nanpy.nanpy import servo

servo3_R=servo.Servo()

servo3_R.attached(7, 500, 2500)

for move in [0, 90, 180, 90, 0]:
    servo3_R.write(mvoe)
    time.sleep(1)
