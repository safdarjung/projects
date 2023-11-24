#include <Stepper.h>
int stepsperrev = 2048;
Stepper mystepper(stepsperrev, 8,10,9,11); 
int motSpeed=10;
int dt =500; 
int buttonPin=2;
int motDir=1;
int buttonValnew;
int buttonValold=1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  mystepper.setSpeed(motSpeed);
  pinMode(buttonPin,INPUT);
  digitalWrite(buttonPin,HIGH);
  
  

}

void loop() {
  // put your main code here, to run repeatedly:
buttonValnew=digitalRead(buttonPin);
if (buttonValold==1 && buttonValnew==0){
  motDir=motDir*(-1);
}
mystepper.step(motDir*1);
buttonValold=buttonValold;

mystepper.step(stepsperrev);
delay(dt);
mys tepper.step(-stepsperrev);
delay(dt);
}
