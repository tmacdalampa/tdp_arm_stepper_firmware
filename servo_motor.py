from math import floor

import RPi.GPIO as GPIO
import time


class ServoMotor(object):

    def __init__(self, control_pin, PWM_FREQ, STEP)
        self.CONTROL_PIN = control_pin
        self.PWM_FREQ = PWM_FREQ
        #self.STEP= STEP

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.CONTROL_PIN, GPIO.OUT)

        pwm = GPIO.PWM(self.CONTROL_PIN, self.PWM_FREQ)
        pwm.start(0)

    def angle_to_PWM(angle=0):
        duty_cycle = (0.05 * self.PWM_FREQ) + (0.2 * self.PWM_FREQ * angle / 180)
        dc=pwm.ChangeDutyCycle(duty_cycle)
        return dc

    PWM.stop()
    GPIO.cleanup()
"""
try:
    print('按下 Ctrl-C 可停止程式')
    for angle in range(0, 181, STEP):
        dc = angle_to_duty_cycle(angle)
        pwm.ChangeDutyCycle(dc)
        print('角度={: >3}, 工作週期={:.2f}'.format(angle, dc))
        time.sleep(2)
    for angle in range(180, -1, -STEP):
        dc = angle_to_duty_cycle(angle)
        print('角度={: >3}, 工作週期={:.2f}'.format(angle, dc))
        pwm.ChangeDutyCycle(dc)
        time.sleep(2)
    pwm.ChangeDutyCycle(angle_to_duty_cycle(0))
    while True:
        next
except KeyboardInterrupt:
    print('關閉程式')
finally:
    pwm.stop()
    GPIO.cleanup()
