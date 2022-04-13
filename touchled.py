#!/bin/python3

# setup imports for our program.
import os
import time
time.sleep(0.100)
import random
import RPi.GPIO as GPIO

# code below is GPIO configuration. BLUE is the label I used for the code as I was lighting a blue LED. You can label it whatever you like. Same goes with the assigned GPIO pin #.
GPIO.setmode(GPIO.BCM)
BLUE = 18
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

# Line 17 of this program is for touch sensor.
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# The while loop that detects if the touch sensor is being touched and lights the LED accordingly.

while True:
  if (GPIO.input(17) == True):
    print ("Touch Detected")
    GPIO.output(BLUE, GPIO.HIGH)
    time.sleep(0.5)
  if (GPIO.input(17) == False):
    print ("No Touch Detected")
    GPIO.output(BLUE, GPIO.LOW)
    time.sleep(0.5) ;

# This code will continuously run and detect if the touch sensor is being touched. To end it, type ctrl + c.
