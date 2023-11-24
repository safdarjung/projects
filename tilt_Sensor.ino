int tiltPin=2;
int tiltval;
int redPin=7;
int bluePin=8;
int dt=500;


void setup() {
  // put your setup code here, to run once:
pinMode(tiltPin,INPUT);
pinMode(bluePin,OUTPUT);
pinMode(redPin,OUTPUT);
digitalWrite(tiltPin,HIGH);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
tiltval=digitalRead(tiltPin);
if (tiltval==0){
  digitalWrite(redPin,HIGH);
  delay(dt);
  digitalWrite(bluePin,LOW);
}
if (tiltval==1){
  digitalWrite(bluePin,HIGH);
  delay(dt);
  digitalWrite(redPin,LOW);
  
}
Serial.println(tiltval);

}
