int ret = 250;
char ordre;
int numero_pasos;
String movs;
String mov;

void setup() {
  Serial.begin(9600);
  Serial.println("Serial Available - Nothing to do :(");

  pinMode(13, OUTPUT); //U STEP
  pinMode(12, OUTPUT); //U DIR
  pinMode(11, OUTPUT); //R STEP
  pinMode(10, OUTPUT); //R DIR
  pinMode(9, OUTPUT);  //F STEP
  pinMode(8, OUTPUT);  //F DIR
  pinMode(7, OUTPUT);  //D STEP
  pinMode(6, OUTPUT);  //D DIR
  pinMode(5, OUTPUT);  //L STEP
  pinMode(4, OUTPUT);  //L DIR
  pinMode(3, OUTPUT);  //B STEP
  pinMode(2, OUTPUT);  //B DIR

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
void apagado() {
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
void U_mov() {
  digitalWrite(13, HIGH);
  delayMicroseconds(ret);
  digitalWrite(13, LOW);
  delayMicroseconds(ret);
}
void R_mov() {
  digitalWrite(11, HIGH);
  delayMicroseconds(ret);
  digitalWrite(11, LOW);
  delayMicroseconds(ret);
}
void F_mov() {
  digitalWrite(9, HIGH);
  delayMicroseconds(ret);
  digitalWrite(9, LOW);
  delayMicroseconds(ret);
}
void D_mov() {
  digitalWrite(7, HIGH);
  delayMicroseconds(ret);
  digitalWrite(7, LOW);
  delayMicroseconds(ret);
}
void L_mov() {
  digitalWrite(5, HIGH);
  delayMicroseconds(ret);
  digitalWrite(5, LOW);
  delayMicroseconds(ret);
}
void B_mov() {
  digitalWrite(3, HIGH);
  delayMicroseconds(ret);
  digitalWrite(3, LOW);
  delayMicroseconds(ret);
}

void loop() {
  while (Serial.available()) {
    ordre = Serial.read();
    Serial.println(ordre);
    movs += ordre;
    while (movs.length() > 0) {
      delay(200);
      ordre = Serial.read();
      movs += ordre;
      mov = movs.substring(0, 1);

      if (mov == "U") {
        Serial.println(mov + " - Motor 1 - Sentit horari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(12, LOW);
          U_mov();
        }
      }
      if (mov == "u") {
        Serial.println(mov + " - Motor 1 - Sentit antihorari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(12, HIGH);
          U_mov();
        }
      }
      if (mov == "R") {
        Serial.println(mov + " - Motor 2 - Sentit horari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(10, LOW);
          R_mov();
        }
      }
      if (mov == "r") {
        Serial.println(mov + " - Motor 2 - Sentit antihorari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(10, HIGH);
          R_mov();
        }
      }
      if (mov == "F") {
        Serial.println(mov + " - Motor 2 - Sentit horari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(8, LOW);
          F_mov();
        }
      }
      if (mov == "f") {
        Serial.println(mov + " - Motor 2 - Sentit antihorari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(8, HIGH);
          F_mov();
        }
      }
      if (mov == "D") {
        Serial.println(mov + " - Motor 3 - Sentit horari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(6, LOW);
          D_mov();
        }
      }
      if (mov == "d") {
        Serial.println(mov + " - Motor 3 - Sentit antihorari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(6, HIGH);
          D_mov();
        }
      }
      if (mov == "L") {
        Serial.println(mov + " - Motor 2 - Sentit horari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(4, LOW);
          L_mov();
        }
      }
      if (mov == "l") {
        Serial.println(mov + " - Motor 2 - Sentit antihorari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(4, HIGH);
          L_mov();
        }
      }
      if (mov == "B") {
        Serial.println(mov + " - Motor 3 - Sentit horari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(2, LOW);
          B_mov();
        }
      }
      if (mov == "b") {
        Serial.println(mov + " - Motor 3 - Sentit antihorari");
        for (int i = 0; i < 400; i++) {
          digitalWrite(2, HIGH);
          B_mov();
        }
      }
      apagado();
      movs = movs.substring(1, 10000000000);
    }
  }
}
