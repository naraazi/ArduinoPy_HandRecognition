void setup() {
    Serial.begin(9600);
    Serial.setTimeout(100);

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
        String teststr = Serial.readString();  // -- read until timeout
        teststr.trim();  // -- remove any \r \n whitespace at the end of the String

        if (teststr.equals("a")) {
            digitalWrite(8, HIGH);
            delay(1000);
            digitalWrite(8, LOW);
        }
        if (teststr.equals("b")) {
            digitalWrite(9, HIGH);
            delay(1000);
            digitalWrite(9, LOW);
        }
        if (teststr.equals("c")) {
            digitalWrite(10, HIGH);
            delay(1000);
            digitalWrite(10, LOW);
        }
        if (teststr.equals("d")) {
            digitalWrite(11, HIGH);
            delay(1000);
            digitalWrite(11, LOW);
        }
        if (teststr.equals("e")) {
            digitalWrite(12, HIGH);
            delay(1000);
            digitalWrite(12, LOW);
        }
    }
}
