from time import sleep
import RPi.GPIO as GPIO

DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
NSLEEP = 16 # Sleep GPIO Pin
MODE = (12, 7, 8)   # Microstep Resolution GPIO Pins
MICRO = 16
DELAY = 0.0008
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 7.5)
RESOLUTION = {1 : (0, 0, 0),
              2 : (1, 0, 0),
              4 : (0, 1, 0),
              8 : (1, 1, 0),
              16: (0, 0, 1),
              32: (1, 0, 1)}
REV = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(NSLEEP, GPIO.OUT)
GPIO.setup(MODE, GPIO.OUT)



GPIO.output(MODE, RESOLUTION[MICRO])
GPIO.output(NSLEEP, GPIO.HIGH)
GPIO.output(DIR, CW)



step_count = REV*SPR*MICRO
delay = DELAY/MICRO

sleep(0.5)
GPIO.output(DIR, CCW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay/2)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay/2)
    

GPIO.output(NSLEEP, GPIO.LOW)

GPIO.cleanup()