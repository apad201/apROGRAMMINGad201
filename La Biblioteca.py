#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class LED:
    

GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO_LEDA = 4
GPIO_LEDB = 17
GPIO_LEDC = 22


print "Starting Program"
print "Auto Mode On"

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LEDA, GPIO.OUT)
GPIO.setup(GPIO_LEDB, GPIO.OUT)
GPIO.setup(GPIO_LEDC, GPIO.OUT)

# Allow module to settle
time.sleep(0.5)

# Send 10us pulse to trigger
GPIO.output(GPIO_TRIGGER, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)
start = time.time()
while GPIO.input(GPIO_ECHO) == 0:
    start = time.time()
    
    
    
while GPIO.input(GPIO_ECHO) == 1:
    stop = time.time()
    
# Calculate the pulse length   
elapsed = stop-start


# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
distance = elapsed * 34000

# That was the distance there and back so halve the value
distane = distance / 2

print "Distance : %.1f" % distance


