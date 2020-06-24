# -*- coding: latin-1 -*-


#   Name:       Verifizieren.py
#   Author:     Michael Schilling
#   Edited:     27.03.2010 - 14.11.2010
#   Version:    6.1.3

from unicodedata import*



class Verifizieren:

    #   Verifizierende Entries -> Endlich Fertig:
    #   Bringt Strings welche später in Zahlen umgewandelt werden sollen in Form!
    #   Wir unterscheiden dabei Zahlen die größer als null sein sollen, solche bei denen dies egal ist und Zahlen die Ganzzahlig sein müssen, also kein Komma enthalten,
    #   diese Algorithmen sind nicht besonders Effektiv, müssen aber auchnicht zu hauf ablaufen und wenn dann immer nur mit einem Entry,
    #   da ja auch immer nur ein Entry verändert werden kann!

    def Verifizieren(stringvar):
        Anfang=0
        string=""
        string=string+str(stringvar)
        # String Zeichen Bereinigen
        zahlen_buchstaben = ("0","1","2","3","4","5","6","7","8","9","-","E","e",".")           # Eine Liste von Buchstaben die in den Zahlenentries verwendet werden dürfen.
        new_string=""
        for i in range(0,len(string)):                                      # Sortiert unerwünschte Zeichen aus
            Vorhanden_Zaehler=0
            for j in range(0,14):
                if string[i]==zahlen_buchstaben[j]:
                    Vorhanden_Zaehler=1
            if Vorhanden_Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        new_string=""
        for i in range (0,len(string)):                                     # Formt kleines e zu großem E um
            if string[i]=="e":
                new_string=new_string+"E"
            else:
                new_string=new_string+string[i]
        string=new_string
        # Überflüssige Punkte entfernen (nur letzter bleibt bestehen)
        Zaehler_P=0                                                         # Zaehlt Punkte
        for i in range(0,len(string)):                                      # Sucht nach E's -> nicht mehr als eines erwünscht, und das muss sich nach einem Punkt befinden oder es darf sich kein Punkt im Entry befinden
            if string[i]==".":
                Zaehler_P=Zaehler_P+1
        if Zaehler_P>1:                                                     # Löscht überflüssige Punkte
            x=1
            a=0
            new_string=""
            while x<Zaehler_P:
                if a<len(string):
                    if string[a]!=".":
                        new_string=new_string+string[a]
                        a=a+1
                    else:
                        x=x+1
                        a=a+1
            while a<len(string):
                new_string=new_string+string[a]
                a=a+1
            string=new_string
            Zaehler_P=1
        # Überflüssige Minuszeichen entfernen
        Zaehler_minus=0                                                     # Zaehlt Minuszeichen des Anfangs
        Position=0                                                          # Position des Zeigers
        if len(string)>1:
            while Position==Zaehler_minus and Position!=len(string)-1:          # Löscht überflüssige Minuszeichen am Anfang
                if string[Position]=="-":
                    Zaehler_minus=Zaehler_minus+1
                Position=Position+1
            Anfang=0                                                            # Speichert die Anfangsposition der Ziffern
            if Zaehler_minus % 2 ==1:                                           # Bei ungerader Zahl wird ein Minus übrig gelassen
                new_string="-"
                for i in range(Zaehler_minus,len(string)):
                    new_string=new_string+string[i]
                string=new_string
                Anfang=1
            else:                                                               # Bei gerader Anzahl wird kein Minus übrig gelassen
                new_string=""
                for i in range(Zaehler_minus,len(string)):
                    new_string=new_string+string[i]
                string=new_string
                Anfang=0
        else:
            Anfang=0
        # Überflüssige E's entfernen (nur letztes E bleibt bestehen)
        for i in range(0,len(string)-1):                                    # Löscht E's vor einem Punkt -> bei fehlendem Punkt ist das E jedoch erlaubt
            if string[i]==".":
                for j in range(0,i):
                    if string[j]=="E":
                        new_string=""
                        for k in range (0,len(string)):
                            if k!=j:
                                new_string=new_string+string[k]
                        string=new_string
        E_Liste=[]                                                          # Liste aller E's
        Letztes_E=0                                                         # Nennt die Position des letzten E's und somit die letzte Position
        E_Liste_2=[]                                                        # Liste aller E's außer dem Letzten
        for i in range(0,len(string)):                                      # Löscht alle E's bis auf das letzte E
            if string[i]=="E":
                Letztes_E=i
                E_Liste.append(i)
        for i in range (0,len(E_Liste)):                                    # Entfernt den Letzten Wert der E-Liste
            if E_Liste[i]!=Letztes_E:
                E_Liste_2.append(E_Liste[i])
        new_string=""
        for i in range(0,len(string)):
            x=0
            for j in range(0,len(E_Liste_2)):
                if E_Liste_2[j]==i:
                    x=1
            if x==0:
                new_string=new_string+string[i]
        string=new_string
        Liste_minus=[]                                                      # Liste mit Minus zwischen den Ziffern und dem E
        for i in range(0,len(string)):                                      # Entfernen von Minus zwischen den Ziffern und dem E
            if i>=Anfang and i<=Letztes_E:
                if string[i]=="-":
                    Liste_minus.append(i)
        new_string=""
        for i in range (0,len(string)):
            x=0
            for j in range (0,len(Liste_minus)):
                if i==Liste_minus[j]:
                    x=1
            if x==0:
                new_string=new_string+string[i]
        string=new_string
        Letztes_E=0
        for i in range(0,len(string)):                                      # Sucht das letzte E
            if string[i]=="E":
                Letztes_E=i
        Positionszaehler=0                                                  # Zählt die Positionen hinter dem E
        # Überflüssige Minusse Entfernen (max. 1 bleibt stehen
        Minus_zaehler=0                                                     # Zählt die Minuszeichen hinter dem E bis zum nächsten Buchstabe
        for i in range(0,len(string)):                                      # Zählt die Minuszeichen hinter dem E bis zum nächsten Buchstabe
            if i>Letztes_E:
                if Minus_zaehler==Positionszaehler and Position!=len(string)-1:
                    if string[i]=="-":
                        Minus_zaehler=Minus_zaehler+1
                    Positionszaehler=Positionszaehler+1
                else:
                    break
            new_string=""
            x=0
        for i in range(0,len(string)):                                      # Löscht überflüssige Minuszeichen
            if i<=Letztes_E:
               new_string=new_string+string[i]
            else:
                if Minus_zaehler % 2 == 1 and x==0:
                    new_string=new_string+"-"
                    x=1
                elif string[i]!="-":
                    new_string=new_string+string[i]
        string=new_string
        # E's Sonderfälle
        if Letztes_E==len(string)-1:                                        # Behandelt Sonderfälle (kein Buchstabe vor dem E und keiner dahinter)
            string=string+"1"
        if len(string)>0:
            if Letztes_E==0 and string[0]=="E":
                new_string="1"+string
                string=new_string
        # Nullen am Anfang entfernen oder hinzufügen
        Zaehler=0                                                           # beendet die Suche nach einer Zahl
        Zahl=0                                                            # 1 wenn bis zum Punkt keine Zahl außer null vorkam
        new_string=""
        Zahlen_ohne_null=("1","2","3","4","5","6","7","8","9")
        for i in range (0,len(string)):
            if string[i]=="-" and Zaehler==0:
                new_string=new_string+"-"
            elif string[i] in Zahlen_ohne_null and Zaehler==0 and Zahl==0:
                new_string=new_string+string[i]
                Zaehler=1
            elif Zaehler==0 and Zahl==0:
                if string[i]==".":
                    new_string=new_string+"0."
                    Zahl=1
                elif string[i]=="E":
                    new_string=new_string+"1E"
                    Zaehler=1
                elif i==len(string)-1 and string[i]=="0":
                    new_string=new_string+"1"
                elif i==len(string)-1 and string[i]==".":
                    new_String==new_string+".1"
            elif Zaehler==0 and Zahl==1:
                if string[i] in Zahlen_ohne_null:
                    new_string=new_string+string[i]
                    Zaehler=1
                elif string[i]=="0" and not i==len(string)-1:
                    new_string=new_string+string[i]
                elif string[i]=="E":
                    new_string=new_string+"1E"
                    Zaehler=1
                elif i==len(string)-1 and string[i]=="0":
                    new_string=new_string+"1"
                elif i==len(string)-1 and string[i]==".":
                    new_String==new_string+".1"
            elif Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        # Nullen hinter einem E entfernen
        Zaehler=0                                                           # beendet die Suche nach einer Zahl
        E_Zaehler=0                                                         # beendet die Suche nach einemE
        new_string=""
        Zahlen_ohne_null=("1","2","3","4","5","6","7","8","9")
        for i in range (0,len(string)):
            if E_Zaehler==0:
                new_string=new_string+string[i]
                if string[i]=="E":
                    E_Zaehler=1
            elif E_Zaehler==1:
                if string[i]=="-" and i!=len(string)-1:
                    new_string=new_string+"-"
                elif Zaehler==0 and string[i] not in Zahlen_ohne_null and i!=len(string)-1:
                    pass
                elif Zaehler==1 and string[i] not in Zahlen_ohne_null and i!=len(string)-1:
                    new_string=new_string+string[i]
                elif string[i] in Zahlen_ohne_null and i!=len(string)-1:
                    new_string=new_string+string[i]
                    Zaehler=1
                elif i==len(string)-1:
                    if Zaehler==0 and string[i]=="0":
                        new_string=new_string+"1"
                    elif Zaehler==0 and string[i] in Zahlen_ohne_null:
                        new_string=new_string+string[i]
                    elif Zaehler==1 and string[i]=="0":
                        new_string=new_string+"0"
                    elif Zaehler==1 and string[i] in Zahlen_ohne_null:
                        new_string=new_string+string[i]
                    elif string[i]=="-":
                        new_string==new_string+"-1"
        string=new_string
        # Kommas
        for i in range(0,len(string)):                                      # Setzt Kommas
            if string[i]=="." or string[i]=="E":
                Zaehler=i                                                   # Zaehlt zahlen bis zu einem Punkt oder E
                break
            elif i==len(string)-1:
                Zaehler=i+1
        Finder=[]                                                           # Findet heraus welche Zahlen ein Komma bekommen sollen
        if len(string)>0:
            if string[0]=="-":
                Sucher=(Zaehler-1) % 3                                      # Wie viele Ziffern vor dem ersten Komma
                for i in range (0,Zaehler):
                    if i>=Sucher:
                        if (i-(Sucher+1)) % 3 == 0 and i!=1:
                            Finder.append(i)
            else:
                Sucher=(Zaehler-1) % 3                                      # Wie viele Ziffern vor dem ersten Komma
                for i in range (0,Zaehler):
                    if i>=Sucher:
                        if (i-(Sucher-1)) % 3 == 0 and i!=1:
                            Finder.append(i-2)
            new_string=""
            for j in range(0,len(string)):
                x=0
                for k in range(0,len(Finder)):
                    if j==Finder[k]:
                        x=1
                if x==1:
                    if string[0]=="-":
                        new_string=new_string+","+string[j]
                    else:
                        new_string=new_string+string[j]+","
                else:
                    new_string=new_string+string[j]
        string=new_string
        # Leere Zeile etc.
        if len(string)==0:                                                  # Fügt leerem String eine 1 hinzu
            string="1"
        elif len(string)==1:                                                # Fügt bei kurzem String Zeichen hinzu
            if string[0]=="0":
                string="1"
            elif string[0]==".":
                string="0.1"
            elif string[0]=="-":
                string="-1"
        #print ("Verifizierter String:"+string)                             # Zeigt bearbeiteten String an, deaktivieren bei vollendetem Skript!
        return string

    def Verifizieren_mit_Null(stringvar):
        Anfang=0
        string=""
        string=string+str(stringvar)
        # String Zeichen Bereinigen
        zahlen_buchstaben = ("0","1","2","3","4","5","6","7","8","9","-","E","e",".")           # Eine Liste von Buchstaben die in den Zahlenentries verwendet werden dürfen.
        new_string=""
        for i in range(0,len(string)):                                      # Sortiert unerwünschte Zeichen aus
            Vorhanden_Zaehler=0
            for j in range(0,14):
                if string[i]==zahlen_buchstaben[j]:
                    Vorhanden_Zaehler=1
            if Vorhanden_Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        new_string=""
        for i in range (0,len(string)):                                     # Formt kleines e zu großem E um
            if string[i]=="e":
                new_string=new_string+"E"
            else:
                new_string=new_string+string[i]
        string=new_string
        # Überflüssige Punkte entfernen (nur letzter bleibt bestehen)
        Zaehler_P=0                                                         # Zaehlt Punkte
        for i in range(0,len(string)):                                      # Sucht nach E's -> nicht mehr als eines erwünscht, und das muss sich nach einem Punkt befinden oder es darf sich kein Punkt im Entry befinden
            if string[i]==".":
                Zaehler_P=Zaehler_P+1
        if Zaehler_P>1:                                                     # Löscht überflüssige Punkte
            x=1
            a=0
            new_string=""
            while x<Zaehler_P:
                if a<len(string):
                    if string[a]!=".":
                        new_string=new_string+string[a]
                        a=a+1
                    else:
                        x=x+1
                        a=a+1
            while a<len(string):
                new_string=new_string+string[a]
                a=a+1
            string=new_string
            Zaehler_P=1
        # Überflüssige Minuszeichen entfernen
        Zaehler_minus=0                                                     # Zaehlt Minuszeichen des Anfangs
        Position=0                                                          # Position des Zeigers
        if len(string)>1:
            while Position==Zaehler_minus and Position!=len(string)-1:          # Löscht überflüssige Minuszeichen am Anfang
                if string[Position]=="-":
                    Zaehler_minus=Zaehler_minus+1
                Position=Position+1
            Anfang=0                                                            # Speichert die Anfangsposition der Ziffern
            if Zaehler_minus % 2 ==1:                                           # Bei ungerader Zahl wird ein Minus übrig gelassen
                new_string="-"
                for i in range(Zaehler_minus,len(string)):
                    new_string=new_string+string[i]
                string=new_string
                Anfang=1
            else:                                                               # Bei gerader Anzahl wird kein Minus übrig gelassen
                new_string=""
                for i in range(Zaehler_minus,len(string)):
                    new_string=new_string+string[i]
                string=new_string
                Anfang=0
        else:
            Anfang=0
        # Überflüssige E's entfernen (nur letztes E bleibt bestehen)
        for i in range(0,len(string)-1):                                    # Löscht E's vor einem Punkt -> bei fehlendem Punkt ist das E jedoch erlaubt
            if string[i]==".":
                for j in range(0,i):
                    if string[j]=="E":
                        new_string=""
                        for k in range (0,len(string)):
                            if k!=j:
                                new_string=new_string+string[k]
                        string=new_string
        E_Liste=[]                                                          # Liste aller E's
        Letztes_E=0                                                         # Nennt die Position des letzten E's und somit die letzte Position
        E_Liste_2=[]                                                        # Liste aller E's außer dem Letzten
        for i in range(0,len(string)):                                      # Löscht alle E's bis auf das letzte E
            if string[i]=="E":
                Letztes_E=i
                E_Liste.append(i)
        for i in range (0,len(E_Liste)):                                    # Entfernt den Letzten Wert der E-Liste
            if E_Liste[i]!=Letztes_E:
                E_Liste_2.append(E_Liste[i])
        new_string=""
        for i in range(0,len(string)):
            x=0
            for j in range(0,len(E_Liste_2)):
                if E_Liste_2[j]==i:
                    x=1
            if x==0:
                new_string=new_string+string[i]
        string=new_string
        Liste_minus=[]                                                      # Liste mit Minus zwischen den Ziffern und dem E
        for i in range(0,len(string)):                                      # Entfernen von Minus zwischen den Ziffern und dem E
            if i>=Anfang and i<=Letztes_E:
                if string[i]=="-":
                    Liste_minus.append(i)
        new_string=""
        for i in range (0,len(string)):
            x=0
            for j in range (0,len(Liste_minus)):
                if i==Liste_minus[j]:
                    x=1
            if x==0:
                new_string=new_string+string[i]
        string=new_string
        Letztes_E=0
        for i in range(0,len(string)):                                      # Sucht das letzte E
            if string[i]=="E":
                Letztes_E=i
        Positionszaehler=0                                                  # Zählt die Positionen hinter dem E
        # Überflüssige Minusse Entfernen (max. 1 bleibt stehen
        Minus_zaehler=0                                                     # Zählt die Minuszeichen hinter dem E bis zum nächsten Buchstabe
        for i in range(0,len(string)):                                      # Zählt die Minuszeichen hinter dem E bis zum nächsten Buchstabe
            if i>Letztes_E:
                if Minus_zaehler==Positionszaehler and Position!=len(string)-1:
                    if string[i]=="-":
                        Minus_zaehler=Minus_zaehler+1
                    Positionszaehler=Positionszaehler+1
                else:
                    break
            new_string=""
            x=0
        for i in range(0,len(string)):                                      # Löscht überflüssige Minuszeichen
            if i<=Letztes_E:
               new_string=new_string+string[i]
            else:
                if Minus_zaehler % 2 == 1 and x==0:
                    new_string=new_string+"-"
                    x=1
                elif string[i]!="-":
                    new_string=new_string+string[i]
        string=new_string
        # E's Sonderfälle
        if Letztes_E==len(string)-1 and len(string)!=1:                                        # Behandelt Sonderfälle (kein Buchstabe vor dem E und keiner dahinter)
            string=string+"1"
        if len(string)>0:
            if Letztes_E==0 and string[0]=="E":
                new_string="1"+string
                string=new_string
        # Nullen am Anfang entfernen oder hinzufügen
        Zaehler=0                                                           # beendet die Suche nach einer Zahl
        Zahl=0                                                            # 1 wenn bis zum Punkt keine Zahl außer null vorkam
        new_string=""
        Zahlen_ohne_null=("1","2","3","4","5","6","7","8","9")
        for i in range (0,len(string)):
            if string[i]=="-" and Zaehler==0:
                new_string=new_string+"-"
            elif string[i] in Zahlen_ohne_null and Zaehler==0 and Zahl==0:
                new_string=new_string+string[i]
                Zaehler=1
            elif Zaehler==0 and Zahl==0:
                if string[i]==".":
                    new_string=new_string+"0."
                    Zahl=1
                elif string[i]=="E":
                    new_string=new_string+"1E"
                    Zaehler=1
                elif i==len(string)-1 and string[i]=="0":
                    new_string=new_string+"0"
                elif i==len(string)-1 and string[i]==".":
                    new_String==new_string+".0"
            elif Zaehler==0 and Zahl==1:
                if string[i] in Zahlen_ohne_null:
                    new_string=new_string+string[i]
                    Zaehler=1
                elif string[i]=="0" and not i==len(string)-1:
                    new_string=new_string+string[i]
                elif string[i]=="E":
                    new_string=new_string+"0E"
                    Zaehler=1
                elif i==len(string)-1 and string[i]=="0":
                    new_string=new_string+"0"
                elif i==len(string)-1 and string[i]==".":
                    new_String==new_string+".0"
            elif Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        # Nullen hinter einem E entfernen
        Zaehler=0                                                           # beendet die Suche nach einer Zahl
        E_Zaehler=0                                                         # beendet die Suche nach einemE
        new_string=""
        Zahlen_ohne_null=("1","2","3","4","5","6","7","8","9")
        for i in range (0,len(string)):
            if E_Zaehler==0:
                new_string=new_string+string[i]
                if string[i]=="E":
                    E_Zaehler=1
            elif E_Zaehler==1:
                if string[i]=="-" and i!=len(string)-1:
                    new_string=new_string+"-"
                elif Zaehler==0 and string[i] not in Zahlen_ohne_null and i!=len(string)-1:
                    pass
                elif Zaehler==1 and string[i] not in Zahlen_ohne_null and i!=len(string)-1:
                    new_string=new_string+string[i]
                elif string[i] in Zahlen_ohne_null and i!=len(string)-1:
                    new_string=new_string+string[i]
                    Zaehler=1
                elif i==len(string)-1:
                    if Zaehler==0 and string[i]=="0":
                        new_string=new_string+"1"
                    elif Zaehler==0 and string[i] in Zahlen_ohne_null:
                        new_string=new_string+string[i]
                    elif Zaehler==1 and string[i]=="0":
                        new_string=new_string+"0"
                    elif Zaehler==1 and string[i] in Zahlen_ohne_null:
                        new_string=new_string+string[i]
                    elif string[i]=="-":
                        new_string==new_string+"-0"
        string=new_string
        # Kommas
        for i in range(0,len(string)):                                      # Setzt Kommas
            if string[i]=="." or string[i]=="E":
                Zaehler=i                                                   # Zaehlt zahlen bis zu einem Punkt oder E
                break
            elif i==len(string)-1:
                Zaehler=i+1
        Finder=[]                                                           # Findet heraus welche Zahlen ein Komma bekommen sollen
        if len(string)>0:
            if string[0]=="-":
                Sucher=(Zaehler-1) % 3                                      # Wie viele Ziffern vor dem ersten Komma
                for i in range (0,Zaehler):
                    if i>=Sucher:
                        if (i-(Sucher+1)) % 3 == 0 and i!=1:
                            Finder.append(i)
            else:
                Sucher=(Zaehler-1) % 3                                      # Wie viele Ziffern vor dem ersten Komma
                for i in range (0,Zaehler):
                    if i>=Sucher:
                        if (i-(Sucher-1)) % 3 == 0 and i!=1:
                            Finder.append(i-2)
            new_string=""
            for j in range(0,len(string)):
                x=0
                for k in range(0,len(Finder)):
                    if j==Finder[k]:
                        x=1
                if x==1:
                    if string[0]=="-":
                        new_string=new_string+","+string[j]
                    else:
                        new_string=new_string+string[j]+","
                else:
                    new_string=new_string+string[j]
        string=new_string
        # Leere Zeile etc.
        if len(string)==0:                                                  # Fügt leerem String eine 1 hinzu
            string="0"
        elif len(string)==1:                                                # Fügt bei kurzem String Zeichen hinzu
            if string[0]=="0":
                string="0"
            elif string[0]==".":
                string="0.0"
            elif string[0]=="-":
                string="-0"
        #print ("Verifizierter String:"+string)                             # Zeigt bearbeiteten String an, deaktivieren bei vollendetem Skript!
        return string


    def Verifizieren_ohne_Minus(stringvar):
        Anfang=0
        string=""
        string=string+str(stringvar)
        # String Zeichen Bereinigen
        zahlen_buchstaben = ("0","1","2","3","4","5","6","7","8","9","-","E","e",".")           # Eine Liste von Buchstaben die in den Zahlenentries verwendet werden dürfen.
        new_string=""
        for i in range(0,len(string)):                                      # Sortiert unerwünschte Zeichen aus
            Vorhanden_Zaehler=0
            for j in range(0,14):
                if string[i]==zahlen_buchstaben[j]:
                    Vorhanden_Zaehler=1
            if Vorhanden_Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        new_string=""
        for i in range (0,len(string)):                                     # Formt kleines e zu großem E um
            if string[i]=="e":
                new_string=new_string+"E"
            else:
                new_string=new_string+string[i]
        string=new_string
        # Überflüssige Punkte entfernen (nur letzter bleibt bestehen)
        Zaehler_P=0                                                         # Zaehlt Punkte
        for i in range(0,len(string)):                                      # Sucht nach E's -> nicht mehr als eines erwünscht, und das muss sich nach einem Punkt befinden oder es darf sich kein Punkt im Entry befinden
            if string[i]==".":
                Zaehler_P=Zaehler_P+1
        if Zaehler_P>1:                                                     # Löscht überflüssige Punkte
            x=1
            a=0
            new_string=""
            while x<Zaehler_P:
                if a<len(string):
                    if string[a]!=".":
                        new_string=new_string+string[a]
                        a=a+1
                    else:
                        x=x+1
                        a=a+1
            while a<len(string):
                new_string=new_string+string[a]
                a=a+1
            string=new_string
            Zaehler_P=1
        # Überflüssige Minuszeichen entfernen
        Zaehler_minus=0                                                     # Zaehlt Minuszeichen des Anfangs
        Position=0                                                          # Position des Zeigers
        if len(string)>1:
            while Position==Zaehler_minus and Position!=len(string)-1:          # Löscht überflüssige Minuszeichen am Anfang
                if string[Position]=="-":
                    Zaehler_minus=Zaehler_minus+1
                Position=Position+1
            Anfang=0                                                            # Speichert die Anfangsposition der Ziffern
            if Zaehler_minus % 2 ==1:                                           # Bei ungerader Zahl wird ein Minus übrig gelassen
                new_string=""
                for i in range(Zaehler_minus,len(string)):
                    new_string=new_string+string[i]
                string=new_string
                Anfang=1
            else:                                                               # Bei gerader Anzahl wird kein Minus übrig gelassen
                new_string=""
                for i in range(Zaehler_minus,len(string)):
                    new_string=new_string+string[i]
                string=new_string
                Anfang=0
        else:
            Anfang=0
        # Überflüssige E's entfernen (nur letztes E bleibt bestehen)
        for i in range(0,len(string)-1):                                    # Löscht E's vor einem Punkt -> bei fehlendem Punkt ist das E jedoch erlaubt
            if string[i]==".":
                for j in range(0,i):
                    if string[j]=="E":
                        new_string=""
                        for k in range (0,len(string)):
                            if k!=j:
                                new_string=new_string+string[k]
                        string=new_string
        E_Liste=[]                                                          # Liste aller E's
        Letztes_E=0                                                         # Nennt die Position des letzten E's und somit die letzte Position
        E_Liste_2=[]                                                        # Liste aller E's außer dem Letzten
        for i in range(0,len(string)):                                      # Löscht alle E's bis auf das letzte E
            if string[i]=="E":
                Letztes_E=i
                E_Liste.append(i)
        for i in range (0,len(E_Liste)):                                    # Entfernt den Letzten Wert der E-Liste
            if E_Liste[i]!=Letztes_E:
                E_Liste_2.append(E_Liste[i])
        new_string=""
        for i in range(0,len(string)):
            x=0
            for j in range(0,len(E_Liste_2)):
                if E_Liste_2[j]==i:
                    x=1
            if x==0:
                new_string=new_string+string[i]
        string=new_string
        Liste_minus=[]                                                      # Liste mit Minus zwischen den Ziffern und dem E
        for i in range(0,len(string)):                                      # Entfernen von Minus zwischen den Ziffern und dem E
            if i>=Anfang and i<=Letztes_E:
                if string[i]=="-":
                    Liste_minus.append(i)
        new_string=""
        for i in range (0,len(string)):
            x=0
            for j in range (0,len(Liste_minus)):
                if i==Liste_minus[j]:
                    x=1
            if x==0:
                new_string=new_string+string[i]
        string=new_string
        Letztes_E=0
        for i in range(0,len(string)):                                      # Sucht das letzte E
            if string[i]=="E":
                Letztes_E=i
        Positionszaehler=0                                                  # Zählt die Positionen hinter dem E
        # Überflüssige Minusse Entfernen (max. 1 bleibt stehen
        Minus_zaehler=0                                                     # Zählt die Minuszeichen hinter dem E bis zum nächsten Buchstabe
        for i in range(0,len(string)):                                      # Zählt die Minuszeichen hinter dem E bis zum nächsten Buchstabe
            if i>Letztes_E:
                if Minus_zaehler==Positionszaehler and Position!=len(string)-1:
                    if string[i]=="-":
                        Minus_zaehler=Minus_zaehler+1
                    Positionszaehler=Positionszaehler+1
                else:
                    break
            new_string=""
            x=0
        for i in range(0,len(string)):                                      # Löscht überflüssige Minuszeichen
            if i<=Letztes_E:
               new_string=new_string+string[i]
            else:
                if Minus_zaehler % 2 == 1 and x==0:
                    new_string=new_string+"-"
                    x=1
                elif string[i]!="-":
                    new_string=new_string+string[i]
        string=new_string
        # E's Sonderfälle
        if Letztes_E==len(string)-1 and string[len(string)-1]=='E':                                        # Behandelt Sonderfälle (kein Buchstabe vor dem E und keiner dahinter)
            string=string+"1"
        if len(string)>0:
            if Letztes_E==0 and string[0]=="E":
                new_string="1"+string
                string=new_string
        # Nullen am Anfang entfernen oder hinzufügen
        Zaehler=0                                                           # beendet die Suche nach einer Zahl
        Zahl=0                                                            # 1 wenn bis zum Punkt keine Zahl außer null vorkam
        new_string=""
        Zahlen_ohne_null=("1","2","3","4","5","6","7","8","9")
        for i in range (0,len(string)):
            if string[i]=="-" and Zaehler==0:
                new_string=new_string+"-"
            elif string[i] in Zahlen_ohne_null and Zaehler==0 and Zahl==0:
                new_string=new_string+string[i]
                Zaehler=1
            elif Zaehler==0 and Zahl==0:
                if string[i]==".":
                    new_string=new_string+"0."
                    Zahl=1
                elif string[i]=="E":
                    new_string=new_string+"1E"
                    Zaehler=1
                elif i==len(string)-1 and string[i]=="0":
                    new_string=new_string+"1"
                elif i==len(string)-1 and string[i]==".":
                    new_String==new_string+".1"
            elif Zaehler==0 and Zahl==1:
                if string[i] in Zahlen_ohne_null:
                    new_string=new_string+string[i]
                    Zaehler=1
                elif string[i]=="0" and not i==len(string)-1:
                    new_string=new_string+string[i]
                elif string[i]=="E":
                    new_string=new_string+"1E"
                    Zaehler=1
                elif i==len(string)-1 and string[i]=="0":
                    new_string=new_string+"1"
                elif i==len(string)-1 and string[i]==".":
                    new_String==new_string+".1"
            elif Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        # Nullen hinter einem E entfernen
        Zaehler=0                                                           # beendet die Suche nach einer Zahl
        E_Zaehler=0                                                         # beendet die Suche nach einemE
        new_string=""
        Zahlen_ohne_null=("1","2","3","4","5","6","7","8","9")
        for i in range (0,len(string)):
            if E_Zaehler==0:
                new_string=new_string+string[i]
                if string[i]=="E":
                    E_Zaehler=1
            elif E_Zaehler==1:
                if string[i]=="-" and i!=len(string)-1:
                    new_string=new_string+"-"
                elif Zaehler==0 and string[i] not in Zahlen_ohne_null and i!=len(string)-1:
                    pass
                elif Zaehler==1 and string[i] not in Zahlen_ohne_null and i!=len(string)-1:
                    new_string=new_string+string[i]
                elif string[i] in Zahlen_ohne_null and i!=len(string)-1:
                    new_string=new_string+string[i]
                    Zaehler=1
                elif i==len(string)-1:
                    if Zaehler==0 and string[i]=="0":
                        new_string=new_string+"1"
                    elif Zaehler==0 and string[i] in Zahlen_ohne_null:
                        new_string=new_string+string[i]
                    elif Zaehler==1 and string[i]=="0":
                        new_string=new_string+"0"
                    elif Zaehler==1 and string[i] in Zahlen_ohne_null:
                        new_string=new_string+string[i]
        string=new_string
        # Kommas
        for i in range(0,len(string)):                                      # Setzt Kommas
            if string[i]=="." or string[i]=="E":
                Zaehler=i                                                   # Zaehlt zahlen bis zu einem Punkt oder E
                break
            elif i==len(string)-1:
                Zaehler=i+1
        Finder=[]                                                           # Findet heraus welche Zahlen ein Komma bekommen sollen
        if len(string)>0:
            if string[0]=="-":
                Sucher=(Zaehler-1) % 3                                      # Wie viele Ziffern vor dem ersten Komma
                for i in range (0,Zaehler):
                    if i>=Sucher:
                        if (i-(Sucher+1)) % 3 == 0 and i!=1:
                            Finder.append(i)
            else:
                Sucher=(Zaehler-1) % 3                                      # Wie viele Ziffern vor dem ersten Komma
                for i in range (0,Zaehler):
                    if i>=Sucher:
                        if (i-(Sucher-1)) % 3 == 0 and i!=1:
                            Finder.append(i-2)
            new_string=""
            for j in range(0,len(string)):
                x=0
                for k in range(0,len(Finder)):
                    if j==Finder[k]:
                        x=1
                if x==1:
                    if string[0]=="-":
                        new_string=new_string+","+string[j]
                    else:
                        new_string=new_string+string[j]+","
                else:
                    new_string=new_string+string[j]
        string=new_string
        # Leere Zeile etc.
        if len(string)==0:                                                  # Fügt leerem String eine 1 hinzu
            string="1"
        elif len(string)==1:                                                # Fügt bei kurzem String Zeichen hinzu
            if string[0]=="0":
                string="1"
            elif string[0]==".":
                string="0.1"
        if string[len(string)-1]==".":
            string=string+"1"
        #print ("Verifizierter String:"+string)                             # Zeigt bearbeiteten String an, deaktivieren bei vollendetem Skript!
        return string



    def Verifizieren_Ganzzahlen(stringvar):
        Anfang=0
        string=""
        string=string+str(stringvar)
        # String Zeichen Bereinigen
        zahlen_buchstaben = ("0","1","2","3","4","5","6","7","8","9","-","E","e")           # Eine Liste von Buchstaben die in den Zahlenentries verwendet werden dürfen.
        new_string=""
        for i in range(0,len(string)):                                      # Sortiert unerwünschte Zeichen aus
            Vorhanden_Zaehler=0
            for j in range(0,13):
                if string[i]==zahlen_buchstaben[j]:
                    Vorhanden_Zaehler=1
            if Vorhanden_Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        new_string=""
        for i in range (0,len(string)):                                     # Formt kleines e zu großem E um
            if string[i]=="e":
                new_string=new_string+"E"
            else:
                new_string=new_string+string[i]
        string=new_string
        # Überflüssige Minuszeichen entfernen
        Zaehler_minus=0                                                     # Zaehlt Minuszeichen des Anfangs
        Position=0                                                          # Position des Zeigers
        if len(string)>1:
            while Position==Zaehler_minus and Position!=len(string)-1:          # Löscht überflüssige Minuszeichen am Anfang
                if string[Position]=="-":
                    Zaehler_minus=Zaehler_minus+1
                Position=Position+1
            Anfang=0                                                            # Speichert die Anfangsposition der Ziffern
            if Zaehler_minus % 2 ==1:                                           # Bei ungerader Zahl wird ein Minus übrig gelassen
                new_string="-"
                for i in range(Zaehler_minus,len(string)):
                    new_string=new_string+string[i]
                string=new_string
                Anfang=1
            else:                                                               # Bei gerader Anzahl wird kein Minus übrig gelassen
                new_string=""
                for i in range(Zaehler_minus,len(string)):
                    new_string=new_string+string[i]
                string=new_string
                Anfang=0
        # Überflüssige E's entfernen (nur letztes E bleibt bestehen)
        for i in range(0,len(string)-1):                                    # Löscht E's vor einem Punkt -> bei fehlendem Punkt ist das E jedoch erlaubt
            if string[i]==".":
                for j in range(0,i):
                    if string[j]=="E":
                        new_string=""
                        for k in range (0,len(string)):
                            if k!=j:
                                new_string=new_string+string[k]
                        string=new_string
        E_Liste=[]                                                          # Liste aller E's
        Letztes_E=0                                                         # Nennt die Position des letzten E's und somit die letzte Position
        E_Liste_2=[]                                                        # Liste aller E's außer dem Letzten
        for i in range(0,len(string)):                                      # Löscht alle E's bis auf das letzte E
            if string[i]=="E":
                Letztes_E=i
                E_Liste.append(i)
        for i in range (0,len(E_Liste)):                                    # Entfernt den Letzten Wert der E-Liste
            if E_Liste[i]!=Letztes_E:
                E_Liste_2.append(E_Liste[i])
        new_string=""
        for i in range(0,len(string)):
            x=0
            for j in range(0,len(E_Liste_2)):
                if E_Liste_2[j]==i:
                    x=1
            if x==0:
                new_string=new_string+string[i]
        string=new_string
        Liste_minus=[]                                                      # Liste mit Minus zwischen den Ziffern und dem E
        for i in range(0,len(string)):                                      # Entfernen von Minus zwischen den Ziffern und dem E
            try:
                if i>=Anfang and i<=Letztes_E:
                    if string[i]=="-":
                        Liste_minus.append(i)
            except:
                pass
        new_string=""
        for i in range (0,len(string)):
            x=0
            for j in range (0,len(Liste_minus)):
                if i==Liste_minus[j]:
                    x=1
            if x==0:
                new_string=new_string+string[i]
        string=new_string
        Letztes_E=0
        for i in range(0,len(string)):                                      # Sucht das letzte E
            if string[i]=="E":
                Letztes_E=i
        Positionszaehler=0                                                  # Zählt die Positionen hinter dem E
        # Überflüssige Minusse Entfernen (max. 1 bleibt stehen
        Minus_zaehler=0                                                     # Zählt die Minuszeichen hinter dem E bis zum nächsten Buchstabe
        for i in range(0,len(string)):                                      # Zählt die Minuszeichen hinter dem E bis zum nächsten Buchstabe
            if i>Letztes_E:
                if Minus_zaehler==Positionszaehler and Position!=len(string)-1:
                    if string[i]=="-":
                        Minus_zaehler=Minus_zaehler+1
                    Positionszaehler=Positionszaehler+1
                else:
                    break
            new_string=""
            x=0
        for i in range(0,len(string)):                                      # Löscht überflüssige Minuszeichen
            if i<=Letztes_E:
               new_string=new_string+string[i]
            else:
                if Minus_zaehler % 2 == 1 and x==0:
                    new_string=new_string+"-"
                    x=1
                elif string[i]!="-":
                    new_string=new_string+string[i]
        string=new_string
        # E's Sonderfälle
        if Letztes_E==len(string)-1 and string[len(string)-1]=="E":                                        # Behandelt Sonderfälle (kein Buchstabe vor dem E und keiner dahinter)
            string=string+"1"
        if len(string)>0:
            if Letztes_E==0 and string[0]=="E":
                new_string="1"+string
                string=new_string
        # Nullen am Anfang entfernen oder hinzufügen
        Zaehler=0                                                           # beendet die Suche nach einer Zahl
        Zahl=0                                                            # 1 wenn bis zum Punkt keine Zahl außer null vorkam
        new_string=""
        Zahlen_ohne_null=("1","2","3","4","5","6","7","8","9")
        for i in range (0,len(string)):
            if string[i]=="-" and Zaehler==0:
                new_string=new_string+"-"
            elif string[i] in Zahlen_ohne_null and Zaehler==0 and Zahl==0:
                new_string=new_string+string[i]
                Zaehler=1
            elif Zaehler==0 and Zahl==0:
                if string[i]==".":
                    new_string=new_string+"0."
                    Zahl=1
                elif string[i]=="E":
                    new_string=new_string+"1E"
                    Zaehler=1
                elif i==len(string)-1 and string[i]=="0":
                    new_string=new_string+"1"
                elif i==len(string)-1 and string[i]==".":
                    new_String==new_string+".1"
            elif Zaehler==0 and Zahl==1:
                if string[i] in Zahlen_ohne_null:
                    new_string=new_string+string[i]
                    Zaehler=1
                elif string[i]=="0" and not i==len(string)-1:
                    new_string=new_string+string[i]
                elif string[i]=="E":
                    new_string=new_string+"1E"
                    Zaehler=1
                elif i==len(string)-1 and string[i]=="0":
                    new_string=new_string+"1"
                elif i==len(string)-1 and string[i]==".":
                    new_String==new_string+".1"
            elif Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        # Nullen hinter einem E entfernen
        Zaehler=0                                                           # beendet die Suche nach einer Zahl
        E_Zaehler=0                                                         # beendet die Suche nach einemE
        new_string=""
        Zahlen_ohne_null=("1","2","3","4","5","6","7","8","9")
        for i in range (0,len(string)):
            if E_Zaehler==0:
                new_string=new_string+string[i]
                if string[i]=="E":
                    E_Zaehler=1
            elif E_Zaehler==1:
                if string[i]=="-" and i!=len(string)-1:
                    new_string=new_string+"-"
                elif Zaehler==0 and string[i] not in Zahlen_ohne_null and i!=len(string)-1:
                    pass
                elif Zaehler==1 and string[i] not in Zahlen_ohne_null and i!=len(string)-1:
                    new_string=new_string+string[i]
                elif string[i] in Zahlen_ohne_null and i!=len(string)-1:
                    new_string=new_string+string[i]
                    Zaehler=1
                elif i==len(string)-1:
                    if Zaehler==0 and string[i]=="0":
                        new_string=new_string+"1"
                    elif Zaehler==0 and string[i] in Zahlen_ohne_null:
                        new_string=new_string+string[i]
                    elif Zaehler==1 and string[i]=="0":
                        new_string=new_string+"0"
                    elif Zaehler==1 and string[i] in Zahlen_ohne_null:
                        new_string=new_string+string[i]
                    elif string[i]=="-":
                        new_string==new_string+"-1"
        string=new_string
        # Kommas
        for i in range(0,len(string)):                                      # Setzt Kommas
            if string[i]=="." or string[i]=="E":
                Zaehler=i                                                   # Zaehlt zahlen bis zu einem Punkt oder E
                break
            elif i==len(string)-1:
                Zaehler=i+1
        Finder=[]                                                           # Findet heraus welche Zahlen ein Komma bekommen sollen
        if len(string)>0:
            if string[0]=="-":
                Sucher=(Zaehler-1) % 3                                      # Wie viele Ziffern vor dem ersten Komma
                for i in range (0,Zaehler):
                    if i>=Sucher:
                        if (i-(Sucher+1)) % 3 == 0 and i!=1:
                            Finder.append(i)
            else:
                Sucher=(Zaehler-1) % 3                                      # Wie viele Ziffern vor dem ersten Komma
                for i in range (0,Zaehler):
                    if i>=Sucher:
                        if (i-(Sucher-1)) % 3 == 0 and i!=1:
                            Finder.append(i-2)
            new_string=""
            for j in range(0,len(string)):
                x=0
                for k in range(0,len(Finder)):
                    if j==Finder[k]:
                        x=1
                if x==1:
                    if string[0]=="-":
                        new_string=new_string+","+string[j]
                    else:
                        new_string=new_string+string[j]+","
                else:
                    new_string=new_string+string[j]
        string=new_string
        # Leere Zeile etc.
        if len(string)==0:                                                  # Fügt leerem String eine 1 hinzu
            string="1"
        elif len(string)==1:                                                # Fügt bei kurzem String Zeichen hinzu
            if string[0]=="0":
                string="1"
            elif string[0]==".":
                string="0.1"
            elif string[0]=="-":
                string="-1"
        #print ("Verifizierter String:"+string)                             # Zeigt bearbeiteten String an, deaktivieren bei vollendetem Skript!
        return string

    def Verifizieren_ohne_Null_ohne_Minus_Ganzzahl(stringvar):
        Anfang=0
        string=""
        string=string+str(stringvar)
        # String Zeichen Bereinigen
        zahlen_buchstaben = ("0","1","2","3","4","5","6","7","8","9","E","e")   # Eine Liste von Buchstaben die in den Zahlenentries verwendet werden dürfen.
        new_string=""
        for i in range(0,len(string)):                                      # Sortiert unerwünschte Zeichen aus
            Vorhanden_Zaehler=0
            for j in range(0,12):
                if string[i]==zahlen_buchstaben[j]:
                    Vorhanden_Zaehler=1
            if Vorhanden_Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        new_string=""
        for i in range (0,len(string)):                                     # Formt kleines e zu großem E um
            if string[i]=="e":
                new_string=new_string+"E"
            else:
                new_string=new_string+string[i]
        string=new_string
        # Überflüssige Punkte entfernen (nur letzter bleibt bestehen)
        Zaehler_P=0                                                         # Zaehlt Punkte
        for i in range(0,len(string)):                                      # Sucht nach E's -> nicht mehr als eines erwünscht, und das muss sich nach einem Punkt befinden oder es darf sich kein Punkt im Entry befinden
            if string[i]==".":
                Zaehler_P=Zaehler_P+1
        if Zaehler_P>1:                                                     # Löscht überflüssige Punkte
            x=1
            a=0
            new_string=""
            while x<Zaehler_P:
                if a<len(string):
                    if string[a]!=".":
                        new_string=new_string+string[a]
                        a=a+1
                    else:
                        x=x+1
                        a=a+1
            while a<len(string):
                new_string=new_string+string[a]
                a=a+1
            string=new_string
            Zaehler_P=1
        # Überflüssige Minuszeichen entfernen
        Zaehler_minus=0                                                     # Zaehlt Minuszeichen des Anfangs
        Position=0                                                          # Position des Zeigers
        if len(string)>1:
            while Position==Zaehler_minus and Position!=len(string)-1:          # Löscht überflüssige Minuszeichen am Anfang
                if string[Position]=="-":
                    Zaehler_minus=Zaehler_minus+1
                Position=Position+1
            Anfang=0                                                            # Speichert die Anfangsposition der Ziffern
            if Zaehler_minus % 2 ==1:                                           # Bei ungerader Zahl wird ein Minus übrig gelassen
                new_string="-"
                for i in range(Zaehler_minus,len(string)):
                    new_string=new_string+string[i]
                string=new_string
                Anfang=1
            else:                                                               # Bei gerader Anzahl wird kein Minus übrig gelassen
                new_string=""
                for i in range(Zaehler_minus,len(string)):
                    new_string=new_string+string[i]
                string=new_string
                Anfang=0
        else:
            Anfang=0
        # Überflüssige E's entfernen (nur letztes E bleibt bestehen)
        for i in range(0,len(string)-1):                                    # Löscht E's vor einem Punkt -> bei fehlendem Punkt ist das E jedoch erlaubt
            if string[i]==".":
                for j in range(0,i):
                    if string[j]=="E":
                        new_string=""
                        for k in range (0,len(string)):
                            if k!=j:
                                new_string=new_string+string[k]
                        string=new_string
        E_Liste=[]                                                          # Liste aller E's
        Letztes_E=0                                                         # Nennt die Position des letzten E's und somit die letzte Position
        E_Liste_2=[]                                                        # Liste aller E's außer dem Letzten
        for i in range(0,len(string)):                                      # Löscht alle E's bis auf das letzte E
            if string[i]=="E":
                Letztes_E=i
                E_Liste.append(i)
        for i in range (0,len(E_Liste)):                                    # Entfernt den Letzten Wert der E-Liste
            if E_Liste[i]!=Letztes_E:
                E_Liste_2.append(E_Liste[i])
        new_string=""
        for i in range(0,len(string)):
            x=0
            for j in range(0,len(E_Liste_2)):
                if E_Liste_2[j]==i:
                    x=1
            if x==0:
                new_string=new_string+string[i]
        string=new_string
        Liste_minus=[]                                                      # Liste mit Minus zwischen den Ziffern und dem E
        for i in range(0,len(string)):                                      # Entfernen von Minus zwischen den Ziffern und dem E
            if i>=Anfang and i<=Letztes_E:
                if string[i]=="-":
                    Liste_minus.append(i)
        new_string=""
        for i in range (0,len(string)):
            x=0
            for j in range (0,len(Liste_minus)):
                if i==Liste_minus[j]:
                    x=1
            if x==0:
                new_string=new_string+string[i]
        string=new_string
        Letztes_E=0
        for i in range(0,len(string)):                                      # Sucht das letzte E
            if string[i]=="E":
                Letztes_E=i
        Positionszaehler=0                                                  # Zählt die Positionen hinter dem E
        # Überflüssige Minusse Entfernen (max. 1 bleibt stehen
        Minus_zaehler=0                                                     # Zählt die Minuszeichen hinter dem E bis zum nächsten Buchstabe
        for i in range(0,len(string)):                                      # Zählt die Minuszeichen hinter dem E bis zum nächsten Buchstabe
            if i>Letztes_E:
                if Minus_zaehler==Positionszaehler and Position!=len(string)-1:
                    if string[i]=="-":
                        Minus_zaehler=Minus_zaehler+1
                    Positionszaehler=Positionszaehler+1
                else:
                    break
            new_string=""
            x=0
        for i in range(0,len(string)):                                      # Löscht überflüssige Minuszeichen
            if i<=Letztes_E:
               new_string=new_string+string[i]
            else:
                if Minus_zaehler % 2 == 1 and x==0:
                    new_string=new_string+"-"
                    x=1
                elif string[i]!="-":
                    new_string=new_string+string[i]
        string=new_string
        # E's Sonderfälle
        if Letztes_E==len(string)-1:                                        # Behandelt Sonderfälle (kein Buchstabe vor dem E und keiner dahinter)
            string=string+"1"
        if len(string)>0:
            if Letztes_E==0 and string[0]=="E":
                new_string="1"+string
                string=new_string
        # Nullen am Anfang entfernen oder hinzufügen
        Zaehler=0                                                           # beendet die Suche nach einer Zahl
        Zahl=0                                                            # 1 wenn bis zum Punkt keine Zahl außer null vorkam
        new_string=""
        Zahlen_ohne_null=("1","2","3","4","5","6","7","8","9")
        for i in range (0,len(string)):
            if string[i]=="-" and Zaehler==0:
                new_string=new_string+"-"
            elif string[i] in Zahlen_ohne_null and Zaehler==0 and Zahl==0:
                new_string=new_string+string[i]
                Zaehler=1
            elif Zaehler==0 and Zahl==0:
                if string[i]==".":
                    new_string=new_string+"0."
                    Zahl=1
                elif string[i]=="E":
                    new_string=new_string+"1E"
                    Zaehler=1
                elif i==len(string)-1 and string[i]=="0":
                    new_string=new_string+"1"
                elif i==len(string)-1 and string[i]==".":
                    new_String==new_string+".1"
            elif Zaehler==0 and Zahl==1:
                if string[i] in Zahlen_ohne_null:
                    new_string=new_string+string[i]
                    Zaehler=1
                elif string[i]=="0" and not i==len(string)-1:
                    new_string=new_string+string[i]
                elif string[i]=="E":
                    new_string=new_string+"1E"
                    Zaehler=1
                elif i==len(string)-1 and string[i]=="0":
                    new_string=new_string+"1"
                elif i==len(string)-1 and string[i]==".":
                    new_String==new_string+".1"
            elif Zaehler==1:
                new_string=new_string+string[i]
        string=new_string
        # Nullen hinter einem E entfernen
        Zaehler=0                                                           # beendet die Suche nach einer Zahl
        E_Zaehler=0                                                         # beendet die Suche nach einemE
        new_string=""
        Zahlen_ohne_null=("1","2","3","4","5","6","7","8","9")
        for i in range (0,len(string)):
            if E_Zaehler==0:
                new_string=new_string+string[i]
                if string[i]=="E":
                    E_Zaehler=1
            elif E_Zaehler==1:
                if string[i]=="-" and i!=len(string)-1:
                    new_string=new_string+"-"
                elif Zaehler==0 and string[i] not in Zahlen_ohne_null and i!=len(string)-1:
                    pass
                elif Zaehler==1 and string[i] not in Zahlen_ohne_null and i!=len(string)-1:
                    new_string=new_string+string[i]
                elif string[i] in Zahlen_ohne_null and i!=len(string)-1:
                    new_string=new_string+string[i]
                    Zaehler=1
                elif i==len(string)-1:
                    if Zaehler==0 and string[i]=="0":
                        new_string=new_string+"1"
                    elif Zaehler==0 and string[i] in Zahlen_ohne_null:
                        new_string=new_string+string[i]
                    elif Zaehler==1 and string[i]=="0":
                        new_string=new_string+"0"
                    elif Zaehler==1 and string[i] in Zahlen_ohne_null:
                        new_string=new_string+string[i]
                    elif string[i]=="-":
                        new_string==new_string+"-1"
        string=new_string
        # Kommas
        for i in range(0,len(string)):                                      # Setzt Kommas
            if string[i]=="." or string[i]=="E":
                Zaehler=i                                                   # Zaehlt zahlen bis zu einem Punkt oder E
                break
            elif i==len(string)-1:
                Zaehler=i+1
        Finder=[]                                                           # Findet heraus welche Zahlen ein Komma bekommen sollen
        if len(string)>0:
            if string[0]=="-":
                Sucher=(Zaehler-1) % 3                                      # Wie viele Ziffern vor dem ersten Komma
                for i in range (0,Zaehler):
                    if i>=Sucher:
                        if (i-(Sucher+1)) % 3 == 0 and i!=1:
                            Finder.append(i)
            else:
                Sucher=(Zaehler-1) % 3                                      # Wie viele Ziffern vor dem ersten Komma
                for i in range (0,Zaehler):
                    if i>=Sucher:
                        if (i-(Sucher-1)) % 3 == 0 and i!=1:
                            Finder.append(i-2)
            new_string=""
            for j in range(0,len(string)):
                x=0
                for k in range(0,len(Finder)):
                    if j==Finder[k]:
                        x=1
                if x==1:
                    if string[0]=="-":
                        new_string=new_string+","+string[j]
                    else:
                        new_string=new_string+string[j]+","
                else:
                    new_string=new_string+string[j]
        string=new_string
        # Leere Zeile etc.
        if len(string)==0:                                                  # Fügt leerem String eine 1 hinzu
            string="1"
        elif len(string)==1:                                                # Fügt bei kurzem String Zeichen hinzu
            if string[0]=="0":
                string="1"
            elif string[0]==".":
                string="0.1"
            elif string[0]=="-":
                string="-1"
        #print ("Verifizierter String:"+string)                             # Zeigt bearbeiteten String an, deaktivieren bei vollendetem Skript!
        return string

    def Namen_Verifizeren(Name,Namen_Body):                                               # a=0 wenn der string leer ist, 1, wenn der name bereits vorkommt und 2 wenn er ein unikat ist
        a=0
        if len(Name)==0:
            a=0
            return(a)
        elif len(Name)>0:
            for i in range(0,len(Namen_Body)):
                b=0
                if len(Name)==len(Namen_Body[i]):
                    for j in range(0,len(Name)):
                        if Name[j]==Namen_Body[i][j]:
                            b=b+1
                    if b==len(Name):
                        a=1
                        return(a)
            if a==0:
                a=2
                return(a)

    def Namen_Verifizeren_2(Name,Namen_Body, name_3):                                               # a=0 wenn der string leer ist, 1, wenn der name bereits vorkommt und 2 wenn er ein unikat ist
        a=0
        if len(Name)==0:
            a=0
            return(a)
        elif len(Name)>0:
            for i in range(0,len(Namen_Body)):
                b=0
                if len(Name)==len(Namen_Body[i]):
                    for j in range(0,len(Name)):
                        if Name[j]==Namen_Body[i][j]:
                            b=b+1
                    if b==len(Name):
                        if name_3!=Name[j]:
                            a=1
                            return(a)
                        else:
                            a=0
                            return(a)
            if a==0:
                a=2
                return(a)