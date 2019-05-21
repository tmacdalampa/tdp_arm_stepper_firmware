from math import floor

import RPi.GPIO as GPIO
import time


class ServoMotor(object):
    def __init__(self, control_pin, pwm_freq):
        self.CONTROL_PIN = control_pin
        self.PWM_FREQ = pwm_freq

    def begin(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.CONTROL_PIN, GPIO.OUT)
        
    def angle_to_duty_cycle(self, angle):
        duty_cycle = (0.05 * self.PWM_FREQ) + (0.2 * self.PWM_FREQ * angle / 180)
        return duty_cycle

