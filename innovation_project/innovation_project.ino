#include <OneWire.h>
#include <DallasTemperature.h>
#include "SR04.h"
#include <SoftwareSerial.h>
#include <LiquidCrystal.h>

/* Depth sensor */
int depth = 0;
int depthPin = A1;
#define DEPTH_DANGER 400

/* Temperature sensor */
// Data wire is connected to the Arduino digital pin 4
#define ONE_WIRE_BUS 4

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature tempSensor(&oneWire);

float temperature;
// Temperature where we need to alert
#define TEMPERATURE_DANGER 20

/* Flow sensor */
/*YF- S201 water Flow sensor code for Arduino */
const int flowPin = 2;

volatile int  pulseCount;
unsigned int  literPerHour;
unsigned long currentTime, loopTime;

//Flow rate where we need to alert
#define FLOW_DANGER 20

/*Turbidity*/
int turbidityPin = A0;
int turbidity = 0;

// Turbidity value where we need to alert
#define TURBIDITY_DANGER 500

/* Ultrasonic */
#define ULTRASONIC_TRIG_PIN 12
#define ULTRASONIC_ECHO_PIN 11
SR04 fishSensor = SR04(ULTRASONIC_ECHO_PIN,ULTRASONIC_TRIG_PIN);

// Keep current and previous value to be able to compare and find out when fish is seen.
long fishDistance;
long prevFishDistance;
int fishCount = 0;

// Distance to the wall where ultrasonic sensor is facing.
#define WALL_DISTANCE 8

/* Status LEDs */
int tempLED = 6;
int turbidityLED = 7;
int flowLED = 8;
int depthLED = 9;

/* Buzzer */
int buzzer = 13;

//Value used to switch LED and buzzer to on and off.
bool valLEDBuzzer;


/* LCD */
LiquidCrystal lcd(5, 3, 10, 14, 15, 16);

/* Debugging */
// If this pin is not connected, we run in regular mode.
// If pin is connected to ground, we run in debug mode where we print sensr values.
int debugPin = 20;
bool debugMode = true;

void setup() {
  
  /* Set up buzzer */
  pinMode(buzzer, OUTPUT);

  /* Set up depth sensor */
  pinMode(depthPin, INPUT);

  /* Start up the temperature library */
  tempSensor.begin();

  /* Set up flow sensor */
  pinMode(flowPin, INPUT);
  attachInterrupt(0, detectRisingEdge, RISING);
  currentTime = millis();
  loopTime = currentTime;

  /* Set up turbidity sensor */
  pinMode(turbidityPin, INPUT);

  /* Set up Serial connection to computer */
  Serial.begin(9600);

  /* Set up Bluetooth connection */
  Serial1.begin(9600);

  /* Set Up LEDS */
  pinMode(tempLED,OUTPUT);
  pinMode(turbidityLED, OUTPUT);
  pinMode(flowLED, OUTPUT);
  pinMode(depthLED, OUTPUT);
  
  /* Set up LCD */
  lcd.begin(16,2);

  /* Set up debug pin */
  pinMode(debugPin, INPUT_PULLUP);
}

void processDepth(){
  /* Reads the depth sensor - save it into depth variable, so we can use later. */
  depth = analogRead(depthPin);
}

void processTemp(){
  /* Read the temperature sensor - save it into temperature variable, so we can use later.  */
  tempSensor.requestTemperatures(); 
  temperature = tempSensor.getTempFByIndex(0);
}

void processFlow(){
  /* Read the flow sensor - save it into literPerHour variable, so we can use later. */
  currentTime = millis();
   if(currentTime >= (loopTime + 1000))
   {
      loopTime = currentTime;
      literPerHour = (pulseCount * 60 / 7.5);
      pulseCount = 0;
   }

}

void detectRisingEdge ()
{ 
  /* This is called when the flow sensor interrupts arduino. */
  pulseCount++;
}

