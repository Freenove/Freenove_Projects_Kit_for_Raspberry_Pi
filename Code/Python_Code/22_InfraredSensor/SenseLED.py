#!/usr/bin/env python3
########################################################################
# Filename    : SenseLED.py
# Description : Control led with infrared Motion sensor.
# auther      : www.freenove.com
# modification: 2021/1/1
########################################################################
import RPi.GPIO as GPIO

ledPin = 11       # define ledPin
sensorPin = 18    # define sensorPin

def setup():
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)    # set ledPin to OUTPUT mode
    GPIO.setup(sensorPin, GPIO.IN)  # set sensorPin to INPUT mode

def loop():
    while True:
        if GPIO.input(sensorPin)==GPIO.HIGH:
            GPIO.output(ledPin,GPIO.LOW) # turn on led
            print ('led turned off >>>')
        else :
            GPIO.output(ledPin,GPIO.HIGH) # turn off led
            print ('led turned on <<<')

def destroy():
    GPIO.cleanup()                     # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

