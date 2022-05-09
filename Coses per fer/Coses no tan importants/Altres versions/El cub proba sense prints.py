espai="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
llistamoviments=["U","U'","F","F'","L","L'","R","R'","D","D'","B","B'","sortir","SORTIR","inicial","INICIAL"]
llistasortir=["sortir","SORTIR"]
moves=["U","U'","F","F'","L","L'","R","R'","D","D'","B","B'"]
W = "W";R = "R";G = "G";B = "B";Y = "Y";O = "O"
c11 = "WR";c12 = "RW";c21 = "WG";c22 = "GW";c31 = "WO";c32 = "OW";c41 = "WB";c42 = "BW";c51 = "RG";c52 = "GR";c61 = "GO";c62 = "OG";c71 = "OB";c72 = "BO";c81 = "BR";c82 = "RB";c91 = "YR";c92 = "RY";c101 = "YG";c102 = "GY";c111 = "YO";c112 = "OY";c121 = "YB";c122 = "BY"
a11 = "WRG";a12 = "RGW";a13 = "GWR";a21 = "WBR";a22 = "BRW";a23 = "RWB";a31 = "WGO";a32 = "GOW";a33 = "OWG";a41 = "WOB";a42 = "OBW";a43 = "BWO";a51 = "YGR";a52 = "GRY";a53 = "RYG";a61 = "YRB";a62 = "RBY";a63 = "BYR";a71 = "YOG";a72 = "OGY";a73 = "GYO";a81 = "YBO";a82 = "BOY";a83 = "OYB"
def cub():
    print("\n"+"              ___________\n"+"             |"+a31+"|"+c31+" |"+a41+"| \n"+"             |___|___|___| \n"+"             |"+c21+" |",W,"|"+c41+" | \n"+"             |___|___|___| \n"+"             |"+a11+"|"+c11+" |"+a21+"| \n"+" ___________ |___|___|___| ___________  ___________ \n"+"|"+a32+"|"+c22+" |"+a13+"||"+a12+"|"+c12+" |"+a23+"||"+a22+"|"+c42+" |"+a43+"||"+a42+"|"+c32+" |"+a33+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"|"+c61+" |",G,"|"+c52+" ||"+c51+" |",R,"|"+c82+" ||"+c81+" |",B,"|"+c72+" ||"+c71+" |",O,"|"+c62+" | \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"|"+a73+"|"+c102+" |"+a52+"||"+a53+"|"+c92+" |"+a62+"||"+a63+"|"+c122+" |"+a82+"||"+a83+"|"+c112+" |"+a72+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"             |"+a51+"|"+c91+" |"+a61+"| \n"+"             |___|___|___| \n"+"             |"+c101+" |",Y,"|"+c121+" | \n"+"             |___|___|___| \n"+"             |"+a71+"|"+c111+" |"+a81+"| \n"+"             |___|___|___| \n")
llista123=["1","2","3","4","5","6"]
print("Benvingut al meu cub \n   -PMG  \n\n")
cub()
print("Blanc: W");print("Vermell: R");print("Verd: G");print("Blau: B");print("Groc: Y");print("Taronja: O")
print("\n")
input("Prem ENTER per continuar")
print(espai)
opciomenu=0
while opciomenu not in llista123:
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
    if opciomenu not in llista123:
        print("\nOpció incorrecta.\n")
    else:
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
                            na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                            a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                        if mov=="U'":
                            na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                            a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                        if mov=="F":
                            nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                            c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22                   
                        if mov=="F'":
                            nc51=c12;nc12=c82;nc82=c92;nc92=c51;na12=a23;na23=a62;na53=a12;na62=a53;nc91=c52;nc52=c11;nc11=c81;nc81=c91;na51=a13;na13=a21;na21=a63;na63=a51;na61=a52;na52=a11;na11=a22;na22=a61
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
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
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
                    print("(D,U',F,B',R,L',D,U')")
                    cub()
                    input("Prem enter")            
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    print("Algoritme realitzat! Prem ENTER")
                    input()
                    nalgor=0
                if nalgor=="3":
                    print(espai)
                    print("GIR D'ARESTES")
                    print("(R',L,F,R',L,D,R',L,B,R',L,U - D',U,L,D',U,B,D',U,R,D',U,F - B',F,U,B',F,R,B',F,D,B',F,L)")
                    cub()
                    input("Prem enter")            
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
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
            import random
            for a in range(0,20):
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
                    nc51=c12;nc12=c82;nc82=c92;nc92=c51;na12=a23;na23=a62;na53=a12;na62=a53;nc91=c52;nc52=c11;nc11=c81;nc81=c91;na51=a13;na13=a21;na21=a63;na63=a51;na61=a52;na52=a11;na11=a22;na22=a61
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
            opciomenu=0
            print(espai)
        if opciomenu=="4":
            c11 = "WR";c12 = "RW";c21 = "WG";c22 = "GW";c31 = "WO";c32 = "OW";c41 = "WB";c42 = "BW";c51 = "RG";c52 = "GR";c61 = "GO";c62 = "OG";c71 = "OB";c72 = "BO";c81 = "BR";c82 = "RB";c91 = "YR";c92 = "RY";c101 = "YG";c102 = "GY";c111 = "YO";c112 = "OY";c121 = "YB";c122 = "BY"
            a11 = "WRG";a12 = "RGW";a13 = "GWR";a21 = "WBR";a22 = "BRW";a23 = "RWB";a31 = "WGO";a32 = "GOW";a33 = "OWG";a41 = "WOB";a42 = "OBW";a43 = "BWO";a51 = "YGR";a52 = "GRY";a53 = "RYG";a61 = "YRB";a62 = "RBY";a63 = "BYR";a71 = "YOG";a72 = "OGY";a73 = "GYO";a81 = "YBO";a82 = "BOY";a83 = "OYB"
            opciomenu=0
            print(espai)
        if opciomenu=="5":
            break
        if opciomenu=="6":
            while c82 != "RB":
                if c92== "RB":
                    nc51=c12;nc12=c82;nc82=c92;nc92=c51;na12=a23;na23=a62;na53=a12;na62=a53;nc91=c52;nc52=c11;nc11=c81;nc81=c91;na51=a13;na13=a21;na21=a63;na63=a51;na61=a52;na52=a11;na11=a22;na22=a61
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22     
                    cub()
                if c51=="RB":
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                if c12=="RB":
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                if c81=="RB":
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                if c11=="RB":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                if c52=="RB":
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                if c91=="RB":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c22=="RB":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                if c61=="RB":
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                if c102=="RB":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c101=="RB":
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                if c21=="RB":
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                if c111=="RB":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c121=="RB":
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                if c122=="RB":
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                if c42=="RB":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                if c41=="RB":
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                if c31=="RB":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                if c72=="RB":
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                if c71=="RB":
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                if c32=="RB":
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                if c62=="RB":
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                if c112=="RB":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
            while c12!="RW":
                if c51=="RW":
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                if c92=="RW":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72                               
                    cub()
                if c11=="RW":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12                    
                    cub()
                if c52=="RW":
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                    
                    cub()
                if c61=="RW":
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                                            
                    cub()
                if c102=="RW":
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                                            
                    cub()
                if c22=="RW":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12                    
                    cub()
                if c21=="RW":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                if c42=="RW":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                if c41=="RW":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                if c91=="RW":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c101=="RW":
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                if c121=="RW":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c111=="RW":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                if c122=="RW":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c112=="RW":
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                if c71=="RW":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                if c62=="RW":
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                if c32=="RW":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                if c31=="RW":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                if c72=="RW":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                            
                    cub()
            while c51 != "RG":
                if c21=="RG":
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                if c31=="RG":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                if c61=="RG":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                if c22=="RG":
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                if c52=="RG":
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                if c102=="RG":
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                if c101=="RG":
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                if c111=="RG":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c121=="RG":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c91=="RG":

                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                if c92=="RG":
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72                   
                    cub()
                if c72=="RG":
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                if c112=="RG":
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72                   
                    cub()
                if c71=="RG":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                if c32=="RG":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                if c122=="RG":
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72                   
                    cub()
                if c62=="RG":
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                    
                    cub()
                if c41=="RG" or c42 == "RG":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
            while c92!="RY":
                 
                if c102=="RY":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c101=="RY":
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                if c111=="RY":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                if c121=="RY":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c122=="RY":
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                if c72=="RY":
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                if c42=="RY":
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                if c71=="RY":
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                if c62=="RY":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                if c112=="RY":
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                if c91=="RY":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                if c32=="RY":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                if c22=="RY":
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                if c61=="RY":
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()
                if c31=="RY":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                   
                if c41=="RY":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                if c21=="RY":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
            n=1
            for a in range(0,4):               
                esquina=[0,"RGW","RYG","RBY","RWB"]
                while a12!=esquina[n]:
                    if a21 == esquina[n] or a22 == esquina[n] or a23 == esquina[n]:
                        nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                        c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                        cub()
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()
                        nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                        c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                        cub()
                    if a61 == esquina[n] or a62 == esquina[n] or a63 == esquina[n]:
                        nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                        c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                        cub()
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()
                        nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                        c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                        cub()
                    if a51 == esquina[n] or a52 == esquina[n] or a53 == esquina[n]:
                        nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                        cub()
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()
                        nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                        cub()
                    if a71 == esquina[n] or a72 == esquina[n]:
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                       
                    if a11  == esquina[n] or a13 == esquina[n]:
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                        cub()
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                        cub()
                    if a42 == esquina[n] or a83 == esquina[n] or a43 == esquina[n] or a73 == esquina[n] or a41 == esquina[n] or a82 == esquina[n] or a73 == esquina[n] or a81 == esquina[n]:
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()              
                    if a33 == esquina[n]:
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                        cub()                              
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                        
                        cub()                    
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                        cub()                    
                    if a31 == esquina[n]:
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                        cub()
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                        cub()
                    if a32 == esquina[n]:
                        nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                        cub()
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                        cub()
                        nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                        cub()                    
                nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                cub()
                n=n+1
            while c21!="WG":
                if c22=="WG":
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()                    
                if c31=="WG":
                    #b'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                if c72=="WG":
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()                    
                if c61=="WG":
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                if c111=="WG":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                if c41 == "WG" or c42 =="WG":
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                                        
                if c122 =="WG" or c121 == "WG":
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                if c101 == "WG" or c102 == "WG":
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()                    
                    
                if c71 == "WG" or c32 == "WG" or c62 == "WG" or c112 == "WG":
                    cub()
                    while c22 != "GW":
                        if c72 =="GW":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()
                        if c31 =="GW":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                        if c111 == "GW":
                            #U
                            na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                            a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                            cub()                    
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
                            #U'
                            na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                            a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                            cub()                    
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
                            #L'
                            nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                            c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                            cub()                    
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                            #L
                            nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                            c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                            cub()                    
                        if c61 == "GW":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                    
            #input("aristas nivel 2. SEGUNDA")
            while c41!="WB":
                if c31=="WB":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                if c72=="WB":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                if c61=="WB":
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                if c111=="WB":
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                if c42 =="WB":
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                                        
                if c122 == "WB" or c121 == "WB":
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                if c101 =="WB" or c102 == "WB":
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()        
                if c71 == "WB" or c32 == "WB" or c62 == "WB" or c112 == "WB":
                    while c42 != "BW":
                        if c111 =="BW":
                            #U'
                            na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                            a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                            cub()                    
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                            #U
                            na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                            a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                            cub()                    
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                            #R
                            nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                            c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                            cub()                    
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
                            #R'
                            nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                            c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                            cub()                    
                        if c61 =="BW":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                        if c31 == "BW":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
                        if c72 == "BW":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
            while c101 != "YG":
                if c102 == "YG":
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()                    
                if c121 == "YG" or c122 == "YG":
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                if c111 == "YG":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                if c72 == "YG":
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()                    
                if c61 == "YG":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                if c31 == "YG":
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                if c71 == "YG" or c112 == "YG" or c62 == "YG" or c32 == "YG":
                    cub()
                    while c102 != "GY":
                        if c31 == "GY":
                            #D'
                            nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                            c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                            cub()                    
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                            #D
                            nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                            c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                            cub()                    
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                            #L
                            nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                            c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                            cub()                    
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
                            #L'
                            nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                            c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                            cub()                    
                        if c72 == "GY":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                        if c61 == "GY":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
                        if c111 == "GY":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
            while c121 != "YB":
                if c122 == "YB":
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                if c111 == "YB" or c72 =="YB" or c31 =="YB":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                if c61 == "YB":
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()                    
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()                    
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()                    
                if c71 == "YB" or c112 == "YB" or c62 == "YB" or c32 == "YB":
                    cub()
                    while c122 != "BY":
                        if c31 == "BY":
                            #D
                            nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                            c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                            cub()                    
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
                            #D'
                            nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                            c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                            cub()                    
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
                            #R'
                            nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                            c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                            cub()                    
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                            #R
                            nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                            c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                            cub()                    
                        if c72 == "BY":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()                    
                        if c61 == "BY":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
                        if c111 == "BY":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()                    
            while a42[0] != "O" or a33[0] != "O" or a72[0] != "O" or a83[0] != "O" or c32[0] != "O" or c62[0] != "O" or c112[0] != "O" or c71[0] != "O":
                while c32[0] != "O" or c62[0] != "O" or c112[0] != "O" or c71[0] != "O":
                    if c32[0] != "O" and c62[0] != "O" and c112[0] != "O" and c71[0] != "O":
                        #L
                        nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                        cub()                    
                        #U
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                        cub()                    
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()                    
                        #U'
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                        cub()                    
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                        cub()                    
                        #L' 
                        nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                        cub()                                            
                    if c32[0] == "O" and c62[0] == "O":
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()                    
                    if c32[0] == "O" and c71[0] == "O":
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                        cub()                        
                    if c112[0] == "O" and c62[0] == "O":
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()                    
                    if c71[0] == "O" and c112[0] == "O":
                        #L
                        nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                        cub()                    
                        #U
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                        cub()                    
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()                    
                        #U'
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                        cub()                    
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                        cub()                    
                        #L' 
                        nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                        cub()                    
                    if c71[0] == "O" and c62[0] == "O":
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()                    
                    if c32[0] == "O" and c112[0] == "O":
                        #L
                        nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                        cub()                    
                        #U
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                        cub()                    
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()                    
                        #U'
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                        cub()                    
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                        cub()                    
                        #L' 
                        nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                        cub()                    
                if c32[0] == "O" and c62[0] == "O" and c112[0] == "O" and c71[0] == "O":
                    if a42[0] == "O" and a33[0] == "O" and a72[0] == "O" and a83[0] == "O":
                        daflf=4
                    else:
                        k=1
                        for a in range (0,4):
                            while a83[0] != "O":
                                for b in range (0,2):
                                    #D'
                                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                                    cub()
                                    #F'
                                    nc51=c12;nc12=c82;nc82=c92;nc92=c51;na12=a23;na23=a62;na53=a12;na62=a53;nc91=c52;nc52=c11;nc11=c81;nc81=c91;na51=a13;na13=a21;na21=a63;na63=a51;na61=a52;na52=a11;na11=a22;na22=a61
                                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22     
                                    cub()
                                    #D
                                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                                    cub()
                                    #F
                                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                                    cub()                            
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()
                            k=k+1
            cub()
            while a43[0] != a82[0] or a81[0] != a71[0] or a73[0] != a32[0] or a31[0] != a41[0]:
                for a in range (0,4):
                    if a32[0] != a73[0]:
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()                       
                #U
                na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                cub()                    
                #R'
                nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                cub()                    
                #U
                na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                cub()                    
                #2L
                nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                cub()                    
                nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                cub()                    
                na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                cub()                    
                nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                cub()                    
                na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                cub()                    
                nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                cub()                    
                nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                cub()                    
                na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                cub()                    
                na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                cub()                    
            while c72[0] != a43[0] or c111[0] != a81[0] or c31[0] != a41[0] or c61[0] != a32[0]:
                if a43[0] != c72[0] and a81[0] != c111[0] and a41[0] != c31[0] and a32[0] == c61[0]:
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                if a81[0] != c111[0] and a73[0] != c61[0] and a31[0] != c31[0]  and c72[0] == a43[0]:
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()                    
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                if a43[0] != c72[0] and a81[0] != c111[0] and a73[0] != c61[0] and a31[0] == c31[0]:
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                if a31[0] != c31[0] and a73[0] != c61[0] and a43[0] != c72[0] and a71[0] == c111[0]:
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                if a81[0] != c111[0] and a73[0] != c61[0] and a31[0] != c31[0]  and c72[0] != a43[0]:
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()                    
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()                    
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
            while a43[0] != "B" or a43[0] == "Y" or a43[0] == "W" or a43[0] == "G":
                nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                         
                cub()                    
            if c11 == "WR" and c12 == "RW" and c21 == "WG" and c22 == "GW" and c31 == "WO" and c32 == "OW" and c41 == "WB" and c42 == "BW" and c51 == "RG" and c52 == "GR" and c61 == "GO" and c62 == "OG" and c71 == "OB" and c72 == "BO" and c81 == "BR" and c82 == "RB" and c91 == "YR" and c92 == "RY" and c101 == "YG" and c102 == "GY" and c111 == "YO" and c112 == "OY" and c121 == "YB" and c122 == "BY" and a11 == "WRG" and a12 == "RGW" and a13 == "GWR" and a21 == "WBR" and a22 == "BRW" and a23 == "RWB" and a31 == "WGO" and a32 == "GOW" and a33 == "OWG" and a41 == "WOB" and a42 == "OBW" and a43 == "BWO" and a51 == "YGR" and a52 == "GRY" and a53 == "RYG" and a61 == "YRB" and a62 == "RBY" and a63 == "BYR" and a71 == "YOG" and a72 == "OGY" and a73 == "GYO" and a81 == "YBO" and a82 == "BOY" and a83 == "OYB":
                print("Fet!")             
            input()
            
            print(espai)
            opciomenu=0




 
