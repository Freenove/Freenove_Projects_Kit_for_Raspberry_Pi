#!/usr/bin/env python3
#############################################################################
# Filename    : SevenSegmentDisplay.py
# Description : Control SevenSegmentDisplay with 74HC595
# Author      : www.freenove.com
# modification: 2021/1/1
########################################################################
import RPi.GPIO as GPIO
import time

LSBFIRST = 1
MSBFIRST = 2
# define the pins for 74HC595
dataPin   = 15      # DS Pin of 74HC595(Pin14)
latchPin  = 13      # ST_CP Pin of 74HC595(Pin12)
clockPin = 11       # CH_CP Pin of 74HC595(Pin11)
# SevenSegmentDisplay display the character "0"- "F" successively
num = [0xffc0,0xfff9,0xffa4,0xffb0,0xff99,0xff92,0xff82,0xfff8,0xff80,0xff90,0xff88,0xff83,0xffc6,0xffa1,0xff86,0xff8e]

def setup():
    GPIO.setmode(GPIO.BOARD)   # use PHYSICAL GPIO Numbering
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    
def shiftOut(dPin,cPin,order,val):
    for i in range(0,16):
        GPIO.output(cPin,GPIO.LOW);
        if(order == LSBFIRST):
            GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin,(0x8000&(val<<i)==0x8000) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin,GPIO.HIGH);

def loop():
    while True:
        for i in range(0,len(num)):
            GPIO.output(latchPin,GPIO.LOW)
            shiftOut(dataPin,clockPin,MSBFIRST,num[i])  # Send serial data to 74HC595
            GPIO.output(latchPin,GPIO.HIGH)
            time.sleep(0.5)   

def destroy():  
    GPIO.cleanup()

if __name__ == '__main__': # Program entrance
    print ('Program is starting...' )
    setup() 
    try:
        loop()  
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()  
