from math import floor

import RPi.GPIO as GPIO
import time


class ServoMotor(object):
    def __init__(self, control_pin, pwm_freq):
        self.CONTROL_PIN = control_pin
        self.PWM_FREQ = pwm_freq
        #self.STEP= STEP

    def begin(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.CONTROL_PIN, GPIO.OUT)
        pwm = GPIO.PWM(self.CONTROL_PIN, self.PWM_FREQ)

    def angle_to_PWM(self, angle):
        pwm = GPIO.PWM(self.CONTROL_PIN, self.PWM_FREQ)
        pwm.start(0)
        duty_cycle = (0.05 * self.PWM_FREQ) + (0.2 * self.PWM_FREQ * angle / 180)
        dc=pwm.ChangeDutyCycle(duty_cycle)
        pwm.stop()
        GPIO.cleanup()
        return dc

