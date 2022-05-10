# TDR-ElCub

Repositori del treball de recerca que vaig fer amb 16 quan era alumne de batxillerat del INS Gallecs.
Al repositori està el PDF amb el document que vaig entregar i la presentació que vaig fer.
També el codi que vaig desenvolupar durant l'estiu de batxillerat.

El meu treball de recerca porta el nom de "Programació, disseny i muntatge d'un robot capaç de resoldre el cub de Rubik"

El codi del meu treball està dividit en tres parts principals:

  * Simulació virtual d'un cub de Rubik (Python):<br>
        Programa amb Python (molt poc organitzat, tenia 16 anys i no sabia programar).
        Simula un cub de rubik amb les seves cares i arestes.
        Permet moure les cares independentment, mostrant per pantalla.
        També es pot desmuntar aleatoriament.
        I muntar de nou, guardant els moviments que ha fet (que posteriorment li passava al Arduino per a resoldre el cub físic).
        
  * Detecció de colors (Java amb Processing):<br>
        Aquest programa agafa 6 fotos (1 de cada cara) i torna un arxiu de text amb els colors que ha sapigut detectar.
        El programa amb Python pot agafar aquest arxiu i posar els colors detectats a les variables pertinents.
        
  * Monitorització de motors per a resoldre el cub físicament (C++ amb Arduino):<br>
        Programa amb Arduino
        Requereix de 6 motors pas a pas i 6 drivers per a controlarlos.
        Rep instruccions pel terminal manualment o des del programa de Python i mou el motor respectiu.
        Les ordres que detecta son strings com per exemple (fRlRUd).
        La lletra diu quin motor es mou, per exemple f vol dir Front, r - Right ...
        Si es majúscula o minúscula representa si s'ha de moure horariament o antihorariament.
        
Està tot millor explicat a la memoria TDR-ElCub.pdf
