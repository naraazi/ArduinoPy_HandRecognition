void setup() {
    Serial.begin(9600);
    Serial.setTimeout(100);

    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(12, OUTPUT);
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
    digitalWrite(12, LOW);
}

void loop() {
    if (Serial.available() > 0) {
        String teststr = Serial.readString();  // -- read until timeout
        teststr.trim();  // -- remove any \r \n whitespace at the end of the String

        if (teststr.equals("a")) {
            digitalWrite(2, HIGH);
            delay(1000);
            digitalWrite(2, LOW);
        }
        if (teststr.equals("b")) {
            digitalWrite(3, HIGH);
            delay(1000);
            digitalWrite(3, LOW);
        }
        if (teststr.equals("c")) {
            digitalWrite(4, HIGH);
            delay(1000);
            digitalWrite(4, LOW);
        }
        if (teststr.equals("d")) {
            digitalWrite(5, HIGH);
            delay(1000);
            digitalWrite(5, LOW);
        }
        if (teststr.equals("e")) {
            digitalWrite(12, HIGH);
            delay(1000);
            digitalWrite(12, LOW);
        }
    }
}
