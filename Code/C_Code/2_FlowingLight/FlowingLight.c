/**********************************************************************
* Filename    : LightWater.c
* Description : Use LEDBar Graph(10 LED) 
* Author      : www.freenove.com
* modification: 2024/07/29
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>

#define ledCounts 12
int pins[ledCounts] = {14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21};

void main(void)
{
	int i;
	printf("Program is starting ... \n");
	wiringPiSetupGpio();//Initialize wiringPi. Use BCM Number.
	for(i=0;i<ledCounts;i++){       //Set pinMode for all led pins to output
		pinMode(pins[i], OUTPUT);		
	}
	while(1){
		for(i=0;i<ledCounts;i++){   // move led(on) from top to bottom
			digitalWrite(pins[i],HIGH);
			delay(100);
			digitalWrite(pins[i],LOW);
		}
		for(i=ledCounts-1;i>-1;i--){   // move led(on) from bottom to top
			digitalWrite(pins[i],HIGH);
			delay(100);
			digitalWrite(pins[i],LOW);
		}
	}
}

