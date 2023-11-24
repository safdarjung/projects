
int lightPin=A0;
int lightVal;
int dv=250;
int redPin=11;
int bluePin=10;

void setup() {
  // put your setup code here, to run once:
pinMode(lightPin,INPUT);
pinMode(redPin,OUTPUT);
pinMode(bluePin,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
lightVal=analogRead(lightPin);
Serial.println(lightVal);
delay(dv);

if (lightVal<=400){
  digitalWrite(redPin,HIGH);
  digitalWrite(bluePin,LOW);
}

if (lightVal>=400){
  digitalWrite(redPin,LOW);
  digitalWrite(bluePin,HIGH);
}

if (lightVal<=200){
  digitalWrite(redPin,LOW);
  digitalWrite(bluePin,LOW);
}
}
