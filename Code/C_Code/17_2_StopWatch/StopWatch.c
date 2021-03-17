/**********************************************************************
* Filename    : StopWatch.c
* Description : Control 4_Digit_7_Segment_Display by 74HC595
* Author      : www.freenove.com
* modification: 2021/1/1
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <wiringShift.h>
#include <signal.h>
#include <unistd.h>
#define     dataPin     3   //DS Pin of 74HC595(Pin14)
#define     latchPin    2   //ST_CP Pin of 74HC595(Pin12)
#define     clockPin    0    //CH_CP Pin of 74HC595(Pin11)
// character 0-9 code of common anode 7-segment display 
unsigned char num[]={0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90};
int counter = 0;    //variable counter,the number will be displayed by 7-segment display
//Open one of the 7-segment display and close the remaining three, the parameter digit is optional for 1,2,4,8
unsigned long selectDigit(unsigned long digit){  
    if (digit==0x01){
        return (0x08<<8);
        } 
    else if (digit==0x02){
        return (0x04<<8);
        } 
    else if (digit==0x04){
        return (0x02<<8);
        } 
    else if (digit==0x08){
        return (0x01<<8);
        } 
    else{
        return (0xf0<<8);
        }

}
void _shiftOut(int dPin,int cPin,int order,int val){   
	int i;  
    for(i = 0; i < 16; i++){
        digitalWrite(cPin,LOW);
        if(order == LSBFIRST){
            digitalWrite(dPin,((0x01&(val>>i)) == 0x01) ? HIGH : LOW);
            delayMicroseconds(1);
		}
        else {//if(order == MSBFIRST){
            digitalWrite(dPin,((0x8000&(val<<i)) == 0x8000) ? HIGH : LOW);
            delayMicroseconds(1);
		}
        digitalWrite(cPin,HIGH);
        delayMicroseconds(1);
	}
}
void outData(unsigned long data){      //function used to output data for 74HC595
    digitalWrite(latchPin,LOW);
    _shiftOut(dataPin,clockPin,MSBFIRST,data);
    digitalWrite(latchPin,HIGH);
}
void display(int dec){  //display function for 7-segment display
	int delays = 1;
    unsigned long  digit;
	outData(0xffff);	
    digit=selectDigit(0x01);      //select the first, and display the single digit
    outData(num[dec%10]|digit);   
    delay(delays);          //display duration
    
    outData(0xffff);    
    digit=selectDigit(0x02);      //select the second, and display the tens digit
    outData(num[dec%100/10]|digit);
    delay(delays);
    
    outData(0xffff);    
    digit=selectDigit(0x04);      //select the third, and display the hundreds digit
    outData(num[dec%1000/100]|digit);
    delay(delays);
    
    outData(0xffff);    
    digit=selectDigit(0x08);      //select the fourth, and display the thousands digit
    outData(num[dec%10000/1000]|digit);
    delay(delays);
}
void timer(int  sig){       //Timer function
    if(sig == SIGALRM){   //If the signal is SIGALRM, the value of counter plus 1, and update the number displayed by 7-segment display
        counter ++;         
        alarm(1);           //set the next timer time
        printf("counter : %d \n",counter);
    }
}
int main(void)
{
    int i;
    
    printf("Program is starting ...\n");
    
    wiringPiSetup();
    
    pinMode(dataPin,OUTPUT);        //set the pin connected to74HC595 for output mode
    pinMode(latchPin,OUTPUT);
    pinMode(clockPin,OUTPUT);
    
    signal(SIGALRM,timer);  //configure the timer
    alarm(1);               //set the time of timer to 1s
    while(1){
        display(counter);   //display the number counter
    }
    return 0;
}


