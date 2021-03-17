/**********************************************************************
* Filename    : Doorbell.c
* Description : Make doorbell with buzzer and button.
* Author      : www.freenove.com
* modification: 2021/1/1
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>

#define buzzerPin 26  	//define the buzzerPin
#define buttonPin 29		//define the buttonPin

void main(void)
{
	printf("Program is starting ... \n");
	
	wiringPiSetup();
	
	pinMode(buzzerPin, OUTPUT); 
	pinMode(buttonPin, INPUT);

	pullUpDnControl(buttonPin, PUD_UP);  //pull up to HIGH level
	while(1){
		
		if(digitalRead(buttonPin) == LOW){ //button is pressed
			digitalWrite(buzzerPin, HIGH);   //Turn on buzzer 
			printf("buzzer turned on >>> \n");
		}
		else {				//button is released 
			digitalWrite(buzzerPin, LOW);   //Turn off buzzer
			printf("buzzer turned off <<< \n");
		}
	}
}

