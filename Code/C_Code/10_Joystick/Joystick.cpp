/**********************************************************************
* Filename    : Joystick.cpp
* Description : Read Joystick
* Author      : www.freenove.com
* modification: 2021/1/1
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <softPwm.h>
#include <ADCDevice.hpp>

#define Z_Pin 11     //define pin for axis Z

ADCDevice *adc;  // Define an ADC Device class object

int main(void){
    adc = new ADCDevice();
    printf("Program is starting ... \n");
    
    if(adc->detectI2C(0x48)){    // Detect the ads7830
        delete adc;               // Free previously pointed memory
        adc = new ADS7830(0x48);      // If detected, create an instance of ADS7830.
    }
    else{
        printf("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        return -1;
    }    
    wiringPiSetup();    
    pinMode(Z_Pin,INPUT);       //set Z_Pin as input pin and pull-up mode
    pullUpDnControl(Z_Pin,PUD_UP);    
    while(1){
        int val_Z = digitalRead(Z_Pin);  //read digital value of axis Z
        int val_Y = adc->analogRead(5);      //read analog value of axis X and Y
        int val_X = adc->analogRead(6);
        printf("val_X: %d  ,\tval_Y: %d  ,\tval_Z: %d \n",val_X,val_Y,val_Z);
        delay(100);
    }
    return 0;
}

