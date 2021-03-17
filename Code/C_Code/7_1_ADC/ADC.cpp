/**********************************************************************
* Filename    : ADC.cpp
* Description : Use ADC module to read the voltage value of potentiometer.
* Author      : www.freenove.com
* modification: 2021/1/1
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <ADCDevice.hpp>

ADCDevice *adc;  // Define an ADC Device class object

int main(void){
    adc = new ADCDevice();
    printf("Program is starting ... \n");
    if(adc->detectI2C(0x48)){   // Detect the ads7830
        delete adc;               // Free previously pointed memory
        adc = new ADS7830(0x48);      // If detected, create an instance of ADS7830.
    }
    else{
        printf("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        return -1;
    }
    
    while(1){
        int adcValue = adc->analogRead(2);    //read analog value of A2 pin
        float voltage = (float)adcValue / 255.0 * 5.0;  // Calculate voltage
        printf("ADC value : %d  ,\tVoltage : %.2fV\n",adcValue,voltage);
        delay(100);
    }
    return 0;
}
