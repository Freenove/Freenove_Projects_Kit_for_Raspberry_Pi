#!/usr/bin/env python3
#############################################################################
# Filename    : Softlight.py
# Description : Control RGBLED with Potentiometer 
# Author      : www.freenove.com
# modification: 2024/07/29
########################################################################
from gpiozero import RGBLED
import time
from ADCDevice import *

led = RGBLED(red=5, green=6, blue=13, active_high=False) 
adc = ADCDevice(0x48) # Define an ADCDevice class object

def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = ADS7830(0x48)
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
    
def loop():
    while True:     
        value_Red = adc.analogRead(2)       # read ADC value of 3 potentiometers
        value_Green = adc.analogRead(3)
        value_Blue = adc.analogRead(4)
        led.red   =value_Red/255  # map the read value of potentiometers into PWM value and output it 
        led.green =value_Green/255
        led.blue  =value_Blue/255
        # print read ADC value
        print ('ADC Value value_Red: %d ,\tvlue_Green: %d ,\tvalue_Blue: %d'%(value_Red,value_Green,value_Blue))
        time.sleep(0.01)

def destroy():
    adc.close()
    led.close()
    
if __name__ == '__main__': # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
    finally:
        destroy()
