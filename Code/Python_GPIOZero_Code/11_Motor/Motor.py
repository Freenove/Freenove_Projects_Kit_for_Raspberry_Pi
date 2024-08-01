#!/usr/bin/env python3
#############################################################################
# Filename    : Motor.py
# Description : Control Motor with L293D
# Author      : www.freenove.com
# modification: 2024/07/29
########################################################################
from gpiozero import DigitalOutputDevice,PWMOutputDevice
import time
from ADCDevice import *

# define the pins connected to L293D
motoRPin1 = PWMOutputDevice(15,frequency=1000)
motoRPin2 = PWMOutputDevice(14,frequency=1000)
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
# mapNUM function: map the value from a range of mapping to another range.
def mapNUM(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

# motor function: determine the direction and speed of the motor according to the input ADC value input
def motor(ADC):
    value = ADC -128
    if (value > 0):  # make motor turn forward
        motoRPin1.value=abs(value)/127          # motoRPin1 output HIHG level
        motoRPin2.value=0                       # motoRPin2 output LOW level
        print ('Turn Forward...')
    elif (value < 0): # make motor turn backward
        motoRPin1.value=0                       # motoRPin1 output LOW level
        motoRPin2.value=abs(value)/128          # motoRPin2 output HIHG level
        print ('Turn Backward...')
    else :
        motoRPin1.value=0 
        motoRPin2.value=0 
        print ('Motor Stop...')

def loop():
    while True:
        value = adc.analogRead(2) # read ADC value of channel 0
        print ('ADC Value : %d'%(value))
        motor(value)
        time.sleep(0.2)

def destroy():
    motoRPin1.close()          
    motoRPin2.close()        
    adc.close()

if __name__ == '__main__':  # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
    finally:
        destroy()