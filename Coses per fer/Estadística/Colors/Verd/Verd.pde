int Rr1 = 0;
int Rg1 = 140;
int Rb1 = 0;
int Rb1i= Rb1;
int Rr2 = 149; //115
int Rg2 = 255; //80
int Rb2 = 120; //80
int count;
String name;
int canvi = 0;
int wr = 0;
int capt = 1;
int tocapt = 1;

void setup() {
  size(505, 550);
  background(0);
  stroke(255, 100);
  strokeWeight(1);
  stroke(255, 0, 0, 150);
  line(16, 3*(Rg2-Rg1)+60, 3*(Rr2-Rr1)+29, 3*(Rg2-Rg1)+60);
  line(15, 3*(Rg2-Rg1)+57, 15, 3*(Rg2-Rg1)+63);
  line(3*(Rr2-Rr1)+30, 3*(Rg2-Rg1)+57, 3*(Rr2-Rr1)+30, 3*(Rg2-Rg1)+63);
  point(15+((Rr1/255)*(3*(Rr2-Rr1)+15)), 3*(Rg2-Rg1)+58);
  noStroke();
  fill(255, 0, 0);
  rect(15+Rr1*(3*(Rr2-Rr1)+15)/255, 3*(Rg2-Rg1)+58, (Rr2-Rr1+1)*(3*(Rr2-Rr1)+15)/255, 5);
  strokeWeight(1);
  stroke(0, 255, 0, 150);
  line(15, 3*(Rg2-Rg1)+90, 3*(Rr2-Rr1)+30, 3*(Rg2-Rg1)+90);
  line(15, 3*(Rg2-Rg1)+87, 15, 3*(Rg2-Rg1)+93);
  line(3*(Rr2-Rr1)+30, 3*(Rg2-Rg1)+87, 3*(Rr2-Rr1)+30, 3*(Rg2-Rg1)+93);
  noStroke();
  fill(0, 255, 0);
  rect(15+(Rg1*(15+3*(Rr2-Rr1)))/255, 3*(Rg2-Rg1)+88, (Rg2-Rg1+1)*(3*(Rr2-Rr1)+15)/255, 5);
  stroke(255);
  line(15, 3*(Rg2-Rg1)+25, 3*(Rr2-Rr1)+17, 3*(Rg2-Rg1)+25);
  line(15, 3*(Rg2-Rg1)+22, 15, 3*(Rg2-Rg1)+28);
  line(3*(Rr2-Rr1)+17, 3*(Rg2-Rg1)+22, 3*(Rr2-Rr1)+17, 3*(Rg2-Rg1)+28);
  line(3*(Rr2-Rr1)+25, 15, 3*(Rr2-Rr1)+25, 3*(Rg2-Rg1)+17);
  line(3*(Rr2-Rr1)+22, 15, 3*(Rr2-Rr1)+28, 15);
  line(3*(Rr2-Rr1)+22, 3*(Rg2-Rg1)+17, 3*(Rr2-Rr1)+28, 3*(Rg2-Rg1)+17);
  fill(255);
  text(round(Rr1), 5, 3*(Rg2-Rg1)+41);
  text(round(Rr2), 3*(Rr2-Rr1)+8, 3*(Rg2-Rg1)+41);
  text("RED", (3*(Rr2-Rr1)+10)/2, 3*(Rg2-Rg1)+41);
  text(round(Rg1), 3*(Rr2-Rr1)+32, 20);
  text(round(Rg2), 3*(Rr2-Rr1)+32, 3*(Rg2-Rg1)+22);
  text("G\nR\nE\nE\nN", 3*(Rr2-Rr1)+32, Rg2-Rg1+40);
}

void draw() {
  for (int i = 5; i<(Rr2-Rr1)+6; i++) {
    for (int j = 5; j<(Rg2-Rg1)+6; j++) { 
      noStroke();
      fill(Rr1+i-5, Rg1+j-5, Rb1);
      rect(3*i, 3*j, 3, 3);
      if ((Rb1-1)<255 && wr==1) {
        print((i-5)+" "+(j-5)+" "+round(Rr1+i-5)+" "+round(Rg1+j-5)+" "+round(Rb1));
        print("\n");
      }
    }
  }

  fill(0);
  noStroke();
  rect(0, 3*(Rg2-Rg1)+110, 800, 800);

  noStroke();
  fill(0, 0, 255);
  ellipse(15+Rb1*(3*(Rr2-Rr1)+15)/255, 3*(Rg2-Rg1)+120, 5, 5);

  fill(255);
  text("R: "+round(Rr1)+" - "+round(Rr2), 15, 3*(Rg2-Rg1)+150);
  text("G: "+round(Rg1)+" - "+round(Rg2), 15, 3*(Rg2-Rg1)+170);
  text("B: "+round(Rb1)+" ("+round(Rb1i)+" - "+round(Rb2)+")", 15, 3*(Rg2-Rg1)+190);

  strokeWeight(1);
  stroke(0, 0, 255, 150);
  line(15, 3*(Rg2-Rg1)+120, 3*(Rr2-Rr1)+30, 3*(Rg2-Rg1)+120);
  line(15, 3*(Rg2-Rg1)+117, 15, 3*(Rg2-Rg1)+123);
  line(3*(Rr2-Rr1)+30, 3*(Rg2-Rg1)+117, 3*(Rr2-Rr1)+30, 3*(Rg2-Rg1)+123);

  if (capt==1 && tocapt==1) {
    count=count+1;
    name="Frames/Verds_possibles_"+(count)+".jpg";
    saveFrame(name);
  }
  if (Rb1==Rb2) {
    canvi=1;
  }
  if (Rb1<Rb2 && canvi==0) {
    Rb1++;
  }
  if (Rb1>Rb1i && canvi==1) {
    Rb1--;
  }
  if (Rb1==Rb1i) {
    canvi=0;
    tocapt=0;
  }
}
