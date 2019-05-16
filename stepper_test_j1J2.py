# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.

from time import sleep

import bigeasydriver
import RPi.GPIO as GPIO
import time
#t0=time.time()
#stepper1 = bigeasydriver.BigEasyDriver()
stepper1 = bigeasydriver.BigEasyDriver(en_pin=5, ms1_pin=6)
#stepper1.enable_pin = 5
#stepper1.MS1_pin = 6
stepper1.MS2_pin = 13
stepper1.MS3_pin = 19
stepper1.direction_pin = 26
stepper1.step_pin = 16

stepper1.begin()
stepper1.degrees_per_step = 1.8
stepper1.pulse_interval=10e-5

import numpy as np

stepper1.set_direction('ccw')
stepper1.set_stepsize('sixteenth step')

#different degrees and different angle
theta=[1, 5, 10, 45, 90, 180]
theta_j1=[j*2.95 for j in theta]
for i in range(0,6):
  t0=time.time()
  print(stepper1.move_degrees(theta_j1[i]))
  print (time.time()-t0, "seconds")
  sleep(1)

"""
#simple test
t0=time.time()
print(stepper.move_degrees(2.95*180))
print(time.time()-t0, "seconds")
"""
stepper.disable()
