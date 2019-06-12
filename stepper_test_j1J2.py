# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.

from time import sleep

import bigeasydriver
import servo_motor
import RPi.GPIO as GPIO
import time
from nanpy import Servo
#宣告六
stepper1 = bigeasydriver.BigEasyDriver(en_pin=5, ms1_pin=6, ms2_pin=13, ms3_pin=19, direction_pin=26, step_pin=16, degrees_per_step = 1.8, pulse_interval=10e-5)
stepper2 = bigeasydriver.BigEasyDriver(en_pin=5, ms1_pin=6, ms2_pin=13, ms3_pin=19, direction_pin=20, step_pin=21, degrees_per_step = 1.8, pulse_interval=10e-5)
servo3R=Servo(7)
servo3L=Servo(8)
servo4=Servo(9)
servo5=Servo(10)
servo6=Servo(11)

stepper1.begin()
stepper2.begin()

import numpy as np

stepper1.set_stepsize('sixteenth step')
stepper2.set_stepsize('sixteenth step')

#jointspace
theta1=[-90, 90]
theta2=[-70, 70]

#motorspace 
theta_j1=[j*2.95 for j in theta1]
theta_j2=[j*30 for j in theta2]

try:
  t0=time.time()
  print(stepper1.move_degrees(90*2.95))
  sleep(2)
  print(stepper2.move_degrees(-90*30))
  sleep(2)

       
  for pos in range(90, 180, 2):
    servo3L.write(pos)
    servo3R.write(180-pos)
    servo5.write(180-pos)
    print('motor3 &5', pos)
    time.sleep(0.015)

  for pos in range(181, 90,-2):
    servo3L.write(pos-1)
    servo3R.write(181-pos)
    servo5.write(181-pos)
    print('motor3&5', pos-1)
    time.sleep(0.015)
  sleep(2)


    
  print(stepper2.move_degrees(90*30))
  sleep(2)
  print(stepper1.move_degrees(-90*2.95))
  sleep(2)

  for move in [0, 90, 180, 0]:
    servo4.write(move)
    servo6.write(move)
    time.sleep(1)
        
except KeyboardInterrupt:
  print('close')
finally:
  print('finally')
  stepper1.disable()
  stepper2.disable()
  GPIO.cleanup()
  
  
