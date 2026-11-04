#include <OneWire.h>
#include <DallasTemperature.h>
#include "SR04.h"
#include <SoftwareSerial.h>

/* Depth sensor */
int depth = 0;
int depthPin = A1;
#define DEPTH_DANGER 400

/* Temperature sensor */
// Data wire is conntec to the Arduino digital pin 4
#define ONE_WIRE_BUS 4


// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature tempSensor(&oneWire);

/* Flow sensor */
/*YF- S201 water Flow sensor code for Arduino */
const int flowPin = 2;

volatile int  pulseCount;
unsigned int  literPerHour;
unsigned long currentTime, loopTime;

#define FLOW_DANGER 20

/*Turbidity*/
int turbidityPin = A0;
int turbidity = 0;
#define TURBIDITY_DANGER 20
//Ultrusonic
#define ULTRASONIC_TRIG_PIN 12
#define ULTRASONIC_ECHO_PIN 11
SR04 fishSensor = SR04(ULTRASONIC_ECHO_PIN,ULTRASONIC_TRIG_PIN);
long fishDistance;

long prevFishDistance;

#define WALL_DISTANCE 23

// Bluetooth
SoftwareSerial BTSerial(14,15); 
//LEDs
int tempLED = 6;
int turbidityLED = 7;
int flowLED = 8;
int depthLED = 9;


/* Buzzer */
int buzzer = 13;
bool valLEDBuzzer;

void setup() {
  
  // Set up buzzer
  pinMode(buzzer, OUTPUT);
  // Set up depth sensor
  pinMode(depthPin, INPUT);
  // Start up the temperature library
  tempSensor.begin();
  // Set up flow sensor
  pinMode(flowPin, INPUT);
  attachInterrupt(0, detectRisingEdge, RISING);
  currentTime = millis();
  loopTime = currentTime;
  //set up turbidity
  pinMode(turbidityPin, INPUT);
  /* Set up Serial connection */
  Serial.begin(9600);
  /* Set up Bluetooth connection */
  BTSerial.begin(9600);
  //Set Up LEDS
  pinMode(tempLED,OUTPUT);
  pinMode(turbidityLED, OUTPUT);
  pinMode(flowLED, OUTPUT);
  pinMode(depthLED, OUTPUT);
}

void processDepth(){
    // Reads the depth sensor
  depth = analogRead(depthPin);
  Serial.print("Depth: ");
  Serial.println(depth);
}

void processTemp(){
  tempSensor.requestTemperatures(); 
  
  Serial.print("Celsius temperature: ");
  // Why "byIndex"? You can have more than one IC on the same bus. 0 refers to the first IC on the wire
  Serial.print(tempSensor.getTempCByIndex(0)); 
  Serial.print(" - Fahrenheit temperature: ");
  Serial.println(tempSensor.getTempFByIndex(0));
}

void processFlow(){
  currentTime = millis();
   if(currentTime >= (loopTime + 1000))
   {
      loopTime = currentTime;
      literPerHour = (pulseCount * 60 / 7.5);
      pulseCount = 0;
      Serial.print(literPerHour, DEC);
      Serial.println(" Liter/hour");
   }

}
void detectRisingEdge ()
{ 
   pulseCount++;
}
void processTurbidity ()
{
  turbidity = analogRead(turbidityPin);
  Serial.print("turbidity: ");
  Serial.println(turbidity);
}
void processFish ()
{
  fishDistance =fishSensor.Distance();
  Serial.print(fishDistance);
  Serial.println("cm");
  if ((fishDistance < WALL_DISTANCE) && (prevFishDistance > WALL_DISTANCE)) {
    Serial.println("fish found");
  }
  prevFishDistance = fishDistance;
}
void playBuzzer ()
{
  if ((depth > DEPTH_DANGER) || (literPerHour > FLOW_DANGER) ||
      (turbidity > TURBIDITY_DANGER)){
    digitalWrite(buzzer, valLEDBuzzer);
  }
}

void blinkTempLED ()
{
  digitalWrite(tempLED,HIGH);
}
void blinkTurbidityLED ()
{
  if (turbidity > TURBIDITY_DANGER){
    digitalWrite(turbidityLED, valLEDBuzzer);
  }

}
void blinkFlowLED ()
{
  if (literPerHour > FLOW_DANGER){
    digitalWrite(flowLED, valLEDBuzzer);

  }

}
void blinkDepthLED ()
{
  if (depth > DEPTH_DANGER) {
    //Alert
    digitalWrite (depthLED, valLEDBuzzer);
  }
}
void loop() {
  //Serial.write("\n\n\n\n\n\n\n");
  processDepth();
  processTemp();
  processFlow();
  processTurbidity();
  processFish();
  playBuzzer();
  blinkTempLED();
  blinkTurbidityLED();
  blinkFlowLED ();
  blinkDepthLED ();
  BTSerial.print("IT IS WORKING! YAY\n");
  
  if (BTSerial.available()){
    Serial.print(BTSerial.read());
    playBuzzer();
  }
  valLEDBuzzer = !valLEDBuzzer;
  
}
