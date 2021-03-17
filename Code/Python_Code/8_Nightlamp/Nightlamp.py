#!/usr/bin/env python3
#############################################################################
# Filename    : Nightlamp.py
# Description : Control LED with Photoresistor
# Author      : www.freenove.com
# modification: 2021/1/1
########################################################################
import RPi.GPIO as GPIO
import time
from ADCDevice import *

ledPin = 11 # define ledPin
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
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin,GPIO.OUT)   # set ledPin to OUTPUT mode
    GPIO.output(ledPin,GPIO.LOW)
    
    p = GPIO.PWM(ledPin,1000) # set PWM Frequence to 1kHz
    p.start(0)
    
def loop():
    while True:
        value = adc.analogRead(1)    # read the ADC value of channel 0
        p.ChangeDutyCycle(value*100/255)
        voltage = value / 255.0 * 5.5
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        time.sleep(0.01)

def destroy():
    adc.close()
    GPIO.cleanup()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        
    
