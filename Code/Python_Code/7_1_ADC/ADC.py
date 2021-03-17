#!/usr/bin/env python3
########################################################################
# Filename    : ADC.py
# Description : Use ADC module to read the voltage value of potentiometer.
# Author      : www.freenove.com
# modification: 2021/1/1
########################################################################
import time
from ADCDevice import *

adc = ADCDevice(0x48) # Define an ADCDevice class object

def setup():
    global adc
    if(adc.detectI2C(0x48)):
        adc = ADS7830(0x48)
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
        
def loop():
    while True:
        value = adc.analogRead(2)    # read the ADC value of channel 2
        voltage = value / 255.0 * 5.0  # calculate the voltage value
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        time.sleep(0.1)

def destroy():
    adc.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
        
    
