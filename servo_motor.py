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
        self.pwm=GPIO.PWM(self.CONTROL_PIN, self.PWM_FREQ)
        self.pwm.start(0)
    def angle_to_duty_cycle(self, angle):
        angle=angle+90
        duty_cycle = (0.05 * self.PWM_FREQ) + (0.15 * self.PWM_FREQ * angle / 180)
        self.pwm.ChangeDutyCycle(duty_cycle)
        return True
    def pwm_stop(self):
        self.pwm.stop()
        return True
