# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.

from time import sleep

import bigeasydriver
import RPi.GPIO as GPIO
import time
#t0=time.time()
stepper = bigeasydriver.BigEasyDriver()
stepper.enable_pin = 5
stepper.MS1_pin = 6
stepper.MS2_pin = 13
stepper.MS3_pin = 19
stepper.direction_pin = 26
stepper.step_pin = 16

stepper.begin()
stepper.degrees_per_step = 1.8

import numpy as np

stepper.set_direction('ccw')
stepper.set_stepsize('sixteenth step')

#different degrees and different angle
theta=[1, 5, 10, 45, 90, 180]*2.95
for i in range(0,6):
  t0=time.time()
  print(stepper.move_degrees(theta[i]))
  print (time.time()-t0, "seconds")
  sleep(1)

"""
#simple test
t0=time.time()
print(stepper.move_degrees(180))
print(time.time()-t0, "seconds")
"""
stepper.disable()
