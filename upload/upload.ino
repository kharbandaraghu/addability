/*
 * Connect thw pwm pins in this fashion and dont forget to download the pwm driver
 * 
 * vcc-5v
 * sda-A4
 * sce-A5
 * gnd-gnd
 */
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  125 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  575 // this is the 'maximum' pulse length count (out of 4096)

// create array for incoming bytes
int incoming[2];

void setup() 
{
  Serial.begin(9600);
  pwm.begin();
  // Analog servos run at ~60 Hz updates
  pwm.setPWMFreq(60); 
  // Set arduino's LED for testing purposes 
  pinMode(13,OUTPUT);
}

void loop() 
{
  if (Serial.available() >= 3) 
  {
    // get input bytes    
    for (int i = 0; i < 3; i++)
    {
      incoming[i] = Serial.read();
    }
    // send the first value as 255 to trigger, second arguement - is pin and the third one is degrees
    if (incoming[0] == 255)
    {
        pwm.setPWM(incoming[1], 0, angleToPulse(incoming[2])); 
    }
  }
}

// Function to change degress into pulse
int angleToPulse(int ang){
   int pulse = map(ang,0, 180, SERVOMIN,SERVOMAX);// map angle of 0 to 180 to Servo min and Servo max 
   Serial.print("Angle: ");Serial.print(ang);
   Serial.print(" pulse: ");Serial.println(pulse);
   return pulse;
}
