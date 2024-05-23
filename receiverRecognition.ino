void setup() {
    Serial.begin(9600);
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
    pinMode(11, OUTPUT);
    pinMode(12, OUTPUT);
    digitalWrite(8, LOW);
    digitalWrite(9, LOW);
    digitalWrite(10, LOW);
    digitalWrite(11, LOW);
    digitalWrite(12, LOW);

}

void loop() {
    if (Serial.available() > 0) {
        int quant = Serial.available();
        String teststr = Serial.readStringUntil("\r");  // -- read until timeout - remove any \r \n whitespace at the end of the String

        if (quant == 1) {
            digitalWrite(8, HIGH);
            delay(1000);
            digitalWrite(8, LOW);
            }
        if (quant == 2) {
            digitalWrite(9, HIGH);
            delay(1000);
            digitalWrite(9, LOW);
        }
        if (quant == 3) {
            digitalWrite(10, HIGH);
            delay(1000);
            digitalWrite(10, LOW);
        }
        if (quant == 4) {
            digitalWrite(11, HIGH);
            delay(1000);
            digitalWrite(11, LOW);
        }
        if (quant == 5) {
            digitalWrite(12, HIGH);
            delay(1000);
            digitalWrite(12, LOW);
        }
    }
}
