import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class Deteccio_color extends PApplet {

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

public void setup() {
  
  line(0,155,width,155);
  colors = createWriter("colors.txt");
}

public void draw() {
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
        if (R>=140 &&G>=175 &&B>=175) {
          col="W";
          EW++;
          fill(255);
        }
        if (R>=180 && G>=60 && G<=175 && B<=60) {
          col="O";
          EO++;
          fill(255,130,0);
        }
        if (R<=120 && G>=100 && B>=170) {
          col="B";
          EB++;
          fill(0,0,255);
        }
        if (R>=150 && G>=200 && B<=30) {
          col="Y";
          EY++;
          fill(255,255,0);
        }
        if (R<=149 && G>=140 && B<=120) {
          col="G";
          EG++;
          fill(0,255,0);
        }
        if (R>=180 && G<=60 && B<=110) {
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
  public void settings() {  size(220, 315); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Deteccio_color" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
