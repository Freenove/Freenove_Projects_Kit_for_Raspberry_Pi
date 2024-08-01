#!/usr/bin/env python3
#############################################################################
# Filename    : SevenSegmentDisplay.py
# Description : Control SevenSegmentDisplay with 74HC595
# Author      : www.freenove.com
# modification: 2024/07/29
########################################################################
from gpiozero import OutputDevice
import time
import threading

LSBFIRST = 1
MSBFIRST = 2
# define the pins for 74HC595
dataPin   = OutputDevice(22)      # DS Pin of 74HC595(Pin14)
latchPin  = OutputDevice(27)      # ST_CP Pin of 74HC595(Pin12)
clockPin  = OutputDevice(17)      # CH_CP Pin of 74HC595(Pin11)
# SevenSegmentDisplay display the character "0"- "F" successively
num = [0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0x83,0xc6,0xa1,0x86,0x8e]
decimalPoint = 0xff
counter = 0         # Variable counter, the number will be dislayed by 7-segment display
t = None            # define the Timer object

def setDecimalPoint(state):
    global decimalPoint
    if state==1:
        decimalPoint = 0x7f
    elif state==0:
        decimalPoint = 0xff
        
def shiftOut(order,val):
    for i in range(0,8):
        clockPin.off()
        if(order == LSBFIRST):
            dataPin.on() if (0x01&(val>>i)==0x01) else dataPin.off()
        elif(order == MSBFIRST):
            dataPin.on() if (0x80&(val<<i)==0x80) else dataPin.off()
        clockPin.on()
        
def display(values, showTimes=10):
    bits = [0x01,0x02,0x04,0x08]
    bitValues=[0,0,0,0]
    bitValues[0] = values // 1000  
    bitValues[1] = (values // 100) % 10  
    bitValues[2] = (values // 10) % 10 
    bitValues[3] = values % 10  
    for j in range(showTimes):
        for i in range(0,len(bits)):
            latchPin.off()
            shiftOut(MSBFIRST, bits[i])
            shiftOut(MSBFIRST, num[bitValues[i]]&decimalPoint)
            latchPin.on()
            time.sleep(0.0002)
            latchPin.off()
            shiftOut(MSBFIRST, bits[i])
            shiftOut(MSBFIRST, 0xff)
            latchPin.on()
            time.sleep(0.00005)
    
def timer():       
    global counter
    global t
    t = threading.Timer(1.0,timer)      # reset time of timer to 1s
    t.start()                           # Start timing
    counter+=1                          
    print ("counter : %d"%counter)
    
def loop():
    global t
    global counter
    setDecimalPoint(0)
    t = threading.Timer(1.0,timer)      # set the timer
    t.start()                           # Start timing
    while True:
        display(counter)                # display the number counter
        
def destroy(): 
    global t
    t.cancel()
    latchPin.off()
    shiftOut(MSBFIRST, 0x00)
    shiftOut(MSBFIRST, 0x00)
    latchPin.on()
    dataPin.close()
    latchPin.close()
    clockPin.close() 
    

if __name__ == '__main__': # Program entrance
    print ('Program is starting...' )
    try:
        loop()  
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
    finally:
        destroy()
