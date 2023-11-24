#include <Servo.h>

int lightVal;
int lightPin=A4;
int dt=250;
Servo myservo;
int servoPin=9;
int angle=0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(lightPin,INPUT);
pinMode(servoPin,OUTPUT);
myservo.attach(servoPin);
}

void loop() {
  // put your main code here, to run repeatedly:
lightVal=analogRead(lightPin);

delay(dt);
angle=(-0.253)*(lightVal-780);
myservo.write(angle);
Serial.println(angle);
}
