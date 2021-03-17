/*****************************************************
 * Filename    : Sketch_02_1_1_FollowLight
 * Description : Use the mouse to control the LEDGraph Bar 
 * auther      : www.freenove.com
 * modification: 2016/08/15
 *****************************************************/
import processing.io.*;
int leds[]={17,27,22,10,9,11,5,6,13,19,26}; //define ledPins
void setup() {
  size(640, 360);  //display window size
  for (int i=0; i<11; i++) {  //set led Pins to output mode
    GPIO.pinMode(leds[i], GPIO.OUTPUT);
  }
  background(102);
  textAlign(CENTER);    //set the text centered
  textSize(40);        //set text size
  text("Follow Light", width / 2, 40);    //title
  textSize(16);
  text("www.freenove.com", width / 2, height - 20);    //site
}

void draw() {
  for (int i=0; i<11; i++) {    //draw 10 rectanglar box
    if (mouseX>(100+40*i)) {    //if the mouse cursor on the right of rectanglar box 
      fill(255, 0, 0);        //fill the rectanglar box in red color
      GPIO.digitalWrite(leds[i],GPIO.HIGH );  //turn on the corresponding led
    } else { 
      fill(255, 255, 255);  //else fill the rectanglar box in white color and turn off the led
      GPIO.digitalWrite(leds[i], GPIO.LOW);  
    }
    rect(100+40*i, 90, 35, 180);    //draw a rectanglar box
  }
}
