from time import sleep
import RPi.GPIO as GPIO

DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
NSLEEP = 16 # Sleep GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 7.5)


GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(NSLEEP, GPIO.OUT)

GPIO.output(DIR, CW)
GPIO.output(NSLEEP, GPIO.HIGH)

step_count = SPR
delay = 0.004

sleep(0.5)
GPIO.output(DIR, CCW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
    delay = delay - 0.000002
    

GPIO.output(NSLEEP, GPIO.LOW)

GPIO.cleanup()