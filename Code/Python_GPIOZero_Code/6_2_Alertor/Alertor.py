#!/usr/bin/env python3
########################################################################
# Filename    : Alertor.py
# Description : Make Alertor with buzzer and button
# Author      : www.freenove.com
# modification: 2024/07/29
########################################################################
from gpiozero import TonalBuzzer,Button
from gpiozero.tones import Tone
import time
import math

buzzer = TonalBuzzer(4)
button = Button(20) # define Button pin according to BCM Numbering

def loop():
    while True:
        if button.is_pressed:  # if button is pressed
            alertor()
            print ('alertor turned on >>> ')
        else :
            stopAlertor()
            print ('alertor turned off <<<')
def alertor():
    buzzer.play(Tone(220.0)) 
    time.sleep(0.1)
        
def stopAlertor():
    buzzer.stop()
            
def destroy():
    buzzer.close() 
    button.close()     

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
    finally:
        destroy()