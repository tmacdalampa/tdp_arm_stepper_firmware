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
stepper.degrees_per_step = 0.9
stepper.pulse_interval=10e-5

import numpy as np

#stepper.set_direction('ccw')
stepper.set_stepsize('sixteenth step')

#different degrees and different angle

theta=[1, -1, 5, -5, 10, -10, 45, -45, 90, -90, 180, -180]
for i in range(0,12):
  t0=time.time()
  print(stepper.move_degrees(theta[i]))
  print (time.time()-t0, "seconds")
  sleep(1)
 # stepper.set_direction('cw')
 # t0=time.time()
 # print(stepper.move_degrees(theta[i]))
 # print (time.time()-t0, "seconds")
 # sleep(1)
"""
#simple test
t0=time.time()
print(stepper.move_degrees(180))
print(time.time()-t0, "seconds")
"""
stepper.disable()
