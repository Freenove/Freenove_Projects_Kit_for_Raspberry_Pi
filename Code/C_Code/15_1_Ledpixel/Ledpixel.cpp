/**********************************************************************
* Filename    : Ledpixel.cpp
* Description : Drive stepping Motor
* Author      : www.freenove.com
* modification: 2021/1/1
**********************************************************************/
#include <wiringPi.h>
#include "Freenove_WS2812_Lib_for_Raspberry_Pi.hpp"
Freenove_WS2812 *a;
int constrain(int value,int min,int max){
    if (value>max){
        return max;
    }
    else if (value<min){
        return min;
    }
    else {
        return value;
    }
} 
int main(){
    printf("Program is starting ...\n");
    int i;
    a= new Freenove_WS2812(18,8,GRB);//pin led_count type
    a->set_Led_Brightness(50); 
    while(1){
        
        for(i=0;i<8;i++){
            a->set_Led_Color(i,255,0,0);  
            a->show();
            delay(100);
            }
        for(i=0;i<8;i++){
            a->set_Led_Color(i,0,255,0);  
            a->show();
            delay(100);
            }
        for(i=0;i<8;i++){
            a->set_Led_Color(i,0,0,255);  
            a->show();
            delay(100);
            }
    }
    a->clear();
    return 0;
}
