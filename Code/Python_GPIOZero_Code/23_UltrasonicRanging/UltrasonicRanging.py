#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance via UltrasonicRanging sensor
# auther      : www.freenove.com
# modification: 2024/07/29
########################################################################
from gpiozero import DistanceSensor
from time import sleep
import warnings  
warnings.filterwarnings("ignore")  
  
trigPin = 14
echoPin = 15
sensor = DistanceSensor(echo=echoPin, trigger=trigPin ,max_distance=3)

def loop():
    while True:
        print('Distance: ', sensor.distance * 100,'cm')
        sleep(1)
        
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
    finally:
        sensor.close()
