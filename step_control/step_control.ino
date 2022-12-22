const int stepPin= 2 ;
const int dirPin= 3 ;
const int spr=4000;

void setup() {
  pinMode(stepPin,OUTPUT);
  pinMode(dirPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(dirPin, HIGH);
  
  for(int x=0; x<spr;x++)
 {   
    digitalWrite(stepPin,HIGH);
    delayMicroseconds(1000);
    
    digitalWrite(stepPin,LOW);
    delayMicroseconds(1000);
 }
 delay(2000) ;
 
  digitalWrite(dirPin, LOW);
  
  for(int x=0; x<spr;x++)
 {   
    digitalWrite(stepPin,HIGH);
    delayMicroseconds(1000);
    
    digitalWrite(stepPin,LOW);
    delayMicroseconds(1000);
 }
 delay(2000) ;

}