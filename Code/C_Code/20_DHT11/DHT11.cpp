/**********************************************************************
* Filename    : DHT11.cpp
* Description : Read the temperature and humidity data of DHT11
* Author      : www.freenove.com
* modification: 2021/1/1
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <stdint.h>
#include "DHT.hpp"

#define DHT11_Pin  4    //define the pin of sensor 

int main(){
    DHT dht;        //create a DHT class object
    int chk,sumCnt;//chk:read the return value of sensor; sumCnt:times of reading sensor
    
    printf("Program is starting ...\n");
    
    wiringPiSetup();
    
    while(1){
        chk = dht.readDHT11(DHT11_Pin); //read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
        sumCnt++;       //counting number of reading times
        printf("The sumCnt is : %d \n",sumCnt);
        switch(chk){
            case DHTLIB_OK:     //if the return value is DHTLIB_OK, the data is normal.
                printf("DHT11,OK! \n"); 
                break;
            case DHTLIB_ERROR_CHECKSUM:     //data check has errors
                printf("DHTLIB_ERROR_CHECKSUM! \n");
                break;
            case DHTLIB_ERROR_TIMEOUT:      //reading DHT times out
                printf("DHTLIB_ERROR_TIMEOUT! \n");
                break;
            case DHTLIB_INVALID_VALUE:      //other errors
                printf("DHTLIB_INVALID_VALUE! \n");
                break;
        }
        printf("Humidity is %.2f %%, \t Temperature is %.2f *C\n\n",dht.humidity,dht.temperature);
        delay(3000);
    }   
    return 1;
}