void processTurbidity ()
{
  /* Read the turbidity sensor - save it into turbidity variable, so we can use later. */
  turbidity = analogRead(turbidityPin);
}
void processFish ()
{
  /* Read the ultrasonic sensor and detect when a fish is found. */
  fishDistance = fishSensor.Distance();
  if ((fishDistance < WALL_DISTANCE) && (prevFishDistance > WALL_DISTANCE)) {
    Serial.println("fish found");
    Serial1.println("fish found");
    fishCount++;
  }
  prevFishDistance = fishDistance;
}
void playBuzzer ()
{
  if ((depth > DEPTH_DANGER) || (literPerHour > FLOW_DANGER) ||
      (turbidity > TURBIDITY_DANGER) || (temperature > TEMPERATURE_DANGER)){
    digitalWrite(buzzer, valLEDBuzzer);
  }
}

void blinkTempLED ()
{
  if (temperature > TEMPERATURE_DANGER) {
    digitalWrite(tempLED,valLEDBuzzer);
    Serial1.println("Temperature is too hot!");
  
  }
}
void blinkTurbidityLED ()
{
  if (turbidity > TURBIDITY_DANGER){
    digitalWrite(turbidityLED, valLEDBuzzer);
    Serial.println("Water is too dirty!");
    Serial1.println("Water is too dirty!");
  }

}
void blinkFlowLED ()
{
  if (literPerHour > FLOW_DANGER){
    digitalWrite(flowLED, valLEDBuzzer);
    Serial.println("Water flow is too fast!");
    Serial1.println("Water flow is too fast!");
  }

}
void blinkDepthLED ()
{
  if (depth > DEPTH_DANGER) {
    //Alert
    digitalWrite (depthLED, valLEDBuzzer);
    Serial.println("Water is too deep!");
    Serial1.println("Water is too deep!");
  }
}

void readFromBluetooth()
{
  if (Serial1.available()){
    
    // If we read debug or demo, change the mode
  }
}

void writeToBluetooth()
{
  
  //In debug mode: Print depth, flow, temp, turbidity and fish count(ultrasonic sensor) in one line.
  //Always print the danger info and when fish count increases.
  if (debugMode == LOW) {
    /* Computer */
    Serial.print("Flow rate: ");
    Serial.print(literPerHour);
    Serial.print(" liters/hour, Depth: ");
    Serial.print(depth);
    Serial.print(" cm, Temperature: ");
    Serial.print(temperature);
    Serial.print("F, Turbidity: ");
    Serial.print(turbidity); 
    Serial.print(", Fish count: ");
    Serial.println(fishCount);

    /* Bluetooth */
    Serial1.print("Flow rate: ");
    Serial1.print(literPerHour);
    Serial1.print(" liters/hour, Depth: ");
    Serial1.print(depth);
    Serial1.print(" cm, Temperature: ");
    Serial1.print(temperature);
    Serial1.print("F, Turbidity: ");
    Serial1.print(turbidity); 
    Serial1.print(", Fish distance: ");
    Serial1.print(fishDistance);
    Serial1.print(", Fish count: ");
    Serial1.println(fishCount);
    
  }
}

void writeLCD()
{
  lcd.clear();
  lcd.print("Fish:");
  lcd.setCursor(6,0);
  lcd.print(fishCount);
  if (debugMode == LOW) {
    lcd.setCursor(0,1);
    lcd.print(literPerHour);
    
    lcd.print(",");
    lcd.print(depth);
    lcd.print(",");
    lcd.print(temperature);
    
    lcd.print(",");
    lcd.print(turbidity);
    lcd.print(",");
    lcd.print(fishDistance);
  }

}
void loop() {
  debugMode = digitalRead(debugPin);
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

  readFromBluetooth();
  writeToBluetooth();
  writeLCD();
  

  valLEDBuzzer = !valLEDBuzzer;
  
}
