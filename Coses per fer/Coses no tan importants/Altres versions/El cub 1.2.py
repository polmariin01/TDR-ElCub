espai="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

llistamoviments=["U","U'","F","F'","L","L'","R","R'","D","D'","B","B'","sortir","SORTIR","inicial","INICIAL"]
llistasortir=["sortir","SORTIR"]
moves=["U","U'","F","F'","L","L'","R","R'","D","D'","B","B'"]

#HAZLO CON UN DICCIONARIO
#dic={G:"w",R:"R",G:"R",Y:"Y",O:"O"}


W = "W";R = "R";G = "G";B = "B";Y = "Y";O = "O"

c11 = "WR";c12 = "RW";c21 = "WG";c22 = "GW";c31 = "WO";c32 = "OW";c41 = "WB";c42 = "BW";c51 = "RG";c52 = "GR";c61 = "GO";c62 = "OG";c71 = "OB";c72 = "BO";c81 = "BR";c82 = "RB";c91 = "YR";c92 = "RY";c101 = "YG";c102 = "GY";c111 = "YO";c112 = "OY";c121 = "YB";c122 = "BY"

a11 = "WRG";a12 = "RGW";a13 = "GWR";a21 = "WBR";a22 = "BRW";a23 = "RWB";a31 = "WGO";a32 = "GOW";a33 = "OWG";a41 = "WOB";a42 = "OBW";a43 = "BWO";a51 = "YGR";a52 = "GRY";a53 = "RYG";a61 = "YRB";a62 = "RBY";a63 = "BYR";a71 = "YOG";a72 = "OGY";a73 = "GYO";a81 = "YBO";a82 = "BOY";a83 = "OYB"

