PImage cara;
String col;
int mult;
PrintWriter colors;

int EW=0;
int ER=0;
int EB=0;
int EO=0;
int EG=0;
int EY=0;

void setup() {
  size(220, 315);
  line(0,155,width,155);
  colors = createWriter("colors.txt");
}

void draw() {
  loadPixels();
  for (int i = 1; i <= 6; i++) {
    cara = loadImage("cub ("+i+").jpg");
    if (i!=1) {
      colors.println("");
    }
    for (int j = 0; j < 3; j++) {
      for (int k = 0; k<3; k++) {
        
        float R1 = red(cara.pixels[((cara.width/6)+cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float R2 = red(cara.pixels[((cara.width/6)-cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float R0 = red(cara.pixels[((cara.width/6)+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float R = (R0+R1+R2)/3;
        
        float G1 = green(cara.pixels[((cara.width/6)+cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float G2 = green(cara.pixels[((cara.width/6)-cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float G0 = green(cara.pixels[((cara.width/6)+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float G = (G0+G1+G2)/3;

        float B1 = blue(cara.pixels[((cara.width/6)+cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float B2 = blue(cara.pixels[((cara.width/6)-cara.width/24+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
        float B0 = blue(cara.pixels[((cara.width/6)+j*cara.width/3)+cara.width*(cara.height/6+k*cara.height/3)]);
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
        col = "X";
        if (R>=120 && G>=150 && B>=150) {
          col="W";
          EW++;
          fill(255);
        }
        if (R>=160 && G>=60 && G<=180 && B<=80) {
          col="O";
          EO++;
          fill(255,130,0);
        }
        if (R<=119 && G>=100 && B>=160) {
          col="B";
          EB++;
          fill(0,0,255);
        }
        if (R>=150 && G>=170 && B<=60) {
          col="Y";
          EY++;
          fill(255,255,0);
        }
        if (R<=149 && G>=140 && B<=120) {
          col="G";
          EG++;
          fill(0,255,0);
        }
        if (R>=150 && G<=60 && B<=110) {
          col="R";
          ER++;
          fill(255,0,0);
        }
        
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
        if (j!=1 || k!=1){
          colors.print(col);
        }
      }     
    }
  }
  colors.close();

  if (EW>=8 && EY>=8 && EG>=8 && ER>=8 && EB>=8 && EO>=8) {
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
