byte pin[] = {2, 3, 4, 5, 6, 7, 8, 9}; // arduino pin array
String serialData;

void setup()
{
    for (byte a = 0; a < 8; a++)
    {
        pinMode(pin[a], OUTPUT); // define output pins
    }

    Serial.begin(9600);
    Serial.setTimeout(10);
}

void loop()
{

    if (Serial.available() > 0)
    {
        String command = Serial.readString();
        command.trim();

        Serial.print(command);

        if (command == "reset")
        {
            Serial.print("Here");
            reset();
        }
        else
        {
            int digit = command.toInt();
            if (digitalRead(digit) == HIGH)
            {
                digitalWrite(digit, LOW);
            }
            else
            {
                digitalWrite(digit, HIGH);
            }
        }
    }
}

void reset()
{
    for (byte a = 0; a < 8; a++)
    {
        digitalWrite(pin[a], LOW); // turn off each pin
    }
}