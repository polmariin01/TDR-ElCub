espai="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

llistamoviments=["U","U'","F","F'","L","L'","R","R'","D","D'","B","B'","sortir","SORTIR","inicial","INICIAL"]
llistasortir=["sortir","SORTIR"]
moves=["U","U'","F","F'","L","L'","R","R'","D","D'","B","B'"]
colors=["W","B","G","R","Y","O"]
cadenamovs=str()

W = "W";R = "R";G = "G";B = "B";Y = "Y";O = "O"

c11 = "WR";c12 = "RW";c21 = "WG";c22 = "GW";c31 = "WO";c32 = "OW";c41 = "WB";c42 = "BW";c51 = "RG";c52 = "GR";c61 = "GO";c62 = "OG";c71 = "OB";c72 = "BO";c81 = "BR";c82 = "RB";c91 = "YR";c92 = "RY";c101 = "YG";c102 = "GY";c111 = "YO";c112 = "OY";c121 = "YB";c122 = "BY"

a11 = "WRG";a12 = "RGW";a13 = "GWR";a21 = "WBR";a22 = "BRW";a23 = "RWB";a31 = "WGO";a32 = "GOW";a33 = "OWG";a41 = "WOB";a42 = "OBW";a43 = "BWO";a51 = "YGR";a52 = "GRY";a53 = "RYG";a61 = "YRB";a62 = "RBY";a63 = "BYR";a71 = "YOG";a72 = "OGY";a73 = "GYO";a81 = "YBO";a82 = "BOY";a83 = "OYB"

sesstaresolent=0
movperres=0

