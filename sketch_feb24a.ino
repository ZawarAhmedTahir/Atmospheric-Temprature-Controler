/*

*/
#include <Wire.h>
#include <Adafruit_ADS1015.h>

unsigned long elapsed = 0;

float ifactor = 3.5355; // current correction factor
float sfactor = 30;
float y;
float b;
float r;

float Yrms;
float Brms;
float Rrms;

int ns = 20;
int ys = 0;
int rs = 0;
int bs = 0;
int rz = 0;
int yz = 0;
int bz = 0;

float py=0.0;
float pb=0.0;
float pr=0.0;
int start=0;
int16_t adc0, adc1, adc2, adc3;

Adafruit_ADS1115 ads;

void setup() {
  Serial.begin(115200);
  //Wire.begin();
  pinMode(A3, OUTPUT);
  

  ads.setGain(GAIN_TWO);
  ads.begin();
}

void loop() {
  if(start==0){
    Serial.println("wait");
    //digitalWrite(A3, LOW);
    delay(20000);
    digitalWrite(A3, LOW);
    start=1;
    }
  if (ys < ns) {
    adc1 = ads.readADC_SingleEnded(1);
    if (adc1 < 0) {
      adc1 = 0;
      yz += 1;
    }
    else {
      y = (adc1 * 0.0625) / 1000;
      if (py <= y) py = y;
      //sqY = py * py;
      //sumY += sqY;
      ys += 1;
      yz = 0;
    }
  }
  if (rs < ns) {
    adc2 = ads.readADC_SingleEnded(3);
    if (adc2 < 0) {
      adc2 = 0;
      rz += 1;
    }
    else {
      r = (adc2 * 0.0625) / 1000;
      if (pr <= r) pr = r;
      //sqR = pr * pr;
      //sumR += sqR;
      rs += 1;
      rz = 0;
    }
  }
  if (bs < ns) {
    adc3 = ads.readADC_SingleEnded(2);
    if (adc3 < 0) {
      adc3 = 0;
      bz += 1;
    }
    else {
      b = (adc3 * 0.0625) / 1000;
      if (pb <= b) pb = b;
      //sqB = pb * pb;
      //sumB += sqB;
      bs += 1;
      bz = 0;
    }
  }
  if (ys >= ns) {
    //Yrms = ifactor * sqrt(sumY / ns);
    Yrms = ifactor * sfactor * py;
    if (Yrms < 0.05) Yrms = 0.00;
    ys = 0;
    py = 0;
  }
  if (yz >= ns) {
    Yrms = 0;
    yz = 0;
  }
  if (rs >= ns) {
    //Rrms = ifactor * sqrt(sumR / ns);
    Rrms = ifactor * sfactor * pr;
    if (Rrms < 0.05) Rrms = 0.00;
    rs = 0;
    pr = 0;
  }
  if (rz >= ns) {
    Rrms = 0;
    rz = 0;
  }
  if (bs >= ns) {
    //Brms = ifactor * sqrt(sumB / ns);
    Brms = ifactor * sfactor * pb;
    if (Brms < 0.05) Brms = 0.00;
    bs = 0;
    pb = 0;
  }
  if (bz >= ns) {
    Brms = 0;
    bz = 0;
  }

  Serial.print(Yrms*1.35);
  Serial.print(" ");
  Serial.print(Brms*1.35);
  Serial.print(" ");
  Serial.println(Rrms*1.35);

}
