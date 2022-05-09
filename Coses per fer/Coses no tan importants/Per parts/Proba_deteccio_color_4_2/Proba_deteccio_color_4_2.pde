PImage cara;
String col;
int mult;

int EW=0;
int ER=0;
int EB=0;
int EO=0;
int EG=0;
int EY=0;

int WRM = 255;
int WRL = 140;
int WGM = 255;
int WGL = 175;
int WBM = 255;
int WBL = 175;

int GRM = 149;
int GRL = 0;
int GGM = 255;
int GGL = 140;
int GBM = 120;
int GBL = 0;

int RRM = 255;
int RRL = 180;
int RGM = 60;
int RGL = 0;
int RBM = 110;
int RBL = 0;

int BRM = 120;
int BRL = 0;
int BGM = 255;
int BGL = 100;
int BBM = 255;
int BBL = 170;

int ORM = 255;
int ORL = 180;
int OGM = 175;
int OGL = 60;
int OBM = 60;
int OBL = 0;

int YRM = 255;
int YRL = 150;
int YGM = 255;
int YGL = 200;
int YBM = 30;
int YBL = 0;

void setup() {
  size(220, 315);
  line(0,155,width,155);
}

void draw() {
  loadPixels();
  for (int i = 1; i <= 6; i++) {
    print("\n");
    print(i+"____________\n");

    for (int j = 0; j < 3; j++) {

      for (int k = 0; k<3; k++) {
        col = "X";
        cara = loadImage("cub ("+i+").jpg");
        
        float R1 = red(cara.pixels[((cara.width/6)+cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float R2 = red(cara.pixels[((cara.width/6)-cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float R0 = red(cara.pixels[((cara.width/6)+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float R = (R0+R1+R2)/3;
        
        float G0 = green(cara.pixels[((cara.width/6)+cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float G1 = green(cara.pixels[((cara.width/6)-cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float G2 = green(cara.pixels[((cara.width/6)+j*cara.width/3)+cara.width*((cara.height/6+cara.height/15)+k*cara.height/3)]);
        float G = (G0+G1+G2)/3;

        float B0 = blue(cara.pixels[((cara.width/6)+cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float B1 = blue(cara.pixels[((cara.width/6)-cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float B2 = blue(cara.pixels[((cara.width/6)+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float B = (B1+B2+B0)/3;
        
        if (j==1 && k==1) {
          mult = 1;
        }
        else {
          mult = 0;
        }

        
        fill(R,G,B);
        if (i < 5) {
          ellipse(10+55*(i-1)+15*j,60+ 15*k,10+2*mult,10+2*mult);
        }
        if (i == 5) {
          ellipse(10+15*j,10+15*k,10+2*mult,10+2*mult);
        }
        if (i == 6) {
          ellipse(10+15*j,110+15*k,10+2*mult,10+2*mult);
        }

        fill(0);
        
        if (R>=WRL && R<=WRM && G>=WGL && G<=WGM && B>=WBL && B<=WBM) {
          col="W";
          EW++;
          fill(255);
        }
        if (R>=ORL && R<=ORM && G>=OGL && G<=OGM && B>=OBL && B<=OBM) {
          col="O";
          EO++;
          fill(255,130,0);
        }
        if (R>=BRL && R<=BRM && G>=BGL && G<=BGM && B>=BBL && B<=BBM) {
          col="B";
          EB++;
          fill(0,0,255);
        }
        if (R>=YRL && R<=YRM && G>=YGL && G<=YGM && B>=YBL && B<=YBM) {
          col="Y";
          EY++;
          fill(255,255,0);
        }
        if (R>=GRL && R<=GRM && G>=GGL && G<=GGM && B>=GBL && B<=GBM) {
          col="G";
          EG++;
          fill(0,255,0);
        }
        if (R>=RRL && R<=RRM && G>=RGL && G<=RGM && B>=RBL && B<=RBM) {
          col="R";
          ER++;
          fill(255,0,0);
        }

        print((3*(j)+(k+1))+": "+round(R)+" "+round(G)+" "+round(B)+"  - "+col+"\n");
        
        if (k==1 && j==1){
          if (i==1) {
            fill(255,0,0);
          }
          if (i==2) {
            fill(0,0,255);            
          }
          if (i==3) {
            fill(255,130,0);            
          }
          if (i==4) {
            fill(0,255,0);
          }
          if (i==5) {
            fill(255);
          }
          if (i==6) {
            fill(255,255,0);            
          }

        }

        if (i < 5) {
          ellipse(10+55*(i-1)+15*j,160+60+ 15*k,10+2*mult,10+2*mult);
        }
        if (i == 5) {
          ellipse(10+15*j,160+10+15*k,10+2*mult,10+2*mult);
        }
        if (i == 6) {
          ellipse(10+15*j,160+110+15*k,10+2*mult,10+2*mult);
        }
      }     
    }
  }
  print(EW+" "+EY+" "+EG+" "+ER+" "+EB+" "+EO);

  if (EW>=8 && EY==9 && EG==9 && ER==9 && EB==9 && EO==9) {
    stroke(0,255,0);
    strokeWeight(5);
    noFill();
    ellipse(width-30,height-30,30,30);    
  }
  else {    
    stroke(255,0,0);
    strokeWeight(5);
    line(width-45,height-45,width-10,height-10);
    line(width-10,height-45,width-45,height-10);    
  }
  saveFrame("Detecció color.jpg");
  noLoop();
}