def cub():
    if conf1==1:
        print("\n"+"              ___________\n"+"             |"+a31+"|"+c31+" |"+a41+"| \n"+"             |___|___|___| \n"+"             |"+c21+" |",W,"|"+c41+" | \n"+"             |___|___|___| \n"+"             |"+a11+"|"+c11+" |"+a21+"| \n"+" ___________ |___|___|___| ___________  ___________ \n"+"|"+a32+"|"+c22+" |"+a13+"||"+a12+"|"+c12+" |"+a23+"||"+a22+"|"+c42+" |"+a43+"||"+a42+"|"+c32+" |"+a33+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"|"+c61+" |",G,"|"+c52+" ||"+c51+" |",R,"|"+c82+" ||"+c81+" |",B,"|"+c72+" ||"+c71+" |",O,"|"+c62+" | \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"|"+a73+"|"+c102+" |"+a52+"||"+a53+"|"+c92+" |"+a62+"||"+a63+"|"+c122+" |"+a82+"||"+a83+"|"+c112+" |"+a72+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"             |"+a51+"|"+c91+" |"+a61+"| \n"+"             |___|___|___| \n"+"             |"+c101+" |",Y,"|"+c121+" | \n"+"             |___|___|___| \n"+"             |"+a71+"|"+c111+" |"+a81+"| \n"+"             |___|___|___| \n")

def cub2():
    print("\n"+"              ___________\n"+"             |"+a31+"|"+c31+" |"+a41+"| \n"+"             |___|___|___| \n"+"             |"+c21+" |",W,"|"+c41+" | \n"+"             |___|___|___| \n"+"             |"+a11+"|"+c11+" |"+a21+"| \n"+" ___________ |___|___|___| ___________  ___________ \n"+"|"+a32+"|"+c22+" |"+a13+"||"+a12+"|"+c12+" |"+a23+"||"+a22+"|"+c42+" |"+a43+"||"+a42+"|"+c32+" |"+a33+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"|"+c61+" |",G,"|"+c52+" ||"+c51+" |",R,"|"+c82+" ||"+c81+" |",B,"|"+c72+" ||"+c71+" |",O,"|"+c62+" | \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"|"+a73+"|"+c102+" |"+a52+"||"+a53+"|"+c92+" |"+a62+"||"+a63+"|"+c122+" |"+a82+"||"+a83+"|"+c112+" |"+a72+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"             |"+a51+"|"+c91+" |"+a61+"| \n"+"             |___|___|___| \n"+"             |"+c101+" |",Y,"|"+c121+" | \n"+"             |___|___|___| \n"+"             |"+a71+"|"+c111+" |"+a81+"| \n"+"             |___|___|___| \n")

    
llista123=["1","2","3","4","5","6","7","8","9","0"]

modeseleccionat=0
heacabatfridich=0

conf1=1
conf2=0
conf3=1
conf4=0
conf5=0
conf51=0
conf52=0
conf6=1
conf7=0
conf8=0
conf9=0 

entradamod=0

ydfas=0
ncultiu="0"
ncultiu2=0
sortircul=0
acabadecul=0
godmode=2

qnumerosaleatori=20

print("Benvingut al meu cub \n   -PMG  \n\n")
cub2()

print("Blanc: W");print("Vermell: R");print("Verd: G");print("Blau: B");print("Groc: Y");print("Taronja: O")

print("\n")

input("Prem ENTER per continuar")
print(espai)
opciomenu=0
while opciomenu not in llista123:
    
    if conf5==0:
        print(espai)
        print("MENÚ PRINCIPAL")
        print("**************")
        cub2()
        print("1. Moure el cub lliurement")
        print("2. Utilitzar algoritmes")
        print("3. Desmuntar aleatoriament")
        print("4. Reiniciar el cub (tornar a l'estat resolt)")
        print("5. Resoldre el cub")
        print("6. Introduir colors")
        print("7. Configuració")
        print("8. Esborrar Moviments_cub.txt")
        print("9. Detecció colors")
        print("")
        print("0. Tancar el programa")
        print()
        opciomenu=input("Tria una opció. ")
        print(espai)
    else:
        if conf5==1:
            poscultius=["5","10","20","50","100","200","500","1000","5000","14000","32000","224000"]
            while ncultiu=="0":
                while ncultiu not in poscultius:
                    print("Mode cultiu a punt de començar")
                    print("")
                    print("Quantes vegades vols executar-ho?")
                    print("Possibles cultius: 5, 10, 20, 50, 100, 200, 500, 1000, 5000, 14000. 0 per sortir del mode cultiu")
                    ncultiu=str(input())
                    print()
                    if ncultiu=="0":
                        sortircul=1
                        ncultiu="5"
                    if ncultiu not in poscultius:
                        print("Quantitat incorrecte\n")
                    if ncultiu in poscultius:
                        ncultiu2=int(ncultiu)
                        print(espai)
                        if ncultiu == "14000" or ncultiu == "5000" or ncultiu == "224000" or ncultiu == "1000":
                            sinotot=0
                            sinolist=["si","SI","no","NO","Si","No"]
                            silist=["si","SI","Si"]
                            while sinotot not in sinolist:
                                print("Anar canviant de número de moviments al desordenar?")
                                print("(Respondre amb SI o NO)")
                                sinotot=input()
                                print(espai)
                                if sinotot not in sinolist:
                                    print("Resposta incorrecta! \n")
                                if sinotot in silist:
                                    print("ha dicho si")
                                    conf52=1
                                else:
                                    conf52=0
            if godmode==1:
                ncultiu=0
                entradamod=1
            #if ncultiu in poscultius:
            if ncultiu2 != 0:
                if conf51==0:
                    opciomenu="3"
                if conf51==1:
                    opciomenu="5"

                if opciomenu=="3":
                    ncultiu2=ncultiu2-1
                    restacul=int(ncultiu)-ncultiu2
                    #print()
                    #print("Contador:",str(restacul))
                    print(restacul)

                    if conf52==1:
                        if conf6==0 or conf6==1 or conf6==2 or conf6==3 or conf6==4 or conf6==5:
                            conf6=conf6+1
                        else:
                            conf6=0
                        #print("Conf52:",conf52,"\nConf6:",conf6)
            if sortircul==1 or ncultiu2==0:
                conf5=0
                ncultiu="0"
                sortircul=0
                opciomenu=0
                acabadecul=1
        if conf8==1:
            print("mode 8?")
            input()





            conf8=0
            opciomenu=0
    if opciomenu not in llista123:
        if acabadecul==0:
            print("\nOpció incorrecta.\n")
        acabadecul=0
    else:
        if opciomenu=="1":
            if conf9==1:
                import serial
                import time
                ardu=serial.Serial("com5",9600)
            movmoure=open("Moviments_cub.txt","w")
            mov=0
            while mov not in llistamoviments:
                print(espai)
                cub2()
                print("Quin moviment vols fer? [U,U',D,D',R,R',L,L',F,F',B,B'] \n[Escriu SORTIR per tornar al menú d'inici]")
                mov=input()
                if mov not in llistamoviments:
                    print("\nMoviment no vàlid, torna a provar. \n")
                else:
                    if mov in llistasortir:
                        if conf9==1:
                            ardu.close()
                        opciomenu=0
                        print(espai)
                    else:
                        if mov=="U":
                            na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                            a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                            textmov="U"
                            movardu=b'U'
                        if mov=="U'":
                            na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                            a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                            textmov="u"
                            movardu=b'u'                            
                        if mov=="F":
                            nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                            c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                            textmov="F"
                            movardu=b'F'                            
                        if mov=="F'":
                            nc51=c12;nc12=c82;nc82=c92;nc92=c51;na12=a23;na23=a62;na53=a12;na62=a53;nc91=c52;nc52=c11;nc11=c81;nc81=c91;na51=a13;na13=a21;na21=a63;na63=a51;na61=a52;na52=a11;na11=a22;na22=a61
                            c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22     
                            textmov="f"
                            movardu=b'f'
                        if mov=="R":
                            nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                            c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                            textmov="R"
                            movardu=b'R'
                        if mov=="R'":                      
                            nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                            c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                            textmov="r"
                            movardu=b'r'
                        if mov=="L":
                            nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                            c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                            textmov="L"
                            movardu=b'L'
                        if mov=="L'":
                            nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                            c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                            textmov="l"
                            movardu=b'l'
                        if mov=="D":
                            nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                            c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                            textmov="D"
                            movardu=b'D'
                        if mov=="D'":
                            nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                            c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                            textmov="d"
                            movardu=b'd'
                        if mov=="B":
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            textmov="B"
                            movardu=b'B'
                        if mov=="B'":
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            textmov="b"
                            movardu=b'b'

                        if conf4==1:
                            movmoure=open("Moviments_cub.txt","a")
                            movmoure.write(textmov)
                            movmoure.close()
                        if conf9==1:
                            ardu.write(movardu)
                            
                        mov=0

        if opciomenu=="2":
            nalgor=0
            if conf9==1:
                import serial
                ardu=serial.Serial("COM5",9600)
            while nalgor != "1" or "2" or "3" or "4":
                print(espai)
                cub2()
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
                    cub2()
                    input("Prem ENTER")            
                    if conf4==1:
                        movalgor=open("Moviments_cub.txt","a")
                        movalgor.write("UUDDRRLLFFBB")
                        movalgor.close()
                    if conf9==1:
                        ardu.write(b'UUDDRRLLFFBB')
                    
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
                    print("(D,U',F,B',R,L',D,U')")
                    cub2()
                    input("Prem enter")            
                    if conf4==1:
                        movalgor=open("Moviments_cub.txt","a")
                        movalgor.write("DuFbRlDu")
                        movalgor.close()          
                    if conf9==1:
                        ardu.write(b'DuFbRlDu')
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    #F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    cub()
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    cub()
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    cub()
                    #U'
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
                    cub2()
                    input("Prem enter")            
                    if conf4==1:
                        movalgor=open("Moviments_cub.txt","a")
                        movalgor.write("rLFrLDrLBrLUdULdUBdURdUFbFUbFRbFDbFL")
                        movalgor.close()          
                    if conf9==1:
                        ardu.write(b'rLFrLDrLBrLUdULdUBdURdUFbFUbFRbFDbFL')
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
                    if conf9==1:
                        ardu.close()
                    opciomenu=0
                    print(espai)
                    break

        if opciomenu=="3":
            if conf4==1:
                movatzar=open("Moviments_cub.txt","a")
            if conf2==1:
                movsatzar=[]
            if conf1==1:
                cub()
            if conf6==0:
                qnumerosaleatori=10
            else:
                if conf6==1:
                    qnumerosaleatori=20
                else:
                    if conf6==2:
                        qnumerosaleatori=30
                    else:
                        if conf6==3:
                            qnumerosaleatori=40
                        else:
                            if conf6==4:
                                qnumerosaleatori=50
                            else:
                                if conf6==5:
                                    qnumerosaleatori=60
                                else:
                                    if conf6==6:
                                        qnumerosaleatori=70                                                

            if conf2==1:
                print("Números aleatoris:",qnumerosaleatori)
            import random
            if conf9==1:
                cadenamovs= ""
                import time
                import serial
                ardu=serial.Serial("COM5",9600)
            for a in range(0,qnumerosaleatori):
                random.shuffle(moves)
                mov2=(moves[1])
                if mov2=="U":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    movran="U"
                    extratz="U"
                if mov2=="U'":
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    movran="U'"
                    extratz="u"
                if mov2=="F":
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    movran="F"
                    extratz="F"
                if mov2=="F'":
                    nc51=c12;nc12=c82;nc82=c92;nc92=c51;na12=a23;na23=a62;na53=a12;na62=a53;nc91=c52;nc52=c11;nc11=c81;nc81=c91;na51=a13;na13=a21;na21=a63;na63=a51;na61=a52;na52=a11;na11=a22;na22=a61
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22     
                    movran="F'"
                    extratz="f"
                if mov2=="R":
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    movran="R"
                    extratz="R"
                if mov2=="R'":                     
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    movran="R'"
                    extratz="r"
                if mov2=="L":
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    movran="L"
                    extratz="L"
                if mov2=="L'":
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    movran="L'"
                    extratz="l"
                if mov2=="D":
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    movran="D"
                    extratz="D"
                if mov2=="D'":
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    movran="D'"
                    extratz="d"
                if mov2=="B":
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    movran="B"
                    extratz="B"
                if mov2=="B'":
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    movran="B'"
                    extratz="b"

                if conf1==1:
                    cub()
                if conf3==1:
                    print(a+1,"-",movran)
                if conf4==1:
                    movatzar.write(extratz)
                if conf2==1:
                    movsatzar.append(movran)
                if conf9==1:
                    cadenamovs=str(cadenamovs)+str(extratz)
                    if a == (qnumerosaleatori-1):
                        movardu=str.encode(cadenamovs)
                        print(cadenamovs)
                        print(movardu)
                        ardu.write(movardu)
                        time.sleep(5)
                        print("xd")
                        input()
                    
            if conf2==1:
                frasemovatzar="Moviments fets "+str(qnumerosaleatori)+": "
                n=0
                for a in range(0,qnumerosaleatori):
                    frasemovatzar=frasemovatzar+movsatzar[n]+", "
                    n=n+1
                print(frasemovatzar)
                input()
            if conf4==1:
                movatzar.close()
            if conf9==1:
                ardu.close()
            if conf5==1:
                conf51=1
            else:
                print(espai)
            opciomenu=0
            
        if opciomenu=="4":
            c11 = "WR";c12 = "RW";c21 = "WG";c22 = "GW";c31 = "WO";c32 = "OW";c41 = "WB";c42 = "BW";c51 = "RG";c52 = "GR";c61 = "GO";c62 = "OG";c71 = "OB";c72 = "BO";c81 = "BR";c82 = "RB";c91 = "YR";c92 = "RY";c101 = "YG";c102 = "GY";c111 = "YO";c112 = "OY";c121 = "YB";c122 = "BY"
            a11 = "WRG";a12 = "RGW";a13 = "GWR";a21 = "WBR";a22 = "BRW";a23 = "RWB";a31 = "WGO";a32 = "GOW";a33 = "OWG";a41 = "WOB";a42 = "OBW";a43 = "BWO";a51 = "YGR";a52 = "GRY";a53 = "RYG";a61 = "YRB";a62 = "RBY";a63 = "BYR";a71 = "YOG";a72 = "OGY";a73 = "GYO";a81 = "YBO";a82 = "BOY";a83 = "OYB"
            opciomenu=0
            print(espai)

        if opciomenu=="6":
            opcio6=0
            llista6=["2","1","3"]
            while opcio6 not in llista6:
                print(espai)
                print("Introduir colors\n")
                cub()
                print("1. Els colors de totes les peces")
                print("2. Canviar algun color")
                print("\n3. Tornar enrere\n")
                opcio6=input("Tria una opció ")
                if opcio6 in llista6:
                    if opcio6 == "1":
                        print(espai)
                        ic11=" - ";ic12=" - ";ic21=" - ";ic22=" - ";ic31=" - ";ic32=" - ";ic41=" - ";ic42=" - ";ic51=" - ";ic52=" - ";ic61=" - ";ic62=" - ";ic71=" - ";ic72=" - ";ic81=" - ";ic82=" - ";ic91=" - ";ic92=" - ";ic101=" - ";ic102=" - ";ic111=" - ";ic112=" - ";ic121=" - ";ic122=" - "
                        ia11 =" - ";ia12=" - ";ia13=" - ";ia21=" - ";ia22=" - ";ia23=" - ";ia31=" - ";ia32=" - ";ia33=" - ";ia41=" - ";ia42=" - ";ia43=" - ";ia51=" - ";ia52=" - ";ia53=" - ";ia61=" - ";ia62=" - ";ia63=" - ";ia71=" - ";ia72=" - ";ia73=" - ";ia81=" - ";ia82=" - ";ia83=" - "

                        pecesc=[0,ic31,ic21,ic41,ic11,ic22,ic12,ic42,ic32,ic61,ic52,ic51,ic82,ic81,ic72,ic71,ic62,ic102,ic92,ic122,ic112,ic91,ic101,ic121,ic111]
                        pecesa=[0,ia31,ia41,ia11,ia21,ia32,ia13,ia12,ia23,ia22,ia43,ia42,ia33,ia73,ia52,ia53,ia62,ia63,ia82,ia83,ia72,ia51,ia61,ia71,ia81]
                        pecesc2=[0]
                        pecesa2=[0]
                        def cubinput():
                            print("\n"+"              ___________\n"+"             |"+pecesa[1]+"|"+pecesc[1]+"|"+pecesa[2]+"| \n"+"             |___|___|___| \n"+"             |"+pecesc[2]+"|",W,"|"+pecesc[3]+"| \n"+"             |___|___|___| \n"+"             |"+pecesa[3]+"|"+pecesc[4]+"|"+pecesa[4]+"| \n"+" ___________ |___|___|___| ___________  ___________ \n"+"|"+pecesa[5]+"|"+pecesc[5]+"|"+pecesa[6]+"||"+pecesa[7]+"|"+pecesc[6]+"|"+pecesa[8]+"||"+pecesa[9]+"|"+pecesc[7]+"|"+pecesa[10]+"||"+pecesa[11]+"|"+pecesc[8]+"|"+pecesa[12]+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"|"+pecesc[9]+"|",G,"|"+pecesc[10]+"||"+pecesc[11]+"|",R,"|"+pecesc[12]+"||"+pecesc[13]+"|",B,"|"+pecesc[14]+"||"+pecesc[15]+"|",O,"|"+pecesc[16]+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"|"+pecesa[13]+"|"+pecesc[17]+"|"+pecesa[14]+"||"+pecesa[15]+"|"+pecesc[18]+"|"+pecesa[16]+"||"+pecesa[17]+"|"+pecesc[19]+"|"+pecesa[18]+"||"+pecesa[19]+"|"+pecesc[20]+"|"+pecesa[20]+"| \n"+"|___|___|___||___|___|___||___|___|___||___|___|___| \n"+"             |"+pecesa[21]+"|"+pecesc[21]+"|"+pecesa[22]+"| \n"+"             |___|___|___| \n"+"             |"+pecesc[22]+"|",Y,"|"+pecesc[23]+"| \n"+"             |___|___|___| \n"+"             |"+pecesa[23]+"|"+pecesc[24]+"|"+pecesa[24]+"| \n"+"             |___|___|___| \n")

                        w=1
                        for r in range(0,24):
                            pecesc[w]=" X "
                            cubinput()
                            colorpeces=0
                            while colorpeces not in colors:
                                print("De quin color és la peça que té una X.\nW-Blanc,G-Verd,R-Vermell,B-Blau,O-Taronja,Y-Groc")
                                colorpeces=input()
                                if colorpeces not in colors:
                                    print("Color incorrecte.")
                                else:
                                    pecesc[w]=" "+colorpeces+" "
                                    pecesc2.append(colorpeces)
                                    print(pecesc2)
                            print(espai)
                            w=w+1
                        y=1
                        for t in range(0,24):
                            pecesa[y]=" X "
                            cubinput()
                            colorpeces=0
                            while colorpeces not in colors:
                                print("De quin color és la peça que té una X.\nW-Blanc,G-Verd,R-Vermell,B-Blau,O-Taronja,Y-Groc")
                                colorpeces=input()
                                if colorpeces not in colors:
                                    print("Color incorrecte.")
                                else:
                                    pecesa[y]=" "+colorpeces+" "
                                    pecesa2.append(colorpeces)
                                    print(pecesa2)
                            print(espai)
                            y=y+1

                        ic31=pecesc2[1];ic21=pecesc2[2];ic41=pecesc2[3];ic11=pecesc2[4];ic22=pecesc2[5];ic12=pecesc2[6];ic42=pecesc2[7];ic32=pecesc2[8];ic61=pecesc2[9];ic52=pecesc2[10];ic51=pecesc2[11];ic82=pecesc2[12];ic81=pecesc2[13];ic72=pecesc2[14];ic71=pecesc2[15];ic62=pecesc2[16];ic102=pecesc2[17];ic92=pecesc2[18];ic122=pecesc2[19];ic112=pecesc2[20];ic91=pecesc2[21];ic101=pecesc2[22];ic121=pecesc2[23];ic111=pecesc2[24]
                        ia31=pecesa2[1];ia41=pecesa2[2];ia11=pecesa2[3];ia21=pecesa2[4];ia32=pecesa2[5];ia13=pecesa2[6];ia12=pecesa2[7];ia23=pecesa2[8];ia22=pecesa2[9];ia43=pecesa2[10];ia42=pecesa2[11];ia33=pecesa2[12];ia73=pecesa2[13];ia52=pecesa2[14];ia53=pecesa2[15];ia62=pecesa2[16];ia63=pecesa2[17];ia82=pecesa2[18];ia83=pecesa2[19];ia72=pecesa2[20];ia51=pecesa2[21];ia61=pecesa2[22];ia71=pecesa2[23];ia81=pecesa2[24]

                        c11=ic11+ic12;c21=ic21+ic22;c31=ic31+ic32;c41=ic41+ic42;c51=ic51+ic52;c61=ic61+ic62;c71=ic71+ic72;c81=ic81+ic82;c91=ic91+ic92;c101=ic101+ic102;c111=ic111+ic112;c121=ic121+ic122
                        c12=ic12+ic11;c22=ic22+ic21;c32=ic32+ic31;c42=ic42+ic41;c52=ic52+ic51;c62=ic62+ic61;c72=ic72+ic71;c82=ic82+ic81;c92=ic92+ic91;c102=ic102+ic101;c112=ic112+ic111;c122=ic122+ic121
                        a11=ia11+ia12+ia13;a21=ia21+ia22+ia23;a31=ia31+ia32+ia33;a41=ia41+ia42+ia43;a51=ia51+ia52+ia53;a61=ia61+ia62+ia63;a71=ia71+ia72+ia73;a81=ia81+ia82+ia83
                        a12=ia12+ia13+ia11;a22=ia22+ia23+ia21;a32=ia32+ia33+ia31;a42=ia42+ia43+ia41;a52=ia52+ia53+ia51;a62=ia62+ia63+ia61;a72=ia72+ia73+ia71;a82=ia82+ia83+ia81
                        a13=ia13+ia11+ia12;a23=ia23+ia21+ia22;a33=ia33+ia31+ia32;a43=ia43+ia41+ia42;a53=ia53+ia51+ia52;a63=ia63+ia61+ia62;a73=ia73+ia71+ia72;a83=ia83+ia81+ia82

                        opcio6=0
                        
                    if opcio6 == "2":
                        print(espai)
                        pc11=c11[0];pc21=c21[0];pc31=c31[0];pc41=c41[0];pc51=c51[0];pc61=c61[0];pc71=c71[0];pc81=c81[0];pc91=c91[0];pc101=c101[0];pc111=c111[0];pc121=c121[0]
                        pc12=c12[0];pc22=c22[0];pc32=c32[0];pc42=c42[0];pc52=c52[0];pc62=c62[0];pc72=c72[0];pc82=c82[0];pc92=c92[0];pc102=c102[0];pc112=c112[0];pc122=c122[0];
                        pa11=a11[0];pa21=a21[0];pa31=a31[0];pa41=a41[0];pa51=a51[0];pa61=a61[0];pa71=a71[0];pa81=a81[0]
                        pa12=a12[0];pa22=a22[0];pa32=a32[0];pa42=a42[0];pa52=a52[0];pa62=a62[0];pa72=a72[0];pa82=a82[0]
                        pa13=a13[0];pa23=a23[0];pa33=a33[0];pa43=a43[0];pa53=a53[0];pa63=a63[0];pa73=a73[0];pa83=a83[0]

                        v=[0,pa32,pc61,pa73,pc22,pc102,pa13,pc52,pa52,pa31,pc21,pa11,pa12,pc51,pa53,pa51,pc101,pa71,pc31,pc11,pc12,pc92,pc91,pc111,pa41,pc41,pa21,pa23,pc82,pa62,pa61,pc121,pa81,pa22,pc81,pa63,pc42,pc122,pa43,pc72,pa82,pa42,pc71,pa83,pc32,pc112,pa33,pc62,pa72]

                        def cubinput2():
                            print("     A   B   C    D   E   F    G   H   I    J   K   L"+"\n"+"                 ___________\n"+"1               | "+v[9]+" | "+v[18]+" | "+v[24]+" | \n"+"                |___|___|___| \n"+"2               | "+v[10]+" |",W,"| "+v[25]+" | \n"+"                |___|___|___| \n"+"3               | "+v[11]+" | "+v[19]+" | "+v[26]+" | \n"+"    ___________ |___|___|___| ___________  ___________ \n"+"4  | "+v[1]+" | "+v[4]+" | "+v[6]+" || "+v[12]+" | "+v[20]+" | "+v[27]+" || "+v[33]+" | "+v[36]+" | "+v[38]+" || "+v[41]+" | "+v[44]+" | "+v[46]+" | \n"+"   |___|___|___||___|___|___||___|___|___||___|___|___| \n"+"5  | "+v[2]+" |",G,"| "+v[7]+" || "+v[13]+" |",R,"| "+v[28]+" || "+v[34]+" |",B,"| "+v[39]+" || "+v[42]+" |",O,"| "+v[47]+" | \n"+"   |___|___|___||___|___|___||___|___|___||___|___|___| \n"+"6  | "+v[3]+" | "+v[5]+" | "+v[8]+" || "+v[14]+" | "+v[21]+" | "+v[29]+" || "+v[35]+" | "+v[37]+" | "+v[40]+" || "+v[43]+" | "+v[45]+" | "+v[48]+" | \n"+"   |___|___|___||___|___|___||___|___|___||___|___|___| \n"+"7               | "+v[15]+" | "+v[22]+" | "+v[30]+" | \n"+"                |___|___|___| \n"+"8               | "+v[16]+" |",Y,"| "+v[31]+" | \n"+"                |___|___|___| \n"+"9               | "+v[17]+" | "+v[23]+" | "+v[32]+" | \n"+"                |___|___|___| \n")
                        llistaquadre=[0,"A4","A5","A6”","B4","B6","C4","C5","C6","D1","D2","D3","D4","D5","D6","D7","D8","D9","E1","E3","E4","E6","E7","E9","F1","F2","F3","F4","F5","F6","F7","F8","F9","G4","G5","G6","H4","H6","I4","I5","I6","J4","J5","J6","K4","K6","L4","L5","L6","SORTIR","sortir"]
                        celescentre=["B5","E2","E5","E8","H5","K5"]
                        canvicolor=1
                        while canvicolor not in llistaquadre:
                            
                            cubinput2()
                            print("Quina peça vols canviar? (Escriu SORTIR per tonrar al menú INTRODUIR COLORS)")
                            canvicolor=input()
                            print(espai)
                            if canvicolor in llistaquadre:
                                if canvicolor not in llistasortir:
                                    ones=llistaquadre.index(canvicolor)
                                    v[ones]="X"
                                    noucolor=0
                                    while noucolor not in colors:
                                        cubinput2()
                                        print("De quin color és la cel·la amb la X (casella "+str(canvicolor)+")? (W,G,R,B,O,Y)")
                                        noucolor=input()
                                        print("\n")
                                        if noucolor not in colors:
                                            print("No vàlid.\n")
                                        
                                        else:
                                            v[ones]=noucolor
                                            canvicolor=1
                                            print(espai)
                                else:
                                    canvicolor=0

                            else:
                                    
                                if canvicolor in celescentre:
                                    print(espai)
                                    print("No es pot canviar el color d'un centre \n")
                                else:
                                    print(espai)
                                    print("Coordenada incorrecta\n")



                        mc11=v[19];mc12=v[20];mc21=v[10];mc22=v[4];mc31=v[18];mc32=v[44];mc41=v[25];mc42=v[36];mc51=v[13];mc52=v[7];mc61=v[2];mc62=v[47];mc71=v[42];mc72=v[39];mc81=v[34];mc82=v[28];mc91=v[22];mc92=v[21];mc101=v[16];mc102=v[5];mc111=v[23];mc112=v[45];mc121=v[31];mc122=v[37]
                        ma11=v[11];ma12=v[12];ma13=v[6];ma21=v[26];ma22=v[33];ma23=v[27];ma31=v[9];ma32=v[1];ma33=v[46];ma41=v[24];ma42=v[41];ma43=v[38];ma51=v[15];ma52=v[8];ma53=v[14];ma61=v[30];ma62=v[29];ma63=v[35];ma71=v[17];ma72=v[48];ma73=v[3];ma81=v[32];ma82=v[40];ma83=v[43]

                        c11=mc11+mc12;c21=mc21+mc22;c31=mc31+mc32;c41=mc41+mc42;c51=mc51+mc52;c61=mc61+mc62;c71=mc71+mc72;c81=mc81+mc82;c91=mc91+mc92;c101=mc101+mc102;c111=mc111+mc112;c121=mc121+mc122
                        c12=mc12+mc11;c22=mc22+mc21;c32=mc32+mc31;c42=mc42+mc41;c52=mc52+mc51;c62=mc62+mc61;c72=mc72+mc71;c82=mc82+mc81;c92=mc92+mc91;c102=mc102+mc101;c112=mc112+mc111;c122=mc122+mc121
                        a11=ma11+ma12+ma13;a21=ma21+ma22+ma23;a31=ma31+ma32+ma33;a41=ma41+ma42+ma43;a51=ma51+ma52+ma53;a61=ma61+ma62+ma63;a71=ma71+ma72+ma73;a81=ma81+ma82+ma83
                        a12=ma12+ma13+ma11;a22=ma22+ma23+ma21;a32=ma32+ma33+ma31;a42=ma42+ma43+ma41;a52=ma52+ma53+ma51;a62=ma62+ma63+ma61;a72=ma72+ma73+ma71;a82=ma82+ma83+ma81
                        a13=ma13+ma11+ma12;a23=ma23+ma21+ma22;a33=ma33+ma31+ma32;a43=ma43+ma41+ma42;a53=ma53+ma51+ma52;a63=ma63+ma61+ma62;a73=ma73+ma71+ma72;a83=ma83+ma81+ma82
                        
                        opcio6=0

                    if opcio6== "3":
                        opciomenu=0
                        
            print(espai)
            opciomenu=0

            
        if opciomenu=="0":
            break
                    
        if opciomenu=="8":
            import os
            os.remove("Moviments_cub.txt")
            opciomenu=0

        if opciomenu=="9":
            
            colores = open("colors.txt","r")
            caraR = colores.readline()
            caraB = colores.readline()
            caraO = colores.readline()
            caraG = colores.readline()
            caraW = colores.readline()
            caraY = colores.readline()

            R1=caraR[0];R2=caraR[3];R3=caraR[5];R4=caraR[1];R6=caraR[6];R7=caraR[2];R8=caraR[4];R9=caraR[7]
            W1=caraW[0];W2=caraW[3];W3=caraW[5];W4=caraW[1];W6=caraW[6];W7=caraW[2];W8=caraW[4];W9=caraW[7]
            O1=caraO[0];O2=caraO[3];O3=caraO[5];O4=caraO[1];O6=caraO[6];O7=caraO[2];O8=caraO[4];O9=caraO[7]
            G1=caraG[0];G2=caraG[3];G3=caraG[5];G4=caraG[1];G6=caraG[6];G7=caraG[2];G8=caraG[4];G9=caraG[7]
            B1=caraB[0];B2=caraB[3];B3=caraB[5];B4=caraB[1];B6=caraB[6];B7=caraB[2];B8=caraB[4];B9=caraB[7]
            Y1=caraY[0];Y2=caraY[3];Y3=caraY[5];Y4=caraY[1];Y6=caraY[6];Y7=caraY[2];Y8=caraY[4];Y9=caraY[7]

            a11=W7+R1+G3;a12=R1+G3+W7;a13=G3+W7+R1;a21=W9+B1+R3;a22=B1+R3+W9;a23=R3+W9+B1;a31=W1+G1+O3;a32=G1+O3+W1;a33=O3+W1+G1;a41=W3+O1+B3;a42=O1+B3+W3;a43=B3+W3+O1;a51=Y1+G9+R7;a52=G9+R7+Y1;a53=R7+Y1+G9;a61=Y3+R9+B7;a62=R9+B7+Y3;a63=B7+Y3+R9;a71=Y7+O9+G7;a72=O9+G7+Y7;a73=G7+Y7+O9;a81=Y9+B9+O7;a82=B9+O7+Y9;a83=O7+Y9+B9
            c11=W8+R2;c12=R2+W8;c21=W4+G2;c22=G2+W4;c31=W2+O2;c32=O2+W2;c41=W6+B2;c42=B2+W6;c51=R4+G6;c52=G6+R4;c61=G4+O6;c62=O6+G4;c71=O4+B6;c72=B6+O4;c81=B4+R6;c82=R6+B4;c91=Y2+R8;c92=R8+Y2;c101=Y4+G8;c102=G8+Y4;c111=Y8+O8;c112=O8+Y8;c121=Y6+B8;c122=B8+Y6

            opciomenu=0

            
        if opciomenu=="7":
            opcioconf="1"
            espaiconf="                              "
            opcionsconf=["0","1","2","3","4","5","6","7","8","9"]

            while opcioconf in opcionsconf:

                if conf1==0:
                    stat1="          **********"
                if conf1==1:
                    stat1="*******"
                    
                if conf2==0:
                    stat2="          **********"
                if conf2==1:
                    stat2="*******"

                if conf3==0:
                    stat3="          **********"
                if conf3==1:
                    stat3="*******"

                if conf4==0:
                    stat4="          **********"
                if conf4==1:
                    stat4="*******"
                    
                if conf5==0:
                    stat5="          **********"
                if conf5==1:
                    stat5="*******"

                if conf6==0:
                    stat6="**"
                if conf6==1:
                    stat6="   **"
                if conf6==2:
                    stat6="      **"
                if conf6==3:
                    stat6="         **"
                if conf6==4:
                    stat6="            **"
                if conf6==5:
                    stat6="               **"
                if conf6==6:
                    stat6="                  **"
                    
                if conf7==0:
                    stat7="************"
                if conf7==1:
                    stat7="               ********"

                if conf8==0:                 
                    stat8="          **********"
                if conf8==1:
                    stat8="*******"

                if conf9==0:                 
                    stat9="          **********"
                if conf9==1:
                    stat9="*******"

                print("CONFIGURACIÓ")
                print()
                print("1. Imprimir cub               ACTIVAT - DESACTIVAT")
                print(espaiconf+stat1)
                print("2. Imprimir anotacions        ACTIVAT - DESACTIVAT")
                print(espaiconf+stat2)
                print("3. Imprimir moviments         ACTIVAT - DESACTIVAT")
                print(espaiconf+stat3)
                print("4. Extreure moviments         ACTIVAT - DESACTIVAT")
                print(espaiconf+stat4)
                print("5. Mode cultiu dades          ACTIVAT - DESACTIVAT")
                print(espaiconf+stat5)
                print("6. Nº de moviments aleatoris  10 20 30 40 50 60 70")
                print(espaiconf+stat6)
                print("7. Mode resolució cub         PRINCIPIANTS - FRIDRICH")
                print(espaiconf+stat7)
                print("8. Mode final                 ACTIVAT - DESACTIVAT")
                print(espaiconf+stat8)
                print("9. Enviar moviments Arduino   ACTIVAT - DESACTIVAT")
                print(espaiconf+stat9)
                print()
                print("0. Tornar enrere")
                print("\n\n")
                opcioconf=input("Tria una opció per canviar. ")
                print(espai)

                if opcioconf in opcionsconf:
                        
                    if opcioconf=="1":
                        if conf1==0:
                            conf1 = 1
                            conf5=0
                            conf8=0
                        else:
                            conf1=0

                    if opcioconf=="2":
                        if conf2==0:
                            conf2=1
                            conf5=0
                            conf8=0
                        else:
                            conf2=0

                    if opcioconf=="3":
                        if conf3==0:
                            conf3=1
                            conf5=0
                            conf8=0
                        else:
                            conf3=0

                    if opcioconf=="4":
                        if conf4==0:
                            conf4=1
                            conf5=0
                            conf8=0
                        else:
                            conf4=0
                            conf8=0

                    if opcioconf=="5":
                        if conf5==0:
                            conf1=0
                            conf2=0
                            conf3=0
                            conf4=0
                            conf5=1
                            conf8=0
                            entradamod=1
                        else:
                            conf5=0
                            
                    if opcioconf=="6":
                        if conf6==0 or conf6==1 or conf6==2 or conf6==3 or conf6==4 or conf6==5:
                            conf6=conf6+1
                        else:
                            conf6=0
                        
                    if opcioconf=="7":
                        if conf7==0:
                            conf7 = 0
                            print("Mode no acabat.\n")
                        else:
                            conf7=0

                    if opcioconf=="8":
                        if conf8==0:
                            conf8=1
                            conf1=0
                            conf2=0
                            conf3=0
                            conf4=1
                            conf5=0
                            conf6=1
                            conf9=1
                        else:
                            conf8=0

                    if opcioconf=="9":
                        if conf9==0:
                            conf5=0
                            conf9=1
                        else:
                            conf9=0
                            conf8=0

                    if opcioconf=="0":
                        opciomenu=0
                        opcioconf=0

                else:
                    print("Resposta incorrecta \n")
                    opcioconf="1"
                    

        if opciomenu=="5":
            cadmov=str(0)
            if conf4==1:
                solve=open("Moviments_cub.txt","a")
            if conf9==1:
                ardu=serial.Serial("COM5",9600)
            movperres=0
            if conf5==0:
                print(espai)
            while c82 != "RB":
                if c51=="RB" or c12=="RB":
                    #F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    if conf4==1:
                        solve.write("F")
                    if conf9==1:
                        cadmov=str(cadmov)+str("F")
                        ardu.write(b'F')
                        time.sleep(0.1)
                    movperres=movperres+1
                    cub()

                if c92== "RB":
                    #F'
                    nc51=c12;nc12=c82;nc82=c92;nc92=c51;na12=a23;na23=a62;na53=a12;na62=a53;nc91=c52;nc52=c11;nc11=c81;nc81=c91;na51=a13;na13=a21;na21=a63;na63=a51;na61=a52;na52=a11;na11=a22;na22=a61
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22     
                    if conf4==1:
                        solve.write("f") 
                    if conf9==1:
                        cadmov=str(cadmov)+str("f")
                        ardu.write(b'f')
                        time.sleep(0.1)
                    movperres=movperres+1                  
                    cub()

                if c81=="RB" or c121=="RB" or c71=="RB":
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    if conf4==1:
                        solve.write("R")
                    if conf9==1:
                        cadmov=str(cadmov)+str("R")
                        ardu.write(b'R')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c41=="RB" or c72=="RB":
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    if conf4==1:
                        solve.write("r")
                    if conf9==1:
                        cadmov=str(cadmov)+str("r")
                        ardu.write(b'r')
                        time.sleep(0.1)
                    movperres=movperres+1
                    cub()
                    
                if c42=="RB" or c31=="RB":
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    if conf4==1:
                        solve.write("U")
                    if conf9==1:
                        cadmov=str(cadmov)+str("U")
                        ardu.write(b'U')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()

                if c11=="RB" or c22=="RB":
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    if conf4==1:
                        solve.write("u")
                    if conf9==1:
                        cadmov=str(cadmov)+str("u")
                        ardu.write(b'u')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c61=="RB" or c21=="RB":
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    if conf4==1:
                        solve.write("L")
                    if conf9==1:
                        cadmov=str(cadmov)+str("L")
                        ardu.write(b'L')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()

                if c52=="RB" or c101=="RB":
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    if conf4==1:
                        solve.write("l")
                    if conf9==1:
                        cadmov=str(cadmov)+str("l")
                        ardu.write(b'l')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c91=="RB" or c102=="RB":
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;
                    c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    if conf4==1:
                        solve.write("D")
                    if conf9==1:
                        cadmov=str(cadmov)+str("D")
                        ardu.write(b'D')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c122=="RB"or c111=="RB":
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    if conf4==1:
                        solve.write("d")
                    if conf9==1:
                        cadmov=str(cadmov)+str("d")
                        ardu.write(b'd')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c112=="RB":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    if conf4==1:
                        solve.write("B")
                    if conf9==1:
                        cadmov=str(cadmov)+str("B")
                        ardu.write(b'B')
                        time.sleep(0.1)
                    movperres=movperres+1                                        
                    cub()

                if c32=="RB" or c62=="RB":
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    if conf4==1:
                        solve.write("b")
                    if conf9==1:
                        cadmov=str(cadmov)+str("b")
                        ardu.write(b'b')
                        time.sleep(0.1)
                    movperres=movperres+1
                    cub()

            while c12!="RW":
                if c21=="RW" or c42=="RW" or c32=="RW":
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    if conf4==1:
                        solve.write("U")
                    if conf9==1:
                        cadmov=str(cadmov)+str("U")
                        ardu.write(b'U')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c11=="RW" or c22=="RW" or c41=="RW":
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12                    
                    if conf4==1:
                        solve.write("u")
                    if conf9==1:
                        cadmov=str(cadmov)+str("u")
                        ardu.write(b'u')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c61=="RW" or c102=="RW":
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                                            
                    if conf4==1:
                        solve.write("L")
                    if conf9==1:
                        cadmov=str(cadmov)+str("L")
                        ardu.write(b'L')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c51=="RW" or c52=="RW":
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    if conf4==1:
                        solve.write("l")
                    if conf9==1:
                        cadmov=str(cadmov)+str("l")
                        ardu.write(b'l')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c92=="RW" or c91=="RW" or c121=="RW" or c122=="RW":
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72                               
                    if conf4==1:
                        solve.write("D")
                    if conf9==1:
                        cadmov=str(cadmov)+str("D")
                        ardu.write(b'D')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c101=="RW":
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    if conf4==1:
                        solve.write("d")
                    if conf9==1:
                        cadmov=str(cadmov)+str("d")
                        ardu.write(b'd')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()

                if c111=="RW" or c71=="RW" or c31=="RW" or c72=="RW":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    if conf4==1:
                        solve.write("B")
                    if conf9==1:
                        cadmov=str(cadmov)+str("B")
                        ardu.write(b'B')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()

                if c112=="RW" or c62=="RW":
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    if conf4==1:
                        solve.write("b")
                    if conf9==1:
                        cadmov=str(cadmov)+str("b")
                        ardu.write(b'b')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()

            while c51 != "RG":
                if c21=="RG" or c52=="RG" or c102=="RG":
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    if conf4==1:
                        solve.write("L")
                    if conf9==1:
                        cadmov=str(cadmov)+str("L")
                        ardu.write(b'L')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c22=="RG" or c101=="RG" or c62=="RG":
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                    if conf4==1:
                        solve.write("l")
                    if conf9==1:
                        cadmov=str(cadmov)+str("l")
                        ardu.write(b'l')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c31=="RG" or c61=="RG" or c71=="RG" or c32=="RG":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    if conf4==1:
                        solve.write("B")
                    if conf9==1:
                        cadmov=str(cadmov)+str("B")
                        ardu.write(b'B')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c72=="RG":
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    if conf4==1:
                        solve.write("b")
                    if conf9==1:
                        cadmov=str(cadmov)+str("b")
                        ardu.write(b'b')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c111=="RG" or c121=="RG":
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    if conf4==1:
                        solve.write("D")
                    if conf9==1:
                        cadmov=str(cadmov)+str("D")
                        ardu.write(b'D')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c91=="RG" or c92=="RG" or c112=="RG" or c122=="RG":
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    if conf4==1:
                        solve.write("d")
                    if conf9==1:
                        cadmov=str(cadmov)+str("d")
                        ardu.write(b'd')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c41=="RG" or c42 == "RG":
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
                    if conf4==1:
                        solve.write("uBU")
                    if conf9==1:
                        cadmov=str(cadmov)+str("uBU")
                        ardu.write(b'uBU')
                        time.sleep(0.1)
                    movperres=movperres+3                    
                    cub()

                    
            while c92!="RY":

                if c102=="RY" or c121 == "RY" or c91=="RY":
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72           
                    if conf4==1:
                        solve.write("D")
                    if conf9==1:
                        cadmov=str(cadmov)+str("D")
                        ardu.write(b'D')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c101=="RY" or c122 == "RY" or c112=="RY":
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    if conf4==1:
                        solve.write("d")
                    if conf9==1:
                        cadmov=str(cadmov)+str("d")
                        ardu.write(b'd')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c111=="RY" or c62=="RY" or c32=="RY" or c31=="RY":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    if conf4==1:
                        solve.write("B")
                    if conf9==1:
                        cadmov=str(cadmov)+str("B")
                        ardu.write(b'B')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()

                if c71=="RY":
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    if conf4==1:
                        solve.write("b")
                    if conf9==1:
                        cadmov=str(cadmov)+str("b")
                        ardu.write(b'b')
                        time.sleep(0.1)
                    movperres=movperres+1                    
                    cub()
                    
                if c72=="RY":
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42                    
                    cub()
                    #D'
                    nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72
                    cub()
                    #R'
                    nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                    c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                    if conf4==1:
                        solve.write("Rdr")
                    if conf9==1:
                        cadmov=str(cadmov)+str("Rdr")
                        ardu.write(b'Rdr')
                        time.sleep(0.1)
                    movperres=movperres+3                    
                    cub()
                    
                if c42=="RY":
                    #2F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22              
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    #U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    #2F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22                
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    if conf4==1:
                        solve.write("FFUFF")
                    if conf9==1:
                        cadmov=str(cadmov)+str("FFUFF")
                        ardu.write(b'FFUFF')
                        time.sleep(0.1)
                    movperres=movperres+5                    
                    cub()
                    
                if c22=="RY":
                    #2F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22                    
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12
                    cub()
                    #2F
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22        
                    cub()
                    nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                    c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                    cub()
                    if conf4==1:
                        solve.write("FFuFF")
                    if conf9==1:
                        cadmov=str(cadmov)+str("FFuFF")
                        ardu.write(b'FFuFF')
                        time.sleep(0.1)
                    movperres=movperres+5                    
                    
                if c61=="RY":
                    #L'
                    nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31              
                    cub()
                    #D
                    nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                    c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72                          
                    cub()
                    #L
                    nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                    c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                    if conf4==1:
                        solve.write("lDL")
                    if conf9==1:
                        cadmov=str(cadmov)+str("lDL")
                        ardu.write(b'lDL')
                        time.sleep(0.1)
                    movperres=movperres+3
                    cub()
                    
                if c41=="RY":
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
                    if conf4==1:
                        solve.write("uBU")   
                    if conf9==1:
                        cadmov=str(cadmov)+str("uBU")
                        ardu.write(b'uBU')
                        time.sleep(0.1)
                    movperres=movperres+3                 
                    cub()
                                        
                if c21=="RY":
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
                    if conf4==1:
                        solve.write("UBu")  
                    if conf9==1:
                        cadmov=str(cadmov)+str("UBu")
                        ardu.write(b'UBu')
                        time.sleep(0.1)
                    movperres=movperres+3                  


            n=1
            for a in range(0,4):        
                esquina=[0,"RGW","RYG","RBY","RWB"]
                while a12!=esquina[n]:
                    if a21 == esquina[n] or a22 == esquina[n] or a23 == esquina[n]:
                        #R
                        nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
                        c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42         
                        cub()
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                            
                        cub()
                        #R'
                        nc122=c81;nc81=c42;nc42=c72;nc72=c122;na63=a22;na22=a43;na43=a82;na82=a63;nc121=c82;nc82=c41;nc41=c71;nc71=c121;na61=a23;na23=a41;na41=a83;na83=a61;na81=a62;na62=a21;na21=a42;na42=a81
                        c122=nc122;c81=nc81;c42=nc42;c72=nc72;a63=na63;a22=na22;a43=na43;a82=na82;c121=nc121;c82=nc82;c41=nc41;c71=nc71;a61=na61;a23=na23;a41=na41;a83=na83;a81=na81;a62=na62;a21=na21;a42=na42
                        cub()
                        
                        movperres=movperres+3
                        if conf4==1:
                            solve.write("RBr")                                            
                        if conf9==1:
                            cadmov=str(cadmov)+str("RBr")
                            ardu.write(b'RBr')
                            time.sleep(0.1)

                    if a61 == esquina[n] or a62 == esquina[n] or a63 == esquina[n]:
                        #D
                        nc91=c101;nc121=c91;nc111=c121;nc101=c111;na61=a51;na81=a61;na71=a81;na51=a71;nc92=c102;nc122=c92;nc112=c122;nc102=c112;na73=a83;na53=a73;na63=a53;na83=a63;na52=a72;na62=a52;na82=a62;na72=a82
                        c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72                              
                        cub()
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                                  
                        cub()
                        #D'
                        nc91=c121;nc121=c111;nc111=c101;nc101=c91;na61=a81;na81=a71;na71=a51;na51=a61;nc92=c122;nc122=c112;nc112=c102;nc102=c92;na73=a53;na53=a63;na63=a83;na83=a73;na52=a62;na62=a82;na82=a72;na72=a52
                        c91=nc91;c121=nc121;c111=nc111;c101=nc101;a61=na61;a81=na81;a71=na71;a51=na51;c92=nc92;c122=nc122;c112=nc112;c102=nc102;a73=na73;a53=na53;a63=na63;a83=na83;a52=na52;a62=na62;a82=na82;a72=na72                        
                        cub()
                        movperres=movperres+3
                        if conf4==1:
                            solve.write("DBd")                    
                        if conf9==1:
                            cadmov=str(cadmov)+str("DBd")
                            ardu.write(b'DBd')
                            time.sleep(0.1)

                    if a51 == esquina[n] or a52 == esquina[n] or a53 == esquina[n]:
                        #L
                        nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                               
                        cub()
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                  
                        cub()
                        #L'
                        nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31
                        cub()
                        movperres=movperres+3
                        if conf4==1:
                            solve.write("LBl")                    
                        if conf9==1:
                            cadmov=str(cadmov)+str("Lbl")
                            ardu.write(b'Lbl')
                            time.sleep(0.1)
                    
                    if a71 == esquina[n] or a72 == esquina[n]:
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                        cub()
                        movperres=movperres+1
                        if conf4==1:
                            solve.write("b")                    
                        if conf9==1:
                            cadmov=str(cadmov)+str("b")
                            ardu.write(b'b')
                            time.sleep(0.1)
                   
                    if a11  == esquina[n] or a13 == esquina[n]:
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
                        movperres=movperres+3
                        if conf4==1:
                            solve.write("UBu")                    
                        if conf9==1:
                            cadmov=str(cadmov)+str("UBu")
                            ardu.write(b'UBu')
                            time.sleep(0.1)
                      
                    if a42 == esquina[n] or a83 == esquina[n] or a43 == esquina[n] or a73 == esquina[n] or a41 == esquina[n] or a82 == esquina[n] or a73 == esquina[n] or a81 == esquina[n]:
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                                    
                        cub()
                        movperres=movperres+1
                        if conf4==1:
                            solve.write("B")
                        if conf9==1:
                            cadmov=str(cadmov)+str("B")
                            ardu.write(b'B')
                            time.sleep(0.1)
  
                    if a33 == esquina[n]:
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
                        movperres=movperres+3
                        if conf4==1:
                            solve.write("Ubu")                    
                        if conf9==1:
                            cadmov=str(cadmov)+str("Ubu")
                            ardu.write(b'Ubu')
                            time.sleep(0.1)
                                        
                    if a31 == esquina[n]:
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
                        movperres=movperres+3
                        if conf4==1:
                            solve.write("UBu")                    
                        if conf9==1:
                            cadmov=str(cadmov)+str("Ubu")
                            ardu.write(b'Ubu')
                            time.sleep(0.1)

                    if a32 == esquina[n]:
                        #L'
                        nc22=c52;nc52=c102;nc102=c61;nc61=c22;na13=a52;na52=a73;na73=a32;na32=a13;nc51=c101;nc101=c62;nc62=c21;nc21=c51;na53=a71;na71=a33;na33=a11;na11=a53;na12=a51;na51=a72;na72=a31;na31=a12
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31             
                        cub()
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73            
                        cub()
                        #L
                        nc22=c61;nc52=c22;nc102=c52;nc61=c102;na13=a32;na52=a13;na73=a52;na32=a73;nc51=c21;nc101=c51;nc62=c101;nc21=c62;na53=a11;na71=a53;na33=a71;na11=a33;na12=a31;na51=a12;na72=a51;na31=a72
                        c22=nc22;c52=nc52;c102=nc102;c61=nc61;a13=na13;a52=na52;a73=na73;a32=na32;c51=nc51;c101=nc101;c62=nc62;c21=nc21;a53=na53;a71=na71;a33=na33;a11=na11;a12=na12;a51=na51;a72=na72;a31=na31                                        
                        cub()
                        movperres=movperres+3
                        if conf4==1:
                            solve.write("lbL")                    
                        if conf9==1:
                            cadmov=str(cadmov)+str("lbL")
                            ardu.write(b'lbL')
                            time.sleep(0.1)

                #F
                nc51=c92;nc12=c51;nc82=c12;nc92=c82;na12=a53;na23=a12;na53=a62;na62=a23;nc91=c81;nc52=c91;nc11=c52;nc81=c11;na51=a63;na13=a51;na21=a13;na63=a21;na61=a22;na52=a61;na11=a52;na22=a11
                c92=nc92;c51=nc51;c82=nc82;c12=nc12;a53=na53;a12=na12;a62=na62;a23=na23;c81=nc81;c91=nc91;c52=nc52;c11=nc11;a63=na63;a51=na51;a13=na13;a21=na21;a61=na61;a52=na52;a11=na11;a22=na22
                if conf4==1:
                    solve.write("F")                                   
                if conf9==1:
                    cadmov=str(cadmov)+str("F")
                    ardu.write(b'F')
                    time.sleep(0.1)
                cub()
                movperres=movperres+1
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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("UbublBL")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("UbublBL")
                        ardu.write(b'UbublBL')
                        time.sleep(0.1)

                if c31=="WG" or c61=="WG":
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    movperres=movperres+1
                    if conf4==1:
                        solve.write("b")
                    if conf9==1:
                        cadmov=str(cadmov)+str("b")
                        ardu.write(b'b')
                        time.sleep(0.1)
                                        
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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("lBLBUbu")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("lBLBUbu")
                        ardu.write(b'lBLBUbu')
                        time.sleep(0.1)
                                        
                if c111=="WG":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                    movperres=movperres+1
                    if conf4==1:
                        solve.write("B")
                    if conf9==1:
                        cadmov=str(cadmov)+str("B")
                        ardu.write(b'B')
                        time.sleep(0.1)
                                        
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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("RbrbuBU")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("RbrbuBU")
                        ardu.write(b'RbrbuBU')
                        time.sleep(0.1)
                                                            
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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("DbdbrBR")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("DbdbrBR")
                        ardu.write(b'DbdbrBR')
                        time.sleep(0.1)
                                        
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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("LblbdBD")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("LblbdBD")
                        ardu.write(b'LblbdBD')
                        time.sleep(0.1)
                    
                if c71 == "WG" or c32 == "WG" or c62 == "WG" or c112 == "WG":
                    while c22 != "GW":
                        if c72 =="GW":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("b")
                            if conf9==1:
                                cadmov=str(cadmov)+str("b")
                                ardu.write(b'b')
                                time.sleep(0.1)
                            
                        if c31 =="GW" or c61 == "GW":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("B")
                            if conf9==1:
                                cadmov=str(cadmov)+str("B")
                                ardu.write(b'B')
                                time.sleep(0.1)
                                                
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
                            movperres=movperres+7
                            if conf4==1:
                                solve.write("UbublBL")                    
                            if conf9==1:
                                cadmov=str(cadmov)+str("UbublBL")
                                ardu.write(b'UbublBL')
                                time.sleep(0.1)

            while c41!="WB":
                if c31=="WB" or c72=="WB":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                    movperres=movperres+1
                    if conf4==1:
                        solve.write("B")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("B")
                        ardu.write(b'B')
                        time.sleep(0.1)

                if c61=="WB" or c42=="WB":
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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("RbrbuBU")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("RbrbuBU")
                        ardu.write(b'RbrbuBU')
                        time.sleep(0.1)
                                        
                if c111=="WB":
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                    cub()
                    movperres=movperres+1
                    if conf4==1:
                        solve.write("b")
                    if conf9==1:
                        cadmov=str(cadmov)+str("b")
                        ardu.write(b'b')
                        time.sleep(0.1)
      
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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("DbdbrBR")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("DbdbrBR")
                        ardu.write(b'DbdbrBR')
                        time.sleep(0.1)
                                        
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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("LblbdBD")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("LblbdBD")
                        ardu.write(b'LblbdBD')
                        time.sleep(0.1)
                    
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
                            movperres=movperres+7
                            if conf4==1:
                                solve.write("uBUBRbr")                    
                            if conf9==1:
                                cadmov=str(cadmov)+str("uBUBRbr")
                                ardu.write(b'uBUBRbr')
                                time.sleep(0.1)
                                            
                        if c61 =="BW":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("B")                    
                            if conf9==1:
                                cadmov=str(cadmov)+str("B")
                                ardu.write(b'B')
                                time.sleep(0.1)
                                        
                        if c31 == "BW" or c72 == "BW":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("b")                    
                            if conf9==1:
                                cadmov=str(cadmov)+str("b")
                                ardu.write(b'b')
                                time.sleep(0.1)

            while c101 != "YG":
                if c102 == "YG" or c72 == "YG":
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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("LblbdBD")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("LblbdBD")
                        ardu.write(b'LblbdBD')
                        time.sleep(0.1)

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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("DbdbrBR")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("DbdbrBR")
                        ardu.write(b'DbdbrBR')
                        time.sleep(0.1)

                if c111 == "YG" or c61 == "YG":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                    cub()
                    movperres=movperres+1
                    if conf4==1:
                        solve.write("B")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("B")
                        ardu.write(b'B')
                        time.sleep(0.1)

                if c31 == "YG":
                    #B'
                    nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                       
                    cub()
                    movperres=movperres+1
                    if conf4==1:
                        solve.write("b")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("b")
                        ardu.write(b'b')
                        time.sleep(0.1)

                if c71 == "YG" or c112 == "YG" or c62 == "YG" or c32 == "YG":                   
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
                            movperres=movperres+7
                            if conf4==1:
                                solve.write("dBDBLbl")                    
                            if conf9==1:
                                cadmov=str(cadmov)+str("dBDBLbl")
                                ardu.write(b'dBDBLbl')
                                time.sleep(0.1)

                        if c72 == "GY":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("B")                    
                            if conf9==1:
                                cadmov=str(cadmov)+str("B")
                                ardu.write(b'B')
                                time.sleep(0.1)
                                                
                        if c61 == "GY" or c111== "GY":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("b")
                            if conf9==1:
                                cadmov=str(cadmov)+str("b")
                                ardu.write(b'b')
                                time.sleep(0.1)

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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("DbdbrBR")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("DbdbrBR")
                        ardu.write(b'DbdbrBR')
                        time.sleep(0.1)
                    
                if c111 == "YB" or c72 =="YB" or c31 =="YB":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                                          
                    cub()
                    movperres=movperres+1
                    if conf4==1:
                        solve.write("B")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("B")
                        ardu.write(b'B')
                        time.sleep(0.1)

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
                    movperres=movperres+7
                    if conf4==1:
                        solve.write("rBRBDbd")                    
                    if conf9==1:
                        cadmov=str(cadmov)+str("rBRBDbd")
                        ardu.write(b'rBRBDbd')
                        time.sleep(0.1)
                                        
                if c71 == "YB" or c112 == "YB" or c62 == "YB" or c32 == "YB":
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
                            movperres=movperres+7
                            if conf4==1:
                                solve.write("DbdbrBR")                    
                            if conf9==1:
                                cadmov=str(cadmov)+str("DbdbrBR")
                                ardu.write(b'DbdbrBR')
                                time.sleep(0.1)
                                                       
                        if c72 == "BY":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("B")                    
                            if conf9==1:
                                cadmov=str(cadmov)+str("B")
                                ardu.write(b'B')
                                time.sleep(0.1)
                                      
                        if c61 == "BY" or c111 == "BY":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("b")                    
                            if conf9==1:
                                cadmov=str(cadmov)+str("b")
                                ardu.write(b'b')
                                time.sleep(0.1)

            if conf2 ==1:
                print(cadmov)
                print(movperres)
                input()
            if conf7==0:
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
                            movperres=movperres+6
                            if conf4==1:
                                solve.write("LUBubl")                                                              
                            if conf9==1:
                                cadmov=str(cadmov)+str("")
                                ardu.write(b'LUBubl')
                                time.sleep(0.1)
                       
                        if c32[0] == "O" and c62[0] == "O":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("B")
                            if conf9==1:
                                ardu.write(b'B')
                                time.sleep(0.1)
                   
                        if c32[0] == "O" and c71[0] == "O":
                            #B'
                            nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                            
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("b")
                            if conf9==1:
                                cadmov=str(cadmov)+str("")
                                ardu.write(b'b')
                                time.sleep(0.1)

                        if c112[0] == "O" and c62[0] == "O":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                                                        
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("B")
                            if conf9==1:
                                cadmov=str(cadmov)+str("")
                                ardu.write(b'B')
                                time.sleep(0.1)

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
                            movperres=movperres+6
                            if conf4==1:
                                solve.write("LUBubl")                                                                                                          
                            if conf9==1:
                                cadmov=str(cadmov)+str("")
                                ardu.write(b'LUBubl')
                                time.sleep(0.1)

                        if c71[0] == "O" and c62[0] == "O":
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                                                        
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("B")
                            if conf9==1:
                                cadmov=str(cadmov)+str("")
                                ardu.write(b'B')
                                time.sleep(0.1)

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
                            movperres=movperres+6
                            if conf4==1:
                                solve.write("LUBubl")
                            if conf9==1:
                                cadmov=str(cadmov)+str("")
                                ardu.write(b'LUBubl')
                                time.sleep(0.1)

                    if c32[0] == "O" and c62[0] == "O" and c112[0] == "O" and c71[0] == "O":
                        if a42[0] == "O" and a33[0] == "O" and a72[0] == "O" and a83[0] == "O":
                            l=0
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
                                        movperres=movperres+4
                                        if conf4==1:
                                            solve.write("dfDF")
                                        if conf9==1:
                                            cadmov=str(cadmov)+str("")
                                            ardu.write(b'dfDF')
                                            time.sleep(0.1)

                                #B
                                nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                                c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                                cub()
                                movperres=movperres+1
                                if conf4==1:
                                    solve.write("B")
                                if conf9==1:
                                    cadmov=str(cadmov)+str("")
                                    ardu.write(b'B')
                                    time.sleep(0.1)
                                k=k+1


                while a43[0] != a82[0] or a81[0] != a71[0] or a73[0] != a32[0] or a31[0] != a41[0]:
                    for a in range (0,4):
                        if a32[0] != a73[0]:
                            #B
                            nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                            c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                            cub()
                            movperres=movperres+1
                            if conf4==1:
                                solve.write("B")                                                              
                            if conf9==1:
                                cadmov=str(cadmov)+str("")
                                ardu.write(b'B')
                                time.sleep(0.1)
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
                    #U'
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na31;a12=na32;a13=na33;a21=na11;a22=na12;a23=na13;a31=na41;a32=na42;a33=na43;a41=na21;a42=na22;a43=na23;c11=nc21;c12=nc22;c21=nc31;c22=nc32;c31=nc41;c32=nc42;c41=nc11;c42=nc12                                   
                    cub()
                    #R
                    nc122=c72;nc81=c122;nc42=c81;nc72=c42;na63=a82;na22=a63;na43=a22;na82=a43;nc121=c71;nc82=c121;nc41=c82;nc71=c41;na61=a83;na23=a61;na41=a23;na83=a41;na81=a42;na62=a81;na21=a62;na42=a21
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
                    #2U
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32                                    
                    cub()
                    na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                    a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                    cub()
                    movperres=movperres+12
                    if conf4==1:
                        solve.write("UrULLuRULLUU")                                                              
                    if conf9==1:
                        cadmov=str(cadmov)+str("")
                        ardu.write(b'UrULLuRULLUU')
                        time.sleep(0.1)

                while c72[0] != a43[0] or c111[0] != a81[0] or c31[0] != a41[0] or c61[0] != a32[0]:
                    if a43[0] != c72[0] and a81[0] != c111[0] and a41[0] != c31[0] and a32[0] == c61[0]:
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()
                        movperres=movperres+1
                        if conf4==1:
                            solve.write("B")                                                              
                        if conf9==1:
                            cadmov=str(cadmov)+str("")
                            ardu.write(b'B')
                            time.sleep(0.1)

                    if a81[0] != c111[0] and a73[0] != c61[0] and a31[0] != c31[0]  and c72[0] == a43[0]:
                        #U
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32                                        
                        cub()
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
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
                        #U
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
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
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                        
                        cub()
                        #2U 
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32                                        
                        cub()
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                        cub()
                        movperres=movperres+12
                        if conf4==1:
                            solve.write("UbUBUBUbubUU")                                                              
                        if conf9==1:
                            cadmov=str(cadmov)+str("")
                            ardu.write(b'UbUBUBUbubUU')
                            time.sleep(0.1)
                        
                    if a43[0] != c72[0] and a81[0] != c111[0] and a73[0] != c61[0] and a31[0] == c31[0]:
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73
                        cub()
                        movperres=movperres+1
                        if conf4==1:
                            solve.write("b")
                        if conf9==1:
                            cadmov=str(cadmov)+str("")
                            ardu.write(b'b')
                            time.sleep(0.1)
                                            
                    if a31[0] != c31[0] and a73[0] != c61[0] and a43[0] != c72[0] and a71[0] == c111[0]:
                        #B
                        nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                            
                        cub()
                        movperres=movperres+1
                        if conf4==1:
                            solve.write("B")                                                                                                      
                        if conf9==1:
                            cadmov=str(cadmov)+str("")
                            ardu.write(b'B')
                            time.sleep(0.1)

                    if a81[0] != c111[0] and a73[0] != c61[0] and a31[0] != c31[0]  and c72[0] != a43[0]:
                        #U
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32                                        
                        cub()
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
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
                        #U
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32                                        
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
                        #B'
                        nc32=c62;nc62=c112;nc112=c71;nc71=c32;na72=a83;na83=a42;na42=a33;na33=a72;nc111=c72;nc72=c31;nc31=c61;nc61=c111;na82=a41;na41=a32;na32=a71;na71=a82;na81=a43;na43=a31;na31=a73;na73=a81
                        c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                        
                        cub()
                        #2U 
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                        cub()
                        na11=a11;na12=a12;na13=a13;na21=a21;na22=a22;na23=a23;na31=a31;na32=a32;na33=a33;na41=a41;na42=a42;na43=a43;nc11=c11;nc12=c12;nc21=c21;nc22=c22;nc31=c31;nc32=c32;nc41=c41;nc42=c42
                        a11=na21;a12=na22;a13=na23;a21=na41;a22=na42;a23=na43;a31=na11;a32=na12;a33=na13;a41=na31;a42=na32;a43=na33;c11=nc41;c12=nc42;c21=nc11;c22=nc12;c31=nc21;c32=nc22;c41=nc31;c42=nc32
                        cub()
                        movperres=movperres+12
                        if conf4==1:
                            solve.write("UbUBUBUbubUU")                                                              
                        if conf9==1:
                            cadmov=str(cadmov)+str("")
                            ardu.write(b'UbUBUBUbubUU')
                            time.sleep(0.1)
                        
                while a43[0] != "B" or a43[0] == "Y" or a43[0] == "W" or a43[0] == "G":
                    #B
                    nc32=c71;nc62=c32;nc112=c62;nc71=c112;na72=a33;na83=a72;na42=a83;na33=a42;nc111=c61;nc72=c111;nc31=c72;nc61=c31;na82=a71;na41=a82;na32=a41;na71=a32;na81=a73;na43=a81;na31=a43;na73=a31
                    c32=nc32;c62=nc62;c112=nc112;c71=nc71;a72=na72;a83=na83;a42=na42;a33=na33;c111=nc111;c72=nc72;c31=nc31;c61=nc61;a82=na82;a41=na41;a32=na32;a71=na71;a81=na81;a43=na43;a31=na31;a73=na73                                         
                    cub()
                    movperres=movperres+1
                    if conf4==1:
                        solve.write("B")                                                              
                    if conf9==1:
                        cadmov=str(cadmov)+str("")
                        ardu.write(b'B')
                        time.sleep(0.1)
            if conf7==1:
                while a42[0] != "O" or a33[0] != "O" or a72[0] != "O" or a83[0] != "O" or c32[0] != "O" or c62[0] != "O" or c112[0] != "O" or c71[0] != "O":
                    if c71[0] == "O" and c32[0] == "O" and c62[0] == "O" and c112[0] == "O":
                        #ARISTAS BIEN PUESTAS
                        if a42[0] != "O" and a33[0] != "O" and a83[0] != "O" and a72[0] != "O":
                            #NINGUNA ESQUINA BIEN
                            if a82[0] == "O" and a43[0] == "O" and a32[0] == "O" and a73[0] == "O":
                                print()
                            else:
                                if a32[0] == "O" and a41[0] == "O" and a81[0] == "O" and a71[0] == "O":
                                    #DBBD'B'DB'D
                                    print()
                                else:
                                    #B
                                    print()
                    if a42[0] == "O" and a72[0] == "O" and a33[0] != "O" and a83[0] != "O":
                        #B
                        print()
                    if a42[0] != "O" and a72[0] != "O" and a33[0] == "O" and a83[0] == "O":
                        #SOLO DOS ESQUINAS BIEN (OPUESTAS)
                        if a41[0] == "O" and a73[0] == "O":
                            #D
                            print()

                        if a41[0] != "O" and a73[0] != "O":
                            #BB
                            print()
                            





                
            if conf4==1:
                solve.close()
            if conf8==1:
                transard=open("Moviments_cub.txt","r")
                movard = transard.read()
                print(movard)
                input()
                transard.close()
            
            cub()
            if conf5==0:
                print("cub resolt!")

            if c11 == "WR" and c12 == "RW" and c21 == "WG" and c22 == "GW" and c31 == "WO" and c32 == "OW" and c41 == "WB" and c42 == "BW" and c51 == "RG" and c52 == "GR" and c61 == "GO" and c62 == "OG" and c71 == "OB" and c72 == "BO" and c81 == "BR" and c82 == "RB" and c91 == "YR" and c92 == "RY" and c101 == "YG" and c102 == "GY" and c111 == "YO" and c112 == "OY" and c121 == "YB" and c122 == "BY" and a11 == "WRG" and a12 == "RGW" and a13 == "GWR" and a21 == "WBR" and a22 == "BRW" and a23 == "RWB" and a31 == "WGO" and a32 == "GOW" and a33 == "OWG" and a41 == "WOB" and a42 == "OBW" and a43 == "BWO" and a51 == "YGR" and a52 == "GRY" and a53 == "RYG" and a61 == "YRB" and a62 == "RBY" and a63 == "BYR" and a71 == "YOG" and a72 == "OGY" and a73 == "GYO" and a81 == "YBO" and a82 == "BOY" and a83 == "OYB":
                if conf5==0:
                    print("Comprobació, està bé!")
                    print("Han calgut",movperres,"moviments!")
                if qnumerosaleatori==10:
                    quantsmov=open("Número_moviments_10mov1.txt","a")
                if qnumerosaleatori==20:
                    quantsmov=open("Número_moviments_20mov1.txt","a")
                if qnumerosaleatori==30:
                    quantsmov=open("Número_moviments_30mov1.txt","a")
                if qnumerosaleatori==40:
                    quantsmov=open("Número_moviments_40mov1.txt","a")
                if qnumerosaleatori==50:
                    quantsmov=open("Número_moviments_50mov1.txt","a")
                if qnumerosaleatori==60:
                    quantsmov=open("Número_moviments_60mov1.txt","a")
                if qnumerosaleatori==70:
                    quantsmov=open("Número_moviments_70mov1.txt","a")
                    
                quantsmov.write(str(movperres)+"\n")
                quantsmov.close()
            if conf5==1:
                conf51=0
            sestaresolent=0
            
            if conf5==0:
                input()
                print(espai)
            opciomenu=0