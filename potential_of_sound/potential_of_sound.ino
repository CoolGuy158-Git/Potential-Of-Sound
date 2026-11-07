/* Very beginner(y) thing I made*/
/* Just bought an arduino and bro, why didn't I buy one years ago?? */
void setup() {
    Serial.begin(9600);
    pinMode(2, INPUT_PULLUP);
    pinMode(3, INPUT_PULLUP);
}

void loop() {
    /* Just sends voltage read from the potentiometer, and which buttons are pressed to python */
    /* Python can then interpret the signals from a potentiometer as a knob being turned */
    /* And button... As a button */
    int raw = analogRead(A2);
    int buttonPushed1 = !digitalRead(2);
    int buttonPushed2 = !digitalRead(3);
    float volts = raw * (5.0 / 1023.0);

    Serial.println(String("A2: ") + volts);
    Serial.println(String("2: ") + buttonPushed1);
    Serial.println(String("3: ") + buttonPushed2);
    delay(500);
}
