#!/usr/bin/env python3
########################################################################
# Filename    : Sweep.py
# Description : Servo sweep
# Author      : www.freenove.com
# modification: 2021/1/1
########################################################################
import RPi.GPIO as GPIO
import time
from ADCDevice import *

adc = ADCDevice(0x48) # Define an ADCDevice class object

OFFSE_DUTY = 0.5        #define pulse offset of servo
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     #define pulse duty cycle for minimum angle of servo
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    #define pulse duty cycle for maximum angle of servo
servoPin = 12

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
        
    global p
    GPIO.setmode(GPIO.BOARD)         # use PHYSICAL GPIO Numbering
    GPIO.setup(servoPin, GPIO.OUT)   # Set servoPin to OUTPUT mode
    GPIO.output(servoPin, GPIO.LOW)  # Make servoPin output LOW level

    p = GPIO.PWM(servoPin, 50)     # set Frequece to 50Hz
    p.start(0)                     # Set initial Duty Cycle to 0
    
def servoWrite(angle):      # make the servo rotate to specific angle, 0-180 
    if(angle<0):
        angle = 0
    elif(angle > 180):
        angle = 180
    p.ChangeDutyCycle(map(angle,0,180,SERVO_MIN_DUTY,SERVO_MAX_DUTY)) # map the angle to duty cycle and output it
    
def loop():
    while True:
        value = adc.analogRead(2)    # read the ADC value of channel 2
        servoWrite(round(value/255.0*180.0))
        print ('ADC Value : %d'%(value))
        time.sleep(0.1)
    
            
        

def destroy():
    p.stop()
    GPIO.cleanup()

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
