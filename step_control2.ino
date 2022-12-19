const int stepPin= 2 ;
const int dirPin= 3 ;
const int stepPin2= 8 ;
const int dirPin2= 9 ;
const int spr=4000;

void setup() {
  pinMode(stepPin,OUTPUT);
  pinMode(dirPin,OUTPUT);
  pinMode(stepPin2,OUTPUT);
  pinMode(dirPin2,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(dirPin, HIGH);
  digitalWrite(dirPin2, HIGH);
  for(int x=0; x<spr;x++)
 {   
    digitalWrite(stepPin,HIGH);
    digitalWrite(stepPin2,HIGH);

    delayMicroseconds(1000);
    
    digitalWrite(stepPin,LOW);
    digitalWrite(stepPin2,LOW);

    delayMicroseconds(1000);
 }
 delay(2000) ;
 
  digitalWrite(dirPin, LOW);
  digitalWrite(dirPin2, LOW);
  
  
  for(int x=0; x<spr;x++)
 {   
    digitalWrite(stepPin,HIGH);
    digitalWrite(stepPin2,HIGH);

    delayMicroseconds(1000);
    
    digitalWrite(stepPin,LOW);
    digitalWrite(stepPin2,LOW);

    delayMicroseconds(1000);
 }
 delay(2000) ;

}