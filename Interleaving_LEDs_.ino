int switchState = 0;
bool vLED = false;
bool bLED = false;
bool firstHigh = false;
void setup() {
  // put your setup code here, to run once:
  pinMode(3, INPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    switchState = digitalRead(3);
  Serial.print("switchState: ");
  Serial.println(switchState);
  
    if(!firstHigh){
    
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);

      if (switchState == HIGH){
            firstHigh = true;      
            bLED = !bLED;
            digitalWrite(4, HIGH);
            //(250);
            
            digitalWrite(5, LOW);
            bLED = !bLED;
        }
        }
     if(firstHigh){

       if (switchState == HIGH){
                  
            bLED = !bLED;
            digitalWrite(4, HIGH);
            //(250);
            
            digitalWrite(5, LOW);
            bLED = !bLED;
       }else if(switchState == LOW){
           //if (bLED == vLED){
            vLED = !vLED;
            digitalWrite(5, HIGH);
                      
            digitalWrite(4,LOW); 
            vLED = !vLED;
          //}

        }
     }
        



    } 