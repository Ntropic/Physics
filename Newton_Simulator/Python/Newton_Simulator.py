# -*- coding: latin-1 -*-


#   Name:       Newton_Simulator.py
#   Author:     Michael Schilling
#   Edited:     19.08.2010 - 20.12.2010
#   Version:    1.2.2

from tkinter import*

from String_Number import*

class Newton_Simulator:

    def __init__ (self):

#-------------------------------------------------------------------
    # Variabeln für das Öffnen und Speichern von Dateien:

        self.filename_old       = ""
        self.filename_new       = ""

        self.datei_opened       = 0                                             # Wenn datei_opened = 1 ist, soll der Pfad der geöffneten Datei angezeigt werden, ist datei_opened = 0 wird der Pfad nicht angezeigt, dies ist der Fall falls eine Datei noch keinen Speicherort hat!

#-------------------------------------------------------------------
    # Variabeln der Einstellungen:

        self.Gravitationskonstante  = 6.67428E-11

        self.Berechnungsart     = 'N'                                             # self.Berechnungsart = J -> Relativistische Berechnung, self.Berechnungsart = N -> Rein Newtonsche Berechnung

        self.Lichtgeschwindigkeit   = 299792458

        self.Iterationsanzahl   = 10000
        self.Iterationsintervall= 1800                                         # in Sekunden
        self.Speicherintervall  = 10

#-------------------------------------------------------------------
    # Listen:

        self.Name               = []

        self.Name_Body          = ["Sonne", "Erde", "Mond"]                     # Namen der Objekte (Bodies(z.B. Sonne Erde Mond))

        self.Typ_Body           = ["Stern", "Planet", "Mond"]                   # Typ des Objekts (z.B. Sonne Planet Mond)

        self.Zugehoerigkeit_Body= ['','Sonne','Erde']                                  # Zum wievielten Element der Liste das Objekt ein Satellit ist

        self.Radius_Anteil_Body = []

        self.Masse_Body         = [[1.989E30],[5.974E24],[7.349E22]]            # Massen der Objekte in Kg (Bodies(z.B. Sonne Erde Mond))

        self.Radius_Body        = [[1.3914E9],[6.37E6],[1.738E6]]               # Radius der Objekte in m (Bodies(z.B. Sonne Erde Mond))

        self.VX                 = [[0.0],[0.0],[0.0]]                           # Geschwindigkeit der Objekte X in m/s (Bodies(z.B. Sonne Erde Mond))

        self.VY                 = [[0.0],[29.78E3],[30.803E3]]                  #  Geschwindigkeit  der Objekte Y in m/s (Bodies(z.B. Sonne Erde Mond))

        self.VZ                 = [[0.0],[0.0],[0.0]]                           # Geschwindigkeit  der Objekte Z in m/s (Bodies(z.B. Sonne Erde Mond))

        self.X                  = [[0.0],[1.496E11],[1.499844E11]]              # Position der Objekte X in m (Bodies(z.B. Sonne Erde Mond))

        self.Y                  = [[0.0],[0.0],[0.0]]                           # Position der Objekte Y in m (Bodies(z.B. Sonne Erde Mond))

        self.Z                  = [[0.0],[0.0],[0.0]]                           # Position der Objekte Z in m (Bodies(z.B. Sonne Erde Mond))

        self.Color              = ['#ffff00', '#464646', '#f1ae57']             # Farbe der Objekte in Hex nach der in Randomcolor.Randomcolor() beschriebenen Form

        self.MinX =0
        self.MaxX =0
        self.MinY =0
        self.MaxY =0
        self.MinZ =0
        self.MaxZ =0

