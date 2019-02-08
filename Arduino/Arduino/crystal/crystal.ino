#include <dht.h>
dht DHT;
//Constants
#define DHT21_PIN A0     // DHT 22  (AM2302) - what pin we're connected to

//Variables
float hum;  //Stores humidity value
float temp; //Stores temperature value

#include <LiquidCrystal.h> // includes the LiquidCrystal Library 
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // Creates an LC object. Parameters: (rs, enable, d4, d5, d6, d7) 
void setup() { 
 Serial.begin(9600);
 lcd.begin(16,2); // Initializes the interface to the LCD screen, and specifies the dimensions (width and height) of the display } 
}
void loop() { 
  int chk = DHT.read21(DHT21_PIN);
    //Read data and store it to variables hum and temp
    hum = DHT.humidity;
    temp= DHT.temperature;
    //Print temp and humidity values to serial monitor
     lcd.setCursor(0,0);
 lcd.println("Fukt.: "); 
 Serial.println(hum);
 lcd.print("%"); 
 lcd.print(hum); 
 lcd.setCursor(0,1);
 lcd.println("Temp.: ");
 lcd.print(temp); 
 delay(5000); //Delay 2 sec.
 lcd.clear();
}
