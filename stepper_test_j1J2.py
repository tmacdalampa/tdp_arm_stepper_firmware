# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.

from time import sleep

import bigeasydriver
import servo_motor
import RPi.GPIO as GPIO
import time

#宣告六顆馬達
stepper1 = bigeasydriver.BigEasyDriver(en_pin=5, ms1_pin=6, ms2_pin=13, ms3_pin=19, direction_pin=26, step_pin=16, degrees_per_step = 1.8, pulse_interval=10e-5)
stepper2 = bigeasydriver.BigEasyDriver(en_pin=5, ms1_pin=6, ms2_pin=13, ms3_pin=19, direction_pin=20, step_pin=21, degrees_per_step = 1.8, pulse_interval=10e-5)
stepper3 = bigeasydriver.BigEasyDriver(en_pin=5, ms1_pin=6, ms2_pin=13, ms3_pin=19, direction_pin=8, step_pin=7, degrees_per_step = 1.8, pulse_interval=10e-5)
servo4=servo_motor.ServoMotor(control_pin=17, pwm_freq=50)
servo5=servo_motor.ServoMotor(control_pin=27, pwm_freq=50)
servo6=servo_motor.ServoMotor(control_pin=22, pwm_freq=50)

stepper1.begin()
stepper2.begin()
stepper3.begin()
servo4.begin()
servo5.begin()
servo6.begin()

import numpy as np

stepper1.set_stepsize('sixteenth step')
stepper2.set_stepsize('sixteenth step')
stepper3.set_stepsize('sixteenth step')

theta=[5, -5, 10, -10, 45, -45, 90, -90, 180, -180]
theta_j1=[j*2.95 for j in theta]
theta_j2=[j*20.72 for j in theta]
theta_j3=[j*5.18 for j in theta]
angle=[0, 5, 10, 45, 90, 135, 180, 0]

try:
  for i in range(0,8):
    t0=time.time()
    print(stepper1.move_degrees(theta_j1[i]),
          stepper2.move_degrees(theta_j2[i]),
          stepper3.move_degrees(theta_j3[i]),
          servo4.angle_to_duty_cycle(angle[i]),
          servo5.angle_to_duty_cycle(angle[i]),
          servo6.angle_to_duty_cycle(angle[i]))
    sleep(1)
except KeyboardInterrupt:
  print('close')
finally:
  print('finally')
  stepper1.disable()
  stepper2.disable()
  stepper3.disable()
  servo4.pwm_stop
  servo5.pwm_stop
  servo6.pwm_stop
  GPIO.cleanup()
  