#-------------------------------------------------------------------

    def Suche_parallel_Childs (self,id):
        # Sucht nach name der id und seinen childs:
        name=self.Name_Body[id]
        n=1
        for i in range(0,len(self.Name_Body)):
            if self.Zugehoerigkeit_Body[i]==name:
                n=n+1
        # nummer wird buchstabe zugeordnet:
        if n<=26:
            return(str(chr(64+n)))
        elif n<255:
            string=""
            a = n
            string_2=str(hex(a)[2:])
            if len(string_2)==1:
                string = string+string_2+"0"
            elif len(string_2)==0:
                string = string+"00"
            else:
                string = string +string_2
            return (string)
        else:
            return ("")

    def hole_GBLIIS(self,Gravitationskonstante,Berechnungsart,Lichtgeschwindigkeit,Iterationsanzahl,Iterationsintervall,Speicherintervall,jap):
        self.Gravitationskonstante=Gravitationskonstante
        self.Berechnungsart=str(Berechnungsart)
        self.Lichtgeschwindigkeit=Lichtgeschwindigkeit
        self.Iterationsanzahl=int(Iterationsanzahl)
        self.Iterationsintervall=int(Iterationsintervall)
        self.Speicherintervall=int(Speicherintervall)
        if jap==1:
            if self.Berechnungsart=='N':
                print('Berechnung erfolgt, nichtrelativistisch mit der Gravitationskonstante: '+str(Gravitationskonstante)+".")
            else:
                print('Berechnung erfolgt,  relativistisch mit der Lichtgeschwindigkeit: '+str(self.Lichtgeschwindigkeit)+' und der Gravitationskonstante: '+str(Gravitationskonstante)+".")
            print('Dabei werden '+str(self.Iterationsanzahl)+' Iterationsschritte berechnet, im Intervall von '+str(self.Iterationsintervall)+".")
            print('Jeder '+str(self.Speicherintervall)+'. Wert wird gespeichert.')

    def Radius_Anteil(self,Groesse_1,Groesse_2,rad):
        self.Radius_Anteil_Body=[]
        # Suche nach dem kleinsten und Groessten Objekt:
        minR=0
        maxR=0
        diffG=0
        diffR=0
        for i in range(0,len(self.Name_Body)):
            if self.Radius_Body[i][0]>maxR:
                maxR=self.Radius_Body[i][0]
            elif self.Radius_Body[i][0]<minR:
                minR=self.Radius_Body[i][0]
        if rad>maxR:
                maxR=rad
        elif rad<minR:
                minR=rad
        if Groesse_1>Groesse_2:
            maxG=Groesse_1
            minG=Groesse_2
        elif Groesse_1<Groesse_2:
            maxG=Groesse_2
            minG=Groesse_1
        elif Groesse_2==Groesse_1:
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(Groesse_1)
        if minR==maxR and len(self.Radius_Anteil_Body)==0:
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(Groesse_1)
        if len(self.Radius_Anteil_Body)==0:
            # Nun wird die Differenz der beiden ermittelt:
            diffR=maxR-minR
            diffG=maxG-minG
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(minG+diffG*(self.Radius_Body[i][0]-minR)/diffR)
        # Die letzten drei Werte der Liste sind diffR/diffG und n, n ist der R Achsenabschnitt wenn man G und R auf einem Graphen aufzeichnet, so kann man ein Steigungsdreieck bilden
        if diffG!=0:
            self.Radius_Anteil_Body.append(diffR/diffG)
            n= minG
            self.Radius_Anteil_Body.append(n)
        else:
            self.Radius_Anteil_Body.append(0)
            n= Groesse_2
            self.Radius_Anteil_Body.append(n)
        return self.Radius_Anteil_Body

    def Entfernung_Anteil_x(self,Groesse_1,Groesse_2,rad):
        self.Radius_Anteil_Body=[]
        # Suche nach dem kleinsten und Groessten Objekt:
        diffG=0
        diffA=0
        minA=0          # Am fernsten und mit Kleinstem X
        maxA=0          # Am nächsten und mit Größtem X
        for i in range(0,len(self.Name_Body)):
            if self.X[i][0]>maxA:
                maxA=self.X[i][0]
            elif self.X[i][0]<minA:
                minA=self.X[i][0]
        if rad>maxA:
                maxA=rad
        elif rad<minA:
                minA=rad
        if Groesse_1>Groesse_2:
            maxG=Groesse_1
            minG=Groesse_2
        elif Groesse_1<Groesse_2:
            maxG=Groesse_2
            minG=Groesse_1
        elif Groesse_2==Groesse_1:
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(Groesse_1)
        if minA==maxA and len(self.Radius_Anteil_Body)==0:
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(Groesse_1)
        if len(self.Radius_Anteil_Body)==0:
            # Nun wird die Differenz der beiden ermittelt:
            diffA=maxA-minA
            diffG=maxG-minG
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(minG+diffG*(self.X[i][0]-minA)/diffA)
        # Die letzten drei Werte der Liste sind diffA/diffG und n, n ist der R Achsenabschnitt wenn man G und A auf einem Graphen aufzeichnet, so kann man ein Steigungsdreieck bilden
        if diffG!=0:
            self.Radius_Anteil_Body.append(diffG/diffA)
            n= minG
            self.Radius_Anteil_Body.append(n)
        else:
            self.Radius_Anteil_Body.append(0)
            n= Groesse_2
            self.Radius_Anteil_Body.append(n)
        return self.Radius_Anteil_Body

    def Entfernung_Anteil_y(self,Groesse_1,Groesse_2,rad):
        self.Radius_Anteil_Body=[]
        diffG=0
        diffA=0
        # Suche nach dem kleinsten und Groessten Objekt:
        minA=0          # Am fernsten und mit Kleinstem Y
        maxA=0          # Am nächsten und mit Größtem Y
        for i in range(0,len(self.Name_Body)):
            if self.Y[i][0]>maxA:
                maxA=self.Y[i][0]
            elif self.Y[i][0]<minA:
                minA=self.Y[i][0]
        if rad>maxA:
                maxA=rad
        elif rad<minA:
                minA=rad
        if Groesse_1>Groesse_2:
            maxG=Groesse_1
            minG=Groesse_2
        elif Groesse_1<Groesse_2:
            maxG=Groesse_2
            minG=Groesse_1
        elif Groesse_2==Groesse_1:
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(Groesse_1)
        if minA==maxA and len(self.Radius_Anteil_Body)==0:
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(Groesse_1)
        if len(self.Radius_Anteil_Body)==0:
            # Nun wird die Differenz der beiden ermittelt:
            diffA=maxA-minA
            diffG=maxG-minG
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(minG+diffG*(self.Y[i][0]-minA)/diffA)
        # Die letzten drei Werte der Liste sind diffA/diffG und n, n ist der R Achsenabschnitt wenn man G und A auf einem Graphen aufzeichnet, so kann man ein Steigungsdreieck bilden
        if diffG!=0:
            self.Radius_Anteil_Body.append(diffG/diffA)
            n= minG
            self.Radius_Anteil_Body.append(n)
        else:
            self.Radius_Anteil_Body.append(0)
            n= Groesse_2
            self.Radius_Anteil_Body.append(n)
        return self.Radius_Anteil_Body

    def Entfernung_Anteil_z(self,Groesse_1,Groesse_2,rad):
        self.Radius_Anteil_Body=[]
        # Suche nach dem kleinsten und Groessten Objekt:
        minA=0          # Am fernsten und mit Kleinstem X
        maxA=0          # Am nächsten und mit Größtem X
        diffG=0
        diffA=0
        for i in range(0,len(self.Name_Body)):
            if self.Z[i][0]>maxA:
                maxA=self.Z[i][0]
            elif self.Z[i][0]<minA:
                minA=self.Z[i][0]
        if rad>maxA:
                maxA=rad
        elif rad<minA:
                minA=rad
        if Groesse_1>Groesse_2:
            maxG=Groesse_1
            minG=Groesse_2
        elif Groesse_1<Groesse_2:
            maxG=Groesse_2
            minG=Groesse_1
        elif Groesse_2==Groesse_1:
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(Groesse_1)
        if minA==maxA and len(self.Radius_Anteil_Body)==0:
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(Groesse_1)
        if len(self.Radius_Anteil_Body)==0:
            # Nun wird die Differenz der beiden ermittelt:
            diffA=maxA-minA
            diffG=maxG-minG
            for i in range(0,len(self.Name_Body)):
                self.Radius_Anteil_Body.append(minG+diffG*(self.Z[i][0]-minA)/diffA)
        # Die letzten drei Werte der Liste sind diffA/diffG und n, n ist der R Achsenabschnitt wenn man G und A auf einem Graphen aufzeichnet, so kann man ein Steigungsdreieck bilden
        if diffG!=0:
            self.Radius_Anteil_Body.append(diffG/diffA)
            n= minG
            self.Radius_Anteil_Body.append(n)
        else:
            self.Radius_Anteil_Body.append(0)
            n= Groesse_2
            self.Radius_Anteil_Body.append(n)
        return self.Radius_Anteil_Body

    def Objekt_Hinzufuegen(self,Name,Typ,Masse,Radius,X_Geschwindigkeit,Y_Geschwindigkeit,Z_Geschwindigkeit,X_Position,Y_Position,Z_Position,Color):
        Anhaengende_Liste=[]
        self.Name_Body.append(Name)
        self.Typ_Body.append(Typ)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Masse)
        self.Masse_Body.append(Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Radius)
        self.Radius_Body.append(Anhaengende_Liste)
        self.Zugehoerigkeit_Body.append('')
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(X_Geschwindigkeit)
        self.VX.append(Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Y_Geschwindigkeit)
        self.VY.append(Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Z_Geschwindigkeit)
        self.VZ.append(Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(X_Position)
        self.X.append(Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Y_Position)
        self.Y.append( Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Z_Position)
        self.Z.append(Anhaengende_Liste)
        self.Color.append(Color)

    def Objekt_Hinzufuegen_2(self,Name,Typ,Masse,Radius,X_Geschwindigkeit,Y_Geschwindigkeit,Z_Geschwindigkeit,X_Position,Y_Position,Z_Position,Color,Zugehoer):
        Anhaengende_Liste=[]
        self.Name_Body.append(Name)
        self.Typ_Body.append(Typ)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Masse)
        self.Masse_Body.append(Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Radius)
        self.Radius_Body.append(Anhaengende_Liste)
        self.Zugehoerigkeit_Body.append(Zugehoer)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(X_Geschwindigkeit)
        self.VX.append(Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Y_Geschwindigkeit)
        self.VY.append(Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Z_Geschwindigkeit)
        self.VZ.append(Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(X_Position)
        self.X.append(Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Y_Position)
        self.Y.append( Anhaengende_Liste)
        Anhaengende_Liste=[]
        Anhaengende_Liste.append(Z_Position)
        self.Z.append(Anhaengende_Liste)
        self.Color.append(Color)

    def Objekt_loeschen(self,namen):
        self.Name=[]
        for i in range(0,len(self.Name_Body)):
            if namen==self.Name_Body[i]:
                position=i
        self.Name.append(self.Name_Body[position])
        print(self.Name_Body[position])
        print('Objekt gelöscht, suche nach Childs...')
        # jetzt muss nach den 'descendants' (zu diesem objekt gehörenden elementen) gesucht werden:
        k=1
        while k==1:
            k=0
            i=0
            for i in range(0,len(self.Name_Body)):
                for j in range(0,len(self.Name)):
                    if self.Name[j]==self.Zugehoerigkeit_Body[i]:
                        # Wenn self.Name_Body[i] nicht in der Liste self.Name ist:
                        y=0
                        for l in range(0,len(self.Name)):
                            if self.Name_Body[i]==self.Name[l]:
                                y=1
                        if y==0:
                            self.Name.append(self.Name_Body[i])
                            k=1
        if len(self.Name)>1:
            print('Childs werden gelöscht:')
        # Jetzt werden die descendants gelöscht:
        for i in range(0,len(self.Name)):
            for j in range(0,len(self.Name_Body)):
                if self.Name[i]==self.Name_Body[j]:
                    del self.Name_Body[j]
                    del self.Typ_Body[j]
                    del self.Masse_Body[j]
                    del self.Radius_Body[j]
                    del self.Zugehoerigkeit_Body[j]
                    del self.VX[j]
                    del self.VY[j]
                    del self.VZ[j]
                    del self.X[j]
                    del self.Y[j]
                    del self.Z[j]
                    del self.Color[j]
                    print(str(self.Name[i])+' wurde gelöscht.')
                    break
        return(self.Name)

    def Listen_kuerzen(self):
        Masse_Body=[]
        VX=[]
        VY=[]
        VZ=[]
        X=[]
        Y=[]
        Z=[]
        for i in range(0,len(self.Name_Body)):
            Masse_Body.append(self.Masse_Body[i][0])
            VX.append(self.VX[i][0])
            VY.append(self.VY[i][0])
            VZ.append(self.VZ[i][0])
            X.append(self.X[i][0])
            Y.append(self.Y[i][0])
            Z.append(self.Z[i][0])
        self.Masse_Body=[]
        self.VX=[]
        self.VY=[]
        self.VZ=[]
        self.X=[]
        self.Y=[]
        self.Z=[]
        for i in range (0,len(self.Name_Body)):
            Anhaengende_Liste=[]
            Anhaengende_Liste.append(Masse_Body[i])
            self.Masse_Body.append(Anhaengende_Liste)
            Anhaengende_Liste=[]
            Anhaengende_Liste.append(VX[i])
            self.VX.append(Anhaengende_Liste)
            Anhaengende_Liste=[]
            Anhaengende_Liste.append(VY[i])
            self.VY.append(Anhaengende_Liste)
            Anhaengende_Liste=[]
            Anhaengende_Liste.append(VZ[i])
            self.VZ.append(Anhaengende_Liste)
            Anhaengende_Liste=[]
            Anhaengende_Liste.append(X[i])
            self.X.append(Anhaengende_Liste)
            Anhaengende_Liste=[]
            Anhaengende_Liste.append(Y[i])
            self.Y.append(Anhaengende_Liste)
            Anhaengende_Liste=[]
            Anhaengende_Liste.append(Z[i])
            self.Z.append(Anhaengende_Liste)

    def Maximalwertsuche(self):
        # Minima und Maxima für X:
        if len(self.X)>0:
            self.MinX=self.X[0][0]
            self.MaxX=self.X[0][0]
        for i in range(0,len(self.Name_Body)):
            for j in range(0,len(self.X[i])):
                if self.X[i][j]<self.MinX:
                    self.MinX=self.X[i][j]
                elif self.X[i][j]>self.MaxX:
                    self.MaxX=self.X[i][j]
        # Minima und Maxima für Y:
        if len(self.Y)>0:
            self.MinY=self.Y[0][0]
            self.MaxY=self.Y[0][0]
        for i in range(0,len(self.Name_Body)):
            for j in range(0,len(self.Y[i])):
                if self.Y[i][j]<self.MinY:
                    self.MinY=self.Y[i][j]
                elif self.Y[i][j]>self.MaxY:
                    self.MaxY=self.Y[i][j]
        # Minima und Maxima für Z:
        if len(self.Z)>0:
            self.MinZ=self.Z[0][0]
            self.MaxZ=self.Z[0][0]
        for i in range(0,len(self.Name_Body)):
            for j in range(0,len(self.Z[i])):
                if self.Z[i][j]<self.MinZ:
                    self.MinZ=self.Z[i][j]
                elif self.Z[i][j]>self.MaxZ:
                    self.MaxZ=self.Z[i][j]

#-------------------------------------------------------------------

    # Berechnung:
    def Berechnung (self):

        # Listen kürzen:

        self.Listen_kuerzen()

        # Benötigte Variabeln und Speichervariabeln(_2):

        Gravitationskonstante=self.Gravitationskonstante
        Berechnungsart=self.Berechnungsart                                      # J or N
        Lichtgeschwindigkeit=self.Lichtgeschwindigkeit
        Iterationsanzahl=self.Iterationsanzahl
        Iterationsintervall=self.Iterationsintervall
        Speicherintervall=self.Speicherintervall
        Name=self.Name_Body
        Typ=self.Typ_Body
        Masse=self.Masse_Body
        Masse_2=Masse
        Radius=self.Radius_Body
        Radius_2=Radius
        vx=[]
        vy=[]
        vz=[]
        x=[]
        y=[]
        z=[]
        # Erstellt lokale Variabeln:
        for i in range(0,len(Name)):
            vx.append(self.VX[i][0])
            vy.append(self.VY[i][0])
            vz.append(self.VZ[i][0])
            x.append(self.X[i][0])
            y.append(self.Y[i][0])
            z.append(self.Z[i][0])
        vj=0                                                                    # Gesamtgeschwindigkeit für relativistische Betrachtung und Ermittlung der relativistischen Masse
        vk=0

        # Erstellt 4 leere Listen mit a's:
        ax=[]
        ay=[]
        az=[]
        a=[]
        for j in range(0,len(Name)):
            a.append(0.0)
            ax.append(0.0)
            ay.append(0.0)
            az.append(0.0)
        d_2=0.0
        dx=0.0
        dy=0.0
        dz=0.0
        s=0                                                                     # Speicherintervall

        if Berechnungsart=='N':                                                   # Newtonsche Berechnung:
            for i in range(0,Iterationsanzahl):
                s=s+1
                for j in range(0,len(Name)):
                    a[j]=0.0
                    ax[j]=0.0
                    ay[j]=0.0
                    az[j]=0.0
                for j in range(0,len(Name)-1):
                    k=j+1
                    while k<len(Name):
                        # Berechnung von dx dy und dz:
                        dx=x[j]-x[k]
                        dy=y[j]-y[k]
                        dz=z[j]-z[k]
                        # Berechnung des Abstands der beiden Objekte (j & k):
                        d_2=((dx)**2+(dy)**2+(dz)**2)**(0.5)
                        # Berechnung der Beschleunigung a:
                        if d_2>=Radius[k][0]+Radius[j][0]:
                            a[j]=Masse[k][0]*Gravitationskonstante/(d_2**2)
                            a[k]=Masse[j][0]*Gravitationskonstante/(d_2**2)
                            ax[j]=ax[j]-dx/d_2*a[j]
                            ay[j]=ay[j]-dy/d_2*a[j]
                            az[j]=az[j]-dz/d_2*a[j]
                            ax[k]=ax[k]+dx/d_2*a[k]
                            ay[k]=ay[k]+dy/d_2*a[k]
                            az[k]=az[k]+dz/d_2*a[k]
                        elif d_2<(Radius[k][0]+Radius[j][0]):
                            a[j]=Masse[k][0]*Gravitationskonstante/Radius[k][0]**2
                            a[k]=Masse[j][0]*Gravitationskonstante/Radius[j][0]**2
                            ax[j]=ax[j]-dx/Radius[k][0]*a[j]
                            ay[j]=ay[j]-dy/Radius[k][0]*a[j]
                            az[j]=az[j]-dz/Radius[k][0]*a[j]
                            ax[k]=ax[k]+dx/Radius[j][0]*a[k]
                            ay[k]=ay[k]+dy/Radius[j][0]*a[k]
                            az[k]=az[k]+dz/Radius[j][0]*a[k]
                            print("Kollision")
                        k=k+1
                for j in range(0,len(Name)):
                    # Berechnung der neuen Geschwindigkeiten vx vy vz:
                    vx[j]=ax[j]*Iterationsintervall+vx[j]
                    vy[j]=ay[j]*Iterationsintervall+vy[j]
                    vz[j]=az[j]*Iterationsintervall+vz[j]

                    # Berechnung der neuen Positionen (x,y,z):
                    x[j]=(x[j]+vx[j]*Iterationsintervall) #+0.5*ax[j]*Iterationsintervall**2
                    #print(str(Name[j])+"-x-:"+str(x[j]))
                    y[j]=(y[j]+vy[j]*Iterationsintervall) #+0.5*ay[j]*Iterationsintervall**2
                    #print(str(Name[j])+"-y-:"+str(y[j]))
                    z[j]=(z[j]+vz[j]*Iterationsintervall) #+0.5*az[j]*Iterationsintervall**2
                    #print(str(Name[j])+"-z-:"+str(z[j]))

                    if s==Speicherintervall:
                        # Berechnung der neuenGeschwindigkeiten vx vy vz:
                        self.VX[j].append(vx[j])
                        self.VY[j].append(vy[j])
                        self.VZ[j].append(vz[j])
                        # Berechnung der neuen Positionen (x,y,z):
                        self.X[j].append(x[j])
                        self.Y[j].append(y[j])
                        self.Z[j].append(z[j])
                if s==Speicherintervall:
                    s=0
        else:                                                 # Relativistische Berechnung
            for i in range(0,Iterationsanzahl):
                s=s+1
                for j in range(0,len(Name)):
                    a[j]=0.0
                    ax[j]=0.0
                    ay[j]=0.0
                    az[j]=0.0
                for j in range(0,len(Name)-1):
                    k=j+1
                    while k<len(Name):
                        # Berechnung von dx dy und dz:
                        dx=x[j]-x[k]
                        dy=y[j]-y[k]
                        dz=z[j]-z[k]
                        # Berechnung des Abstands der beiden Objekte (j & k):
                        d_2=((dx)**2+(dy)**2+(dz)**2)**(0.5)
                        #Berechnung der Gesamtgeschwindigkeit vj und vk zum Quadrat:
                        vj=(vx[j]**2+vy[j]**2+vz[j]**2)
                        vk=(vx[k]**2+vy[k]**2+vz[k]**2)
                        if vj**0.5>=Lichtgeschwindigkeit or vk**0.5>=Lichtgeschwindigkeit:
                            print('Eines der Objekte bewegt sich mit mehr als Lichtgeschwindigkeit!')
                        # Berechnung der Beschleunigung a:
                        if d_2>=Radius[k][0]+Radius[j][0]:
                            a[j]=Masse[k][0]/(1-vk/Lichtgeschwindigkeit**2)*Gravitationskonstante/d_2**2
                            a[k]=Masse[j][0]/(1-vj/Lichtgeschwindigkeit**2)*Gravitationskonstante/d_2**2
                            ax[j]=ax[j]-dx/d_2*a[j]
                            ay[j]=ay[j]-dy/d_2*a[j]
                            az[j]=az[j]-dz/d_2*a[j]
                            ax[k]=ax[k]+dx/d_2*a[k]
                            ay[k]=ay[k]+dy/d_2*a[k]
                            az[k]=az[k]+dz/d_2*a[k]
                        elif d_2<Radius[k][0]+Radius[j][0]:
                            a[j]=Masse[k][0]/(1-vk/Lichtgeschwindigkeit**2)*Gravitationskonstante/Radius[k][0]**2
                            a[k]=Masse[j][0]/(1-vj/Lichtgeschwindigkeit**2)*Gravitationskonstante/Radius[j][0]**2
                            ax[j]=ax[j]-dx/Radius[k][0]*a[j]
                            ay[j]=ay[j]-dy/Radius[k][0]*a[j]
                            az[j]=az[j]-dz/Radius[k][0]*a[j]
                            ax[k]=ax[k]+dx/Radius[j][0]*a[k]
                            ay[k]=ay[k]+dy/Radius[j][0]*a[k]
                            az[k]=az[k]+dz/Radius[j][0]*a[k]
                        k=k+1
                for j in range(0,len(Name)):
                    # Berechnung der neuen Geschwindigkeiten vx vy vz:
                    vx[j]=ax[j]*Iterationsintervall+vx[j]
                    vy[j]=ay[j]*Iterationsintervall+vy[j]
                    vz[j]=az[j]*Iterationsintervall+vz[j]
                    # Berechnung der neuen Positionen (x,y,z):
                    x[j]=(x[j]+vx[j]*Iterationsintervall)#+ax[j]*Iterationsintervall**2)
                    #print(str(Name[j])+"-x-:"+str(x[j]))
                    y[j]=(y[j]+vy[j]*Iterationsintervall)#+ay[j]*Iterationsintervall**2)
                    #print(str(Name[j])+"-y-:"+str(y[j]))
                    z[j]=(z[j]+vz[j]*Iterationsintervall)#+az[j]*Iterationsintervall**2)
                    #print(str(Name[j])+"-z-:"+str(z[j]))
                    if s==Speicherintervall:
                        # Berechnung der neuenGeschwindigkeiten vx vy vz:
                        self.VX[j].append(vx[j])
                        self.VY[j].append(vy[j])
                        self.VZ[j].append(vz[j])
                        # Berechnung der neuen Positionen (x,y,z):
                        self.X[j].append(x[j])
                        self.Y[j].append(y[j])
                        self.Z[j].append(z[j])
                if s==Speicherintervall:
                    s=0

#-------------------------------------------------------------------
    # Menübefehle:

        # Erstellen einer Datei:

    def new_file (self):
        self.datei_opened       = 0                                             # Wenn datei_opened = 1 ist, soll der Pfad der geöffneten Datei angezeigt werden, ist datei_opened = 0 wird der Pfad nicht angezeigt, dies ist der Fall falls eine Datei noch keinen Speicherort hat!
        self.Gravitationskonstante  = 6.67428E-11
        self.Berechnungsart     = 'N'                                             # self.Berechnungsart = J -> Relativistische Berechnung, self.Berechnungsart = N -> Rein Newtonsche Berechnung
        self.Lichtgeschwindigkeit   = 299792458
        self.Iterationsanzahl   = 10000
        self.Iterationsintervall= 1800
        self.Speicherintervall  = 10
        self.Name               = []
        self.Name_Body          = []
        self.Typ_Body           = []
        self.Zugehoerigkeit_Body= []
        self.Radius_Anteil_Body = []
        self.Masse_Body         = []
        self.Radius_Body        = []
        self.VX                 = []
        self.VY                 = []
        self.VZ                 = []
        self.X                  = []
        self.Y                  = []
        self.Z                  = []
        self.Color              = []



        # Öffnen einer Datei:

    def open_file (self, filename):
        self.filename_new=filename
        print ('opening '+str(self.filename_new)+'   ...')
        if not self.filename_old == self.filename_new:                          # Verifiziert, dass es sich nicht um eine bereits geöffnete Datei handelt um nicht unnötig eine DAtei ein zu lesen.
            #try:
                datei = open (self.filename_new, "r+")                             # Versucht es, die Datei filename_new zu öffnen und für das lesen bereit zu stellen
                k=datei.readline()    # liest eine Zeile aus!
                Grav, Berech, Licht, Itan, Itin, Spin, Anzahl = k.strip('\n').split('?')
                anzahl=int(String_Number.String_to_Number(str(Anzahl)))
                Name=[]
                Typ=[]
                Masse=[]
                Radius=[]
                X=[]
                Y=[]
                Z=[]
                VX=[]
                VY=[]
                VZ=[]
                Color=[]
                Zugehoer=[]
                anzahl_2=anzahl
                while anzahl>0:
                    k=datei.readline()
                    name, typ, mass, rad, x, y, z, vx, vy, vz, color, zuge = k.strip('\n').split('?')
                    anzahl=anzahl-1
                    Name.append(name)
                    Typ.append(typ)
                    Masse.append(mass)
                    Radius.append(rad)
                    X.append(x)
                    Y.append(y)
                    Z.append(z)
                    VX.append(vx)
                    VY.append(vy)
                    VZ.append(vz)
                    Color.append(color)
                    Zugehoer.append(zuge)
                self.datei_opened       = 1                                             # Wenn datei_opened = 1 ist, soll der Pfad der geöffneten Datei angezeigt werden, ist datei_opened = 0 wird der Pfad nicht angezeigt, dies ist der Fall falls eine Datei noch keinen Speicherort hat!
                self.Gravitationskonstante  =String_Number.String_to_Number(str(Grav))
                self.Berechnungsart     = str(Berech)                                             # self.Berechnungsart = J -> Relativistische Berechnung, self.Berechnungsart = N -> Rein Newtonsche Berechnung
                self.Lichtgeschwindigkeit   = String_Number.String_to_Number(str(Licht))
                self.Iterationsanzahl   = int(String_Number.String_to_Number(str(Itan)))
                self.Iterationsintervall= int(String_Number.String_to_Number(str(Itin)))
                self.Speicherintervall  = int(String_Number.String_to_Number(str(Spin)))

                self.Name_Body=[]
                self.Typ_Body=[]
                self.Zugehoerigkeit_Body=[]
                self.Masse_Body=[]
                self.Radius_Body=[]
                self.VX=[]
                self.VY=[]
                self.VZ=[]
                self.X=[]
                self.Y=[]
                self.Z=[]
                self.Color=[]
                for i in range(0,anzahl_2):
                    self.Name_Body.append(str(Name[i]))
                    self.Typ_Body.append(str(Typ[i]))
                    self.Zugehoerigkeit_Body.append(str(Zugehoer[i]))
                    self.Masse_Body.append([String_Number.String_to_Number(Masse[i])])
                    self.Radius_Body.append([String_Number.String_to_Number(Radius[i])])
                    self.VX.append([String_Number.String_to_Number(VX[i])])
                    self.VY.append([String_Number.String_to_Number(VY[i])])
                    self.VZ.append([String_Number.String_to_Number(VZ[i])])
                    self.X.append([String_Number.String_to_Number(X[i])])
                    self.Y.append([String_Number.String_to_Number(Y[i])])
                    self.Z.append([String_Number.String_to_Number(Z[i])])
                    self.Color.append(str(Color[i]))
                datei.close()
            #except:
            #    return(0)
            #    pass
        self.filename_old=filename
        self.filename_new=filename
        self.datei_opened = 1
        return(1)   # \t  -> TAB



    def save_file (self, filename):
        print ('saving '+str(filename)+'   ...')
        datei = open (filename, "w")
        # Zusammentragen eines string mit allen Elementen:
        # 1.Basisvariabeln, dann 2.Körper:
        try:
            # Allgemeine Variabeln:
            string=""
            string=string+String_Number.Number_to_String(self.Gravitationskonstante)
            string=string+"?"
            string=string+String_Number.Number_to_String(self.Berechnungsart)
            string=string+"?"
            string=string+String_Number.Number_to_String(self.Lichtgeschwindigkeit)
            string=string+"?"
            string=string+String_Number.Number_to_String(self.Iterationsanzahl)
            string=string+"?"
            string=string+String_Number.Number_to_String(self.Iterationsintervall)
            string=string+"?"
            string=string+String_Number.Number_to_String(self.Speicherintervall)
            string=string+"?"
            # Anzahl an Körpern:
            string=string+String_Number.Number_to_String(len(self.Name_Body))
            string=string+"\n"
            # Die Körper:
            for i in range(0,len(self.Name_Body)):
                string=string+str(self.Name_Body[i])
                string=string+"?"
                string=string+str(self.Typ_Body[i])
                string=string+"?"
                string=string+String_Number.Number_to_String(self.Masse_Body[i][0])
                string=string+"?"
                string=string+String_Number.Number_to_String(self.Radius_Body[i][0])
                string=string+"?"
                string=string+String_Number.Number_to_String(self.X[i][0])
                string=string+"?"
                string=string+String_Number.Number_to_String(self.Y[i][0])
                string=string+"?"
                string=string+String_Number.Number_to_String(self.Z[i][0])
                string=string+"?"
                string=string+String_Number.Number_to_String(self.VX[i][0])
                string=string+"?"
                string=string+String_Number.Number_to_String(self.VY[i][0])
                string=string+"?"
                string=string+String_Number.Number_to_String(self.VZ[i][0])
                string=string+"?"
                string=string+str(self.Color[i])
                string=string+"?"
                string=string+str(self.Zugehoerigkeit_Body[i])
                string=string+"\n"
            # Liste ist etzt fertig, auf gehts mitm speichern:
        except:
            return(0)
            pass
        datei.write(string)
        datei.close()
        self.filename_old=filename
        self.filename_new=filename
        self.datei_opened = 1
        return(1)   # \t  -> TAB

#-------------------------------------------------------------------

    def import_file(self,filename):
        pass