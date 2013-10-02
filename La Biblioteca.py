#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class LED:
    
    def frontLight(self):
        self.frontstatus = True
        GPIO.output(GPIO_LEDA, True)
        GPIO.output(GPIO_LEDB, True)
        GPIO.output(GPIO_LEDC, True)
    def frontLightOff(self):
        self.frontstatus = False
        GPIO.output(GPIO_LEDA, False)
        GPIO.output(GPIO_LEDB, False)
        GPIO.output(GPIO_LEDC, False)
    def backlight(self):
        self.backstatus = True
        GPIO.output(GPIO_BACKLIGHTA, True)
        GPIO.output(GPIO_BACKLIGHTB, True)
    def backlightOff(self):
        self.backstatus = False
        GPIO.output(GPIO_BACKLIGHTA, False)
        GPIO.output(GPIO_BACKLIGHTB, False)
    def __init__(self):
        self.frontstatus = False
        self.backstatus = False
        self.binstatus = False
    def __str__(self):
        strmessage = "Front light status = " + self.frontstatus + ". Back light status = " + self.backstatus + "."
        return strmessage
        

GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO_LEDA = 4
GPIO_LEDB = 17
GPIO_LEDC = 22
GPIO_BACKLIGHTA = #Enter Value Here
GPIO_BACKLIGHTB = #Enter Value Here

L = LED()
print "Starting Program"
print "Auto Mode On"

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LEDA, GPIO.OUT)
GPIO.setup(GPIO_LEDB, GPIO.OUT)
GPIO.setup(GPIO_LEDC, GPIO.OUT)

# Allow module to settle
time.sleep(0.5)
while True:

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

# That was the distance there and back so find half of the value
distance = distance / 2

print "Distance : %.1f" % distance

if distance < 10 and L.binstatus = False:
	L.frontLightOff()
	L.backLightOff()
	print "Bin in."
	L.binstatus = True
elif distance =< 10:
	L.frontLight()
	L.backLight()
        print "BIN OUT!!!!!!!!!!!!!!!!!!!"
        L.binstatus = False

