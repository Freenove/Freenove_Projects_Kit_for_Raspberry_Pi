#!/usr/bin/env python3
########################################################################
# Filename    : LightWater.py
# Description : Use LEDBar Graph(10 LED) 
# Author      : www.freenove.com
# modification: 2024/07/29
########################################################################
from gpiozero import LED
from time import sleep

ledPins = [14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]
leds = [LED(pin=pin) for pin in ledPins] 
    
def loop():
    while True:
        for index in range(0,len(ledPins),1):      # make led(on) move from left to right
            leds[index].on()  
            sleep(0.1)
            leds[index].off() 
        for index in range(len(ledPins)-1,-1,-1):   #move led(on) from right to left
            leds[index].on()  
            sleep(0.1)
            leds[index].off() 

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
    finally:
        for index in range(0,len(ledPins),1): 
            leds[index].close()  
        
