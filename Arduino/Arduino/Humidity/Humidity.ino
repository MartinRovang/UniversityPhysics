
/* How to use the DHT-21 sensor with Arduino uno
   Temperature and humidity sensor
   More info: http://www.ardumotive.com/how-to-use-dht-21-sensor-en.html
   Dev: Michalis Vasilakis // Date: 19/11/2016 // www.ardumotive.com */

//Libraries
#include <dht.h>
dht DHT;
//Constants
#define DHT21_PIN A0     // DHT 22  (AM2302) - what pin we're connected to

//Variables
float hum;  //Stores humidity value
float temp; //Stores temperature value

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    int chk = DHT.read21(DHT21_PIN);
    //Read data and store it to variables hum and temp
    hum = DHT.humidity;
    temp= DHT.temperature;
    //Print temp and humidity values to serial monitor
    Serial.print("Humidity: ");
    Serial.print(hum);
    Serial.print(" %, Temp: ");
    Serial.print(temp);
    Serial.println(" Celsius");
    delay(2000); //Delay 2 sec.
}
