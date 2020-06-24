# -*- coding: latin-1 -*-


#   Name:       Namensgenerator.py
#   Author:     Michael Schilling
#   Edited:     27.03.2010 - 04.04.2011
#   Version:    1.0.1


from Newton_Simulator import *
from random import randint

class Namensgenerator:

    def Namensgenerator_Buchstaben():
        # Silbenart ist in der Wahrscheinlichkeit angelehnt an der Verteilung der Silben der 8 Planeten und wichtigen Planetoide meinem Namen und den beiden Namen der Sonne (Sonne und Sol)
        # Nächster Schritt wäre die verteilung der Buchstaben und Laute an der Deutschen oder Englischen Sprache zum Vorbild zu benutzen (Ansatzweise vorgenommen worden!)
        #Phonemliste(n) (Lautliste(n)):
        #Vokale:
        Lautv=["a","a","e","e","e","i","i","o","u","io","ia","ae","ao"]
        Lautbv=["A","A","E","E","E","I","I","O","U","Io","Ia","Ae","Ao"]
        #Anzahl an Vokalen:
        v=len(Lautv)
        #Konsonanten:
        Lautk=["b","c","d","f","g","h","j","k","l","m","n","n","p","q","r","r","s","s","t","v","w","x","y","z","rs","rn","sch","qu","ch","rk"]
        Lautbk=["B","C","D","F","G","H","J","K","L","M","N","N","P","Q","R","R","S","S","T","V","W","X","Y","Z","Rs","Rn","Sch","qu","Ch","Rk"]
        #Anzahl an Konsonanten:
        k=len(Lautk)

        name=""
        silbenanzahl=randint(1,4)
        for j in range(0,silbenanzahl):
            x=randint(1,7)
            if x==1 or x==2 or x==3:
                # k v   - Offene Silbe
                if name=="":
                    name=name+Lautbk[randint(0,(k-1))]
                    name=name+Lautv[randint(0,(v-1))]
                else:
                    name=name+Lautk[randint(0,(k-1))]
                    name=name+Lautv[randint(0,(v-1))]
            if x==4:
                # k v k - Geschlossene Silbe
                if name=="":
                    name=name+Lautbk[randint(0,(k-1))]
                    name=name+Lautv[randint(0,(v-1))]
                    name=name+Lautk[randint(0,(k-1))]
                else:
                    name=name+Lautk[randint(0,(k-1))]
                    name=name+Lautv[randint(0,(v-1))]
                    name=name+Lautk[randint(0,(k-1))]
            if x==5 or x==6 or x==7:
                # v k   - Nackte Silbe
                if name=="":
                    name=name+Lautbv[randint(0,(v-1))]
                    name=name+Lautk[randint(0,(k-1))]
                else:
                    name=name+Lautv[randint(0,(v-1))]
                    name=name+Lautk[randint(0,(k-1))]
        print(name)     # Falls jemand versehentlich nochmal draufklickt ist er noch im Speicher und kann dann manuell wieder eingetippt werden!
        return(name)