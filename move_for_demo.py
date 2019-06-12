# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.

from time import sleep

import bigeasydriver
import servo_motor
import RPi.GPIO as GPIO
import time
from nanpy import Servo
#宣告六軸
stepper1 = bigeasydriver.BigEasyDriver(en_pin=5, ms1_pin=6, ms2_pin=13, ms3_pin=19, direction_pin=26, step_pin=16, degrees_per_step = 1.8, pulse_interval=10e-5)
stepper2 = bigeasydriver.BigEasyDriver(en_pin=5, ms1_pin=6, ms2_pin=13, ms3_pin=19, direction_pin=20, step_pin=21, degrees_per_step = 1.8, pulse_interval=10e-5)
servo3R=Servo(7)
servo3L=Servo(8)
#servo4=Servo(9)
servo5=Servo(10)
#servo6=Servo(11)
servo7=Servo(12) #宣告夾具
servo7.write(0) #夾具打開

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
  print(stepper2.move_degrees(-60*30))  #第二軸往下轉60
  sleep(2)

       
  for pos in range(90, 150, 2):   #第三五軸往下轉60
    servo3L.write(pos)
    servo3R.write(180-pos)
    servo5.write(180-pos)
    print('motor3 &5', pos)
    time.sleep(0.015)
  sleep(0.5)

  servo7.write(60) #夾具夾
  sleep(0.5)

  print(stepper2.move_degrees(30*30)) #第二軸稍微往上轉
  sleep(2)

  print(stepper1.move_degrees(90*2.95)) #第一軸轉
  sleep(2)

  print(stepper2.move_degrees(-30*30)) #第二軸往下轉
  sleep(2)

  servo7.write(0) #夾具放開
  sleep(1)
  
  for pos in range(181, 90,-2):  #第三五軸轉回去
    servo3L.write(pos-1)
    servo3R.write(181-pos)
    servo5.write(181-pos)
    print('motor3&5', pos-1)
    time.sleep(0.015)
  sleep(2)

  print(stepper2.move_degrees(60*30)) #第二軸轉回去
  sleep(2)

  print(stepper1.move_degrees(-90*2.95)) #第一軸轉回去
  sleep(2)


        
except KeyboardInterrupt:
  print('close')
finally:
  print('finally')
  stepper1.disable()
  stepper2.disable()
  GPIO.cleanup()
  
  
