#include <dht.h>
dht DHT;
//Constants
#define DHT21_PIN A0     // DHT 22  (AM2302) - what pin we're connected to

//Variables
float hum;  //Stores humidity value
float temp; //Stores temperature value
int switchVal;
int b = 0;
void setup() { 
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  //pinMode(5, INPUT);
  pinMode(7, OUTPUT);
 Serial.begin(9600);
}


void loop() { 
    int chk = DHT.read21(DHT21_PIN);
    //Read data and store it to variables hum and temp
    hum = DHT.humidity;
    temp = DHT.temperature;
    //Print temp and humidity values to serial monitor
  //switchVal = digitalRead(5);
  Serial.println(hum);
  if(hum > 45){
 /*   if(switchVal == HIGH){
      b = 1;
    }
 */
  digitalWrite(2,HIGH);
  digitalWrite(3,LOW);
  digitalWrite(7,HIGH);
 /* if(b == 0) {
    tone(4,400, 125);
    }
 */
  }
  else {
     b = 0;
    if(hum > 43){
    digitalWrite(7,LOW);}
    digitalWrite(3,HIGH);         //HUSK NORMALLY CLOSED
    digitalWrite(2,HIGH);
  }
  if(hum <= 43) {
     b = 0;
     digitalWrite(3,HIGH);
     digitalWrite(7,HIGH);
     digitalWrite(2,LOW);
    }
    delay(2000); //Delay 2 sec.
}
