/**********************************************************************
* Filename    : Motor.cpp
* Description : Control Motor by L293D
* Author      : www.freenove.com
* modification: 2021/1/1
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <softPwm.h>
#include <math.h>
#include <stdlib.h>
#include <ADCDevice.hpp>

#define motorPin1    15        //define the pin connected to L293D
#define motorPin2    16
#define enablePin    3

ADCDevice *adc;  // Define an ADC Device class object

//Map function: map the value from a range to another range.
long map(long value,long fromLow,long fromHigh,long toLow,long toHigh){
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow;
}
//motor function: determine the direction and speed of the motor according to the ADC 
void motor(int ADC){
    int value = ADC -128;
    if(value>0){
        softPwmWrite(motorPin1,map(abs(value),0,128,0,100));
        softPwmWrite(motorPin2,0);
        printf("turn Forward...\n");
    }
    else if (value<0){
        softPwmWrite(motorPin1,0);
        softPwmWrite(motorPin2,map(-value,0,128,0,100));
        printf("turn Back...\n");
    }
    else {
        digitalWrite(motorPin1,LOW); 
        digitalWrite(motorPin2,LOW);
        printf("Motor Stop...\n");
    }
    
    printf("The PWM duty cycle is %d%%\n",abs(value)*100/127);//print the PMW duty cycle
}
int main(void){
    adc = new ADCDevice();
    printf("Program is starting ... \n");
    
    if(adc->detectI2C(0x48)){    // Detect the ads7830
        delete adc;                // Free previously pointed memory
        adc = new ADS7830(0x48);      // If detected, create an instance of ADS7830.
    }
    else{
        printf("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        return -1;
    }
    wiringPiSetup();
    pinMode(motorPin1,OUTPUT);
    pinMode(motorPin2,OUTPUT);
    
    softPwmCreate(motorPin1,0,100);//define PMW pin
    softPwmCreate(motorPin2,0,100);//define PMW pin
    
    while(1){
        int value = adc->analogRead(2);  //read analog value of A0 pin
        printf("ADC value : %d \n",value);
        motor(value);        //make the motor rotate with speed(analog value of A0 pin)
        delay(100);
    }
    return 0;
}

