const unsigned int numReadings = 200; //samples to calculate Vrms.
 
int readingsVClamp[numReadings];    // samples of the sensor SCT-013-000
int readingsGND[numReadings];      // samples of the <span id="result_box" class="" lang="en"><span class="hps">virtual</span> <span class="hps alt-edited">ground</span></span>
float SumSqGND = 0;            
float SumSqVClamp = 0;
float total = 0; 
 
 
int PinVClamp = A0;    // Sensor SCT-013-000
int PinVirtGND = A1;   // <span id="result_box" class="" lang="en"><span class="hps">Virtual</span> <span class="hps alt-edited">ground</span></span>
 
void setup() {
  Serial.begin(9600);
  pinMode(A3, OUTPUT);
  // initialize all the readings to 0:
  for (int thisReading = 0; thisReading < numReadings; thisReading++) {
    readingsVClamp[thisReading] = 0;
    readingsGND[thisReading] = 0;
  }
}
 
void loop() {
  unsigned int i=0;
  SumSqGND = 0;
  SumSqVClamp = 0;
  total = 0; 
   
  for (unsigned int i=0; i<numReadings; i++)
  {
    readingsVClamp[i] = analogRead(PinVClamp) - analogRead(PinVirtGND);
    delay(1); // 
  }
 
  //Calculate Vrms
  for (unsigned int i=0; i<numReadings; i++)
  {
    SumSqVClamp = SumSqVClamp + sq((float)readingsVClamp[i]);
 
  }
   
  total = sqrt(SumSqVClamp/numReadings);
  total= (total*(float)2/3); // Rburden=3300 ohms, LBS= 0,004882 V (5/1024)
                             // Transformer of 2000 laps (SCT-013-000).
                             // 5*220*2000/(3300*1024)= 2/3 (aprox)
   if(total>3){
    analogWrite(A3, 255);
    Serial.println("cross");
    }

   else{
    analogWrite(A3, 0);
    }
  Serial.println(total);
  delay(500);  
}
