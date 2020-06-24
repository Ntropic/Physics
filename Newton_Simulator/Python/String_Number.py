# -*- coding: latin-1 -*-


#   Name:       String_Number.py
#   Author:     Michael Schilling
#   Edited:     27.03.2010 - 12.10.2011
#   Version:    2.0.0

from random import randint
from Verifizieren import*


class String_Number:

    # Da die normalerweise verwendeten Umwandlungen von String zu einer Zahl über logarithmische Funktionen laufen und somit immer mit einem gewissen Rundungsfehler behaftet sind, wird hier nun ein aufwändigerer aber dafür exaktere Umandlungsmechanismus erzeugt

    def String_to_Number(string):

        Minus_am_Anfang=0                                                       # 1 wenn ein Minus am Anfang ist
        Minus_hinter_E=0                                                        # 1 wenn ein Minus hinter einem E ist
        if len(string)!=0:
            if string[0]=="-":
                Minus_am_Anfang=1
        for i in range(0,len(string)-2):
            if string[i+1]=="E" and string[i+2]=="-":
                Minus_hinter_E=1
        zahlen = ("0","1","2","3","4","5","6","7","8","9")
        zahlen_buchstaben = ("0","1","2","3","4","5","6","7","8","9","E","e",".")           # Eine Liste von Buchstaben die verwendet werden dÃ¼rfen.
        new_string=""
        for i in range(0,len(string)):                                          # Sortiert unerwünschte Zeichen aus
            Vorhanden_Zaehler=0
            for j in range(0,13):
                if string[i]==zahlen_buchstaben[j]:
                    Vorhanden_Zaehler=1
            if Vorhanden_Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        number=0.0                                                              # Repräsentiert die zu ermittelnde Zahl
        number_2=0.0                                                            # Zahl hinter einem E
        Zaehler=0                                                               # Zaehlt die Stellen bis zu einem Punkt, einem E oder dem Ende
        Zaehler_2=0                                                             # Zaehlt anschließend rückwärts
        n=0                                                                     # Laufvariabel
        while Zaehler<(len(string)-1) and string[Zaehler]!='.' and string[Zaehler]!='E':
            Zaehler=Zaehler+1
        Zaehler_2=Zaehler-1
        Zaehler=Zaehler+1
        while Zaehler_2>=0:                                                     # Erzeugt Zahlen vor einem Punkt, E oder gar dem Ende
            if string[Zaehler_2]=="1":
                number=number+10**n*1
            elif string[Zaehler_2]=="2":
                number=number+10**n*2
            elif string[Zaehler_2]=="3":
                number=number+10**n*3
            elif string[Zaehler_2]=="4":
                number=number+10**n*4
            elif string[Zaehler_2]=="5":
                number=number+10**n*5
            elif string[Zaehler_2]=="6":
                number=number+10**n*6
            elif string[Zaehler_2]=="7":
                number=number+10**n*7
            elif string[Zaehler_2]=="8":
                number=number+10**n*8
            elif string[Zaehler_2]=="9":
                number=number+10**n*9
            elif string[Zaehler_2]=="0":
                number=number
            n=n+1
            Zaehler_2=Zaehler_2-1
        n=0
        c=0
        if Zaehler<len(string)-1:
            if string[Zaehler-1]=='E':
                c=1
                Zaehler_2=len(string)-1
                while Zaehler_2>=Zaehler:
                    if string[Zaehler_2]=="1":
                        number_2=number_2+1*10**n
                    elif string[Zaehler_2]=="2":
                        number_2=number_2+2*10**n
                    elif string[Zaehler_2]=="3":
                        number_2=number_2+3*10**n
                    elif string[Zaehler_2]=="4":
                        number_2=number_2+4*10**n
                    elif string[Zaehler_2]=="5":
                        number_2=number_2+5*10**n
                    elif string[Zaehler_2]=="6":
                        number_2=number_2+6*10**n
                    elif string[Zaehler_2]=="7":
                        number_2=number_2+7*10**n
                    elif string[Zaehler_2]=="8":
                        number_2=number_2+8*10**n
                    elif string[Zaehler_2]=="9":
                        number_2=number_2+9*10**n
                    elif string[Zaehler_2]=="0":
                        number_2=number_2
                    n=n+1
                    Zaehler_2=Zaehler_2-1
                if Minus_hinter_E==1:
                    number_2=number_2*(-1)
                number=number*10**number_2
            elif string[Zaehler-1]=='.':
                x=0
                n=1
                while Zaehler<len(string) and x==0:
                    if string[Zaehler]=="1":
                        number=number+10**(-n)
                    elif string[Zaehler]=="2":
                        number=number+2*10**(-n)
                    elif string[Zaehler]=="3":
                        number=number+3*10**(-n)
                    elif string[Zaehler]=="4":
                        number=number+4*10**(-n)
                    elif string[Zaehler]=="5":
                        number=number+5*10**(-n)
                    elif string[Zaehler]=="6":
                        number=number+6*10**(-n)
                    elif string[Zaehler]=="7":
                        number=number+7*10**(-n)
                    elif string[Zaehler]=="8":
                        number=number+8*10**(-n)
                    elif string[Zaehler]=="9":
                        number=number+9*10**(-n)
                    elif string[Zaehler]=="0":
                        number=number
                    else:
                        x=1
                    Zaehler=Zaehler+1
                    n=n+1
        n=0
        if c==0:
            if Zaehler<len(string):
                if string[Zaehler-1]=='E':
                    c=1
                    Zaehler_2=len(string)-1
                    while string[Zaehler_2]!='E':
                        if string[Zaehler_2]=="1":
                            number_2=number_2+1*10**n
                        elif string[Zaehler_2]=="2":
                            number_2=number_2+2*10**n
                        elif string[Zaehler_2]=="3":
                            number_2=number_2+3*10**n
                        elif string[Zaehler_2]=="4":
                            number_2=number_2+4*10**n
                        elif string[Zaehler_2]=="5":
                            number_2=number_2+5*10**n
                        elif string[Zaehler_2]=="6":
                            number_2=number_2+6*10**n
                        elif string[Zaehler_2]=="7":
                            number_2=number_2+7*10**n
                        elif string[Zaehler_2]=="8":
                            number_2=number_2+8*10**n
                        elif string[Zaehler_2]=="9":
                            number_2=number_2+9*10**n
                        elif string[Zaehler_2]=="0":
                            number_2=number_2
                        n=n+1
                        Zaehler_2=Zaehler_2-1
                    if Minus_hinter_E==1:
                        number_2=number_2*(-1)
                    number=number*10**number_2
        if Minus_am_Anfang==1:
            number=number*(-1)
        a=0
        for i in range(0,len(string)):
            if string[i]=="." or string[i]=='E':
                a=1
        if a==0:
            number=0.0
            Zaehler_2=len(string)-1
            while Zaehler_2>=0:                                                 # Erzeugt Zahlen vor einem Punkt, E oder gar dem Ende
                if string[Zaehler_2]=="1":
                    number=number+10**n*1
                elif string[Zaehler_2]=="2":
                    number=number+10**n*2
                elif string[Zaehler_2]=="3":
                    number=number+10**n*3
                elif string[Zaehler_2]=="4":
                    number=number+10**n*4
                elif string[Zaehler_2]=="5":
                    number=number+10**n*5
                elif string[Zaehler_2]=="6":
                    number=number+10**n*6
                elif string[Zaehler_2]=="7":
                    number=number+10**n*7
                elif string[Zaehler_2]=="8":
                    number=number+10**n*8
                elif string[Zaehler_2]=="9":
                    number=number+10**n*9
                elif string[Zaehler_2]=="0":
                    number=number
                n=n+1
                Zaehler_2=Zaehler_2-1
            if Minus_am_Anfang==1:
                number=number*(-1)
        return(number)

    def Number_to_String(number):
        return(Verifizieren.Verifizieren_mit_Null(str(number)))



# Testalgorithmus 1
#a='-21.0E10'
#b=0.0
#b=String_Number.String_to_Number(a)
#print(b)

# Testalgorithmus 2

#a=-10.0e+7
#b=""
#b=String_Number.Number_to_String(a)
#print(b)
