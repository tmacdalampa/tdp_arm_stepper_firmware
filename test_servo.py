import RPi.GPIO as GPIO
import time
 
CONTROL_PIN = 17
PWM_FREQ = 50
STEP=15
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROL_PIN, GPIO.OUT)
 
pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
pwm.start(0)
 
def angle_to_duty_cycle(angle=0):
    duty_cycle = (0.05 * PWM_FREQ) + (0.2 * PWM_FREQ * angle / 180)
    #pwm.ChangeDutyCycle(duty_cycle)
    #dc=pwm.ChangeDutyCycle(duty_cycle)
    return duty_cycle
 
try:
    print('按下 Ctrl-C 可停止程式')
    """
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

     """
    pwm.ChangeDutyCycle(angle_to_duty_cycle(0))
    print('set to zero degree')
    angle=[0, 5, -5, 30, -30, 45, -45, 90, -90, 0]
    for i in range (0, 10):
      dc=angle_to_duty_cycle(angle[i])
      pwm.ChangeDutyCycle(dc)
      print(angle[i])
      time.sleep(2)
    pwm.ChangeDutyCycle(angle_to_duty_cycle(0))
    print('set to zero degree')

    #while True:
    #   next
except KeyboardInterrupt:
    print('關閉程式')
finally:
    print('finally')
    pwm.stop()
    GPIO.cleanup()
