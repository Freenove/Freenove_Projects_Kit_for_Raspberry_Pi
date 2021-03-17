/**********************************************************************
* Filename    : LightWater.c
* Description : Use LEDBar Graph(10 LED) 
* Author      : www.freenove.com
* modification: 2021/1/1
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>

#define ledCounts 12
int pins[ledCounts] = {15,16,1,4,5,6,10,11,26,27,28,29};

void main(void)
{
	int i;
	printf("Program is starting ... \n");
	
	wiringPiSetup(); //Initialize wiringPi.
	
	for(i=0;i<ledCounts;i++){       //Set pinMode for all led pins to output
		pinMode(pins[i], OUTPUT);		
	}
	while(1){
		for(i=0;i<ledCounts;i++){   // move led(on) from top to bottom
			digitalWrite(pins[i],LOW);
			delay(100);
			digitalWrite(pins[i],HIGH);
		}
		for(i=ledCounts-1;i>-1;i--){   // move led(on) from bottom to top
			digitalWrite(pins[i],LOW);
			delay(100);
			digitalWrite(pins[i],HIGH);
		}
	}
}

