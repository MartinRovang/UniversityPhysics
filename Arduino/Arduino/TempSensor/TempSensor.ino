
const int sensorPin = A0;
void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  float volts = (sensorValue / 1024.0) * 5;
  float celcius = (volts - .5)*100;
  Serial.println(celcius);
  Serial.print(" degrees Celsius, ");
  if(celcius > 21){
  digitalWrite(2,HIGH);
  digitalWrite(3,LOW);
  }
  else {
    digitalWrite(3,HIGH);
    digitalWrite(2,LOW);
  }
  delay(1000);
}
