#!/usr/bin/python

# Import required Python libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO_LIGHT = 17
loop = 0
print "Ultrasonic Measurment"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  #Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      #Echo
GPIO.setup(GPIO_LIGHT,GPIO.OUT)
# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)


# Allow module to settle
time.sleep(0.5)
while loop < 300:
    

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
    print loop
    print "Distance : %.1f" % distance
    if distance > 30:
        GPIO.output(GPIO_LIGHT, True)
    else:
        GPIO.output(GPIO_LIGHT, False)
    time.sleep(0.1)
    loop = loop + 1
# Reset the GPIO settings
GPIO.output(GPIO_LIGHT, GPIO.LOW)
GPIO.cleanup()
