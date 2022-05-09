int retardo=2;
char ordre;
int numero_pasos;
String movs;
String mov;

void setup() {                
Serial.begin(9600);
pinMode(13, OUTPUT);
pinMode(12, OUTPUT);
pinMode(11, OUTPUT);
pinMode(10, OUTPUT);
pinMode(9, OUTPUT);
pinMode(8, OUTPUT);
pinMode(7, OUTPUT);
pinMode(6, OUTPUT);
pinMode(5, OUTPUT);
pinMode(4, OUTPUT);
pinMode(3, OUTPUT);
pinMode(2, OUTPUT);

}

void U_der(){
 digitalWrite(13, LOW); 
 digitalWrite(12, LOW);  
 digitalWrite(11, HIGH);  
 digitalWrite(10, HIGH);  
   delay(retardo); 
 digitalWrite(13, LOW); 
 digitalWrite(12, HIGH);  
 digitalWrite(11, HIGH);  
 digitalWrite(10, LOW);  
   delay(retardo); 
 digitalWrite(13, HIGH); 
 digitalWrite(12, HIGH);  
 digitalWrite(11, LOW);  
 digitalWrite(10, LOW);  
  delay(retardo); 
 digitalWrite(13, HIGH); 
 digitalWrite(12, LOW);  
 digitalWrite(11, LOW);  
 digitalWrite(10, HIGH);  
  delay(retardo);  
}

void U_izq(){        // Pasos a la izquierda
 digitalWrite(13, HIGH); 
 digitalWrite(12, HIGH);  
 digitalWrite(11, LOW);  
 digitalWrite(10, LOW);  
  delay(retardo); 
 digitalWrite(13, LOW); 
 digitalWrite(12, HIGH);  
 digitalWrite(11, HIGH);  
 digitalWrite(10, LOW);  
  delay(retardo); 
 digitalWrite(13, LOW); 
 digitalWrite(12, LOW);  
 digitalWrite(11, HIGH);  
 digitalWrite(10, HIGH);  
  delay(retardo); 
 digitalWrite(13, HIGH); 
 digitalWrite(12, LOW);  
 digitalWrite(11, LOW);  
 digitalWrite(10, HIGH);  
  delay(retardo); 
}

void R_der(){         // Pasos a la derecha
 digitalWrite(9, LOW); 
 digitalWrite(8, LOW);  
 digitalWrite(7, HIGH);  
 digitalWrite(6, HIGH);  
   delay(retardo); 
 digitalWrite(9, LOW); 
 digitalWrite(8, HIGH);  
 digitalWrite(7, HIGH);  
 digitalWrite(6, LOW);  
   delay(retardo); 
 digitalWrite(9, HIGH); 
 digitalWrite(8, HIGH);  
 digitalWrite(7, LOW);  
 digitalWrite(6, LOW);  
  delay(retardo); 
 digitalWrite(9, HIGH); 
 digitalWrite(8, LOW);  
 digitalWrite(7, LOW);  
 digitalWrite(6, HIGH);  
  delay(retardo);  
}

void R_izq(){        // Pasos a la izquierda
 digitalWrite(9, HIGH); 
 digitalWrite(8, HIGH);  
 digitalWrite(7, LOW);  
 digitalWrite(6, LOW);  
  delay(retardo); 
 digitalWrite(9, LOW); 
 digitalWrite(8, HIGH);  
 digitalWrite(7, HIGH);  
 digitalWrite(6, LOW);  
  delay(retardo); 
 digitalWrite(9, LOW); 
 digitalWrite(8, LOW);  
 digitalWrite(7, HIGH);  
 digitalWrite(6, HIGH);  
  delay(retardo); 
 digitalWrite(9, HIGH); 
 digitalWrite(8, LOW);  
 digitalWrite(7, LOW);  
 digitalWrite(6, HIGH);  
  delay(retardo); 
}

