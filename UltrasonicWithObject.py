#!/usr/bin/python

# Import required Python libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

class Bluelight:
    def __init__(self):
        self.flag = False
    def blink(self):
        self.flag = True
        Red.flag = False
        Green.flag = False
        GPIO.output(GPIO_BLUE, True)
        GPIO.output(GPIO_RED, False)
        GPIO.output(GPIO_GREEN, False)
        
class Redlight:
    def __init__(self):
        self.flag = False
    def blink(self):
        self.flag = True
        Blue.flag = False
        Green.flag = False
        GPIO.output(GPIO_RED, True)
        GPIO.output(GPIO_BLUE, False)
        GPIO.output(GPIO_GREEN, False)
class Greenlight:
    def __init__(self):
        self.flag = False
    def blink(self):
        self.flag = True
        Blue.flag = False
        Red.flag = False
        GPIO.output(GPIO_RED, False)
        GPIO.output(GPIO_BLUE, False)
        GPIO.output(GPIO_GREEN, True)
# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO_BLUE = 17
GPIO_GREEN = 22
GPIO_RED = 4
loop = 0
blueFlag = False
greenFlag = False
redFlag = False
Blue = Bluelight()
Red = Redlight()
Green = Greenlight()
print "Ultrasonic Measurment"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  #Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      #Echo
GPIO.setup(GPIO_BLUE,GPIO.OUT)
GPIO.setup(GPIO_GREEN, GPIO.OUT)
GPIO.setup(GPIO_RED, GPIO.OUT)
# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)


# Allow module to settle
time.sleep(0.5)
while loop < 400:
    

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
    distance = distance / 2
    print loop
    print "Distance : %.1f" % distance
    if distance < 10 and Green.flag is False:
        print "gggggggggggggggggggggggggg"
        Green.blink()
    
    elif distance >= 10 and distance < 30 and Blue.flag is False:
        print "bbbbbbbbbbbbbbbbbbbbbbbbbb"
        Blue.blink()
       
    elif distance >= 50 and Red.flag is False:
        Red.blink()
        print "rrrrrrrrrrrrrrrrrrrrrrrrrrr"
    time.sleep(0.06)
    loop = loop + 1
# Reset the GPIO settings
GPIO.output(GPIO_BLUE, False)
GPIO.output(GPIO_GREEN, False)
GPIO.output(GPIO_RED, False)
GPIO.cleanup()
