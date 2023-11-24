#include <Servo.h>

int servoPin=9;
int lightPin=A0;
int lightVal;
int dt=250;
int angle=0;

Servo myServo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myServo.attach(servoPin);
  pinMode(lightPin,INPUT);
  
}

void loop() {

  lightVal=analogRead(lightPin);
  Serial.println(lightVal);
  delay(dt);
  angle=(0.3*(lightVal-180.));
  myServo.write(angle);
}

  
