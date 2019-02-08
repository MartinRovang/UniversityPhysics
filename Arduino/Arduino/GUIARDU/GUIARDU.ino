char mydata = 0;

void setup() { 
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
 Serial.begin(9600);
 
}
void loop() { 
  mydata = int(Serial.read());
  
  if(mydata == '1')
  {
  digitalWrite(2,HIGH);
  digitalWrite(3,LOW);
  }
  
  if(mydata == '0') {
  digitalWrite(3,HIGH);
  digitalWrite(2,LOW);
  }
  
}
  
