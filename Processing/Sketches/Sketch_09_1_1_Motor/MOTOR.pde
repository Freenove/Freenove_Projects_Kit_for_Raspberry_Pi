/*****************************************************
 * Filename    : MOTOR
 * Description : class MOTOR
 * auther      : www.freenove.com
 * modification: 2016/08/22
 *****************************************************/

import processing.io.*;

class MOTOR {
  int mPin1, mPin2;
  SOFTPWM p1,p2;
  public int dir;
  final public int CW = 1, CCW = 2, STOP = 3;
  public MOTOR(int pin1, int pin2) {
    mPin1 = pin1;
    mPin2 = pin2;
    //GPIO.pinMode(mPin1, GPIO.OUTPUT);
    //GPIO.pinMode(mPin2, GPIO.OUTPUT);
    p1 = new SOFTPWM(mPin1, 0, 200);
    p2 = new SOFTPWM(mPin2, 0, 200);
    dir = 0;
  }
  public void start(int dir, int speed) {
    switch(dir) {
    case CW:
      constrain(speed, 0, 100);
      p1.softPwmWrite(speed);
      p2.softPwmWrite(0);
      break;
    case CCW:
      constrain(speed, 0, 100);
      p1.softPwmWrite(0);
      p2.softPwmWrite(speed);
      break;
    case STOP:
      p1.softPwmWrite(0);
      p2.softPwmWrite(0);
      break;
    default:
      p1.softPwmWrite(0);
      p2.softPwmWrite(0);
      break;
    }
  }
}
