#include "EmonLib.h"
#define VOLT_CAL 598.3 
EnergyMonitor emon1;
  
int potencia;
 
void setup()
{
    emon1.current(0, 60.6);
    emon1.voltage(2, VOLT_CAL, 1.7);
 
    Serial.begin(9600);
}
 
void loop()
{
    emon1.calcVI(20,2000);
    float supplyVoltage   = emon1.Vrms;
    double Irms = emon1.calcIrms(1480);   // Calcula o valor da Corrente
    
    potencia = Irms * supplyVoltage;          // Calcula o valor da Potencia Instantanea    
 
    Serial.print("Corrente = ");
    Serial.print(Irms);
    Serial.println(" A");
    
    Serial.print("Potencia = ");
    Serial.print(potencia);
    Serial.println(" W");

    Serial.print("Tensão : "); //IMPRIME O TEXTO NA SERIAL
    Serial.print(supplyVoltage, 0); //IMPRIME NA SERIAL O VALOR DE TENSÃO MEDIDO E REMOVE A PARTE DECIMAL
    Serial.println("V"); //IMPRIME O TEXTO NA SERIAL
   
    delay(500);
 
    Serial.print(".");
    delay(500);
    Serial.print(".");
    delay(500);
    Serial.println(".");
    delay(500);
}
