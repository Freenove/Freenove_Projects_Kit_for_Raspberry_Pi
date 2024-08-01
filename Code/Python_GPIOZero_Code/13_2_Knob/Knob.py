#!/usr/bin/env python3
########################################################################
# Filename    : Sweep.py
# Description : Servo sweep
# Author      : www.freenove.com
# modification: 2024/07/29
########################################################################
from gpiozero import AngularServo
import time
from ADCDevice import *

adc = ADCDevice(0x48) # Define an ADCDevice class object

myGPIO=18
SERVO_DELAY_SEC = 0.001 
myCorrection=0.0
maxPW=(2.5+myCorrection)/1000
minPW=(0.5-myCorrection)/1000
servo =  AngularServo(myGPIO,initial_angle=0,min_angle=0, max_angle=180,min_pulse_width=minPW,max_pulse_width=maxPW)

def map( value, fromLow, fromHigh, toLow, toHigh):  # map a value from one range to another range
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def setup():
    global adc
    if(adc.detectI2C(0x48)):
        adc = ADS7830(0x48)
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
    
def servoWrite(angle):      # make the servo rotate to specific angle, 0-180 
    if(angle<0):
        angle = 0
    elif(angle > 180):
        angle = 180
    servo.angle = angle # map the angle to duty cycle and output it
    
def loop():
    while True:
        value = adc.analogRead(2)    # read the ADC value of channel 2
        servoWrite(round(value/255.0*180.0))
        print ('ADC Value : %d'%(value))
        time.sleep(0.1)

def destroy():
    adc.close()
    servo.close()

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        setup()
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
    finally:
        destroy()
