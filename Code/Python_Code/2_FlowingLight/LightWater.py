#!/usr/bin/env python3
########################################################################
# Filename    : LightWater.py
# Description : Use LEDBar Graph(10 LED) 
# auther      : www.freenove.com
# modification: 2021/1/1
########################################################################
import RPi.GPIO as GPIO
import time

ledPins = [8,10,12,16,18,22,24,26,32,36,38,40]

def setup():    
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPins, GPIO.OUT)   # set all ledPins to OUTPUT mode
    GPIO.output(ledPins, GPIO.LOW) # make all ledPins output LOW level, turn off all led

def loop():
    while True:
        for pin in ledPins:     # make led(on) move from top to bottom
            GPIO.output(pin, GPIO.HIGH)  
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)
        for pin in ledPins[::-1]:       # make led(on) move from bottom to top
            GPIO.output(pin, GPIO.HIGH)  
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)

def destroy():
    GPIO.cleanup()                     # Release all GPIO

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

