/**********************************************************************
* Filename    : SenseLED.c
* Description : Control led with infrared Motion sensor
* Author      : www.freenove.com
* modification: 2021/1/1
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>

#define ledPin    0  	//define the ledPin
#define sensorPin 5		//define the sensorPin

int main(void)
{	
	printf("Program is starting ... \n");
	
	wiringPiSetup();
	
	pinMode(ledPin, OUTPUT); 
	pinMode(sensorPin, INPUT);

	while(1){
		
		if(digitalRead(sensorPin) == HIGH){ //if read value of sensor is HIGH level
			digitalWrite(ledPin, HIGH);   //make led on
			printf("led turned on >>> \n");
		}
		else {				
			digitalWrite(ledPin, LOW);   //make led off
			printf("led turned off <<< \n");
		}
	}

	return 0;
}

