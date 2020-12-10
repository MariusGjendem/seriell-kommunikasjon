int button = 7;
int buttonstate = 0;
void setup()
{
  pinMode(button, INPUT);
  Serial.begin(9600);
}

void loop()
{
  buttonstate = digitalRead(button);
  if ( buttonstate == HIGH ) {
    Serial.write("hei");
  }
  delay(1000);

}
