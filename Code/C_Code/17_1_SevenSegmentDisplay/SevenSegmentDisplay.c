/**********************************************************************
* Filename    : SevenSegmentDisplay.c
* Description : Control SevenSegmentDisplay by 74HC595
* Author      : www.freenove.com
* modification: 2024/07/29
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <wiringShift.h>

#define   dataPin   22   //DS Pin of 74HC595(Pin14)
#define   latchPin  27   //ST_CP Pin of 74HC595(Pin12)
#define   clockPin  17   //CH_CP Pin of 74HC595(Pin11)
//encoding for character 0-F of common anode SevenSegmentDisplay. 
unsigned long num[]={0xffc0,0xfff9,0xffa4,0xffb0,0xff99,0xff92,0xff82,0xfff8,0xff80,0xff90,0xff88,0xff83,0xffc6,0xffa1,0xff86,0xff8e};

void _shiftOut(int dPin,int cPin,int order,int val){   
	int i;  
    for(i = 0; i < 16; i++){
        digitalWrite(cPin,LOW);
        if(order == LSBFIRST){
            digitalWrite(dPin,((0x01&(val>>i)) == 0x01) ? HIGH : LOW);
            delayMicroseconds(10);
		}
        else {
            digitalWrite(dPin,((0x8000&(val<<i)) == 0x8000) ? HIGH : LOW);
            delayMicroseconds(10);
		}
        digitalWrite(cPin,HIGH);
        delayMicroseconds(10);
	}
}

int main(void)
{
	int i;
	
	printf("Program is starting ...\n");
	
	wiringPiSetupGpio();//Initialize wiringPi. Use BCM Number.
	
	pinMode(dataPin,OUTPUT);
	pinMode(latchPin,OUTPUT);
	pinMode(clockPin,OUTPUT);
	while(1){
		for(i=0;i<sizeof(num)/sizeof(num[0]);i++){
			digitalWrite(latchPin,LOW);
			_shiftOut(dataPin,clockPin,MSBFIRST,num[i]);//Output the figures and the highest level is transfered preferentially. 
			digitalWrite(latchPin,HIGH);
			delay(500);
		}
	}
	return 0;
}

