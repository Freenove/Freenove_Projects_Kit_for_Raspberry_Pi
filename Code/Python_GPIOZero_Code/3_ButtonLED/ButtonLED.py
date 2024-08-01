#!/usr/bin/env python3
########################################################################
# Filename    : ButtonLED.py
# Description : Control led with button.
# Author      : www.freenove.com
# modification: 2024/07/29
########################################################################
from gpiozero import LED, Button

led = LED(17)       # define LED pin according to BCM Numbering
button = Button(26) # define Button pin according to BCM Numbering

def loop():
    key_state = 0
    while True:
        if button.is_pressed==True and key_state == 0:  # if button is pressed
            led.on()        # turn on led
            key_state = 1
            print("Button is pressed, led turned on >>>") # print information on terminal 
        elif button.is_pressed==False and key_state == 1:
            led.off() # turn off led 
            key_state = 0
            print("Button is released, led turned off <<<")    

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
    finally:
        led.close()
        button.close()