def cub():
    print("\n"+"              ___________\n"+"             |"+a31+"|"+c31+" |"+a41+"| \n"+"             |___|___|___| \n"+"             |"+c21+" |",W,"|"+c41+" | \n"+"             |___|___|___| \n"+"             |"+a11+"|"+c11+" |"+a21+"| \n"+" ___________ |___|___|___| ___________  ___________ \n"+"|"+a32+"|"+c22+" |"+a13+"||"+a12+"|"+c12+" |"+a23+"||"+a22+"|"+c42+" |"+a43+"||"+a42+"|"+c32+" |"+a33+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"|"+c61+" |",G,"|"+c52+" ||"+c51+" |",R,"|"+c82+" ||"+c81+" |",B,"|"+c72+" ||"+c71+" |",O,"|"+c62+" | \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"|"+a73+"|"+c102+" |"+a52+"||"+a53+"|"+c92+" |"+a62+"||"+a63+"|"+c122+" |"+a82+"||"+a83+"|"+c112+" |"+a72+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"             |"+a51+"|"+c91+" |"+a61+"| \n"+"             |___|___|___| \n"+"             |"+c101+" |",Y,"|"+c121+" | \n"+"             |___|___|___| \n"+"             |"+a71+"|"+c111+" |"+a81+"| \n"+"             |___|___|___| \n")

#llista123=["1","2","3","4","5"]

print("Benvingut al meu cub \n   -PMG  \n\n")
cub()

print("Blanc: W");print("Vermell: R");print("Verd: G");print("Blau: B");print("Groc: Y");print("Taronja: O")

print("\n")

input("Prem ENTER per continuar")
print(espai)
opciomenu=0

#Tambien puedes hacerlo asi
#opcio_menu=int(input("entra una opcion"))
#while opcio_menu!=-1 ejecuta opciones
#if(opcio_menu==5) opcio_menu=-1

while True:
    print("MENÚ PRINCIPAL")
    print("**************")
    cub()
    print("1. Moure el cub lliurement")
    print("2. Utilitzar algoritmes")
    print("3. Desmontar aleatoriament")
    print("4. Reiniciar el cub (tornar a l'estat resolt)")
    print("")
    print("5. Tancar el programa")
    print()
    opciomenu=input("Tira una opció. ")
    print(espai)

    try:
        if opciomenu=="1":
            cub()
            mov=0
            while mov not in llistamoviments:
                print("Quin moviment vols fer? [U,U',D,D',R,R',L,L',F,F',B,B'] \n[Escriu SORTIR per tornar al menú d'inici]")
                mov=input()
                if mov not in llistamoviments:
                    print("\nMoviment no vàlid, torna a provar. \n")
                else:
                    if mov in llistasortir:
                        opciomenu=0
                        print(espai)
                    else:
                        if mov=="U":
                            print("U",a11)
                            na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                            print(na11,a11)
                            a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                            print("U",na11,a11)
                        if mov=="U'":
                            na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                            a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                            
                        if mov=="F":
                            nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                            c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                            
                        if mov=="F'":
                            nc51=c12;nc12=c82;nc82=c92;nc92=c51;na12=a23;na23=a62;na53=a23;na62=a53;nc91=c52;nc52=c11;nc11=c81;nc81=c91;na51=a13;na13=a21;na21=a63;na63=a51;na61=a52;na52=a11;na11=a22;na22=a61
                            c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22     
                            
                        if mov=="R":
                            nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                            c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42

                        if mov=="R'":                      
                            nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                            c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                            
                        if mov=="L":
                            nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                            c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                                        
                        if mov=="L'":
                            nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                            c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                           
                        if mov=="D":
                            nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                            c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
           
                        if mov=="D'":
                            nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                            c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                            
                        if mov=="B":
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            
                        if mov=="B'":
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73

                        cub()
                        mov=0

        if opciomenu=="2":
            nalgor=0
            while nalgor != "1" or "2" or "3" or "4":
                print(espai)
                cub()
                print("Selecciona l'algoritme que vols fer:\n")
                print("1. La flor")
                print("2. Canvi de centres")
                print("3. Gir d'arestes")
                print("\n4. Tornar enrere")
                print()
                nalgor=input("Tria. ")
                if nalgor=="1":
                    print(espai)
                    print("LA FLOR")
                    print("(2U,2D,2R,2L,2F,2B)")
                    cub()
                    input("Prem ENTER")            
                    
                    #flor
                    #2U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    #2D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    #2R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    #2L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                    #2F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    #2B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()

                    print("Algoritme realitzat! Prem ENTER")
                    input()
                    nalgor=0
                    
                if nalgor=="2":
                    print(espai)
                    print("CANVI DE CENTRES")
                    cub()
                    input("Prem enter")            
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()

                    print("Algoritme realitzat! Prem ENTER")
                    input()
                    nalgor=0

#U
#na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
#a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
#U'
#na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
#a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                            
#F
#nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
#c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
#F'
#nc51=c12;nc12=c82;nc82=c92;nc92=c51;na12=a23;na23=a62;na53=a23;na62=a53;nc91=c52;nc52=c11;nc11=c81;nc81=c91;na51=a13;na13=a21;na21=a63;na63=a51;na61=a52;na52=a11;na11=a22;na22=a61
#c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22     
                            
#R
#nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
#c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
#R'
#nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
#c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42

#L
#nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
#c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
#L'
#nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
#c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                           
#D
#nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
#c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
#D'
#nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
#c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                            
#B
#nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
#c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
#B'
#nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
#c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73



                if nalgor=="3":
                    print(espai)
                    print("GIR D'ARESTES")
                    print("(R',L,F,R',L,D,R',L,B,R',L,U - D',U,L,D',U,B,D',U,R,D',U,F - B',F,U,B',F,R,B',F,D,B',F,L)")
                    cub()
                    input("Prem enter")            
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                    #F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()

                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    #F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()

                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    #F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    #F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    #F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    #F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()


                    print("Algoritme realitzat! Prem ENTER")
                    input()
                    nalgor=0

                if nalgor=="4":
                    opciomenu=0
                    print(espai)
                    break



        if opciomenu=="3":
            cub()
            #print("Prem ENTER")
            import random
            for a in range(0,30):
                random.shuffle
                llistamoviments=["U","U'","F","F'","L","L'","R","R'","D","D'","B","B'","sortir","SORTIR","inicial","INICIAL"]
                random.shuffle(moves)
                mov2=(moves[1])
                if mov2=="U":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                if mov2=="U'":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                if mov2=="F":
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22                          
                if mov2=="F'":
                    nc51=c12;nc12=c82;nc82=c92;nc92=c51;na12=a23;na23=a62;na53=a23;na62=a53;nc91=c52;nc52=c11;nc11=c81;nc81=c91;na51=a13;na13=a21;na21=a63;na63=a51;na61=a52;na52=a11;na11=a22;na22=a61
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22                                 
                if mov2=="R":
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                if mov2=="R'":                      
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42                            
                if mov2=="L":
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                if mov2=="L'":
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                            
                if mov2=="D":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                if mov2=="D'":
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72                            
                if mov2=="B":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                if mov2=="B'":
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                #cub()
            #print("Cub desmontat, prem ENTER per tornar al menú principal")
            #input()
            opciomenu=0
            print(espai)
            

        if opciomenu=="4":
            c11 = "WR";c12 = "RW";c21 = "WG";c22 = "GW";c31 = "WO";c32 = "OW";c41 = "WB";c42 = "BW";c51 = "RG";c52 = "GR";c61 = "GO";c62 = "OG";c71 = "OB";c72 = "BO";c81 = "BR";c82 = "RB";c91 = "YR";c92 = "RY";c101 = "YG";c102 = "GY";c111 = "YO";c112 = "OY";c121 = "YB";c122 = "BY"
            a11 = "WRG";a12 = "RGW";a13 = "GWR";a21 = "WBR";a22 = "BRW";a23 = "RWB";a31 = "WGO";a32 = "GOW";a33 = "OWG";a41 = "WOB";a42 = "OBW";a43 = "BWO";a51 = "YGR";a52 = "GRY";a53 = "RYG";a61 = "YRB";a62 = "RBY";a63 = "BYR";a71 = "YOG";a72 = "OGY";a73 = "GYO";a81 = "YBO";a82 = "BOY";a83 = "OYB"

            opciomenu=0
            print(espai)

        if opciomenu=="5":
            print("SALIR")
            break
    except:
        #cualquier problema del bucle sera tactado por aqui
        print("HAS D'INTROUDIR UN NUMERO")
                    
                
def cubo():
    print()
    print("              ___________")
    print("             |"+a31+"|"+c31+" |"+a41+"|")
    print("             |___|___|___|")
    print("             |"+c21+" |",W,"|"+c41+" |")
    print("             |___|___|___|")
    print("             |"+a11+"|"+c11+" |"+a21+"|")
    print(" ___________ |___|___|___| ________________________")
    print("|"+a32+"|"+c22+" |"+a13+"||"+a12+"|"+c12+" |"+a23+"||"+a22+"|"+c42+" |"+a43+"||"+a42+"|"+c32+" |"+a33+"|")
    print("|___|___|___||___|___|___||___|___|___||___|___|___|")
    print("|"+c61+" |",G,"|"+c52+" ||"+c51+" |",R,"|"+c82+" ||"+c81+" |",B,"|"+c72+" ||"+c71+" |",O,"|"+c62+" |")
    print("|___|___|___||___|___|___||___|___|___||___|___|___|")
    print("|"+a73+"|"+c102+" |"+a52+"||"+a53+"|"+c92+" |"+a62+"||"+a63+"|"+c122+" |"+a82+"||"+a83+"|"+c112+" |"+a72+"|")
    print("|___|___|___||___|___|___||___|___|___||___|___|___|")
    print("             |"+a51+"|"+c91+" |"+a61+"|")
    print("             |___|___|___|")
    print("             |"+c101+" |",Y,"|"+c121+" |")
    print("             |___|___|___|")
    print("             |"+a71+"|"+c111+" |"+a81+"|")
    print("             |___|___|___|")
    print("-")



#####
#"              ___________")
#"             |a31|c31|a41|")
#"             |___|___|___|")
#"             |c21| W |c41|")
#"             |___|___|___|")
#"             |a11|c11|a21|")
#" ___________ |___|___|___| ________________________")
#"|a32|c22|a13||a12|c12|a23||a22|c42|a43||a42|c32|a33|")
#"|___|___|___||___|___|___||___|___|___||___|___|___|")
#"|c61| G |c52||c51| R |c82||c81| B |c72||c71| O |c62|")
#"|___|___|___||___|___|___||___|___|___||___|___|___|")
#"|a73|c102|a52|a53|c92|a62|a63|c122|a82|a83|c112|a72|")
#"|___|___|___||___|___|___||___|___|___||___|___|___|")
#"             |a51|c91|a61|")
#"             |___|___|___|")
#"            |c101| Y |c121|")
#"             |___|___|___|")
#"             |a71|c111|a81|")
#"             |___|___|___|")
#####