void D_der(){         // Pasos a la derecha
 digitalWrite(5, LOW); 
 digitalWrite(4, LOW);  
 digitalWrite(3, HIGH);  
 digitalWrite(2, HIGH);  
   delay(retardo); 
 digitalWrite(5, LOW); 
 digitalWrite(4, HIGH);  
 digitalWrite(3, HIGH);  
 digitalWrite(2, LOW);  
   delay(retardo); 
 digitalWrite(5, HIGH); 
 digitalWrite(4, HIGH);  
 digitalWrite(3, LOW);  
 digitalWrite(2, LOW);  
  delay(retardo); 
 digitalWrite(5, HIGH); 
 digitalWrite(4, LOW);  
 digitalWrite(3, LOW);  
 digitalWrite(2, HIGH);  
  delay(retardo);  
}

void D_izq(){        // Pasos a la izquierda
 digitalWrite(5, HIGH); 
 digitalWrite(4, HIGH);  
 digitalWrite(3, LOW);  
 digitalWrite(2, LOW);  
  delay(retardo); 
 digitalWrite(5, LOW); 
 digitalWrite(4, HIGH);  
 digitalWrite(3, HIGH);  
 digitalWrite(2, LOW);  
  delay(retardo); 
 digitalWrite(5, LOW); 
 digitalWrite(4, LOW);  
 digitalWrite(3, HIGH);  
 digitalWrite(2, HIGH);  
  delay(retardo); 
 digitalWrite(5, HIGH); 
 digitalWrite(4, LOW);  
 digitalWrite(3, LOW);  
 digitalWrite(2, HIGH);  
  delay(retardo); 
}

void apagado(){         // Apagado del Motor
  digitalWrite(13, LOW);
  digitalWrite(12, LOW);
  digitalWrite(11, LOW); 
  digitalWrite(10, LOW);  
  digitalWrite(9, LOW);  
  digitalWrite(8, LOW);  
  digitalWrite(7, LOW); 
  digitalWrite(6, LOW);  
  digitalWrite(5, LOW);  
  digitalWrite(4, LOW);  
  digitalWrite(3, LOW);  
  digitalWrite(2, LOW);  

 }

void loop() {
  Serial.println("Serial Available - Nothing to do :(");
  //Serial.println(Serial.read());
  delay(5000);    
  while (Serial.available()) {
    ordre = Serial.read();
    movs += ordre;
    delay(500);
    while (movs.length() > 1) {
      delay(100);
      ordre = Serial.read();
      movs += ordre;
      //delay(2000);
      mov = movs.substring(0,1);
      //Serial.println(mov);
      //if (mov != "r" && mov != "R" && mov != "D" && mov != "d" && mov != "U" && mov != "u") {
        //apagado();
        //Serial.println("Nothing to do");
        //delay(2000);
        //Serial.println("LLista de moviments: "+movs+" ("+movs.length()+" caracters)");
      //}

      if (mov == "U") {
        Serial.println(mov+" - Motor 1 - Sentit horari"); 
        for (int i=0; i<128; i++){ 
          //Serial.println("Left");
          U_izq();
        }
        apagado();
      }
      if (mov == "u") {
        Serial.println(mov+" - Motor 1 - Sentit antihorari");
        for (int i=0; i<128; i++){ 
          //Serial.printnln("Right");
          U_der();
        }
        apagado();
      }
      if (mov == "R"){ 
        Serial.println(mov+" - Motor 2 - Sentit horari"); 
        for (int i=0; i<128; i++){ 
          //Serial.print("Left");
          R_izq();
        }
        apagado();
      }
      if (mov == "r") {
        Serial.println(mov+" - Motor 2 - Sentit antihorari");
        for (int i=0; i<128; i++){ 
          //Serial.print("Right");
          R_der();
        }
        apagado();
      }
      if (mov == "D"){ 
        Serial.println(mov+" - Motor 3 - Sentit horari"); 
        for (int i=0; i<128; i++){ 
          //Serial.print("Left");
          D_izq();
        }
        apagado();
      }
      if (mov == "d") {
        Serial.println(mov+" - Motor 3 - Sentit antihorari");
        for (int i=0; i<128; i++){ 
          //Serial.print("Right");
          D_der();
        }
        apagado();
      }

      movs= movs.substring(1,100000);
    }
  apagado();
  }
}
