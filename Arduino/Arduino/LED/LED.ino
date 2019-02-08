
void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
}
void loop() {
  digitalWrite(2, HIGH);
  delay(200);
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);
  delay(5000);
  digitalWrite(3, LOW);
}
