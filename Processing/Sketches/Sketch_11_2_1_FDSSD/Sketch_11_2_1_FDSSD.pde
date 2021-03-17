/*****************************************************
 * Filename    : Sketch_11_2_1_FDSSD
 * Description : Control the 4-Digit 7-segment display by 74HC595
 * auther      : www.freenove.com
 * modification: 2016/09/05
 *****************************************************/
import processing.io.*;

int dataPin = 22;    //connect to the 74HC595
int latchPin = 27;
int clockPin = 17;
final int borderSize = 45;    //border size 
ProgressBar mBar;    //ProgressBar Object
IC74HC595 ic;      //IC74HC595 Object
boolean mMouse = false;    //determined whether a mouse click the ProgressBar
int index = 0;           // index of number
int lastMoveTime = 0;      //led last move time point
//encoding for character 0-9 of common anode SevenSegmentDisplay
final int[] numCode = {0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90};
PFont mFont;
int digit;
void setup() {
  size(640, 360);
  mBar = new ProgressBar(borderSize, height-borderSize, width-borderSize*2);
  mBar.setTitle("Speed");    //set the ProgressBar's title
  ic = new IC74HC595(dataPin, latchPin, clockPin);
  mFont = loadFont("DigifaceWide-100.vlw");  //create DigifaceWide font
  thread("displaySSD");
}

void draw() {
  background(255);
  titleAndSiteInfo();  //title and site information
  strokeWeight(4);    //border weight
  mBar.create();      //create the ProgressBar
  //control the speed of number change
  if (millis() - lastMoveTime > 50/(0.05+mBar.progress)) {
    lastMoveTime = millis();
    index++;
    if (index > 9999) {
      index = 0;
    }
  }
  //showNum(index);    //show the number in dispaly window
}
void showNum(int num) {
  fill(0);
  textSize(100);
  textFont(mFont);    //digiface font
  textAlign(CENTER, CENTER);
  text(nf(num,4,0), width/2, height/2);
}

void displaySSD() {
  while (true) {
    display(index);
  }
}
int selectDigit(int digit) {
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
void display(int dec) {
  
  digit=selectDigit(0x01); //select the first, and display the single digit 
  ic.write(ic.MSBFIRST, numCode[dec%10]|digit);       
  delay(1);               //display duration
  
  digit=selectDigit(0x02);  //select the second, and display the tens digit
  ic.write(ic.MSBFIRST, numCode[dec%100/10]|digit);
  delay(1);
  
  digit=selectDigit(0x04);  //select the third, and display the hundreds digit
  ic.write(ic.MSBFIRST, numCode[dec%1000/100]|digit);
  delay(1);
  
  digit=selectDigit(0x08);  //select the fourth, and display the thousands digit
  ic.write(ic.MSBFIRST, numCode[dec%10000/1000]|digit);
  delay(1);
}
void mousePressed() {
  if ( (mouseY< mBar.y+5) && (mouseY>mBar.y-5) ) {
    mMouse = true;    //the mouse click the progressBar
  }
}
void mouseReleased() {
  mMouse  = false;
}
void mouseDragged() {
  int a = constrain(mouseX, borderSize, width - borderSize);
  float t = map(a, borderSize, width - borderSize, 0.0, 1.0);
  if (mMouse) {
    mBar.setProgress(t);
  }
}
void titleAndSiteInfo() {
  fill(0);
  textAlign(CENTER);    //set the text centered
  textFont(createFont("", 100));  //default font
  textSize(40);        //set text size  
  text("4-Digit 7-Segment Display", width / 2, 40);    //title
  textSize(16);
  text("www.freenove.com", width / 2, height - 20);    //site
}
