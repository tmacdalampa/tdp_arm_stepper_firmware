# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.
import time
from time import sleep

import servo_motor

servo4=servo_motor.ServoMotor(control_pin=17, pwm_freq=50)

servo4.begin()

import numpy as np

theta=[5, -5, 10, -10, 45, -45, 90, -90, 180, -180]
for i in range(0,8):
  t0=time.time()
  print(servo4.angle_to_PWM(theta[i]))
  sleep(1)

servo4.disable()
