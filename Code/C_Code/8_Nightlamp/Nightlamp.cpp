/**********************************************************************
* Filename    : Nightlamp.cpp
* Description : Photoresistor control LED
* Author      : www.freenove.com
* modification: 2021/1/1
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <softPwm.h>
#include <ADCDevice.hpp>

#define ledPin 0

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
    softPwmCreate(ledPin,0,100);    
    while(1){
        int value = adc->analogRead(1);  //read analog value of A1 pin
        softPwmWrite(ledPin,value*100/255);
        float voltage = (float)value / 255.0 * 5.0;  // calculate voltage
        printf("ADC value : %d  ,\tVoltage : %.2fV\n",value,voltage);
        delay(100);
    }
    return 0;
}
