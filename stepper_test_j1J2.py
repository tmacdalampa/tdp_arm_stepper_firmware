# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.

from time import sleep

import bigeasydriver
import servo_motor
import RPi.GPIO as GPIO
import time

stepper1 = bigeasydriver.BigEasyDriver(en_pin=5, ms1_pin=6, ms2_pin=13, ms3_pin=19, direction_pin=26, step_pin=16, degrees_per_step = 1.8, pulse_interval=10e-5)
stepper2 = bigeasydriver.BigEasyDriver(en_pin=5, ms1_pin=6, ms2_pin=13, ms3_pin=19, direction_pin=20, step_pin=21, degrees_per_step = 1.8, pulse_interval=10e-5)
servo4=servo_motor.ServoMotor(control_pin=17, pwm_freq=50)

stepper1.begin()
stepper2.begin()
servo4.begin()


import numpy as np

stepper1.set_stepsize('sixteenth step')
stepper2.set_stepsize('sixteenth step')

theta=[5, -5, 10, -10, 45, -45, 90, -90, 180, -180]
theta_j1=[j*2.95 for j in theta]
theta_j2=[j*20.72 for j in theta]
for i in range(0,8):
  t0=time.time()
  print(stepper1.move_degrees(theta_j1[i]),
        stepper2.move_degrees(theta_j2[i]),
        servo4.angle_to_PWM(theta[i]))
  sleep(1)



stepper1.disable()
stepper2.disable()
servo4.disable()
