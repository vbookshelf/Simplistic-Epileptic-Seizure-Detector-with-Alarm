
// Ref videos that explain how the Python code communicates with the Arduino.:
// https://www.youtube.com/watch?v=utnPvE8hN3o
// https://www.youtube.com/watch?v=OJtpA_qTNL0

// Notes: 
// 1- Strings must always be inside double quotes ("text") or the code won't run.



#define signalPin 13

// initialize a variable
String seizure_status;


void setup() {
  // The same baud rate (9600) should be set in the Python code
  // and in the Arduino code.
  Serial.begin(9600);

  // Set LED_BUILTIN (pin 13) as an output.
  // The LED on the Arduino will also switch on when the alarm is triggered.
  pinMode(signalPin, OUTPUT);

}

void loop() {

    // Read the seizure_status sent by the Python code and store it in a variable called "seizure_status".
    // This line means: "read until you reach a newline chracter".
    // You will see that in the Python code we have added a newline character before sending the string.
    seizure_status = Serial.readStringUntil('\n');

    // Remove any leading and trailing whitespaces that could have been added.
    // Sometimes when devices are communicating they add a whitespace.
    seizure_status.trim();
    
    if (seizure_status.equals("one")) {
      
      // Pulse the alarm 100 times. Increasing this number will make the alarm run longer.
      // To switch off the alarm press the reset button on the Arduino.
      // But note that the alarm will trigger again if the hips are above the shoulders.
      for (int x=0; x<100; x++) {

        // Turn on the tone
        tone(signalPin, 200);
        delay(500);
  
        // Turn off the tone
        noTone(signalPin);
        delay(500);
          
        }
      
      }

}
