/**********************************************************************
* Filename    : ButtonLED.c
* Description : Control led by button.
* Author      : www.freenove.com
* modification: 2024/07/29
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>

#define ledPin    17  	//define the ledPin
#define buttonPin 26    //define the buttonPin

void  main(void)
{
	printf("Program is starting ... \n");

	wiringPiSetupGpio();//Initialize wiringPi. Use BCM Number.
	
	pinMode(ledPin, OUTPUT); //Set ledPin to output
	pinMode(buttonPin, INPUT);//Set buttonPin to input

	pullUpDnControl(buttonPin, PUD_UP);  //pull up to HIGH level
	while(1){
		if(digitalRead(buttonPin) == LOW){ //button is pressed 
			digitalWrite(ledPin, HIGH);  //Make GPIO output HIGH level
			printf("Button is pressed, led turned on >>>\n");		//Output information on terminal
		}
		else {							//button is released 
			digitalWrite(ledPin, LOW);  //Make GPIO output LOW level
			printf("Button is released, led turned off <<<\n");		//Output information on terminal
		}
	}
}

