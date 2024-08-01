#!/usr/bin/env python3
########################################################################
# Filename    : ColorfulLED.py
# Description : Random color change ColorfulLED
# Author      : www.freenove.com
# modification: 2024/07/29
########################################################################
from gpiozero import RGBLED
import time
import random

led = RGBLED(red=5, green=6, blue=13, active_high=False) # define the pins for R:GPIO17,G:GPIO18,B:GPIO27 

def setColor(r_val,g_val,b_val):      # change duty cycle for three pins to r_val,g_val,b_val
    led.red=r_val/100                 # change pwmRed duty cycle to r_val
    led.green = g_val/100             # change pwmRed duty cycle to r_val
    led.blue = b_val/100              # change pwmRed duty cycle to r_val

def loop():
    while True :
        r=random.randint(0,100)  #get a random in (0,100)
        g=random.randint(0,100)
        b=random.randint(0,100)
        setColor(r,g,b)          #set random as a duty cycle value 
        print ('r=%d, g=%d, b=%d ' %(r ,g, b))
        time.sleep(1)

if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
    finally:
        led.close()
