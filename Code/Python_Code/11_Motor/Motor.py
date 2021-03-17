#!/usr/bin/env python3
#############################################################################
# Filename    : Motor.py
# Description : Control Motor with L293D
# Author      : www.freenove.com
# modification: 2021/1/1
########################################################################
import RPi.GPIO as GPIO
import time
from ADCDevice import *

# define the pins connected to L293D 
motoRPin1 = 8
motoRPin2 = 10
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
    global p1
    global p2
    GPIO.setmode(GPIO.BOARD)   
    GPIO.setup(motoRPin1,GPIO.OUT)   # set pins to OUTPUT mode
    GPIO.setup(motoRPin2,GPIO.OUT)
    
    p1 = GPIO.PWM(motoRPin1,1000) # creat PWM and set Frequence to 1KHz
    p1.start(0)
    p2 = GPIO.PWM(motoRPin2,1000) # creat PWM and set Frequence to 1KHz
    p2.start(0)

# mapNUM function: map the value from a range of mapping to another range.
def mapNUM(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
	
# motor function: determine the direction and speed of the motor according to the input ADC value input
def motor(ADC):
    value = ADC -128
    
    if (value > 0):  # make motor turn forward
        print(abs(value)*100/127)
        p1.ChangeDutyCycle(abs(value)*100/127)
        p2.ChangeDutyCycle(0)
        print ('Turn Forward...')
    elif (value < 0): # make motor turn backward
        print(abs(value)*100/128)
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(abs(value)*100/128)
        print ('Turn Backward...')
    else :
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)
        print ('Motor Stop...')

def loop():
    while True:
        value = adc.analogRead(2) # read ADC value of channel 0
        print ('ADC Value : %d'%(value))
        motor(value)
        time.sleep(0.05)

def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__':  # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()

