#include <dht.h>
dht DHT;
//Constants
#define DHT21_PIN A0     // DHT 22  (AM2302) - what pin we're connected to

//Variables
float hum;  //Stores humidity value
float temp; //Stores temperature value
void setup() { 
 Serial.begin(9600);
}
void loop() { 
  int chk = DHT.read21(DHT21_PIN);
    //Read data and store it to variables hum and temp
    hum = DHT.humidity;
    temp= DHT.temperature;
    //Print temp and humidity values to serial monitor
    Serial.println(hum);
    delay(5000); //Delay 2 sec.
}
