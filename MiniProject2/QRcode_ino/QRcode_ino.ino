int redPin = 12;
int greenPin = 11;
int bluePin = 13;
int GND = 10;

void setup() {
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT); 
  pinMode(GND, OUTPUT); 
  digitalWrite(GND,0);
}

void loop() {
  if (Serial.available() > 0) {
    char inChar = Serial.read();
    if (inChar == '1') {
      Serial.println(inChar);
      setColor(0, 255, 0); // green
    } 
    else if (inChar == '2') {
      Serial.println(inChar);
      setColor(0, 0, 255); // blue
    }
    else {
      setColor(0, 0, 0); // off
    }
  }
}

void setColor(int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue); 
}

