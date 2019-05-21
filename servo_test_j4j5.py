# Copyright (c) 2017-2025 John R. Leeman
# Distributed under the terms of the MIT License.
import time
from time import sleep
import RPi.GPIO as GPIO
import servo_motor

servo4=servo_motor.ServoMotor(control_pin=17, pwm_freq=50)
servo5=servo_motor.ServoMotor(control_pin=27, pwm_freq=50)
servo4.begin()
servo5.begin()
#pwm=GPIO.PWM(servo4.CONTROL_PIN, servo4.PWM_FREQ)
#pwm.start(0)

import numpy as np
try:
  #pwm.ChangeDutyCycle(0)
  #print('set to zero degree')
  #sleep(1)

  theta=[0, 5, 10, 45, 90, 180, 0]
  for i in range(0,7):
    t0=time.time()
    servo4.angle_to_duty_cycle(theta[i])
    servo5.angle_to_duty_cycle(theta[i])
    print(theta[i])
    sleep(1)
     
except KeyboardInterrupt:
  print('close')
finally:
  print('finally')
  #pwm.ChangeDutyCycle(0)
  #print('set to zero at the end')
  servo4.pwm_stop
  servo5.pwm_stop
  GPIO.cleanup()
