/*****************************************************
 * Filename    : Sketch_15_1_1_Relay
 * Description : Control the Motor by Relay
 * auther      : www.freenove.com
 * modification: 2016/08/30
 *****************************************************/
import processing.io.*;

int relayPin = 12;
int buttonPin = 26;
SingleKey skey = new SingleKey(buttonPin);
boolean relayState = false;
BUTTON btn;
float rotaSpeed = 0.02 * PI;  //virtual fan's rotating speed, 
float rotaPosition = 0;  //motor position
void setup() {
  size(640, 360);
  GPIO.pinMode(relayPin, GPIO.OUTPUT);
  btn = new BUTTON(90, height - 90, 50, 30);   //define the button
  btn.setBgColor(0, 255, 0);  //set button color
  btn.setText("OFF");        //set button text
}

void draw() {
  background(255);
  titleAndSiteInfo();  //title and site information

  skey.keyScan();    //key scan
  if (skey.isPressed) {  //key is pressed?
    relayAction();
  }
  textAlign(RIGHT, CENTER);
  text("RelayState: ", btn.x, btn.y+btn.h/2);
  btn.create();      //create the button
  drawFan(relayState);    //show the virtual fan in Display window
}
//Draw a clover fan according to the stating angle
void drawFan(boolean State) {  
  if(State){
    fill(0,0,255);
    ellipse(width/2, height/2, 150, 150);
  }
  else{
    fill(0,0,0);
    ellipse(width/2, height/2, 150, 150);
  }
  
}
void relayAction() {
  if (relayState) {
    GPIO.digitalWrite(relayPin, GPIO.LOW);
    relayState = false;
    btn.setBgColor(255, 0, 0);
    btn.setText("OFF");
  } else {
    GPIO.digitalWrite(relayPin, GPIO.HIGH);
    relayState = true;
    btn.setBgColor(0, 255, 0);
    btn.setText("ON");
  }
}
void mousePressed() {
  if ((mouseY< btn.y+btn.h) && (mouseY>btn.y) 
    && (mouseX< btn.x+btn.w) && (mouseX>btn.x)) { // the mouse click the button
    relayAction();
  }
}

void titleAndSiteInfo() {
  fill(0);
  textAlign(CENTER);    //set the text centered
  textSize(40);        //set text size
  text("Relay & LED", width / 2, 40);    //title
  textSize(16);
  text("www.freenove.com", width / 2, height - 20);    //site
}
