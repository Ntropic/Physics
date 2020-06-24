# -*- coding: latin-1 -*-


#   Name:       Newton_Simulator_Gui.py
#   Author:     Michael Schilling
#   Edited:     27.03.2010 - 20.12.2010
#   Version:    0.2.4

from unicodedata import*

from tkinter import*
from tkinter.ttk import *
import tkinter as tk
from tkinter.filedialog import*
import tkinter.colorchooser
from threading import Timer

from Newton_Simulator import *
from Verifizieren import *
from Namensgenerator import *
from Randomcolor import *
from String_Number import *
from Basic_Calculations import*

# from Objekt_erstellen import *

version             ="0.2.4"

Zuletzt_Geendert    ="20.12.2010"

class Main:

    def __init__ (self, root):

        self.Newton_Simulator=Newton_Simulator()

        #   Fenstername, Größe und Icon: (root)

        root.title("Newton Simulator   v."+version)
        root.geometry("1024x768")
        root.resizable(width = False, height = False)
        root.wm_iconbitmap('../Icon/Window Icon/Window Icon.ico')

#------------------------------------------------------------------

        # Variabeln:

        self.filename=StringVar()
        self.filename.set('')

        self.ID             =           ['Sonne','Erde','Mond']
        self.Name_13           =        ['Sonne','Erde','Mond']
        self.pos            =           2

            # Maximal- und Minimalwerte für die Cavans Darstellungen:

        self.minX                =           0
        self.maxX                =           0

        self.minY                =           0
        self.maxY                =           0

        self.minZ                =           0
        self.maxZ                =           0

            # Objekt erstellen (Canvas):

        self.Oe_Mpp              =           0
        self.Oe_Mpp_xy           =           0
        self.Oe_Mpp_yz           =           0
        self.Oe_Mpp_xz           =           0

        self.Oe_Mittelpunkt_x    =           0
        self.Oe_Mittelpunkt_y    =           0
        self.Oe_Mittelpunkt_z    =           0

        self.Oe_akt_X            =           0
        self.Oe_akt_Y            =           0
        self.Oe_akt_Z            =           0
        self.Oe_akt_Pos          =           0
        self.Oe_akt_movX         =           0
        self.Oe_akt_movY         =           0
        self.Oe_akt_movZ         =           0
        self.Oe_akt_Tem          =           0
        self.Oe=''

            # Satellit erstellen (Canvas):

        self.Se_Mpp              =           0
        self.Se_Mpp_xy           =           0
        self.Se_Mpp_yz           =           0
        self.Se_Mpp_xz           =           0

        self.Se_Mittelpunkt_x    =           0
        self.Se_Mittelpunkt_y    =           0
        self.Se_Mittelpunkt_z    =           0

        self.Se_akt_X            =           0
        self.Se_akt_Y            =           0
        self.Se_akt_Z            =           0
        self.Se_akt_Pos          =           0
        self.Se_akt_movX         =           0
        self.Se_akt_movY         =           0
        self.Se_akt_movZ         =           0
        self.Se_akt_Tem          =           0

        self.Se_position         =           0
        self.Se=''

            # Berechnung darstellen (Canvas):

        self.Bd_Mpp              =           0
        self.Bd_Mpp_xy           =           0
        self.Bd_Mpp_yz           =           0
        self.Bd_Mpp_xz           =           0

        self.Bd_Mittelpunkt_x    =           0
        self.Bd_Mittelpunkt_y    =           0
        self.Bd_Mittelpunkt_z    =           0

        self.Bd_akt_X            =           0
        self.Bd_akt_Y            =           0
        self.Bd_akt_Z            =           0
        self.Bd_akt_Pos          =           0
        self.Bd_akt_movX         =           0
        self.Bd_akt_movY         =           0
        self.Bd_akt_movZ         =           0
        self.Bd_akt_Tem          =           0

        self.Bd_position         =           0
        self.Bd_Speed               =1
        self.Bd_Kugeln              =1
        self.Linien                 =       0
        self.Bd=''

#-------------------------------------------------------------------

        #   Kommandos der Key Events: (Müssen vor den Key Events definiert werden, sonst: reference before assignment)

        def neu(event):

            self.neu()

        def open(event):

            self.open()

        def save(event):

            self.save()

        def save_as(event):

            self.save_as()

        def quit(event):

            root.quit

        def documentation(event):

            self.documentation()

        def about(event):

            self.about()

#-------------------------------------------------------------------

        #   Key Events: (Gebunden an das root Fenster)

        root.bind("<Control-n>",neu)
        root.bind("<Control-o>",open)
        root.bind("<Control-s>",save)
        root.bind("<Alt-s>",save_as)
        root.bind("<Alt-F4>",quit)

        #root.bind("<Control-d>",documentation)
        root.bind("<Control-f>",about)

#-------------------------------------------------------------------

        #   Die Menübar:

        menubar=Menu(root)

            #   1. Pulldown Menü: (Datei)

        dateimenu = Menu(menubar, tearoff=1)
        dateimenu.add_command(label="Neu", command=self.neu, accelerator="Ctrl+N")
        dateimenu.add_command(label="Öffnen", command=self.open, accelerator="Ctrl+O")
        dateimenu.add_separator()
        speichern_toggled=dateimenu.add_command(label="Speichern", command=self.save, accelerator="Ctrl+S", state=DISABLED)
        def toggle_save(*args):
            if self.filename.get()=="":
                dateimenu.entryconfig(4,state=DISABLED)
            else:
                dateimenu.entryconfig(4,state=NORMAL)
        self.filename.trace("w",toggle_save)
        dateimenu.add_command(label="Speichern unter", command=self.save_as, accelerator="Alt+S")

        dateimenu.add_separator()

        dateimenu.add_command(label="Schließen",command=root.quit, accelerator="Alt+F4")
        menubar.add_cascade(label="Datei", menu=dateimenu)

            #   2. Pulldown Menü: (Hilfe)

        hilfemenu = Menu(menubar)
        #hilfemenu.add_command(label="Dokumentation", command=self.documentation, accelerator="Ctrl+D")
        hilfemenu.add_command(label="Über Newton Simulator",command=self.about, accelerator="Ctrl+F")
        menubar.add_cascade(label="Über", menu=hilfemenu)

            #   Anzeigen der Menübar:

        root.config(menu=menubar)

#-----------------------------------------------------------------

        #   Das Notebook:

        notebook = ttk.Notebook(root, width=1012, height=714)
        

            #   1. Frame:

        frame_1 = Frame(root, width=1012, height=714)                           # Einstellungen

        label_1_frame_1 = Labelframe(frame_1, width=550, height=200, text='Berechnungsart')
        label_1_frame_1.place (x=10, y=10)

        Text_Gravitationskonstante_1_label_1_frame_1 = "Gravitationskonstante ("+chr(0x03B3)+"):"                               # Erzeugt einen Text mit einem Unicode Zeichen
        Gravitationskonstante_1_label_1_frame_1 = Label(label_1_frame_1, text=Text_Gravitationskonstante_1_label_1_frame_1)
        Gravitationskonstante_1_label_1_frame_1.place (x=10, y=10)

        self.Gravitationskonstante = StringVar()                                     # Muss nach dem Importieren in eine String umgewandelt werden! DO NOT FORGET!!! (float(x) if '.' in x else int(x)) -> Davor muss der String jedoch von den Kommas befreit werden!!!
        self.Gravitationskonstante.set ("6.67428E-11")
        Gravitationskonstante_2_label_1_frame_1 = Entry(label_1_frame_1, justify=RIGHT, textvariable = self.Gravitationskonstante, bd=2)
        Gravitationskonstante_2_label_1_frame_1.place (x=250, y=10)

        def Gravitationskonstante_Verifizieren(*args):
            Get_Gravitationskonstante = self.Gravitationskonstante.get()
            self.Gravitationskonstante.set(Verifizieren.Verifizieren(Get_Gravitationskonstante))
        self.Gravitationskonstante.trace("w", Gravitationskonstante_Verifizieren)

        Text_Gravitationskonstante_2_label_1_frame_1 = "[N m²/kg²]:"            # Erzeugt einen Text mit einem Unicode Zeichen
        Gravitationskonstante_2_label_1_frame_1 = Label(label_1_frame_1, text=Text_Gravitationskonstante_2_label_1_frame_1)
        Gravitationskonstante_2_label_1_frame_1.place (x=380, y=10)

        def Gravitationskonstante_Standard (*args):
            self.Gravitationskonstante.set("6.67428E-11")

        Gravitationskonstante_Button_Standard=Button(label_1_frame_1, text="Standard", command=Gravitationskonstante_Standard)
        Gravitationskonstante_Button_Standard.place (x=475, y=6)

        self.Berechnungsart = StringVar()
        self.Berechnungsart.set ("N")
        Einsteinsche_Relativitstheorie_label_1_frame_1 = Checkbutton(label_1_frame_1, text="Beachtung der Relativitätstheorie (Experimentell)", variable=self.Berechnungsart, onvalue="J", offvalue="N")
        Einsteinsche_Relativitstheorie_label_1_frame_1.place (x=10, y=40)

        def Relativitaetsrelevanz(*args):                                        # Aktiviert und Deaktiviert die Lichtgeschwindigkeitseingabe
            if self.Berechnungsart.get() == "N":
                Lichtgeschwindigkeit_2_label_1_frame_1.config(state=DISABLED)
                Lichtgeschwindigkeit_Button_Standard.config(state=DISABLED)
                Lichtgeschwindigkeit_3_label_1_frame_1.config(state=DISABLED)
                Lichtgeschwindigkeit_1_label_1_frame_1.config(state=DISABLED)
            else:
                Lichtgeschwindigkeit_2_label_1_frame_1.config(state=NORMAL)
                Lichtgeschwindigkeit_Button_Standard.config(state=NORMAL)
                Lichtgeschwindigkeit_3_label_1_frame_1.config(state=NORMAL)
                Lichtgeschwindigkeit_1_label_1_frame_1.config(state=NORMAL)
        self.Berechnungsart.trace("w", Relativitaetsrelevanz)

        Lichtgeschwindigkeit_1_label_1_frame_1 = Label(label_1_frame_1, text="Lichtgeschwindigkeit (c):")
        Lichtgeschwindigkeit_1_label_1_frame_1.place (x=10, y=70)
        Lichtgeschwindigkeit_1_label_1_frame_1.config(state=DISABLED)

        self.Lichtgeschwindigkeit = StringVar()                                      # Muss nach dem Importieren in eine String umgewandelt werden! DO NOT FORGET!!! (float(x) if '.' in x else int(x)) -> Davor muss der String jedoch von den Kommas befreit werden!!!
        self.Lichtgeschwindigkeit.set ("299,792,458")
        Lichtgeschwindigkeit_2_label_1_frame_1 = Entry(label_1_frame_1, justify=RIGHT, textvariable = self.Lichtgeschwindigkeit, bd=2)
        Lichtgeschwindigkeit_2_label_1_frame_1.place (x=250, y=70)
        Lichtgeschwindigkeit_2_label_1_frame_1.config(state=DISABLED)

        def Lichtgeschwindigkeit_Verifizieren(*args):
            Get_Lichtgeschwindigkeit = self.Lichtgeschwindigkeit.get()
            self.Lichtgeschwindigkeit.set(Verifizieren.Verifizieren(Get_Lichtgeschwindigkeit))
        self.Lichtgeschwindigkeit.trace("w", Lichtgeschwindigkeit_Verifizieren)

        Lichtgeschwindigkeit_3_label_1_frame_1 = Label(label_1_frame_1, text="[m/s]:")
        Lichtgeschwindigkeit_3_label_1_frame_1.place (x=380, y=70)
        Lichtgeschwindigkeit_3_label_1_frame_1.config(state=DISABLED)

        def Lichtgeschwindigkeit_Standard (*args):
            self.Lichtgeschwindigkeit.set("299,792,458")

        Lichtgeschwindigkeit_Button_Standard=Button(label_1_frame_1, text="Standard", command=Lichtgeschwindigkeit_Standard)
        Lichtgeschwindigkeit_Button_Standard.place (x=475, y=66)
        Lichtgeschwindigkeit_Button_Standard.config(state=DISABLED)

        #-----------------------------------------------------------------------

        label_2_frame_1 = Labelframe(frame_1, width=550, height=200, text='Berechnungszeit')
        label_2_frame_1.place (x=10, y=210)

        Iterationsanzahl_1_label_2_frame_1 = Label(label_2_frame_1, text="Iterationsanzahl:")
        Iterationsanzahl_1_label_2_frame_1.place (x=10, y=10)

        self.Iterationsanzahl = StringVar()                                          # Muss nach dem Importieren in eine String umgewandelt werden! DO NOT FORGET!!! (float(x) if '.' in x else int(x)) -> Davor muss der String jedoch von den Kommas befreit werden!!!
        self.Iterationsanzahl.set ("10,000")
        Iterationsanzahl_2_label_2_frame_1 = Entry(label_2_frame_1, justify=RIGHT, textvariable = self.Iterationsanzahl, bd=2)
        Iterationsanzahl_2_label_2_frame_1.place (x=250, y=10)

        def Iterationsanzahl_Verifizieren(*args):
            Get_Iterationsanzahl = self.Iterationsanzahl.get()
            self.Iterationsanzahl.set(Verifizieren.Verifizieren_ohne_Null_ohne_Minus_Ganzzahl(Get_Iterationsanzahl))
        self.Iterationsanzahl.trace("w", Iterationsanzahl_Verifizieren)

        def Iterationsanzahl_Standard (*args):
            self.Iterationsanzahl.set("10,000")

        Iterationsanzahl_Button_Standard=Button(label_2_frame_1, text="Standard", command=Iterationsanzahl_Standard)
        Iterationsanzahl_Button_Standard.place (x=475, y=6)

        Iterationsintervall_1_label_2_frame_1 = Label(label_2_frame_1, text="Iterationsintervall ("+chr(0x0394)+"t):")
        Iterationsintervall_1_label_2_frame_1.place (x=10, y=40)

        self.Iterationsintervall = StringVar()                                       # Muss nach dem Importieren in eine String umgewandelt werden! DO NOT FORGET!!! (float(x) if '.' in x else int(x)) -> Davor muss der String jedoch von den Kommas befreit werden!!!
        self.Iterationsintervall.set ("1,800")
        Iterationsintervall_2_label_2_frame_1 = Entry(label_2_frame_1, justify=RIGHT, textvariable = self.Iterationsintervall, bd=2)
        Iterationsintervall_2_label_2_frame_1.place (x=250, y=40)

        def Iterationsintervall_Verifizieren(*args):
            Get_Iterationsintervall = self.Iterationsintervall.get()
            self.Iterationsintervall.set(Verifizieren.Verifizieren(Get_Iterationsintervall))
        self.Iterationsintervall.trace("w", Iterationsintervall_Verifizieren)

        Iterationsintervall_3_label_1_frame_1 = Label(label_2_frame_1, text="[s]:")
        Iterationsintervall_3_label_1_frame_1.place (x=380, y=40)

        def Iterationsintervall_Standard (*args):
            self.Iterationsintervall.set("1,800")

        Iterationsintervall_Button_Standard=Button(label_2_frame_1, text="Standard", command=Iterationsintervall_Standard)
        Iterationsintervall_Button_Standard.place (x=475, y=36)

        Speicherintervall_1_label_2_frame_1 = Label(label_2_frame_1, text="Speicherintervall:")
        Speicherintervall_1_label_2_frame_1.place (x=10, y=70)

        self.Speicherintervall = StringVar()                                         # Muss nach dem Importieren in eine String umgewandelt werden! DO NOT FORGET!!! (float(x) if '.' in x else int(x)) -> Davor muss der String jedoch von den Kommas befreit werden!!!
        self.Speicherintervall.set ("10")
        Speicherintervall_2_label_2_frame_1 = Entry(label_2_frame_1, justify=RIGHT, textvariable = self.Speicherintervall, bd=2)
        Speicherintervall_2_label_2_frame_1.place (x=250, y=70)

        def Speicherintervall_Verifizieren(*args):
            Get_Speicherintervall = self.Speicherintervall.get()
            self.Speicherintervall.set(Verifizieren.Verifizieren_Ganzzahlen(Get_Speicherintervall))
        self.Speicherintervall.trace("w", Speicherintervall_Verifizieren)

        Speicherintervall_3_label_1_frame_1 = Label(label_2_frame_1, text="[Intervall(e)]:")
        Speicherintervall_3_label_1_frame_1.place (x=380, y=70)

        def Speicherintervall_Standard (*args):
            self.Speicherintervall.set("10")

        Speicherintervall_Button_Standard=Button(label_2_frame_1, text="Standard", command=Speicherintervall_Standard)
        Speicherintervall_Button_Standard.place (x=475, y=66)

            #   2. Frame:

        frame_2 = Frame(root, width=1012, height=714)                           # Körper

                # Buttons überhalb der Treeview:

        label_1_frame_2 = Labelframe(frame_2, width=995, height=75, text='Objekteigenschaften')
        label_1_frame_2.place (x=10, y=10)

        def Objekt_erstellen():
            Objekt_erstellen_1 = Toplevel(root, width=1024, height=768)
            Objekt_erstellen_1.title ("Objekt erstellen")
            Objekt_erstellen_1.resizable(width = False, height = False)
            Objekt_erstellen_1.wm_iconbitmap('../Icon/Window Icon/Window Icon.ico')
            Objekt_erstellen_1.transient(master=root)

                    #   Das Notebook:

            notebook = ttk.Notebook(Objekt_erstellen_1, width=1012, height=614)


            frame_11 = Frame(Objekt_erstellen_1, width=1012, height=714)

            frame_22 = Frame(Objekt_erstellen_1, width=1012, height=714)

                    #   Spalten:

            notebook.add(frame_11, text="Eingabe")
            notebook.add(frame_22, text="Visieren")

                    #   Anzeigen des Notebooks:

            notebook.place(x=5,y=5)

                        # Größe der Fenster:
            width_x_2=450
            height_y_2=295

            self.Objekt_gesetzt=0
            self.Objekt_Tempo_gesetzt=0

            self.Color_1 = Randomcolor.Randomcolor()

            # Weiterführende Einstellungen der Anzeige:
            self.Zeichenmodus = IntVar()
            self.Zeichenmodus.set(1)
            self.Groesse_Oe_Kugeln=StringVar()
            self.Groesse_Oe_Kugeln.set('3')
            self.Groesse_Oe_Kugeln_2=StringVar()
            self.Groesse_Oe_Kugeln_2.set('10')
            self.Groesse_Oe_text_1=StringVar()
            self.Groesse_Oe_text_1.set("Größe:")
            Kugeln_Oe_1=Radiobutton(frame_22, text="Kugeln gleicher Größe", variable=self.Zeichenmodus, value=1).place(x=59+width_x_2,y=123+height_y_2)
            Kugeln_Oe_2=Radiobutton(frame_22, text="Kugeln nach Radius", variable=self.Zeichenmodus, value=2).place(x=59+width_x_2,y=123+height_y_2+30)
            Kugeln_Oe_3=Radiobutton(frame_22, text="Kugeln nach Entfernung", variable=self.Zeichenmodus, value=3).place(x=59+width_x_2,y=123+height_y_2+60)
            Kugeln_Oe_4=Radiobutton(frame_22, text="Tatsächliche Größe", variable=self.Zeichenmodus, value=4).place(x=59+width_x_2,y=123+height_y_2+90)

            def Kugeln_Oe_1_Angewaehlt(*args):
                if self.Zeichenmodus.get()==1:
                    self.Groesse_Oe_text_1.set("Größe:")
                    Groesse_Oe_1_Label_2.config(state=NORMAL)
                    Groesse_Oe_1_Label.config(state=NORMAL)
                    Groesse_Oe_1.config(state=NORMAL)
                    Groesse_Oe_2.config(state=DISABLED)
                    Groesse_Oe_2_Label_2.config(state=DISABLED)
                    Groesse_Oe_2_Label.config(state=DISABLED)
                elif self.Zeichenmodus.get()==2:
                    self.Groesse_Oe_text_1.set("Von:")
                    Groesse_Oe_1_Label_2.config(state=NORMAL)
                    Groesse_Oe_1_Label.config(state=NORMAL)
                    Groesse_Oe_1.config(state=NORMAL)
                    Groesse_Oe_2.config(state=NORMAL)
                    Groesse_Oe_2_Label_2.config(state=NORMAL)
                    Groesse_Oe_2_Label.config(state=NORMAL)
                elif self.Zeichenmodus.get()==3:
                    self.Groesse_Oe_text_1.set("Von:")
                    Groesse_Oe_1_Label_2.config(state=NORMAL)
                    Groesse_Oe_1_Label.config(state=NORMAL)
                    Groesse_Oe_1.config(state=NORMAL)
                    Groesse_Oe_2.config(state=NORMAL)
                    Groesse_Oe_2_Label_2.config(state=NORMAL)
                    Groesse_Oe_2_Label.config(state=NORMAL)
                elif self.Zeichenmodus.get()==4:
                    self.Groesse_Oe_text_1.set("Groesse:")
                    Groesse_Oe_2.config(state=DISABLED)
                    Groesse_Oe_1_Label_2.config(state=DISABLED)
                    Groesse_Oe_1_Label.config(state=DISABLED)
                    Groesse_Oe_1.config(state=DISABLED)
                    Groesse_Oe_2_Label_2.config(state=DISABLED)
                    Groesse_Oe_2_Label.config(state=DISABLED)
                Einzeichnen()
            self.Zeichenmodus.trace("w", Kugeln_Oe_1_Angewaehlt)

            Groesse_Oe_1_Label=Label(frame_22,textvariable=self.Groesse_Oe_text_1)
            Groesse_Oe_1_Label.place(x=259+width_x_2,y=123+height_y_2)
            Groesse_Oe_1_Label.config(state=NORMAL)
            Groesse_Oe_1=Spinbox(frame_22,from_=1, to=100,textvariable=self.Groesse_Oe_Kugeln,width=7,bd=2)
            Groesse_Oe_1.place(x=329+width_x_2,y=125+height_y_2)
            Groesse_Oe_1.config(state=NORMAL)
            Groesse_Oe_1_Label_2=Label(frame_22,text="[Pixel]")
            Groesse_Oe_1_Label_2.place(x=395+width_x_2,y=123+height_y_2)
            Groesse_Oe_2_Label=Label(frame_22,text="Bis:")
            Groesse_Oe_2_Label.place(x=259+width_x_2,y=153+height_y_2)
            Groesse_Oe_2_Label.config(state=DISABLED)
            Groesse_Oe_2=Spinbox(frame_22,from_=1, to=100,textvariable=self.Groesse_Oe_Kugeln_2,width=7,bd=2)
            Groesse_Oe_2.place(x=329+width_x_2,y=155+height_y_2)
            Groesse_Oe_2.config(state=DISABLED)
            Groesse_Oe_2_Label_2=Label(frame_22,text="[Pixel]")
            Groesse_Oe_2_Label_2.place(x=395+width_x_2,y=153+height_y_2)
            Groesse_Oe_2_Label_2.config(state=DISABLED)
            Geschwindigkeit_Oe_1_Label_1=Label(frame_22, text='Geschwindigkeit:')
            Geschwindigkeit_Oe_1_Label_1.place(x=59+width_x_2,y=125+height_y_2+120)
            self.Geschwindigkeit_pro_Pixel=StringVar()
            self.Geschwindigkeit_pro_Pixel.set('1.0')
            Geschwindigkeit_Oe_1_Label_2=Entry(frame_22, textvariable=self.Geschwindigkeit_pro_Pixel,bd=2,justify=RIGHT,width=17)
            Geschwindigkeit_Oe_1_Label_2.place(x=250+width_x_2,y=125+height_y_2+120)
            Geschwindigkeit_Oe_1_Label_3=Label(frame_22, text='[1000*(m/s)/Pixel]')
            Geschwindigkeit_Oe_1_Label_3.place(x=395+width_x_2,y=125+height_y_2+120)

            def Geschwindigkeit_Verifizieren(*args):
                Get_Geschwindigkeit = self.Geschwindigkeit_pro_Pixel.get()
                a=Verifizieren.Verifizieren_ohne_Minus(Get_Geschwindigkeit)
                self.Geschwindigkeit_pro_Pixel.set(a)
                max_min()
                Masstab_berechnen()
                Einzeichnen()
            self.Geschwindigkeit_pro_Pixel.trace("w", Geschwindigkeit_Verifizieren)

            self.Oe_X=StringVar()
            self.Oe_X.set('0')
            X_Label_Frame_22=Label(frame_22, text='X:').place(x=59+width_x_2,y=123+height_y_2+150)
            X_Label_Frame_22_1=Label(frame_22, textvariable=self.Oe_X, relief=SUNKEN,bd=2,width=15).place(x=89+width_x_2,y=123+height_y_2+150)

            self.Oe_Y=StringVar()
            self.Oe_Y.set('0')
            Y_Label_Frame_22=Label(frame_22, text='Y:').place(x=219+width_x_2,y=123+height_y_2+150)
            Y_Label_Frame_22_1=Label(frame_22, textvariable=self.Oe_Y, relief=SUNKEN,bd=2,width=15).place(x=249+width_x_2,y=123+height_y_2+150)

            self.Oe_Z=StringVar()
            self.Oe_Z.set('0')
            Z_Label_Frame_22=Label(frame_22, text='Z:').place(x=379+width_x_2,y=123+height_y_2+150)
            Z_Label_Frame_22_1=Label(frame_22, textvariable=self.Oe_Z, relief=SUNKEN,bd=2,width=15).place(x=409+width_x_2,y=123+height_y_2+150)

            def max_min():
                # Startwerte für die kleinsten und größten x,y und z Werte der Liste:
                self.Newton_Simulator.Maximalwertsuche()
                self.minX=self.Newton_Simulator.MinX
                self.minY=self.Newton_Simulator.MinY
                self.minZ=self.Newton_Simulator.MinZ
                self.maxX=self.Newton_Simulator.MaxX
                self.maxY=self.Newton_Simulator.MaxY
                self.maxZ=self.Newton_Simulator.MaxZ
                if self.Objekt_gesetzt==1:
                    x=String_Number.String_to_Number(self.X_Position.get())
                    y=String_Number.String_to_Number(self.Y_Position.get())
                    z=String_Number.String_to_Number(self.Z_Position.get())
                    if x>self.maxX:
                        self.minX=x
                    elif x<self.minX:
                        self.minX=x
                    if y>self.maxY:
                        self.maxY=y
                    elif y<self.minY:
                        self.minY=y
                    if z>self.maxZ:
                        self.maxZ=z
                    elif z<self.minZ:
                        self.minZ=z

            def Masstab_berechnen():
                x_diff=self.maxX-self.minX
                y_diff=self.maxY-self.minY
                z_diff=self.maxZ-self.minZ
                if x_diff==0 and y_diff==0 and z_diff==0:
                    x_diff=100
                    y_diff=100
                    z_diff=100
                # Für xy:
                if y_diff!=0:
                    if x_diff!=0:
                        Mpp_y_xy=y_diff/height_y_2
                        Mpp_x_xy=x_diff/width_x_2
                        if Mpp_y_xy>=Mpp_x_xy:
                            self.Oe_Mpp_xy=Mpp_y_xy
                        else:
                            self.Oe_Mpp_xy=Mpp_x_xy
                    elif x_diff==0:
                         self.Oe_Mpp_xy=y_diff/height_y_2
                elif y_diff==0:
                    if x_diff!=0:
                        self.Oe_Mpp_xy=x_diff/width_x_2
                    elif x_diff==0:
                        self.Oe_Mpp_xy=0
                # Für yz:
                if z_diff!=0:
                    if y_diff!=0:
                        Mpp_y_yz=y_diff/height_y_2
                        Mpp_z_yz=z_diff/width_x_2
                        if Mpp_y_yz>=Mpp_z_yz:
                            self.Oe_Mpp_yz=Mpp_y_yz
                        else:
                            self.Oe_Mpp_yz=Mpp_z_yz
                    elif y_diff==0:
                         self.Oe_Mpp_yz=z_diff/width_x_2
                elif z_diff==0:
                    if y_diff!=0:
                        self.Oe_Mpp_yz=y_diff/height_y_2
                    elif y_diff==0:
                        self.Oe_Mpp_yz=0
                # Für xz:
                if z_diff!=0:
                    if x_diff!=0:
                        Mpp_z_xz=z_diff/height_y_2
                        Mpp_x_xz=x_diff/width_x_2
                        if Mpp_z_xz>=Mpp_x_xz:
                            self.Oe_Mpp_xz=Mpp_z_xz
                        else:
                            self.Oe_Mpp_xz=Mpp_x_xz
                    elif x_diff==0:
                         self.Oe_Mpp_xz=z_diff/height_y_2
                elif z_diff==0:
                    if x_diff!=0:
                        self.Oe_Mpp_xz=x_diff/width_x_2
                    elif x_diff==0:
                        self.Oe_Mpp_xz=0
                # Vergleich der Mpp's (meiste Meter pro Pixel gesucht):
                self.Oe_Mpp=self.Oe_Mpp_xy
                if self.Oe_Mpp_xz>self.Oe_Mpp:
                    self.Oe_Mpp=self.Oe_Mpp_xz
                if self.Oe_Mpp_yz>self.Oe_Mpp:
                    self.Oe_Mpp=self.Oe_Mpp_yz
                # Vergrößern von Mpp um 10% pro Seite:
                self.Oe_Mpp=self.Oe_Mpp*1.2
                # Mittelpunkte_bestimmen:
                self.Oe_Mittelpunkt_x=self.minX+x_diff/2
                self.Oe_Mittelpunkt_y=self.minY+y_diff/2
                self.Oe_Mittelpunkt_z=self.minZ+z_diff/2

            def Einzeichnen():
                # Hinzufügen der Punkte / Kreise auf die beschriebenen Arten und Weisen erst in Richtung :
                    Canvas_xy.delete(ALL)
                    Canvas_yz.delete(ALL)
                    Canvas_xz.delete(ALL)
                    self.xy_koord = PhotoImage(file = '../Icon/Koordinaten/xy.gif')
                    Canvas_xy.create_image(12,height_y_2-39, image = self.xy_koord, anchor = NW)
                    self.yz_koord = PhotoImage(file = '../Icon/Koordinaten/yz.gif')
                    Canvas_yz.create_image(width_x_2-39, height_y_2-39, image = self.yz_koord, anchor = NW)
                    self.xz_koord = PhotoImage(file = '../Icon/Koordinaten/xz.gif')
                    Canvas_xz.create_image(12, height_y_2-39, image = self.xz_koord, anchor = NW)
                    Mpp=self.Oe_Mpp
                    if Mpp==0:
                        Mpp=0.1
                    Mitte_x=self.Oe_Mittelpunkt_x
                    Mitte_y=self.Oe_Mittelpunkt_y
                    Mitte_z=self.Oe_Mittelpunkt_z
                    speed=1000*(String_Number.String_to_Number(self.Geschwindigkeit_pro_Pixel.get()))
                    if self.Zeichenmodus.get()==1:
                        Groesse=String_Number.String_to_Number(self.Groesse_Oe_Kugeln.get())
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            # Zeichnet die Punkte ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse>0 and pos_x_xy+Groesse<width_x_2 and pos_y_xy-Groesse>0 and pos_y_xy+Groesse<height_y_2:
                                Canvas_xy.create_oval(abs(pos_x_xy-Groesse),abs(pos_y_xy-Groesse),abs(pos_x_xy+Groesse),abs(pos_y_xy+Groesse), fill=self.Newton_Simulator.Color[i])
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse>0 and pos_z_yz+Groesse<width_x_2 and pos_y_yz-Groesse>0 and pos_y_yz+Groesse<height_y_2:
                                Canvas_yz.create_oval(abs(pos_z_yz-Groesse),abs(pos_y_yz-Groesse),abs(pos_z_yz+Groesse),abs(pos_y_yz+Groesse), fill=self.Newton_Simulator.Color[i])
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse>0 and pos_x_xz+Groesse<width_x_2 and pos_z_xz-Groesse>0 and pos_z_xz+Groesse<height_y_2:
                                Canvas_xz.create_oval(abs(pos_x_xz-Groesse),abs(pos_z_xz-Groesse),abs(pos_x_xz+Groesse),abs(pos_z_xz+Groesse), fill=self.Newton_Simulator.Color[i])
                            # Zeichnet die Geraden der Geschwindigkeit ein:
                            if abs(vx)>speed or abs(vy)>speed:
                                vx_2=vx/speed
                                vy_2=-vy/speed
                                if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                    if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                        Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vy)>speed or abs(vz)>speed:
                                vy_2=-vy/speed
                                vz_2=-vz/speed
                                if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                    if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                        Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vx)>speed or abs(vz)>speed:
                                vx_2=vx/speed
                                vz_2=-vz/speed
                                if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                    if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                        Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                        if self.Objekt_gesetzt==1:
                            x=String_Number.String_to_Number(self.X_Position.get())
                            y=String_Number.String_to_Number(self.Y_Position.get())
                            z=String_Number.String_to_Number(self.Z_Position.get())
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse-1>0 and pos_x_xy+Groesse+1<width_x_2 and pos_y_xy-Groesse-1>0 and pos_y_xy+Groesse+1<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Groesse-1),abs(pos_y_xy-Groesse-1),abs(pos_x_xy+Groesse+1),abs(pos_y_xy+Groesse+1), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse-1>0 and pos_z_yz+Groesse+1<width_x_2 and pos_y_yz-Groesse-1>0 and pos_y_yz+Groesse+1<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Groesse-1),abs(pos_y_yz-Groesse-1),abs(pos_z_yz+Groesse+1),abs(pos_y_yz+Groesse+1), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse-1>0 and pos_x_xz+Groesse+1<width_x_2 and pos_z_xz-Groesse-1>0 and pos_z_xz+Groesse+1<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Groesse-1),abs(pos_z_xz-Groesse-1),abs(pos_x_xz+Groesse+1),abs(pos_z_xz+Groesse+1), fill=str(self.Color_1))
                            if self.Objekt_Tempo_gesetzt==1:
                                    vx=String_Number.String_to_Number(self.X_Geschwindigkeit.get())
                                    vy=String_Number.String_to_Number(self.Y_Geschwindigkeit.get())
                                    vz=String_Number.String_to_Number(self.Z_Geschwindigkeit.get())
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>speed or abs(vy)>speed:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>speed or abs(vz)>speed:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>speed or abs(vz)>speed:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                        if self.Oe_akt_Pos==1:
                            x=self.Oe_akt_X
                            y=self.Oe_akt_Y
                            z=self.Oe_akt_Z
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse-1>0 and pos_x_xy+Groesse+1<width_x_2 and pos_y_xy-Groesse-1>0 and pos_y_xy+Groesse+1<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Groesse-1),abs(pos_y_xy-Groesse-1),abs(pos_x_xy+Groesse+1),abs(pos_y_xy+Groesse+1), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse-1>0 and pos_z_yz+Groesse+1<width_x_2 and pos_y_yz-Groesse-1>0 and pos_y_yz+Groesse+1<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Groesse-1),abs(pos_y_yz-Groesse-1),abs(pos_z_yz+Groesse+1),abs(pos_y_yz+Groesse+1), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse-1>0 and pos_x_xz+Groesse+1<width_x_2 and pos_z_xz-Groesse-1>0 and pos_z_xz+Groesse+1<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Groesse-1),abs(pos_z_xz-Groesse-1),abs(pos_x_xz+Groesse+1),abs(pos_z_xz+Groesse+1), fill=str(self.Color_1))
                            if self.Oe_akt_Tem==1:
                                    vx=self.Oe_akt_movX/Mpp
                                    vy=self.Oe_akt_movY/Mpp
                                    vz=self.Oe_akt_movZ/Mpp
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>1 or abs(vy)>1:
                                        vx_2=vx#speed
                                        vy_2=-vy#/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>1 or abs(vz)>1:
                                        vy_2=-vy#speed
                                        vz_2=-vz#/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>1 or abs(vz)>1:
                                        vx_2=vx#speed
                                        vz_2=-vz#/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                    if self.Zeichenmodus.get()==2:
                        Groesse_1=String_Number.String_to_Number(self.Groesse_Oe_Kugeln.get())
                        Groesse_2=String_Number.String_to_Number(self.Groesse_Oe_Kugeln_2.get())
                        Groesse=[]
                        Groesse=self.Newton_Simulator.Radius_Anteil(Groesse_1,Groesse_2,String_Number.String_to_Number(str(self.Radius.get())))
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            # Zeichnet die Punkte ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse[i]>0 and pos_x_xy+Groesse[i]<width_x_2 and pos_y_xy-Groesse[i]>0 and pos_y_xy+Groesse[i]<height_y_2:
                                Canvas_xy.create_oval(abs(pos_x_xy-Groesse[i]),abs(pos_y_xy-Groesse[i]),abs(pos_x_xy+Groesse[i]),abs(pos_y_xy+Groesse[i]), fill=self.Newton_Simulator.Color[i])
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse[i]>0 and pos_z_yz+Groesse[i]<width_x_2 and pos_y_yz-Groesse[i]>0 and pos_y_yz+Groesse[i]<height_y_2:
                                Canvas_yz.create_oval(abs(pos_z_yz-Groesse[i]),abs(pos_y_yz-Groesse[i]),abs(pos_z_yz+Groesse[i]),abs(pos_y_yz+Groesse[i]), fill=self.Newton_Simulator.Color[i])
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse[i]>0 and pos_x_xz+Groesse[i]<width_x_2 and pos_z_xz-Groesse[i]>0 and pos_z_xz+Groesse[i]<height_y_2:
                                Canvas_xz.create_oval(abs(pos_x_xz-Groesse[i]),abs(pos_z_xz-Groesse[i]),abs(pos_x_xz+Groesse[i]),abs(pos_z_xz+Groesse[i]), fill=self.Newton_Simulator.Color[i])
                            # Zeichnet die Geraden der Geschwindigkeit ein:
                            if abs(vx)>speed or abs(vy)>speed:
                                vx_2=vx/speed
                                vy_2=-vy/speed
                                if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                    if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                        Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vy)>speed or abs(vz)>speed:
                                vy_2=-vy/speed
                                vz_2=-vz/speed
                                if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                    if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                        Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vx)>speed or abs(vz)>speed:
                                vx_2=vx/speed
                                vz_2=-vz/speed
                                if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                    if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                        Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                        if self.Objekt_gesetzt==1:
                            n=Groesse[len(Groesse)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drg=Groesse[len(Groesse)-2] # Steigung der Funktion für die Groesse
                            Grossheit=String_Number.String_to_Number(str(self.Radius.get()))/drg+n
                            x=String_Number.String_to_Number(self.X_Position.get())
                            y=String_Number.String_to_Number(self.Y_Position.get())
                            z=String_Number.String_to_Number(self.Z_Position.get())
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Grossheit>0 and pos_x_xy+Grossheit<width_x_2 and pos_y_xy-Grossheit>0 and pos_y_xy+Grossheit<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Grossheit),abs(pos_y_xy-Grossheit),abs(pos_x_xy+Grossheit),abs(pos_y_xy+Grossheit), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Grossheit>0 and pos_z_yz+Grossheit<width_x_2 and pos_y_yz-Grossheit>0 and pos_y_yz+Grossheit<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Grossheit),abs(pos_y_yz-Grossheit),abs(pos_z_yz+Grossheit),abs(pos_y_yz+Grossheit), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Grossheit>0 and pos_x_xz+Grossheit<width_x_2 and pos_z_xz-Grossheit>0 and pos_z_xz+Grossheit<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Grossheit),abs(pos_z_xz-Grossheit),abs(pos_x_xz+Grossheit),abs(pos_z_xz+Grossheit), fill=str(self.Color_1))
                            if self.Objekt_Tempo_gesetzt==1:
                                    vx=String_Number.String_to_Number(self.X_Geschwindigkeit.get())
                                    vy=String_Number.String_to_Number(self.Y_Geschwindigkeit.get())
                                    vz=String_Number.String_to_Number(self.Z_Geschwindigkeit.get())
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>speed or abs(vy)>speed:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>speed or abs(vz)>speed:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>speed or abs(vz)>speed:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                        if self.Oe_akt_Pos==1:
                            n=Groesse[len(Groesse)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drg=Groesse[len(Groesse)-2] # Steigung der Funktion für die Groesse
                            Grossheit=String_Number.String_to_Number(str(self.Radius.get()))/drg+n
                            x=self.Oe_akt_X
                            y=self.Oe_akt_Y
                            z=self.Oe_akt_Z
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Grossheit>0 and pos_x_xy+Grossheit<width_x_2 and pos_y_xy-Grossheit>0 and pos_y_xy+Grossheit<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Grossheit),abs(pos_y_xy-Grossheit),abs(pos_x_xy+Grossheit),abs(pos_y_xy+Grossheit), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Grossheit>0 and pos_z_yz+Grossheit<width_x_2 and pos_y_yz-Grossheit>0 and pos_y_yz+Grossheit<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Grossheit),abs(pos_y_yz-Grossheit),abs(pos_z_yz+Grossheit),abs(pos_y_yz+Grossheit), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Grossheit>0 and pos_x_xz+Grossheit<width_x_2 and pos_z_xz-Grossheit>0 and pos_z_xz+Grossheit<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Grossheit),abs(pos_z_xz-Grossheit),abs(pos_x_xz+Grossheit),abs(pos_z_xz+Grossheit), fill=str(self.Color_1))
                            if self.Oe_akt_Tem==1:
                                    vx=self.Oe_akt_movX/Mpp
                                    vy=self.Oe_akt_movY/Mpp
                                    vz=self.Oe_akt_movZ/Mpp
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>1 or abs(vy)>1:
                                        vx_2=vx#speed
                                        vy_2=-vy#/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>1 or abs(vz)>1:
                                        vy_2=-vy#speed
                                        vz_2=-vz#/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>1 or abs(vz)>1:
                                        vx_2=vx#speed
                                        vz_2=-vz#/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                    if self.Zeichenmodus.get()==3:
                        # Nach entfernung:
                        Groesse_1=String_Number.String_to_Number(self.Groesse_Oe_Kugeln.get())
                        Groesse_2=String_Number.String_to_Number(self.Groesse_Oe_Kugeln_2.get())
                        Groesse=[]
                        Groesse_x=self.Newton_Simulator.Entfernung_Anteil_x(Groesse_1,Groesse_2,String_Number.String_to_Number(str(self.X_Position.get())))
                        Groesse_y=self.Newton_Simulator.Entfernung_Anteil_y(Groesse_1,Groesse_2,String_Number.String_to_Number(str(self.Y_Position.get())))
                        Groesse_z=self.Newton_Simulator.Entfernung_Anteil_z(Groesse_1,Groesse_2,String_Number.String_to_Number(str(self.Z_Position.get())))
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            # Zeichnet die Punkte ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse_z[i]>0 and pos_x_xy+Groesse_z[i]<width_x_2 and pos_y_xy-Groesse_z[i]>0 and pos_y_xy+Groesse_z[i]<height_y_2:
                                Canvas_xy.create_oval(abs(pos_x_xy-Groesse_z[i]),abs(pos_y_xy-Groesse_z[i]),abs(pos_x_xy+Groesse_z[i]),abs(pos_y_xy+Groesse_z[i]), fill=self.Newton_Simulator.Color[i])
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse_x[i]>0 and pos_z_yz+Groesse_x[i]<width_x_2 and pos_y_yz-Groesse_x[i]>0 and pos_y_yz+Groesse_x[i]<height_y_2:
                                Canvas_yz.create_oval(abs(pos_z_yz-Groesse_x[i]),abs(pos_y_yz-Groesse_x[i]),abs(pos_z_yz+Groesse_x[i]),abs(pos_y_yz+Groesse_x[i]), fill=self.Newton_Simulator.Color[i])
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse_y[i]>0 and pos_x_xz+Groesse_y[i]<width_x_2 and pos_z_xz-Groesse_y[i]>0 and pos_z_xz+Groesse_y[i]<height_y_2:
                                Canvas_xz.create_oval(abs(pos_x_xz-Groesse_y[i]),abs(pos_z_xz-Groesse_y[i]),abs(pos_x_xz+Groesse_y[i]),abs(pos_z_xz+Groesse_y[i]), fill=self.Newton_Simulator.Color[i])
                            # Zeichnet die Geraden der Geschwindigkeit ein:
                            if abs(vx)>speed or abs(vy)>speed:
                                vx_2=vx/speed
                                vy_2=-vy/speed
                                if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                    if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                        Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vy)>speed or abs(vz)>speed:
                                vy_2=-vy/speed
                                vz_2=-vz/speed
                                if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                    if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                        Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vx)>speed or abs(vz)>speed:
                                vx_2=vx/speed
                                vz_2=-vz/speed
                                if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                    if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                        Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                        if self.Objekt_gesetzt==1:
                            nx=Groesse_x[len(Groesse_x)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgx=Groesse_x[len(Groesse_x)-2] # Steigung der Funktion für die Groesse
                            ny=Groesse_y[len(Groesse_y)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgy=Groesse_y[len(Groesse_y)-2] # Steigung der Funktion für die Groesse
                            nz=Groesse_z[len(Groesse_z)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgz=Groesse_z[len(Groesse_z)-2] # Steigung der Funktion für die Groesse
                            Grossheit_x=String_Number.String_to_Number(str(self.X_Position.get()))*drgx+nx
                            Grossheit_y=String_Number.String_to_Number(str(self.Y_Position.get()))*drgy+ny
                            Grossheit_z=String_Number.String_to_Number(str(self.Z_Position.get()))*drgz+nz
                            x=String_Number.String_to_Number(self.X_Position.get())
                            y=String_Number.String_to_Number(self.Y_Position.get())
                            z=String_Number.String_to_Number(self.Z_Position.get())
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Grossheit_z>0 and pos_x_xy+Grossheit_z<width_x_2 and pos_y_xy-Grossheit_z>0 and pos_y_xy+Grossheit_z<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Grossheit_z),abs(pos_y_xy-Grossheit_z),abs(pos_x_xy+Grossheit_z),abs(pos_y_xy+Grossheit_z), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Grossheit_x>0 and pos_z_yz+Grossheit_x<width_x_2 and pos_y_yz-Grossheit_x>0 and pos_y_yz+Grossheit_x<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Grossheit_x),abs(pos_y_yz-Grossheit_x),abs(pos_z_yz+Grossheit_x),abs(pos_y_yz+Grossheit_x), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Grossheit_y>0 and pos_x_xz+Grossheit_y<width_x_2 and pos_z_xz-Grossheit_y>0 and pos_z_xz+Grossheit_y<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Grossheit_y),abs(pos_z_xz-Grossheit_y),abs(pos_x_xz+Grossheit_y),abs(pos_z_xz+Grossheit_y), fill=str(self.Color_1))
                            if self.Objekt_Tempo_gesetzt==1:
                                    vx=String_Number.String_to_Number(self.X_Geschwindigkeit.get())
                                    vy=String_Number.String_to_Number(self.Y_Geschwindigkeit.get())
                                    vz=String_Number.String_to_Number(self.Z_Geschwindigkeit.get())
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>speed or abs(vy)>speed:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>speed or abs(vz)>speed:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>speed or abs(vz)>speed:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                        if self.Oe_akt_Pos==1:
                            nx=Groesse_x[len(Groesse_x)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgx=Groesse_x[len(Groesse_x)-2] # Steigung der Funktion für die Groesse
                            ny=Groesse_y[len(Groesse_y)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgy=Groesse_y[len(Groesse_y)-2] # Steigung der Funktion für die Groesse
                            nz=Groesse_z[len(Groesse_z)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgz=Groesse_z[len(Groesse_z)-2] # Steigung der Funktion für die Groesse
                            Grossheit_x=String_Number.String_to_Number(str(self.X_Position.get()))*drgx+nx
                            Grossheit_y=String_Number.String_to_Number(str(self.Y_Position.get()))*drgy+ny
                            Grossheit_z=String_Number.String_to_Number(str(self.Z_Position.get()))*drgz+nz
                            x=self.Oe_akt_X
                            y=self.Oe_akt_Y
                            z=self.Oe_akt_Z
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Grossheit_z>0 and pos_x_xy+Grossheit_z<width_x_2 and pos_y_xy-Grossheit_z>0 and pos_y_xy+Grossheit_z<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Grossheit_z),abs(pos_y_xy-Grossheit_z),abs(pos_x_xy+Grossheit_z),abs(pos_y_xy+Grossheit_z), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Grossheit_x>0 and pos_z_yz+Grossheit_x<width_x_2 and pos_y_yz-Grossheit_x>0 and pos_y_yz+Grossheit_x<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Grossheit_x),abs(pos_y_yz-Grossheit_x),abs(pos_z_yz+Grossheit_x),abs(pos_y_yz+Grossheit_x), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Grossheit_y>0 and pos_x_xz+Grossheit_y<width_x_2 and pos_z_xz-Grossheit_y>0 and pos_z_xz+Grossheit_y<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Grossheit_y),abs(pos_z_xz-Grossheit_y),abs(pos_x_xz+Grossheit_y),abs(pos_z_xz+Grossheit_y), fill=str(self.Color_1))
                            if self.Oe_akt_Tem==1:
                                    vx=self.Oe_akt_movX/Mpp
                                    vy=self.Oe_akt_movY/Mpp
                                    vz=self.Oe_akt_movZ/Mpp
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>1 or abs(vy)>1:
                                        vx_2=vx#speed
                                        vy_2=-vy#/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>1 or abs(vz)>1:
                                        vy_2=-vy#speed
                                        vz_2=-vz#/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>1 or abs(vz)>1:
                                        vx_2=vx#speed
                                        vz_2=-vz#/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))            # Ein Script wird benötigt, welches die max und min Werte des Screens anzeigt, diese überprüft auf den Ursprung (0) und dann je nach Zoom Verhältnis verschiedene Massstäbe anzeigt, zum Beispiel Millimeter[mm], Meter[m], Kilometer [km], Megameter [Mm] (im Deutschen eher unkonventionell), Astronomische Einheiten [Ae], Parsec [pc], Lichtjahre [Lj]
                    if self.Zeichenmodus.get()==4:
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            # Zeichnet die Punkte ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            # Bestimmt die Groesse (mind. 1 Pixel):
                            Groesse=self.Newton_Simulator.Radius_Body[i][0]/Mpp
                            if Groesse<1:
                                Groesse=1
                            if pos_x_xy-Groesse>0 and pos_x_xy+Groesse<width_x_2 and pos_y_xy-Groesse>0 and pos_y_xy+Groesse<height_y_2:
                                Canvas_xy.create_oval(abs(pos_x_xy-Groesse),abs(pos_y_xy-Groesse),abs(pos_x_xy+Groesse),abs(pos_y_xy+Groesse), fill=self.Newton_Simulator.Color[i])
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse>0 and pos_z_yz+Groesse<width_x_2 and pos_y_yz-Groesse>0 and pos_y_yz+Groesse<height_y_2:
                                Canvas_yz.create_oval(abs(pos_z_yz-Groesse),abs(pos_y_yz-Groesse),abs(pos_z_yz+Groesse),abs(pos_y_yz+Groesse), fill=self.Newton_Simulator.Color[i])
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse>0 and pos_x_xz+Groesse<width_x_2 and pos_z_xz-Groesse>0 and pos_z_xz+Groesse<height_y_2:
                                Canvas_xz.create_oval(abs(pos_x_xz-Groesse),abs(pos_z_xz-Groesse),abs(pos_x_xz+Groesse),abs(pos_z_xz+Groesse), fill=self.Newton_Simulator.Color[i])
                            # Zeichnet die Geraden der Geschwindigkeit ein:
                            if abs(vx)>speed or abs(vy)>speed:
                                vx_2=vx/speed
                                vy_2=-vy/speed
                                if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                    if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                        Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vy)>speed or abs(vz)>speed:
                                vy_2=-vy/speed
                                vz_2=-vz/speed
                                if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                    if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                        Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vx)>speed or abs(vz)>speed:
                                vx_2=vx/speed
                                vz_2=-vz/speed
                                if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                    if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                        Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                        if self.Objekt_gesetzt==1:
                            x=String_Number.String_to_Number(self.X_Position.get())
                            y=String_Number.String_to_Number(self.Y_Position.get())
                            z=String_Number.String_to_Number(self.Z_Position.get())
                            # Bestimmt die Groesse (mind. 1 Pixel):
                            Groesse=String_Number.String_to_Number(self.Radius.get())/Mpp
                            if Groesse<1:
                                Groesse=1
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse-1>0 and pos_x_xy+Groesse+1<width_x_2 and pos_y_xy-Groesse-1>0 and pos_y_xy+Groesse+1<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Groesse),abs(pos_y_xy-Groesse),abs(pos_x_xy+Groesse),abs(pos_y_xy+Groesse), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse-1>0 and pos_z_yz+Groesse+1<width_x_2 and pos_y_yz-Groesse-1>0 and pos_y_yz+Groesse+1<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Groesse),abs(pos_y_yz-Groesse),abs(pos_z_yz+Groesse),abs(pos_y_yz+Groesse), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse-1>0 and pos_x_xz+Groesse+1<width_x_2 and pos_z_xz-Groesse-1>0 and pos_z_xz+Groesse+1<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Groesse),abs(pos_z_xz-Groesse),abs(pos_x_xz+Groesse),abs(pos_z_xz+Groesse), fill=str(self.Color_1))
                            if self.Objekt_Tempo_gesetzt==1:
                                    vx=String_Number.String_to_Number(self.X_Geschwindigkeit.get())
                                    vy=String_Number.String_to_Number(self.Y_Geschwindigkeit.get())
                                    vz=String_Number.String_to_Number(self.Z_Geschwindigkeit.get())
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>speed or abs(vy)>speed:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>speed or abs(vz)>speed:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>speed or abs(vz)>speed:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                        if self.Oe_akt_Pos==1:
                            x=self.Oe_akt_X
                            y=self.Oe_akt_Y
                            z=self.Oe_akt_Z
                            # Bestimmt die Groesse (mind. 1 Pixel):
                            Groesse=String_Number.String_to_Number(self.Radius.get())/Mpp
                            if Groesse<1:
                                Groesse=1
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse-1>0 and pos_x_xy+Groesse+1<width_x_2 and pos_y_xy-Groesse-1>0 and pos_y_xy+Groesse+1<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Groesse-1),abs(pos_y_xy-Groesse-1),abs(pos_x_xy+Groesse+1),abs(pos_y_xy+Groesse+1), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse-1>0 and pos_z_yz+Groesse+1<width_x_2 and pos_y_yz-Groesse-1>0 and pos_y_yz+Groesse+1<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Groesse-1),abs(pos_y_yz-Groesse-1),abs(pos_z_yz+Groesse+1),abs(pos_y_yz+Groesse+1), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse-1>0 and pos_x_xz+Groesse+1<width_x_2 and pos_z_xz-Groesse-1>0 and pos_z_xz+Groesse+1<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Groesse-1),abs(pos_z_xz-Groesse-1),abs(pos_x_xz+Groesse+1),abs(pos_z_xz+Groesse+1), fill=str(self.Color_1))
                            if self.Oe_akt_Tem==1:
                                    vx=self.Oe_akt_movX/Mpp
                                    vy=self.Oe_akt_movY/Mpp
                                    vz=self.Oe_akt_movZ/Mpp
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>1 or abs(vy)>1:
                                        vx_2=vx#speed
                                        vy_2=-vy#/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>1 or abs(vz)>1:
                                        vy_2=-vy#speed
                                        vz_2=-vz#/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>1 or abs(vz)>1:
                                        vx_2=vx#speed
                                        vz_2=-vz#/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                    # Skript welches den Masstab und Orientierungspunkte Anzeigen soll:
                    # Zuerst werden die Maxima und Minima der Canvases bestimmt:
                    Canvas_coord_yz.delete(ALL)
                    Canvas_coord_xz.delete(ALL)
                    Canvas_coord_xy.delete(ALL)
                        # geg.: Mpp, Mitte_z, Mitte_x, Mitte_y
                    pc=30856776000000000    # 1*Parsec
                    Lj=9460528000000000     # 1*Lichtjahr
                    ae=149597870691         # 1*Astronomische Einheit
                    km=1000                 # 1*Kilometer
                    hm=100                  # 1*Hectometer
                    dam=10                  # 1*Dekameter
                    m=1                     # 1*meter
                    dm=0.1                  # 0.1*meter
                    cm=0.01                 # 0.01*meter

                    # xy, yz - y (height_y_2) - Achsen max und min:
                    max_y=Mitte_y+height_y_2*Mpp/2                              # Oberes Ende!
                    min_y=Mitte_y-height_y_2*Mpp/2                              # Unteres Ende!
                    # Die Skala soll ermitelt werden:
                    # Wir teilen min durch die Längen der einheiten und runden diese zu einer int, dann zeichnen wir alle relevanten einund setzen Einheitenanzahl eins höher
                    e=0                     # Anzeige aus=0, an=1
                    Aktueller_Schritt=8     #0=Parsec, 1=Lj, 2=AE.....

                    if Aktueller_Schritt==8:
                        # 1 cm (cm) = 1 m
                        a=int(round(min_y/cm))
                        stop=0
                        d=0
                        c=abs(((a+1)*cm)/Mpp-(a*cm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*cm>min_y:
                                    if a*cm<max_y:
                                        if Mpp!=0:
                                            y=(a*cm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"cm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==7:
                        # 1 dm (dm) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dm)/Mpp-(a*dm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dm>min_y:
                                    if a*dm<max_y:
                                        if Mpp!=0:
                                            y=(a*dm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"dm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==6:
                        # 1 m (m) = 1 m
                        a=int(round(min_y/m))
                        stop=0
                        d=0
                        c=abs(((a+1)*m)/Mpp-(a*m/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*m>min_y:
                                    if a*m<max_y:
                                        if Mpp!=0:
                                            y=(a*m-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"m", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==5:
                        # 1 dam (dam) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dam)/Mpp-(a*dam/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dam>min_y:
                                    if a*dam<max_y:
                                        if Mpp!=0:
                                            y=(a*dam-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"dam", fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==4:
                        # 1 hm (hm) = 100 m
                        a=int(round(min_y/hm))
                        stop=0
                        d=0
                        c=abs(((a+1)*hm)/Mpp-(a*hm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*hm>min_y:
                                    if a*hm<max_y:
                                        if Mpp!=0:
                                            y=(a*hm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"hm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==3:
                        # 1 km (km) = 1000 m
                        a=int(round(min_y/km))
                        stop=0
                        d=0
                        c=abs(((a+1)*km)/Mpp-(a*km/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*km>min_y:
                                    if a*km<max_y:
                                        if Mpp!=0:
                                            y=(a*km-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"km", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==2:
                        # 1 ae (ae) = 149597870691 m
                        a=int(round(min_y/ae))
                        stop=0
                        d=0
                        c=abs(((a+1)*ae)/Mpp-(a*ae/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*ae>min_y:
                                    if a*ae<max_y:
                                        if Mpp!=0:
                                            y=(a*ae-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"AE", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==1:
                        # 1 Lj (Lj) = 9460528000000000 m
                        a=int(round(min_y/Lj))
                        stop=0
                        d=0
                        c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*Lj>min_y:
                                    if a*Lj<max_y:
                                        if Mpp!=0:
                                            y=(a*Lj-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==1:
                        # 1 Lj (Lj) = 9460528000000000 m
                        a=int(round(min_y/Lj))
                        stop=0
                        d=0
                        c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*Lj>min_y:
                                    if a*Lj<max_y:
                                        if Mpp!=0:
                                            y=(a*Lj-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==0:
                        # 1 pc (Lj) = 30856776000000000 m
                        a=int(round(min_y/pc))
                        stop=0
                        d=0
                        c=abs(((a+1)*pc)/Mpp-(a*pc/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*pc>min_y:
                                    if a*pc<max_y:
                                        if Mpp!=0:
                                            y=(a*pc-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"pc", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==-1:
                        # Format unbekannt:
                        if e==0:
                            f=1
                            g=0
                            stop=0
                            d=0
                            while g==0:
                                h=(int(round(min_y/10**f)+1)*10**f)/Mpp-(int(round(min_y/10**f))*10**f)/Mpp
                                if h>20 and h<height_y_2:
                                    a=int(round(min_y/10**f))
                                    c=abs(((a+1)*10**f)/Mpp-(a*10**f/Mpp))
                                    g=1
                                else:
                                    f=f+1
                            while stop==0:
                                #print(a)
                                if a*10**f>min_y:
                                    if a*10**f<max_y:
                                        if Mpp!=0:
                                            y=-(a*10**f-Mitte_y)/Mpp
                                            b=height_y_2/2+y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"mE"+str(f), fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                    # Rechtes Canvas (yz):
                    e=0                     # Anzeige aus=0, an=1
                    Aktueller_Schritt=8     #0=Parsec, 1=Lj, 2=AE.....

                    if Aktueller_Schritt==8:
                        # 1 cm (cm) = 1 m
                        a=int(round(min_y/cm))
                        stop=0
                        d=0
                        c=abs(((a+1)*cm)/Mpp-(a*cm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*cm>min_y:
                                    if a*cm<max_y:
                                        if Mpp!=0:
                                            y=(a*cm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"cm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==7:
                        # 1 dm (dm) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dm)/Mpp-(a*dm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dm>min_y:
                                    if a*dm<max_y:
                                        if Mpp!=0:
                                            y=(a*dm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"dm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==6:
                        # 1 m (m) = 1 m
                        a=int(round(min_y/m))
                        stop=0
                        d=0
                        c=abs(((a+1)*m)/Mpp-(a*m/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*m>min_y:
                                    if a*m<max_y:
                                        if Mpp!=0:
                                            y=(a*m-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,9,4,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"m", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==5:
                        # 1 dam (dam) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dam)/Mpp-(a*dam/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dam>min_y:
                                    if a*dam<max_y:
                                        if Mpp!=0:
                                            y=(a*dam-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"dam", fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==4:
                        # 1 hm (hm) = 100 m
                        a=int(round(min_y/hm))
                        stop=0
                        d=0
                        c=abs(((a+1)*hm)/Mpp-(a*hm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*hm>min_y:
                                    if a*hm<max_y:
                                        if Mpp!=0:
                                            y=(a*hm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"hm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==3:
                        # 1 km (km) = 1000 m
                        a=int(round(min_y/km))
                        stop=0
                        d=0
                        c=abs(((a+1)*km)/Mpp-(a*km/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*km>min_y:
                                    if a*km<max_y:
                                        if Mpp!=0:
                                            y=(a*km-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"km", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==2:
                        # 1 ae (ae) = 149597870691 m
                        a=int(round(min_y/ae))
                        stop=0
                        d=0
                        c=abs(((a+1)*ae)/Mpp-(a*ae/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*ae>min_y:
                                    if a*ae<max_y:
                                        if Mpp!=0:
                                            y=(a*ae-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"AE", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==1:
                        # 1 Lj (Lj) = 9460528000000000 m
                        a=int(round(min_y/Lj))
                        stop=0
                        d=0
                        c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*Lj>min_y:
                                    if a*Lj<max_y:
                                        if Mpp!=0:
                                            y=(a*Lj-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==0:
                        # 1 pc (Lj) = 30856776000000000 m
                        a=int(round(min_y/pc))
                        stop=0
                        d=0
                        c=abs(((a+1)*pc)/Mpp-(a*pc/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*pc>min_y:
                                    if a*pc<max_y:
                                        if Mpp!=0:
                                            y=(a*pc-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"pc", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==-1:
                        # Format unbekannt:
                        if e==0:
                            f=1
                            g=0
                            stop=0
                            d=0
                            while g==0:
                                h=(int(round(min_y/10**f)+1)*10**f)/Mpp-(int(round(min_y/10**f))*10**f)/Mpp
                                if h>20 and h<height_y_2:
                                    a=int(round(min_y/10**f))
                                    c=abs(((a+1)*10**f)/Mpp-(a*10**f/Mpp))
                                    g=1
                                else:
                                    f=f+1
                            while stop==0:
                                if a*10**f>min_y:
                                    if a*10**f<max_y:
                                        if Mpp!=0:
                                            y=(a*10**f-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"mE"+str(f), fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                    # xz - z (height_y_2) - Achsen max und min:
                    min_y=Mitte_z-height_y_2*Mpp/2                                # Oberes Ende!
                    max_y=Mitte_z+height_y_2*Mpp/2                                # Unteres Ende!
                    # Die Skala soll ermitelt werden:
                    # Wir teilen min durch die Längen der einheiten und runden diese zu einer int, dann zeichnen wir alle relevanten einund setzen Einheitenanzahl eins höher
                    e=0                     # Anzeige aus=0, an=1
                    Aktueller_Schritt=8     #0=Parsec, 1=Lj, 2=AE.....
                    if Aktueller_Schritt==8:
                        # 1 cm (cm) = 1 m
                        a=int(round(min_y/cm))
                        stop=0
                        d=0
                        c=abs(((a+1)*cm)/Mpp-(a*cm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*cm>min_y:
                                    if a*cm<max_y:
                                        if Mpp!=0:
                                            y=(a*cm-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"cm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==7:
                        # 1 dm (dm) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dm)/Mpp-(a*dm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dm>min_y:
                                    if a*dm<max_y:
                                        if Mpp!=0:
                                            y=(a*dm-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"dm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==6:
                        # 1 m (m) = 1 m
                        a=int(round(min_y/m))
                        stop=0
                        d=0
                        c=abs(((a+1)*m)/Mpp-(a*m/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*m>min_y:
                                    if a*m<max_y:
                                        if Mpp!=0:
                                            y=(a*m-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"m", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==5:
                        # 1 dam (dam) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dam)/Mpp-(a*dam/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dam>min_y:
                                    if a*dam<max_y:
                                        if Mpp!=0:
                                            y=(a*dam-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"dam", fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==4:
                        # 1 hm (hm) = 100 m
                        a=int(round(min_y/hm))
                        stop=0
                        d=0
                        c=abs(((a+1)*hm)/Mpp-(a*hm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*hm>min_y:
                                    if a*hm<max_y:
                                        if Mpp!=0:
                                            y=(a*hm-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"hm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==3:
                        # 1 km (km) = 1000 m
                        a=int(round(min_y/km))
                        stop=0
                        d=0
                        c=abs(((a+1)*km)/Mpp-(a*km/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*km>min_y:
                                    if a*km<max_y:
                                        if Mpp!=0:
                                            y=(a*km-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"km", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==2:
                        # 1 ae (ae) = 149597870691 m
                        a=int(round(min_y/ae))
                        stop=0
                        d=0
                        c=abs(((a+1)*ae)/Mpp-(a*ae/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*ae>min_y:
                                    if a*ae<max_y:
                                        if Mpp!=0:
                                            y=(a*ae-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"AE", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==1:
                        # 1 Lj (Lj) = 9460528000000000 m
                        a=int(round(min_y/Lj))
                        stop=0
                        d=0
                        c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*Lj>min_y:
                                    if a*Lj<max_y:
                                        if Mpp!=0:
                                            y=(a*Lj-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==0:
                        # 1 pc (Lj) = 30856776000000000 m
                        a=int(round(min_y/pc))
                        stop=0
                        d=0
                        c=abs(((a+1)*pc)/Mpp-(a*pc/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*pc>min_y:
                                    if a*pc<max_y:
                                        if Mpp!=0:
                                            y=(a*pc-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"pc", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==-1:
                        # Format unbekannt:
                        if e==0:
                            f=1
                            g=0
                            stop=0
                            d=0
                            while g==0:
                                h=(int(round(min_y/10**f)+1)*10**f)/Mpp-(int(round(min_y/10**f))*10**f)/Mpp
                                if h>20 and h<height_y_2:
                                    a=int(round(min_y/10**f))
                                    c=abs(((a+1)*10**f)/Mpp-(a*10**f/Mpp))
                                    g=1
                                else:
                                    f=f+1
                            while stop==0:
                                if a*10**f>min_y:
                                    if a*10**f<max_y:
                                        if Mpp!=0:
                                            y=(a*10**f-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"mE"+str(f), fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                    # Nun werden alle Werte eingezeichnet die auf die Anforderungen zutreffen:

            def Normalisieren():
                max_min()
                Masstab_berechnen()
                Einzeichnen()
            Normalisieren_Button=Button(frame_22,text='Normalisieren',command=Normalisieren,width=20, bd=2).place(x=700,y=350)

            def Up(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y-5*self.Oe_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y-5*self.Oe_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-5*self.Oe_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Control-Up>",Up)

            def Down(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+5*self.Oe_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+5*self.Oe_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+5*self.Oe_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Control-Down>",Down)

            def Left(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+5*self.Oe_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-5*self.Oe_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+5*self.Oe_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Control-Left>",Left)

            def Right(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x-5*self.Oe_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+5*self.Oe_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x-5*self.Oe_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Control-Right>",Right)


            def Up(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y-50*self.Oe_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y-50*self.Oe_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-50*self.Oe_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Up>",Up)

            def Down(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+50*self.Oe_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+50*self.Oe_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+50*self.Oe_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Down>",Down)

            def Left(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+50*self.Oe_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-50*self.Oe_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+50*self.Oe_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Left>",Left)

            def Right(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x-50*self.Oe_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+50*self.Oe_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x-50*self.Oe_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Right>",Right)

            def Zoom_2(event):
                Canvas_xy.focus_set()
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        x_zoom_xy=event.x-57
                        y_zoom_xy=event.y-36
                        if event.delta < 0:
                            self.Oe_Mpp=self.Oe_Mpp*(0.8)
                            self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                        else:
                            self.Oe_Mpp=self.Oe_Mpp*(1.2)
                            self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        x_zoom_xy=event.x-509
                        y_zoom_xy=event.y-36
                        if event.delta < 0:
                            self.Oe_Mpp=self.Oe_Mpp*(0.8)
                            self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                            self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                        else:
                            self.Oe_Mpp=self.Oe_Mpp*(1.2)
                            self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                            self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        x_zoom_xy=event.x-57
                        y_zoom_xy=event.y-339
                        if event.delta < 0:
                            self.Oe_Mpp=self.Oe_Mpp*(0.8)
                            #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                        else:
                            self.Oe_Mpp=self.Oe_Mpp*(1.2)
                            #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                Einzeichnen()

            Objekt_erstellen_1.bind("<Control-MouseWheel>",Zoom_2)

            def Zoom(event):
                Canvas_xy.focus_set()
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        x_zoom_xy=event.x-57
                        y_zoom_xy=event.y-36
                        if event.delta < 0:
                            self.Oe_Mpp=self.Oe_Mpp*(0.8)
                            #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                        else:
                            self.Oe_Mpp=self.Oe_Mpp*(1.2)
                            #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        x_zoom_xy=event.x-509
                        y_zoom_xy=event.y-36
                        if event.delta < 0:
                            self.Oe_Mpp=self.Oe_Mpp*(0.8)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                            #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                        else:
                            self.Oe_Mpp=self.Oe_Mpp*(1.2)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                            #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        x_zoom_xy=event.x-57
                        y_zoom_xy=event.y-339
                        if event.delta < 0:
                            self.Oe_Mpp=self.Oe_Mpp*(0.8)
                            #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                        else:
                            self.Oe_Mpp=self.Oe_Mpp*(1.2)
                            #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                Einzeichnen()

            Objekt_erstellen_1.bind("<MouseWheel>",Zoom)

            def Click_xy(event):
                # xy:
                        self.Oe_akt_Tem=0
                        self.Oe_akt_movX=0
                        self.Oe_akt_movY=0
                        self.Oe_akt_movZ=0
                        x_click=event.x#-57
                        y_click=event.y#-36
                        self.Oe_akt_X=((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_click-width_x_2/2)*self.Oe_Mpp)
                        self.Oe_akt_Y=((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_click)*self.Oe_Mpp)
                        self.Oe_akt_Z=(self.Oe_Mittelpunkt_z)
                        self.Oe_akt_Pos=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Click_xz(event):
                # xz:
                        self.Oe_akt_Tem=0
                        self.Oe_akt_movX=0
                        self.Oe_akt_movY=0
                        self.Oe_akt_movZ=0
                        x_click=event.x#-57
                        y_click=event.y#-339
                        self.Oe_akt_X=((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_click-width_x_2/2)*self.Oe_Mpp)
                        self.Oe_akt_Z=((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_click)*self.Oe_Mpp)
                        self.Oe_akt_Y=(self.Oe_Mittelpunkt_y)
                        self.Oe_akt_Pos=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Click_yz(event):
                # yz:
                        self.Oe_akt_Tem=0
                        self.Oe_akt_movX=0
                        self.Oe_akt_movY=0
                        self.Oe_akt_movZ=0
                        x_click=event.x#-509
                        y_click=event.y#-36
                        self.Oe_akt_Z=((self.Oe_Mittelpunkt_z/self.Oe_Mpp-x_click+width_x_2/2)*self.Oe_Mpp)
                        self.Oe_akt_Y=((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_click)*self.Oe_Mpp)
                        self.Oe_akt_X=(self.Oe_Mittelpunkt_x)
                        self.Oe_akt_Pos=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Click_Move_xy(event):
                # xy:
                        self.Oe="xy"
                        x_click=event.x#-57
                        y_click=event.y#-36
                        self.Oe_akt_movX=((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_click-width_x_2/2)*self.Oe_Mpp)-self.Oe_akt_X
                        self.Oe_akt_movY=((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_click)*self.Oe_Mpp)-self.Oe_akt_Y
                        self.Oe_akt_movZ=(self.Oe_Mittelpunkt_z+1)-self.Oe_akt_Z
                        self.Oe_akt_Tem=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Click_Move_xz(event):
                # xz:
                        self.Oe="xz"
                        x_click=event.x#-57
                        y_click=event.y#-339
                        self.Oe_akt_movX=((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_click-width_x_2/2)*self.Oe_Mpp)-self.Oe_akt_X
                        self.Oe_akt_movZ=((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_click)*self.Oe_Mpp)-self.Oe_akt_Z
                        self.Oe_akt_movY=(self.Oe_Mittelpunkt_y+1)-self.Oe_akt_Y
                        self.Oe_akt_Tem=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Click_Move_yz(event):
                # yz:
                        self.Oe="yz"
                        x_click=event.x#-509
                        y_click=event.y#-36
                        self.Oe_akt_movZ=(((self.Oe_Mittelpunkt_z/self.Oe_Mpp-x_click+width_x_2/2)*self.Oe_Mpp)-self.Oe_akt_Z)
                        self.Oe_akt_movY=((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_click)*self.Oe_Mpp)-self.Oe_akt_Y
                        self.Oe_akt_movX=(self.Oe_Mittelpunkt_x+1)-self.Oe_akt_X
                        self.Oe_akt_Tem=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Unclick (event):
                if type(event.widget)==Canvas :
                    # print(type(event.widget))
                    self.Oe_akt_Tem=0
                    self.Oe_akt_Pos=0
                    Mpp=self.Oe_Mpp
                    speed=1000*(String_Number.String_to_Number(self.Geschwindigkeit_pro_Pixel.get()))
                    if self.Oe=="xy":
                        self.X_Geschwindigkeit.set(String_Number.Number_to_String(self.Oe_akt_movX/Mpp*speed))
                        self.Y_Geschwindigkeit.set(String_Number.Number_to_String(self.Oe_akt_movY/Mpp*speed))
                        self.Z_Geschwindigkeit.set(str(0))
                    if self.Oe=="xz":
                        self.X_Geschwindigkeit.set(String_Number.Number_to_String(self.Oe_akt_movX/Mpp*speed))
                        self.Y_Geschwindigkeit.set(str(0))
                        self.Z_Geschwindigkeit.set(String_Number.Number_to_String(self.Oe_akt_movZ/Mpp*speed))
                    if self.Oe=="yz":
                        self.Y_Geschwindigkeit.set(String_Number.Number_to_String(self.Oe_akt_movY/Mpp*speed))
                        self.X_Geschwindigkeit.set(str(0))
                        self.Z_Geschwindigkeit.set(String_Number.Number_to_String(self.Oe_akt_movZ/Mpp*speed))
                    self.X_Position.set(String_Number.Number_to_String(self.Oe_akt_X))
                    self.Y_Position.set(String_Number.Number_to_String(self.Oe_akt_Y))
                    self.Z_Position.set(String_Number.Number_to_String(self.Oe_akt_Z))

            def Mouse_Movement_xy(event):
                if Canvas_xy.canvasx(event.x)>10 and Canvas_xy.canvasy(event.y)>10:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten1.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                elif Canvas_xy.canvasx(event.x)<10 or Canvas_xy.canvasy(event.y)<10:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                # Koordinatenanzeige:
                if self.Oe_Mpp!=0:
                    self.Oe_X.set(String_Number.Number_to_String(round(((self.Oe_Mittelpunkt_x/self.Oe_Mpp+event.x-width_x_2/2)*self.Oe_Mpp),1)))
                    self.Oe_Y.set(String_Number.Number_to_String(round(((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-event.y)*self.Oe_Mpp),1)))
                self.Oe_Z.set('0.0')

            def Mouse_Movement_yz(event):
                if Canvas_yz.canvasx(event.x)>0 and Canvas_yz.canvasy(event.y)>10 and not Canvas_yz.canvasx(event.x)>440 and not Canvas_yz.canvasy(event.y)>285:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten2.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                elif Canvas_yz.canvasy(event.y)<10 or Canvas_yz.canvasx(event.x)>440 or Canvas_yz.canvasy(event.y)>285:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                # Koordinatenanzeige:
                if self.Oe_Mpp!=0:
                    self.Oe_Z.set(String_Number.Number_to_String(round(((self.Oe_Mittelpunkt_z/self.Oe_Mpp-event.x+width_x_2/2)*self.Oe_Mpp),1)))
                    self.Oe_Y.set(String_Number.Number_to_String(round(((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-event.y)*self.Oe_Mpp),1)))
                self.Oe_X.set('0.0')

            def Mouse_Movement_xz(event):
                if not Canvas_xz.canvasx(event.x)<10 and Canvas_xz.canvasy(event.y)>0 and not Canvas_xz.canvasx(event.x)>440 and not Canvas_xz.canvasy(event.y)>285:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten3.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                elif Canvas_xz.canvasx(event.x)<10 or Canvas_xz.canvasy(event.y)<10 or Canvas_xz.canvasx(event.x)>440 or Canvas_xz.canvasy(event.y)>285:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                # Koordinatenanzeige:
                if self.Oe_Mpp!=0:
                    self.Oe_X.set(String_Number.Number_to_String(round(((self.Oe_Mittelpunkt_x/self.Oe_Mpp+event.x-width_x_2/2)*self.Oe_Mpp),1)))
                    self.Oe_Z.set(String_Number.Number_to_String(round(((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-event.y)*self.Oe_Mpp),1)))
                self.Oe_Y.set('0.0')

            Canvas_xy = Canvas (frame_22, width=width_x_2, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_xy.place (x=42,y=5)
            Canvas_xy.bind('<Motion>',Mouse_Movement_xy)
            self.xy_koord = PhotoImage(file = '../Icon/Koordinaten/xy.gif')
            Canvas_xy.create_image(12,height_y_2-39, image = self.xy_koord, anchor = NW)

            Canvas_yz = Canvas (frame_22, width=width_x_2, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_yz.place (x=49+width_x_2,y=5)
            Canvas_yz.bind('<Motion>',Mouse_Movement_yz)
            self.yz_koord = PhotoImage(file = '../Icon/Koordinaten/yz.gif')
            Canvas_yz.create_image(width_x_2-39, height_y_2-39, image = self.yz_koord, anchor = NW)

            Canvas_xz = Canvas (frame_22, width=width_x_2, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_xz.place (x=42,y=12+height_y_2)
            Canvas_xz.bind('<Motion>',Mouse_Movement_xz)
            self.xz_koord = PhotoImage(file = '../Icon/Koordinaten/xz.gif')
            Canvas_xz.create_image(12, height_y_2-39, image = self.xz_koord, anchor = NW)

            Koordinaten = Canvas(frame_22, width = 154, height = 107)
            Koordinaten.place(x=49+width_x_2,y=13+height_y_2)
            self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
            Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)

            Canvas_xy.bind("<Button-1>",Click_xy)
            Canvas_xz.bind("<Button-1>",Click_xz)
            Canvas_yz.bind("<Button-1>",Click_yz)
            Canvas_xy.bind("<B1-Motion>",Click_Move_xy)
            Canvas_xz.bind("<B1-Motion>",Click_Move_xz)
            Canvas_yz.bind("<B1-Motion>",Click_Move_yz)
            Objekt_erstellen_1.bind("<ButtonRelease-1>",Unclick)

            Canvas_coord_yz = Canvas (frame_22, width=33, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_coord_yz.place (x=53+2*width_x_2,y=5)

            Canvas_coord_xz = Canvas (frame_22, width=33, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_coord_xz.place (x=8,y=12+height_y_2)

            Canvas_coord_xy = Canvas (frame_22, width=33, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_coord_xy.place (x=8,y=5)

            label_13_frame_11 = Labelframe(frame_11, width=995, height=180, text='Andere')
            label_13_frame_11.place(x=10, y=10)

            Name_label_1 = Label(label_13_frame_11, text='Name:')
            Name_label_1.place(x=10, y=10)

            self.Name = StringVar()
            self.Name.set ("")
            Name_label_2 = Entry(label_13_frame_11, justify=RIGHT, textvariable = self.Name, bd=2)
            Name_label_2.place(x=250, y=10)

            def Random_Name_1 (*args):
                self.Name.set(Namensgenerator.Namensgenerator_Buchstaben())

            Random_Name=Button(label_13_frame_11, text="Random", command=Random_Name_1)
            Random_Name.place (x=475, y=6)

            Acht=Canvas(label_13_frame_11, width = 20, height = 20)
            Acht.place(x=566,y=10)
            self.Alert_1 = PhotoImage(file = '../Icon/Alert Icon/16/alert.gif')
            Acht.create_image(2, 2, image = self.Alert_1, anchor = NW)

            self.Name_Analyse=StringVar()
            self.Name_Analyse.set('Bitte geben Sie einen Namen ein.')
            Name_label_2 = Label(label_13_frame_11, textvariable=self.Name_Analyse)
            Name_label_2.place (x=610,y=10)

            def Name_Verifizieren(*args):
                Get_Name = self.Name.get()
                abc=Verifizieren.Namen_Verifizeren(Get_Name,self.Newton_Simulator.Name_Body)
                if abc==0:
                    self.Alert_1=PhotoImage(file = '../Icon/Alert Icon/16/alert.gif')
                    Acht.create_image(2, 2, image = self.Alert_1, anchor = NW)
                    self.Name_Analyse.set('Bitte geben Sie einen Namen ein.')
                elif abc==1:
                    self.Alert_1=PhotoImage(file = '../Icon/Alert Icon/16/alert.gif')
                    Acht.create_image(2, 2, image = self.Alert_1, anchor = NW)
                    self.Name_Analyse.set('Der von ihnen gewählte Name wird bereits benutzt.')
                elif abc==2:
                    self.Alert_1=PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
                    Acht.create_image(2, 2, image = self.Alert_1, anchor = NW)
                    self.Name_Analyse.set('Dieser Name wurde noch keinem anderen Körper zugeordnet.')
            self.Name.trace("w", Name_Verifizieren)

            Typ_label_1 = Label(label_13_frame_11, text='Typ:')
            Typ_label_1.place(x=10, y=40)

            self.Objekttypen =["Galaxie", "Stern", "Schwarzes-Loch", "Planet", "Zwergplanet", "Planemo", "Mond", "Satellit", "Asteroid", "Komet"]
            self.Typ_label_3=StringVar()
            self.Typ_label_3=''
            Typ_label_2 = ttk.Combobox(label_13_frame_11, justify=RIGHT, values=self.Objekttypen, textvariable=self.Typ_label_3)
            Typ_label_2.place(x=250, y=40)

            Masse_Label_1 = Label(label_13_frame_11, text='Masse:')
            Masse_Label_1.place(x=10, y=70)

            self.Masse = StringVar()
            self.Masse.set ("1")
            Masse_2_label_2_frame_1 = Entry(label_13_frame_11, justify=RIGHT, textvariable = self.Masse, bd=2)
            Masse_2_label_2_frame_1.place(x=250, y=70)

            def Masse_Verifizieren(*args):
                Get_Masse = self.Masse.get()
                self.Masse.set(Verifizieren.Verifizieren_ohne_Minus(Get_Masse))
                b=String_Number.String_to_Number(Get_Masse)
                a=b/5.9736E24
                self.Erdmassen.set(String_Number.Number_to_String(round(a,4)))
                Dichte_Verifizieren()
            self.Masse.trace("w", Masse_Verifizieren)

            Masse_3_label_1_frame_1 = Label(label_13_frame_11, text="[kg]:")
            Masse_3_label_1_frame_1.place (x=380, y=70)

            Ges_Erdmassen_Label_1 = Label(label_13_frame_11, text='In Erdmassen:')
            Ges_Erdmassen_Label_1.place(x=475, y=70)

            self.Erdmassen = StringVar()
            self.Erdmassen.set ("0.0")
            Ges_Erdmassen_2_label_2_frame_1 = Label(label_13_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Erdmassen, bd=2, width=17, anchor=E)
            Ges_Erdmassen_2_label_2_frame_1.place(x=620, y=70)

            Radius_Label_1 = Label(label_13_frame_11, text='Radius:')
            Radius_Label_1.place(x=10, y=100)

            self.Radius = StringVar()
            self.Radius.set ("1")
            Radius_2_label_2_frame_1 = Entry(label_13_frame_11, justify=RIGHT, textvariable = self.Radius, bd=2)
            Radius_2_label_2_frame_1.place(x=250, y=100)

            def Radius_Verifizieren(*args):
                Get_Radius = self.Radius.get()
                self.Radius.set(Verifizieren.Verifizieren(Get_Radius))
                b=String_Number.String_to_Number(Get_Radius)
                a=b/6378137
                self.Erdradien.set(String_Number.Number_to_String(round(a,4)))
                Dichte_Verifizieren()
            self.Radius.trace("w", Radius_Verifizieren)

            Radius_3_label_1_frame_1 = Label(label_13_frame_11, text="[m]:")
            Radius_3_label_1_frame_1.place (x=380, y=100)

            Ges_Erdradius_Label_1 = Label(label_13_frame_11, text='In Erdradien:')
            Ges_Erdradius_Label_1.place(x=475, y=100)

            self.Erdradien = StringVar()
            self.Erdradien.set ("0.0")
            Ges_Erdradien_2_label_2_frame_1 = Label(label_13_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Erdradien, bd=2, width=17, anchor=E)
            Ges_Erdradien_2_label_2_frame_1.place(x=620, y=100)

            Dichte_Label_1 = Label(label_13_frame_11, text='Dichte ('+chr(0x03C1)+'):')
            Dichte_Label_1.place(x=10, y=130)

            self.Dichte = StringVar()
            self.Dichte.set ("0.2387")
            Dichte_2_label_2_frame_1 = Label(label_13_frame_11, justify=RIGHT, relief=SUNKEN , textvariable = self.Dichte, bd=2, width=17, anchor=E)
            Dichte_2_label_2_frame_1.place(x=250, y=130)

            def Dichte_Verifizieren(*args):
                Get_Masse = String_Number.String_to_Number(self.Masse.get())
                Get_Radius = String_Number.String_to_Number(self.Radius.get())
                b=Basic_Calculations.Dichte(Get_Masse,Get_Radius)
                c=0
                c=b/5497.281
                self.Dichte.set(String_Number.Number_to_String(round(b,4)))
                self.Erddichte.set(String_Number.Number_to_String(round(c,4)))

            Dichte_3_label_1_frame_1 = Label(label_13_frame_11, text="[kg/m³]:")
            Dichte_3_label_1_frame_1.place (x=380, y=130)

            Ges_Erddichte_Label_1 = Label(label_13_frame_11, text='In Erddichten:')
            Ges_Erddichte_Label_1.place(x=475, y=130)

            self.Erddichte = StringVar()
            self.Erddichte.set ("0.0")
            Ges_Erddichte_2_label_2_frame_1 = Label(label_13_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Erddichte, bd=2, width=17, anchor=E)
            Ges_Erddichte_2_label_2_frame_1.place(x=620, y=130)

            label_11_frame_11 = Labelframe(frame_11, width=995, height=120, text='Objektposition')
            label_11_frame_11.place(x=10, y=190)

            def Abstand_Verifizieren(*args):
                Get_X = String_Number.String_to_Number(self.X_Position.get())
                Get_Y = String_Number.String_to_Number(self.Y_Position.get())
                Get_Z = String_Number.String_to_Number(self.Z_Position.get())
                b=Basic_Calculations.Abstand(Get_X,Get_Y,Get_Z)
                self.Abstand_1.set(String_Number.Number_to_String(b))
                self.Abstand_2.set(String_Number.Number_to_String(round((b/149597870691),4)))

            X_Position_Label_1 = Label(label_11_frame_11, text='X-Position:')
            X_Position_Label_1.place(x=10, y=10)

            self.X_Position = StringVar()
            self.X_Position.set ("0")
            X_Position_2_label_2_frame_1 = Entry(label_11_frame_11, justify=RIGHT, textvariable = self.X_Position, bd=2)
            X_Position_2_label_2_frame_1.place(x=250, y=10)

            def X_Position_Verifizieren(*args):
                Get_X_Position = self.X_Position.get()
                self.X_Position.set(Verifizieren.Verifizieren_mit_Null(Get_X_Position))
                Abstand_Verifizieren()
                Positionsanalyse()
            self.X_Position.trace("w", X_Position_Verifizieren)

            X_Position_3_label_1_frame_1 = Label(label_11_frame_11, text="[m]:")
            X_Position_3_label_1_frame_1.place (x=380, y=10)

            Y_Position_Label_1 = Label(label_11_frame_11, text='Y-Position:')
            Y_Position_Label_1.place(x=10, y=40)

            self.Y_Position = StringVar()
            self.Y_Position.set ("0")
            Y_Position_2_label_2_frame_1 = Entry(label_11_frame_11, justify=RIGHT, textvariable = self.Y_Position, bd=2)
            Y_Position_2_label_2_frame_1.place(x=250, y=40)

            def Y_Position_Verifizieren(*args):
                Get_Y_Position = self.Y_Position.get()
                self.Y_Position.set(Verifizieren.Verifizieren_mit_Null(Get_Y_Position))
                Abstand_Verifizieren()
                Positionsanalyse()
            self.Y_Position.trace("w", Y_Position_Verifizieren)

            Y_Position_3_label_1_frame_1 = Label(label_11_frame_11, text="[m]:")
            Y_Position_3_label_1_frame_1.place (x=380, y=40)

            Z_Position_Label_1 = Label(label_11_frame_11, text='Z-Position:')
            Z_Position_Label_1.place(x=10, y=70)

            self.Z_Position = StringVar()
            self.Z_Position.set ("0")
            Z_Position_2_label_2_frame_1 = Entry(label_11_frame_11, justify=RIGHT, textvariable = self.Z_Position, bd=2)
            Z_Position_2_label_2_frame_1.place(x=250, y=70)

            def Z_Position_Verifizieren(*args):
                Get_Z_Position = self.Z_Position.get()
                self.Z_Position.set(Verifizieren.Verifizieren_mit_Null(Get_Z_Position))
                Abstand_Verifizieren()
                Positionsanalyse()
            self.Z_Position.trace("w", Z_Position_Verifizieren)

            Z_Position_3_label_1_frame_1 = Label(label_11_frame_11, text="[m]:")
            Z_Position_3_label_1_frame_1.place (x=380, y=70)

            def Positionsanalyse():
                Get_X_Position = self.X_Position.get()
                Get_X = String_Number.String_to_Number(Get_X_Position)
                Get_Y_Position = self.Y_Position.get()
                Get_Y = String_Number.String_to_Number(Get_Y_Position)
                Get_Z_Position = self.Z_Position.get()
                Get_Z = String_Number.String_to_Number(Get_Z_Position)
                # Vergleich mit anderen Planetenpositionen:
                x=0                             # Kontrollvariabel
                for i in range(0,len(self.Newton_Simulator.Name_Body)):
                    if Get_X==self.Newton_Simulator.X[i][0]:
                        if Get_Y==self.Newton_Simulator.Y[i][0]:
                            if Get_Z==self.Newton_Simulator.Z[i][0]:
                                x=1
                    if x==1:
                        break
                if x==1:
                    self.Posi_2 = PhotoImage(file = '../Icon/Alert Icon/16/alert.gif')
                    Position_2.create_image(2, 2, image = self.Posi_2, anchor = NW)
                    self.Positionsanalyse.set('Andere Körper auf selber Position.')
                if x==0:
                    self.Posi_2 = PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
                    Position_2.create_image(2, 2, image = self.Posi_2, anchor = NW)
                    self.Positionsanalyse.set('Position frei.')
                self.Newton_Simulator.Maximalwertsuche()
                self.Objekt_gesetzt=1
                self.Tempo_gesetzt=1
                self.Oe_akt_Pos=0
                self.Oe_akt_Tem=0
                max_min()
                Masstab_berechnen()
                Einzeichnen()


            Position_2=Canvas(label_11_frame_11, width = 20, height = 20)
            Position_2.place(x=566,y=10)
            self.Posi_2 = PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
            Position_2.create_image(2, 2, image = self.Posi_2, anchor = NW)

            self.Positionsanalyse=StringVar()
            Positionsanalyse()
            Positionsana_label_4 = Label(label_11_frame_11, textvariable=self.Positionsanalyse)
            Positionsana_label_4.place (x=610,y=10)

            Ges_Abstand_Label_1 = Label(label_11_frame_11, text='Abstand zum Ursprung:')
            Ges_Abstand_Label_1.place(x=475, y=40)

            self.Abstand_1 = StringVar()
            self.Abstand_1.set ("0")
            Ges_Abstand_2_label_2_frame_1 = Label(label_11_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Abstand_1, bd=2, width=17, anchor=E)
            Ges_Abstand_2_label_2_frame_1.place(x=620, y=40)

            Ges_Abstand_Label_2 = Label(label_11_frame_11, text='[m]')
            Ges_Abstand_Label_2.place(x=750, y=40)


            Ges_Abstand_Label_2 = Label(label_11_frame_11, text='In AE:')
            Ges_Abstand_Label_2.place(x=475, y=70)

            self.Abstand_2 = StringVar()
            self.Abstand_2.set ("0")
            Ges_Abstand_3_label_2_frame_1 = Label(label_11_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Abstand_2, bd=2, width=17, anchor=E)
            Ges_Abstand_3_label_2_frame_1.place(x=620, y=70)

            Ges_Abstand_Label_3 = Label(label_11_frame_11, text='[AE]')
            Ges_Abstand_Label_3.place(x=750, y=70)


            label_12_frame_11 = Labelframe(frame_11, width=995, height=120, text='Objektgeschwindigkeit')
            label_12_frame_11.place(x=10, y=310)

            X_Geschwindigkeit_Label_1 = Label(label_12_frame_11, text='Geschwindigkeit in X-Richtung:')
            X_Geschwindigkeit_Label_1.place(x=10, y=10)

            self.X_Geschwindigkeit = StringVar()
            self.X_Geschwindigkeit.set ("0")
            X_Geschwindigkeit_2_label_2_frame_1 = Entry(label_12_frame_11, justify=RIGHT, textvariable = self.X_Geschwindigkeit, bd=2)
            X_Geschwindigkeit_2_label_2_frame_1.place(x=250, y=10)

            def X_Geschwindigkeit_Verifizieren(*args):
                Get_X_Geschwindigkeit = self.X_Geschwindigkeit.get()
                self.X_Geschwindigkeit.set(Verifizieren.Verifizieren_mit_Null(Get_X_Geschwindigkeit))
                Geschwindigkeit_Verifizieren()
            self.X_Geschwindigkeit.trace("w", X_Geschwindigkeit_Verifizieren)

            X_Geschwindigkeit_3_label_1_frame_1 = Label(label_12_frame_11, text="[m/s]:")
            X_Geschwindigkeit_3_label_1_frame_1.place (x=380, y=10)

            Y_Geschwindigkeit_Label_1 = Label(label_12_frame_11, text='Geschwindigkeit in Y-Richtung:')
            Y_Geschwindigkeit_Label_1.place(x=10, y=40)

            self.Y_Geschwindigkeit = StringVar()
            self.Y_Geschwindigkeit.set ("0")
            Y_Geschwindigkeit_2_label_2_frame_1 = Entry(label_12_frame_11, justify=RIGHT, textvariable = self.Y_Geschwindigkeit, bd=2)
            Y_Geschwindigkeit_2_label_2_frame_1.place(x=250, y=40)

            def Y_Geschwindigkeit_Verifizieren(*args):
                Get_Y_Geschwindigkeit = self.Y_Geschwindigkeit.get()
                self.Y_Geschwindigkeit.set(Verifizieren.Verifizieren_mit_Null(Get_Y_Geschwindigkeit))
                Geschwindigkeit_Verifizieren()
            self.Y_Geschwindigkeit.trace("w", Y_Geschwindigkeit_Verifizieren)

            Y_Geschwindigkeit_3_label_1_frame_1 = Label(label_12_frame_11, text="[m/s]:")
            Y_Geschwindigkeit_3_label_1_frame_1.place (x=380, y=40)

            Z_Geschwindigkeit_Label_1 = Label(label_12_frame_11, text='Geschwindigkeit in Z-Richtung:')
            Z_Geschwindigkeit_Label_1.place(x=10, y=70)

            self.Z_Geschwindigkeit = StringVar()
            self.Z_Geschwindigkeit.set ("0")
            Z_Geschwindigkeit_2_label_2_frame_1 = Entry(label_12_frame_11, justify=RIGHT, textvariable = self.Z_Geschwindigkeit, bd=2)
            Z_Geschwindigkeit_2_label_2_frame_1.place(x=250, y=70)

            def Z_Geschwindigkeit_Verifizieren(*args):
                Get_Z_Geschwindigkeit = self.Z_Geschwindigkeit.get()
                self.Z_Geschwindigkeit.set(Verifizieren.Verifizieren_mit_Null(Get_Z_Geschwindigkeit))
                Geschwindigkeit_Verifizieren()
            self.Z_Geschwindigkeit.trace("w", Z_Geschwindigkeit_Verifizieren)

            Z_Geschwindigkeit_3_label_1_frame_1 = Label(label_12_frame_11, text="[m/s]:")
            Z_Geschwindigkeit_3_label_1_frame_1.place (x=380, y=70)

            def Geschwindigkeit_Verifizieren():
                Get_X_Geschwindigkeit = self.X_Geschwindigkeit.get()
                Get_X = String_Number.String_to_Number(Get_X_Geschwindigkeit)
                Get_Y_Geschwindigkeit = self.Y_Geschwindigkeit.get()
                Get_Y = String_Number.String_to_Number(Get_Y_Geschwindigkeit)
                Get_Z_Geschwindigkeit = self.Z_Geschwindigkeit.get()
                Get_Z = String_Number.String_to_Number(Get_Z_Geschwindigkeit)
                b=Basic_Calculations.Abstand(Get_X,Get_Y,Get_Z)
                self.Geschwindigkeit_1.set(String_Number.Number_to_String(b))
                if b>=self.Newton_Simulator.Lichtgeschwindigkeit:
                    self.Alert_2 = PhotoImage(file = '../Icon/Alert Icon/16/alert.gif')
                    Acht_2.create_image(2, 2, image = self.Alert_2, anchor = NW)
                    self.Name_Analyse_2.set('Geschwindigkeit ist größer als die gewählte Lichtgeschwindigkeit.')
                elif b<self.Newton_Simulator.Lichtgeschwindigkeit:
                    self.Alert_2 = PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
                    Acht_2.create_image(2, 2, image = self.Alert_2, anchor = NW)
                    self.Name_Analyse_2.set('Geschwindigkeit im grünen Bereich.')
                self.Geschwindigkeit_2.set(String_Number.Number_to_String(round((b/29.78E3),4)))
                self.Objekt_Tempo_gesetzt=1
                max_min()
                Masstab_berechnen()
                Einzeichnen()


            Acht_2=Canvas(label_12_frame_11, width = 20, height = 20)
            Acht_2.place(x=566,y=10)
            self.Alert_2 = PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
            Acht_2.create_image(2, 2, image = self.Alert_2, anchor = NW)

            self.Name_Analyse_2=StringVar()
            self.Name_Analyse_2.set('Geschwindigkeit im grünen Bereich.')
            Name_label_4 = Label(label_12_frame_11, textvariable=self.Name_Analyse_2)
            Name_label_4.place (x=610,y=10)


            Ges_Geschwindigkeit_Label_1 = Label(label_12_frame_11, text='Geschwindigkeit:')
            Ges_Geschwindigkeit_Label_1.place(x=475, y=40)

            self.Geschwindigkeit_1 = StringVar()
            self.Geschwindigkeit_1.set ("0")
            Ges_Geschwindigkeit_2_label_2_frame_1 = Label(label_12_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Geschwindigkeit_1, bd=2, width=17, anchor=E)
            Ges_Geschwindigkeit_2_label_2_frame_1.place(x=620, y=40)

            Ges_Geschwindigkeit_Label_2 = Label(label_12_frame_11, text='[m/s]')
            Ges_Geschwindigkeit_Label_2.place(x=750, y=40)

            Ges_Geschwindigkeit_Label_2 = Label(label_12_frame_11, text='In Erdgeschwindigkeiten:')
            Ges_Geschwindigkeit_Label_2.place(x=475, y=70)

            self.Geschwindigkeit_2 = StringVar()
            self.Geschwindigkeit_2.set ("0")
            Ges_Geschwindigkeit_3_label_2_frame_1 = Label(label_12_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Geschwindigkeit_2, bd=2, width=17, anchor=E)
            Ges_Geschwindigkeit_3_label_2_frame_1.place(x=620, y=70)

            label_14_frame_11 = Labelframe(frame_11, width=995, height=60, text='Objektfarbe')
            label_14_frame_11.place(x=10, y=430)

            Color_Label_1 = Label(label_14_frame_11, text='Farbe:')
            Color_Label_1.place(x=10, y=10)

            Object_Color = Canvas(label_14_frame_11, width=20, height=20, background=self.Color_1)
            Object_Color.place(x=130, y=6)

            self.Color_2 = StringVar()
            self.Color_2.set(self.Color_1)
            Color_2_label_2_frame_1 = Label(label_14_frame_11, justify=RIGHT, textvariable = self.Color_2, relief=SUNKEN, bd=2,width=17, anchor=E)
            Color_2_label_2_frame_1.place(x=250, y=10)


            def Random_Color_1 (*args):
                self.Color_1=Randomcolor.Randomcolor()
                self.Color_2.set(self.Color_1)
                Object_Color.config(background=self.Color_1)

            Random_Color_1_Label=Button(label_14_frame_11, text="Random", command=Random_Color_1)
            Random_Color_1_Label.place (x=475, y=6)

            def Pick_Color_1 (*args):
                triple, hexstr = colorchooser.askcolor(parent=Objekt_erstellen_1)
                if hexstr!=None:
                    self.Color_1=hexstr
                    self.Color_2.set(self.Color_1)
                    Object_Color.config(background=self.Color_1)

            Pick_Color_2_Label=Button(label_14_frame_11, text="Farbe Auswählen", command=Pick_Color_1)
            Pick_Color_2_Label.place (x=625, y=6)

            def Mouse_Movement_11(event):
                modi=0
                Typ_label_2.config(state=NORMAL)
            def Mouse_Movement_22(event):
                modi=1
                Typ_label_2.config(state=DISABLED)
            frame_11.bind('<Enter>',Mouse_Movement_11)
            frame_22.bind('<Enter>',Mouse_Movement_22)
            Canvas_xy.bind('<Enter>',Mouse_Movement_22)
            Canvas_yz.bind('<Enter>',Mouse_Movement_22)
            Canvas_xz.bind('<Enter>',Mouse_Movement_22)
            label_13_frame_11.bind('<Enter>',Mouse_Movement_11)
            label_11_frame_11.bind('<Enter>',Mouse_Movement_11)
            label_12_frame_11.bind('<Enter>',Mouse_Movement_11)

                #   Hinzufügen Button:
            def Hinzufuegen():
                print('Hinzufügen')
                Name_2=''
                Name_2=Name_2+str(self.Name.get())
                Typ_2=''
                Typ_2=Typ_2+str(Typ_label_2.get())
                Masse_2=0.0
                Masse_2=0.0+String_Number.String_to_Number(self.Masse.get())
                Radius_2=0.0
                Radius_2=0.0+String_Number.String_to_Number(self.Radius.get())
                X_Geschwindigkeit_2=0.0
                X_Geschwindigkeit_2=X_Geschwindigkeit_2+String_Number.String_to_Number(self.X_Geschwindigkeit.get())
                Y_Geschwindigkeit_2=0.0
                Y_Geschwindigkeit_2=Y_Geschwindigkeit_2+String_Number.String_to_Number(self.Y_Geschwindigkeit.get())
                Z_Geschwindigkeit_2=0.0
                Z_Geschwindigkeit_2=Z_Geschwindigkeit_2+String_Number.String_to_Number(self.Z_Geschwindigkeit.get())
                X_Position_2=0.0
                X_Position_2=X_Position_2+String_Number.String_to_Number(self.X_Position.get())
                Y_Position_2=0.0
                Y_Position_2=Y_Position_2+String_Number.String_to_Number(self.Y_Position.get())
                Z_Position_2=0.0
                Z_Position_2=Z_Position_2+String_Number.String_to_Number(self.Z_Position.get())
                Color_3=''
                Color_3=Color_3+str(self.Color_2.get())
                # Elemente in die Gui-Listen Hinzufügen:
                self.pos=self.pos+1
                # Elemente in die Liste Hinzufügen (bei simplen Hinzufügen heist das nichts anderes, als es hinten ran zu hängen:
                ab=self.Tree.insert('', self.pos, text=Name_2, values=(Typ_2, Verifizieren.Verifizieren_mit_Null(Masse_2), Verifizieren.Verifizieren_mit_Null(Radius_2), Verifizieren.Verifizieren_mit_Null(X_Geschwindigkeit_2), Verifizieren.Verifizieren_mit_Null(Y_Geschwindigkeit_2), Verifizieren.Verifizieren_mit_Null(Z_Geschwindigkeit_2), Verifizieren.Verifizieren_mit_Null(X_Position_2), Verifizieren.Verifizieren_mit_Null(Y_Position_2), Verifizieren.Verifizieren_mit_Null(Z_Position_2)))
                self.ID.append(ab)
                self.Name_13.append(Name_2)
                self.Newton_Simulator.Objekt_Hinzufuegen(Name_2,Typ_2,Masse_2,Radius_2,X_Geschwindigkeit_2,Y_Geschwindigkeit_2,Z_Geschwindigkeit_2,X_Position_2,Y_Position_2,Z_Position_2,Color_3)
                # Toplevel beenden jucheee:
                Objekt_erstellen_1.destroy()

            def Hinzufuegen_2():
                Name_2=''
                Name_2=Name_2+str(self.Name.get())
                abc=Verifizieren.Namen_Verifizeren(Name_2,self.Newton_Simulator.Name_Body)
                if abc==0:
                    Ausruf = Canvas(frame_11, width = 66, height = 66)
                    Ausruf.place(x=340, y=525)
                    self.Ausruf_2 = PhotoImage(file = '../Icon/Alert Icon/64/alert.gif')
                    Ausruf.create_image(0, 0, image = self.Ausruf_2, anchor = NW)
                    Warnung_Label=Label(frame_11, text="Bitte geben Sie einen Namen ein!")
                    Warnung_Label.place (x=415, y=545)
                if abc==1:
                    Ausruf = Canvas(frame_11, width = 66, height = 66)
                    Ausruf.place(x=340, y=525)
                    self.Ausruf_2 = PhotoImage(file = '../Icon/Alert Icon/64/alert.gif')
                    Ausruf.create_image(0, 0, image = self.Ausruf_2, anchor = NW)
                    Warnung_Label=Label(frame_11, text="Der von ihnen gewählte Name wird bereits benutzt.")
                    Warnung_Label.place (x=415, y=545)
                if abc==2:
                    Hinzufuegen()

#-------------------------------------------------------------------

            Hinzufuegen_2 = Button(Objekt_erstellen_1, text="Hinzufügen", command=Hinzufuegen_2)
            Hinzufuegen_2.place (x=475, y=700)

        Objekt_erstellen = Button (label_1_frame_2, text="Objekt erstellen", command=Objekt_erstellen)
        Objekt_erstellen.place(x=10, y=10)

        def Objekt_bearbeiten():
            pass

        Objekt_bearbeiten = Button (label_1_frame_2, text="Objekt bearbeiten", state=DISABLED, command=Objekt_bearbeiten)
        Objekt_bearbeiten.place(x=200, y=12)

        def Objekt_loeschen():
            try:
                a =self.Tree.selection()[0]
                # Sucht den Eintrag inder ID Liste:
                for i in range(0,len(self.ID)):
                    if self.ID[i]==a:
                        position=i                                              #position ist die Position in den Listen des Eintrags
                self.Tree.delete(self.Tree.selection())
                self.Newton_Simulator.Objekt_loeschen(self.Name_13[position])
            except:
                print('Ups, beim löschen ist wohl was schiefgelaufen, vlt. sollten Sie die Datei neu einlesen.')
            # Die Elemente müsen nun auch noch aus den Listen der Gui gelöscht werden (self.ID und self.Name_13):
            for i in range (0,len(self.Newton_Simulator.Name)):
                for j in range(0,len(self.Name_13)):
                    if self.Name_13[j]==self.Newton_Simulator.Name[i]:
                        del self.Name_13[j]
                        del self.ID[j]
                        break

        Objekt_loeschen = Button (label_1_frame_2, text="Objekt löschen", state=DISABLED, command=Objekt_loeschen)
        Objekt_loeschen.place(x=390, y=12)

        def Satellit_erstellen():
            try:
                se =self.Tree.selection()[0] # se wie satellit erstellen
                # Sucht den Eintrag inder ID Liste:
                for i in range(0,len(self.ID)):
                    if self.ID[i]==se:
                        self.Se_position=i                                              #position ist die Position in den Listen des Eintrags
            except:
                print('Beim öffnen ist etwas schief gelaufen tut mir Leid!')

            Objekt_erstellen_1 = Toplevel(root, width=1024, height=768)
            Objekt_erstellen_1.title ("Satellit erstellen")
            Objekt_erstellen_1.resizable(width = False, height = False)
            Objekt_erstellen_1.wm_iconbitmap('../Icon/Window Icon/Window Icon.ico')
            Objekt_erstellen_1.transient(master=root)

            se_position=self.Se_position

                    #   Das Notebook:

            notebook = ttk.Notebook(Objekt_erstellen_1, width=1012, height=614)


            frame_11 = Frame(Objekt_erstellen_1, width=1012, height=714)

            frame_22 = Frame(Objekt_erstellen_1, width=1012, height=714)

                    #   Spalten:

            notebook.add(frame_11, text="Eingabe")
            notebook.add(frame_22, text="Visieren")

                    #   Anzeigen des Notebooks:

            notebook.place(x=5,y=5)

                        # Größe der Fenster:
            width_x_2=450
            height_y_2=295

            self.Objekt_gesetzt=0
            self.Objekt_Tempo_gesetzt=0

            self.Color_1 = Randomcolor.Randomcolor()

            # Weiterführende Einstellungen der Anzeige:
            self.Zeichenmodus = IntVar()
            self.Zeichenmodus.set(1)
            self.Groesse_Se_Kugeln=StringVar()
            self.Groesse_Se_Kugeln.set('3')
            self.Groesse_Se_Kugeln_2=StringVar()
            self.Groesse_Se_Kugeln_2.set('10')
            self.Groesse_Se_text_1=StringVar()
            self.Groesse_Se_text_1.set("Größe:")
            Kugeln_Se_1=Radiobutton(frame_22, text="Kugeln gleicher Größe", variable=self.Zeichenmodus, value=1).place(x=59+width_x_2,y=123+height_y_2)
            Kugeln_Se_2=Radiobutton(frame_22, text="Kugeln nach Radius", variable=self.Zeichenmodus, value=2).place(x=59+width_x_2,y=123+height_y_2+30)
            Kugeln_Se_3=Radiobutton(frame_22, text="Kugeln nach Entfernung", variable=self.Zeichenmodus, value=3).place(x=59+width_x_2,y=123+height_y_2+60)
            Kugeln_Se_4=Radiobutton(frame_22, text="Tatsächliche Größe", variable=self.Zeichenmodus, value=4).place(x=59+width_x_2,y=123+height_y_2+90)

            modi=0

            def Kugeln_Oe_1_Angewaehlt(*args):
                if self.Zeichenmodus.get()==1:
                    self.Groesse_Se_text_1.set("Größe:")
                    Groesse_Se_1_Label_2.config(state=NORMAL)
                    Groesse_Se_1_Label.config(state=NORMAL)
                    Groesse_Se_1.config(state=NORMAL)
                    Groesse_Se_2.config(state=DISABLED)
                    Groesse_Se_2_Label_2.config(state=DISABLED)
                    Groesse_Se_2_Label.config(state=DISABLED)
                elif self.Zeichenmodus.get()==2:
                    self.Groesse_Se_text_1.set("Von:")
                    Groesse_Se_1_Label_2.config(state=NORMAL)
                    Groesse_Se_1_Label.config(state=NORMAL)
                    Groesse_Se_1.config(state=NORMAL)
                    Groesse_Se_2.config(state=NORMAL)
                    Groesse_Se_2_Label_2.config(state=NORMAL)
                    Groesse_Se_2_Label.config(state=NORMAL)
                elif self.Zeichenmodus.get()==3:
                    self.Groesse_Se_text_1.set("Von:")
                    Groesse_Se_1_Label_2.config(state=NORMAL)
                    Groesse_Se_1_Label.config(state=NORMAL)
                    Groesse_Se_1.config(state=NORMAL)
                    Groesse_Se_2.config(state=NORMAL)
                    Groesse_Se_2_Label_2.config(state=NORMAL)
                    Groesse_Se_2_Label.config(state=NORMAL)
                elif self.Zeichenmodus.get()==4:
                    self.Groesse_Se_text_1.set("Groesse:")
                    Groesse_Se_2.config(state=DISABLED)
                    Groesse_Se_1_Label_2.config(state=DISABLED)
                    Groesse_Se_1_Label.config(state=DISABLED)
                    Groesse_Se_1.config(state=DISABLED)
                    Groesse_Se_2_Label_2.config(state=DISABLED)
                    Groesse_Se_2_Label.config(state=DISABLED)
                Einzeichnen()
            self.Zeichenmodus.trace("w", Kugeln_Oe_1_Angewaehlt)

            Groesse_Se_1_Label=Label(frame_22,textvariable=self.Groesse_Se_text_1)
            Groesse_Se_1_Label.place(x=259+width_x_2,y=123+height_y_2)
            Groesse_Se_1_Label.config(state=NORMAL)
            Groesse_Se_1=Spinbox(frame_22,from_=1, to=100,textvariable=self.Groesse_Se_Kugeln,width=7,bd=2)
            Groesse_Se_1.place(x=329+width_x_2,y=125+height_y_2)
            Groesse_Se_1.config(state=NORMAL)
            Groesse_Se_1_Label_2=Label(frame_22,text="[Pixel]")
            Groesse_Se_1_Label_2.place(x=395+width_x_2,y=123+height_y_2)
            Groesse_Se_2_Label=Label(frame_22,text="Bis:")
            Groesse_Se_2_Label.place(x=259+width_x_2,y=153+height_y_2)
            Groesse_Se_2_Label.config(state=DISABLED)
            Groesse_Se_2=Spinbox(frame_22,from_=1, to=100,textvariable=self.Groesse_Se_Kugeln_2,width=7,bd=2)
            Groesse_Se_2.place(x=329+width_x_2,y=155+height_y_2)
            Groesse_Se_2.config(state=DISABLED)
            Groesse_Se_2_Label_2=Label(frame_22,text="[Pixel]")
            Groesse_Se_2_Label_2.place(x=395+width_x_2,y=153+height_y_2)
            Groesse_Se_2_Label_2.config(state=DISABLED)
            Geschwindigkeit_Se_1_Label_1=Label(frame_22, text='Geschwindigkeit:')
            Geschwindigkeit_Se_1_Label_1.place(x=59+width_x_2,y=125+height_y_2+120)
            self.Geschwindigkeit_pro_Pixel=StringVar()
            self.Geschwindigkeit_pro_Pixel.set('1.0')
            Geschwindigkeit_Se_1_Label_2=Entry(frame_22, textvariable=self.Geschwindigkeit_pro_Pixel,bd=2,justify=RIGHT,width=17)
            Geschwindigkeit_Se_1_Label_2.place(x=250+width_x_2,y=125+height_y_2+120)
            Geschwindigkeit_Se_1_Label_3=Label(frame_22, text='[1000*(m/s)/Pixel]')
            Geschwindigkeit_Se_1_Label_3.place(x=395+width_x_2,y=125+height_y_2+120)

            def Geschwindigkeit_Verifizieren(*args):
                Get_Geschwindigkeit = self.Geschwindigkeit_pro_Pixel.get()
                a=Verifizieren.Verifizieren_ohne_Minus(Get_Geschwindigkeit)
                self.Geschwindigkeit_pro_Pixel.set(a)
                max_min()
                Masstab_berechnen()
                Einzeichnen()
            self.Geschwindigkeit_pro_Pixel.trace("w", Geschwindigkeit_Verifizieren)

            self.Se_X=StringVar()
            self.Se_X.set('0')
            X_Label_Frame_22=Label(frame_22, text='X:').place(x=59+width_x_2,y=123+height_y_2+150)
            X_Label_Frame_22_1=Label(frame_22, textvariable=self.Se_X, relief=SUNKEN,bd=2,width=15).place(x=89+width_x_2,y=123+height_y_2+150)

            self.Se_Y=StringVar()
            self.Se_Y.set('0')
            Y_Label_Frame_22=Label(frame_22, text='Y:').place(x=219+width_x_2,y=123+height_y_2+150)
            Y_Label_Frame_22_1=Label(frame_22, textvariable=self.Se_Y, relief=SUNKEN,bd=2,width=15).place(x=249+width_x_2,y=123+height_y_2+150)

            self.Se_Z=StringVar()
            self.Se_Z.set('0')
            Z_Label_Frame_22=Label(frame_22, text='Z:').place(x=379+width_x_2,y=123+height_y_2+150)
            Z_Label_Frame_22_1=Label(frame_22, textvariable=self.Se_Z, relief=SUNKEN,bd=2,width=15).place(x=409+width_x_2,y=123+height_y_2+150)

            def max_min():
                # Startwerte für die kleinsten und größten x,y und z Werte der Liste:
                self.Newton_Simulator.Maximalwertsuche()
                self.minX=self.Newton_Simulator.MinX
                self.minY=self.Newton_Simulator.MinY
                self.minZ=self.Newton_Simulator.MinZ
                self.maxX=self.Newton_Simulator.MaxX
                self.maxY=self.Newton_Simulator.MaxY
                self.maxZ=self.Newton_Simulator.MaxZ
                if self.Objekt_gesetzt==1:
                    x=String_Number.String_to_Number(self.X_Position.get())
                    y=String_Number.String_to_Number(self.Y_Position.get())
                    z=String_Number.String_to_Number(self.Z_Position.get())
                    if x>self.maxX:
                        self.minX=x
                    elif x<self.minX:
                        self.minX=x
                    if y>self.maxY:
                        self.maxY=y
                    elif y<self.minY:
                        self.minY=y
                    if z>self.maxZ:
                        self.maxZ=z
                    elif z<self.minZ:
                        self.minZ=z

            def Masstab_berechnen():
                x_diff=self.maxX-self.minX
                y_diff=self.maxY-self.minY
                z_diff=self.maxZ-self.minZ
                if x_diff==0 and y_diff==0 and z_diff==0:
                    x_diff=100
                    y_diff=100
                    z_diff=100
                # Für xy:
                if y_diff!=0:
                    if x_diff!=0:
                        Mpp_y_xy=y_diff/height_y_2
                        Mpp_x_xy=x_diff/width_x_2
                        if Mpp_y_xy>=Mpp_x_xy:
                            self.Se_Mpp_xy=Mpp_y_xy
                        else:
                            self.Se_Mpp_xy=Mpp_x_xy
                    elif x_diff==0:
                         self.Se_Mpp_xy=y_diff/height_y_2
                elif y_diff==0:
                    if x_diff!=0:
                        self.Se_Mpp_xy=x_diff/width_x_2
                    elif x_diff==0:
                        self.Se_Mpp_xy=0
                # Für yz:
                if z_diff!=0:
                    if y_diff!=0:
                        Mpp_y_yz=y_diff/height_y_2
                        Mpp_z_yz=z_diff/width_x_2
                        if Mpp_y_yz>=Mpp_z_yz:
                            self.Se_Mpp_yz=Mpp_y_yz
                        else:
                            self.Se_Mpp_yz=Mpp_z_yz
                    elif y_diff==0:
                         self.Se_Mpp_yz=z_diff/width_x_2
                elif z_diff==0:
                    if y_diff!=0:
                        self.Se_Mpp_yz=y_diff/height_y_2
                    elif y_diff==0:
                        self.Se_Mpp_yz=0
                # Für xz:
                if z_diff!=0:
                    if x_diff!=0:
                        Mpp_z_xz=z_diff/height_y_2
                        Mpp_x_xz=x_diff/width_x_2
                        if Mpp_z_xz>=Mpp_x_xz:
                            self.Se_Mpp_xz=Mpp_z_xz
                        else:
                            self.Se_Mpp_xz=Mpp_x_xz
                    elif x_diff==0:
                         self.Se_Mpp_xz=z_diff/height_y_2
                elif z_diff==0:
                    if x_diff!=0:
                        self.Se_Mpp_xz=x_diff/width_x_2
                    elif x_diff==0:
                        self.Se_Mpp_xz=0
                # Vergleich der Mpp's (meiste Meter pro Pixel gesucht):
                self.Se_Mpp=self.Se_Mpp_xy
                if self.Se_Mpp_xz>self.Se_Mpp:
                    self.Se_Mpp=self.Se_Mpp_xz
                if self.Se_Mpp_yz>self.Se_Mpp:
                    self.Se_Mpp=self.Se_Mpp_yz
                # Vergrößern von Mpp um 10% pro Seite:
                self.Se_Mpp=self.Se_Mpp*1.2
                # Mittelpunkte_bestimmen:
                self.Se_Mittelpunkt_x=self.minX+x_diff/2
                self.Se_Mittelpunkt_y=self.minY+y_diff/2
                self.Se_Mittelpunkt_z=self.minZ+z_diff/2

            def Einzeichnen():
                # Hinzufügen der Punkte / Kreise auf die beschriebenen Arten und Weisen erst in Richtung :
                    Canvas_xy.delete(ALL)
                    Canvas_yz.delete(ALL)
                    Canvas_xz.delete(ALL)
                    self.xy_koord = PhotoImage(file = '../Icon/Koordinaten/xy.gif')
                    Canvas_xy.create_image(12,height_y_2-39, image = self.xy_koord, anchor = NW)
                    self.yz_koord = PhotoImage(file = '../Icon/Koordinaten/yz.gif')
                    Canvas_yz.create_image(width_x_2-39, height_y_2-39, image = self.yz_koord, anchor = NW)
                    self.xz_koord = PhotoImage(file = '../Icon/Koordinaten/xz.gif')
                    Canvas_xz.create_image(12, height_y_2-39, image = self.xz_koord, anchor = NW)
                    Mpp=self.Se_Mpp
                    if Mpp==0:
                        Mpp=0.1
                    Mitte_x=self.Se_Mittelpunkt_x
                    Mitte_y=self.Se_Mittelpunkt_y
                    Mitte_z=self.Se_Mittelpunkt_z
                    speed=1000*(String_Number.String_to_Number(self.Geschwindigkeit_pro_Pixel.get()))
                    if self.Zeichenmodus.get()==1:
                        Groesse=String_Number.String_to_Number(self.Groesse_Se_Kugeln.get())
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            # Zeichnet die Punkte ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse>0 and pos_x_xy+Groesse<width_x_2 and pos_y_xy-Groesse>0 and pos_y_xy+Groesse<height_y_2:
                                Canvas_xy.create_oval(abs(pos_x_xy-Groesse),abs(pos_y_xy-Groesse),abs(pos_x_xy+Groesse),abs(pos_y_xy+Groesse), fill=self.Newton_Simulator.Color[i])
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse>0 and pos_z_yz+Groesse<width_x_2 and pos_y_yz-Groesse>0 and pos_y_yz+Groesse<height_y_2:
                                Canvas_yz.create_oval(abs(pos_z_yz-Groesse),abs(pos_y_yz-Groesse),abs(pos_z_yz+Groesse),abs(pos_y_yz+Groesse), fill=self.Newton_Simulator.Color[i])
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse>0 and pos_x_xz+Groesse<width_x_2 and pos_z_xz-Groesse>0 and pos_z_xz+Groesse<height_y_2:
                                Canvas_xz.create_oval(abs(pos_x_xz-Groesse),abs(pos_z_xz-Groesse),abs(pos_x_xz+Groesse),abs(pos_z_xz+Groesse), fill=self.Newton_Simulator.Color[i])
                            # Zeichnet die Geraden der Geschwindigkeit ein:
                            if abs(vx)>speed or abs(vy)>speed:
                                vx_2=vx/speed
                                vy_2=-vy/speed
                                if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                    if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                        Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vy)>speed or abs(vz)>speed:
                                vy_2=-vy/speed
                                vz_2=-vz/speed
                                if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                    if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                        Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vx)>speed or abs(vz)>speed:
                                vx_2=vx/speed
                                vz_2=-vz/speed
                                if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                    if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                        Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                        if self.Objekt_gesetzt==1:
                            x=String_Number.String_to_Number(self.X_Position.get())
                            y=String_Number.String_to_Number(self.Y_Position.get())
                            z=String_Number.String_to_Number(self.Z_Position.get())
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse-1>0 and pos_x_xy+Groesse+1<width_x_2 and pos_y_xy-Groesse-1>0 and pos_y_xy+Groesse+1<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Groesse-1),abs(pos_y_xy-Groesse-1),abs(pos_x_xy+Groesse+1),abs(pos_y_xy+Groesse+1), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse-1>0 and pos_z_yz+Groesse+1<width_x_2 and pos_y_yz-Groesse-1>0 and pos_y_yz+Groesse+1<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Groesse-1),abs(pos_y_yz-Groesse-1),abs(pos_z_yz+Groesse+1),abs(pos_y_yz+Groesse+1), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse-1>0 and pos_x_xz+Groesse+1<width_x_2 and pos_z_xz-Groesse-1>0 and pos_z_xz+Groesse+1<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Groesse-1),abs(pos_z_xz-Groesse-1),abs(pos_x_xz+Groesse+1),abs(pos_z_xz+Groesse+1), fill=str(self.Color_1))
                            if self.Objekt_Tempo_gesetzt==1:
                                    vx=String_Number.String_to_Number(self.X_Geschwindigkeit.get())
                                    vy=String_Number.String_to_Number(self.Y_Geschwindigkeit.get())
                                    vz=String_Number.String_to_Number(self.Z_Geschwindigkeit.get())
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>speed or abs(vy)>speed:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>speed or abs(vz)>speed:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>speed or abs(vz)>speed:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                        if self.Se_akt_Pos==1:
                            x=self.Se_akt_X
                            y=self.Se_akt_Y
                            z=self.Se_akt_Z
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse-1>0 and pos_x_xy+Groesse+1<width_x_2 and pos_y_xy-Groesse-1>0 and pos_y_xy+Groesse+1<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Groesse-1),abs(pos_y_xy-Groesse-1),abs(pos_x_xy+Groesse+1),abs(pos_y_xy+Groesse+1), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse-1>0 and pos_z_yz+Groesse+1<width_x_2 and pos_y_yz-Groesse-1>0 and pos_y_yz+Groesse+1<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Groesse-1),abs(pos_y_yz-Groesse-1),abs(pos_z_yz+Groesse+1),abs(pos_y_yz+Groesse+1), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse-1>0 and pos_x_xz+Groesse+1<width_x_2 and pos_z_xz-Groesse-1>0 and pos_z_xz+Groesse+1<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Groesse-1),abs(pos_z_xz-Groesse-1),abs(pos_x_xz+Groesse+1),abs(pos_z_xz+Groesse+1), fill=str(self.Color_1))
                            if self.Se_akt_Tem==1:
                                    vx=self.Se_akt_movX
                                    vy=self.Se_akt_movY
                                    vz=self.Se_akt_movZ
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>1 or abs(vy)>1:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>1 or abs(vz)>1:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>1 or abs(vz)>1:
                                        vx_2=vx/speed*10
                                        vz_2=-vz/speed*10
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                    if self.Zeichenmodus.get()==2:
                        Groesse_1=String_Number.String_to_Number(self.Groesse_Se_Kugeln.get())
                        Groesse_2=String_Number.String_to_Number(self.Groesse_Se_Kugeln_2.get())
                        Groesse=[]
                        Groesse=self.Newton_Simulator.Radius_Anteil(Groesse_1,Groesse_2,String_Number.String_to_Number(str(self.Radius.get())))
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            # Zeichnet die Punkte ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse[i]>0 and pos_x_xy+Groesse[i]<width_x_2 and pos_y_xy-Groesse[i]>0 and pos_y_xy+Groesse[i]<height_y_2:
                                Canvas_xy.create_oval(abs(pos_x_xy-Groesse[i]),abs(pos_y_xy-Groesse[i]),abs(pos_x_xy+Groesse[i]),abs(pos_y_xy+Groesse[i]), fill=self.Newton_Simulator.Color[i])
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse[i]>0 and pos_z_yz+Groesse[i]<width_x_2 and pos_y_yz-Groesse[i]>0 and pos_y_yz+Groesse[i]<height_y_2:
                                Canvas_yz.create_oval(abs(pos_z_yz-Groesse[i]),abs(pos_y_yz-Groesse[i]),abs(pos_z_yz+Groesse[i]),abs(pos_y_yz+Groesse[i]), fill=self.Newton_Simulator.Color[i])
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse[i]>0 and pos_x_xz+Groesse[i]<width_x_2 and pos_z_xz-Groesse[i]>0 and pos_z_xz+Groesse[i]<height_y_2:
                                Canvas_xz.create_oval(abs(pos_x_xz-Groesse[i]),abs(pos_z_xz-Groesse[i]),abs(pos_x_xz+Groesse[i]),abs(pos_z_xz+Groesse[i]), fill=self.Newton_Simulator.Color[i])
                            # Zeichnet die Geraden der Geschwindigkeit ein:
                            if abs(vx)>speed or abs(vy)>speed:
                                vx_2=vx/speed
                                vy_2=-vy/speed
                                if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                    if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                        Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vy)>speed or abs(vz)>speed:
                                vy_2=-vy/speed
                                vz_2=-vz/speed
                                if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                    if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                        Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vx)>speed or abs(vz)>speed:
                                vx_2=vx/speed
                                vz_2=-vz/speed
                                if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                    if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                        Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                        if self.Objekt_gesetzt==1:
                            n=Groesse[len(Groesse)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drg=Groesse[len(Groesse)-2] # Steigung der Funktion für die Groesse
                            Grossheit=String_Number.String_to_Number(str(self.Radius.get()))/drg+n
                            x=String_Number.String_to_Number(self.X_Position.get())
                            y=String_Number.String_to_Number(self.Y_Position.get())
                            z=String_Number.String_to_Number(self.Z_Position.get())
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Grossheit>0 and pos_x_xy+Grossheit<width_x_2 and pos_y_xy-Grossheit>0 and pos_y_xy+Grossheit<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Grossheit),abs(pos_y_xy-Grossheit),abs(pos_x_xy+Grossheit),abs(pos_y_xy+Grossheit), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Grossheit>0 and pos_z_yz+Grossheit<width_x_2 and pos_y_yz-Grossheit>0 and pos_y_yz+Grossheit<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Grossheit),abs(pos_y_yz-Grossheit),abs(pos_z_yz+Grossheit),abs(pos_y_yz+Grossheit), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Grossheit>0 and pos_x_xz+Grossheit<width_x_2 and pos_z_xz-Grossheit>0 and pos_z_xz+Grossheit<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Grossheit),abs(pos_z_xz-Grossheit),abs(pos_x_xz+Grossheit),abs(pos_z_xz+Grossheit), fill=str(self.Color_1))
                            if self.Objekt_Tempo_gesetzt==1:
                                    vx=String_Number.String_to_Number(self.X_Geschwindigkeit.get())
                                    vy=String_Number.String_to_Number(self.Y_Geschwindigkeit.get())
                                    vz=String_Number.String_to_Number(self.Z_Geschwindigkeit.get())
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>speed or abs(vy)>speed:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>speed or abs(vz)>speed:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>speed or abs(vz)>speed:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                        if self.Se_akt_Pos==1:
                            n=Groesse[len(Groesse)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drg=Groesse[len(Groesse)-2] # Steigung der Funktion für die Groesse
                            Grossheit=String_Number.String_to_Number(str(self.Radius.get()))/drg+n
                            x=self.Se_akt_X
                            y=self.Se_akt_Y
                            z=self.Se_akt_Z
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Grossheit>0 and pos_x_xy+Grossheit<width_x_2 and pos_y_xy-Grossheit>0 and pos_y_xy+Grossheit<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Grossheit),abs(pos_y_xy-Grossheit),abs(pos_x_xy+Grossheit),abs(pos_y_xy+Grossheit), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Grossheit>0 and pos_z_yz+Grossheit<width_x_2 and pos_y_yz-Grossheit>0 and pos_y_yz+Grossheit<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Grossheit),abs(pos_y_yz-Grossheit),abs(pos_z_yz+Grossheit),abs(pos_y_yz+Grossheit), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Grossheit>0 and pos_x_xz+Grossheit<width_x_2 and pos_z_xz-Grossheit>0 and pos_z_xz+Grossheit<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Grossheit),abs(pos_z_xz-Grossheit),abs(pos_x_xz+Grossheit),abs(pos_z_xz+Grossheit), fill=str(self.Color_1))
                            if self.Se_akt_Tem==1:
                                    vx=self.Se_akt_movX
                                    vy=self.Se_akt_movY
                                    vz=self.Se_akt_movZ
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>1 or abs(vy)>1:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>1 or abs(vz)>1:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>1 or abs(vz)>1:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                    if self.Zeichenmodus.get()==3:
                        # Nach entfernung:
                        Groesse_1=String_Number.String_to_Number(self.Groesse_Oe_Kugeln.get())
                        Groesse_2=String_Number.String_to_Number(self.Groesse_Oe_Kugeln_2.get())
                        Groesse=[]
                        Groesse_x=self.Newton_Simulator.Entfernung_Anteil_x(Groesse_1,Groesse_2,String_Number.String_to_Number(str(self.X_Position.get())))
                        Groesse_y=self.Newton_Simulator.Entfernung_Anteil_y(Groesse_1,Groesse_2,String_Number.String_to_Number(str(self.Y_Position.get())))
                        Groesse_z=self.Newton_Simulator.Entfernung_Anteil_z(Groesse_1,Groesse_2,String_Number.String_to_Number(str(self.Z_Position.get())))
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            # Zeichnet die Punkte ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse_z[i]>0 and pos_x_xy+Groesse_z[i]<width_x_2 and pos_y_xy-Groesse_z[i]>0 and pos_y_xy+Groesse_z[i]<height_y_2:
                                Canvas_xy.create_oval(abs(pos_x_xy-Groesse_z[i]),abs(pos_y_xy-Groesse_z[i]),abs(pos_x_xy+Groesse_z[i]),abs(pos_y_xy+Groesse_z[i]), fill=self.Newton_Simulator.Color[i])
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse_x[i]>0 and pos_z_yz+Groesse_x[i]<width_x_2 and pos_y_yz-Groesse_x[i]>0 and pos_y_yz+Groesse_x[i]<height_y_2:
                                Canvas_yz.create_oval(abs(pos_z_yz-Groesse_x[i]),abs(pos_y_yz-Groesse_x[i]),abs(pos_z_yz+Groesse_x[i]),abs(pos_y_yz+Groesse_x[i]), fill=self.Newton_Simulator.Color[i])
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse_y[i]>0 and pos_x_xz+Groesse_y[i]<width_x_2 and pos_z_xz-Groesse_y[i]>0 and pos_z_xz+Groesse_y[i]<height_y_2:
                                Canvas_xz.create_oval(abs(pos_x_xz-Groesse_y[i]),abs(pos_z_xz-Groesse_y[i]),abs(pos_x_xz+Groesse_y[i]),abs(pos_z_xz+Groesse_y[i]), fill=self.Newton_Simulator.Color[i])
                            # Zeichnet die Geraden der Geschwindigkeit ein:
                            if abs(vx)>speed or abs(vy)>speed:
                                vx_2=vx/speed
                                vy_2=-vy/speed
                                if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                    if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                        Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vy)>speed or abs(vz)>speed:
                                vy_2=-vy/speed
                                vz_2=-vz/speed
                                if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                    if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                        Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vx)>speed or abs(vz)>speed:
                                vx_2=vx/speed
                                vz_2=-vz/speed
                                if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                    if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                        Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                        if self.Objekt_gesetzt==1:
                            nx=Groesse_x[len(Groesse_x)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgx=Groesse_x[len(Groesse_x)-2] # Steigung der Funktion für die Groesse
                            ny=Groesse_y[len(Groesse_y)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgy=Groesse_y[len(Groesse_y)-2] # Steigung der Funktion für die Groesse
                            nz=Groesse_z[len(Groesse_z)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgz=Groesse_z[len(Groesse_z)-2] # Steigung der Funktion für die Groesse
                            Grossheit_x=String_Number.String_to_Number(str(self.X_Position.get()))*drgx+nx
                            Grossheit_y=String_Number.String_to_Number(str(self.Y_Position.get()))*drgy+ny
                            Grossheit_z=String_Number.String_to_Number(str(self.Z_Position.get()))*drgz+nz
                            x=String_Number.String_to_Number(self.X_Position.get())
                            y=String_Number.String_to_Number(self.Y_Position.get())
                            z=String_Number.String_to_Number(self.Z_Position.get())
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Grossheit_z>0 and pos_x_xy+Grossheit_z<width_x_2 and pos_y_xy-Grossheit_z>0 and pos_y_xy+Grossheit_z<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Grossheit_z),abs(pos_y_xy-Grossheit_z),abs(pos_x_xy+Grossheit_z),abs(pos_y_xy+Grossheit_z), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Grossheit_x>0 and pos_z_yz+Grossheit_x<width_x_2 and pos_y_yz-Grossheit_x>0 and pos_y_yz+Grossheit_x<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Grossheit_x),abs(pos_y_yz-Grossheit_x),abs(pos_z_yz+Grossheit_x),abs(pos_y_yz+Grossheit_x), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Grossheit_y>0 and pos_x_xz+Grossheit_y<width_x_2 and pos_z_xz-Grossheit_y>0 and pos_z_xz+Grossheit_y<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Grossheit_y),abs(pos_z_xz-Grossheit_y),abs(pos_x_xz+Grossheit_y),abs(pos_z_xz+Grossheit_y), fill=str(self.Color_1))
                            if self.Objekt_Tempo_gesetzt==1:
                                    vx=String_Number.String_to_Number(self.X_Geschwindigkeit.get())
                                    vy=String_Number.String_to_Number(self.Y_Geschwindigkeit.get())
                                    vz=String_Number.String_to_Number(self.Z_Geschwindigkeit.get())
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>speed or abs(vy)>speed:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>speed or abs(vz)>speed:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>speed or abs(vz)>speed:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                        if self.Se_akt_Pos==1:
                            nx=Groesse_x[len(Groesse_x)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgx=Groesse_x[len(Groesse_x)-2] # Steigung der Funktion für die Groesse
                            ny=Groesse_y[len(Groesse_y)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgy=Groesse_y[len(Groesse_y)-2] # Steigung der Funktion für die Groesse
                            nz=Groesse_z[len(Groesse_z)-1]   # Y-Achsenabschnitt der Groessenfunktion
                            drgz=Groesse_z[len(Groesse_z)-2] # Steigung der Funktion für die Groesse
                            Grossheit_x=String_Number.String_to_Number(str(self.X_Position.get()))*drgx+nx
                            Grossheit_y=String_Number.String_to_Number(str(self.Y_Position.get()))*drgy+ny
                            Grossheit_z=String_Number.String_to_Number(str(self.Z_Position.get()))*drgz+nz
                            x=self.Se_akt_X
                            y=self.Se_akt_Y
                            z=self.Se_akt_Z
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Grossheit_z>0 and pos_x_xy+Grossheit_z<width_x_2 and pos_y_xy-Grossheit_z>0 and pos_y_xy+Grossheit_z<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Grossheit_z),abs(pos_y_xy-Grossheit_z),abs(pos_x_xy+Grossheit_z),abs(pos_y_xy+Grossheit_z), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Grossheit_x>0 and pos_z_yz+Grossheit_x<width_x_2 and pos_y_yz-Grossheit_x>0 and pos_y_yz+Grossheit_x<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Grossheit_x),abs(pos_y_yz-Grossheit_x),abs(pos_z_yz+Grossheit_x),abs(pos_y_yz+Grossheit_x), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Grossheit_y>0 and pos_x_xz+Grossheit_y<width_x_2 and pos_z_xz-Grossheit_y>0 and pos_z_xz+Grossheit_y<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Grossheit_y),abs(pos_z_xz-Grossheit_y),abs(pos_x_xz+Grossheit_y),abs(pos_z_xz+Grossheit_y), fill=str(self.Color_1))
                            if self.Se_akt_Tem==1:
                                    vx=self.Se_akt_movX
                                    vy=self.Se_akt_movY
                                    vz=self.Se_akt_movZ
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>1 or abs(vy)>1:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>1 or abs(vz)>1:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>1 or abs(vz)>1:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))            # Ein Script wird benötigt, welches die max und min Werte des Screens anzeigt, diese überprüft auf den Ursprung (0) und dann je nach Zoom Verhältnis verschiedene Massstäbe anzeigt, zum Beispiel Millimeter[mm], Meter[m], Kilometer [km], Megameter [Mm] (im Deutschen eher unkonventionell), Astronomische Einheiten [Ae], Parsec [pc], Lichtjahre [Lj]
                    if self.Zeichenmodus.get()==4:
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            # Zeichnet die Punkte ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            # Bestimmt die Groesse (mind. 1 Pixel):
                            Groesse=self.Newton_Simulator.Radius_Body[i][0]/Mpp
                            if Groesse<1:
                                Groesse=1
                            if pos_x_xy-Groesse>0 and pos_x_xy+Groesse<width_x_2 and pos_y_xy-Groesse>0 and pos_y_xy+Groesse<height_y_2:
                                Canvas_xy.create_oval(abs(pos_x_xy-Groesse),abs(pos_y_xy-Groesse),abs(pos_x_xy+Groesse),abs(pos_y_xy+Groesse), fill=self.Newton_Simulator.Color[i])
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse>0 and pos_z_yz+Groesse<width_x_2 and pos_y_yz-Groesse>0 and pos_y_yz+Groesse<height_y_2:
                                Canvas_yz.create_oval(abs(pos_z_yz-Groesse),abs(pos_y_yz-Groesse),abs(pos_z_yz+Groesse),abs(pos_y_yz+Groesse), fill=self.Newton_Simulator.Color[i])
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse>0 and pos_x_xz+Groesse<width_x_2 and pos_z_xz-Groesse>0 and pos_z_xz+Groesse<height_y_2:
                                Canvas_xz.create_oval(abs(pos_x_xz-Groesse),abs(pos_z_xz-Groesse),abs(pos_x_xz+Groesse),abs(pos_z_xz+Groesse), fill=self.Newton_Simulator.Color[i])
                            # Zeichnet die Geraden der Geschwindigkeit ein:
                            if abs(vx)>speed or abs(vy)>speed:
                                vx_2=vx/speed
                                vy_2=-vy/speed
                                if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                    if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                        Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vy)>speed or abs(vz)>speed:
                                vy_2=-vy/speed
                                vz_2=-vz/speed
                                if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                    if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                        Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                            if abs(vx)>speed or abs(vz)>speed:
                                vx_2=vx/speed
                                vz_2=-vz/speed
                                if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                    if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                        Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                        if self.Objekt_gesetzt==1:
                            x=String_Number.String_to_Number(self.X_Position.get())
                            y=String_Number.String_to_Number(self.Y_Position.get())
                            z=String_Number.String_to_Number(self.Z_Position.get())
                            # Bestimmt die Groesse (mind. 1 Pixel):
                            Groesse=String_Number.String_to_Number(self.Radius.get())/Mpp
                            if Groesse<1:
                                Groesse=1
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse-1>0 and pos_x_xy+Groesse+1<width_x_2 and pos_y_xy-Groesse-1>0 and pos_y_xy+Groesse+1<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Groesse),abs(pos_y_xy-Groesse),abs(pos_x_xy+Groesse),abs(pos_y_xy+Groesse), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse-1>0 and pos_z_yz+Groesse+1<width_x_2 and pos_y_yz-Groesse-1>0 and pos_y_yz+Groesse+1<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Groesse),abs(pos_y_yz-Groesse),abs(pos_z_yz+Groesse),abs(pos_y_yz+Groesse), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse-1>0 and pos_x_xz+Groesse+1<width_x_2 and pos_z_xz-Groesse-1>0 and pos_z_xz+Groesse+1<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Groesse),abs(pos_z_xz-Groesse),abs(pos_x_xz+Groesse),abs(pos_z_xz+Groesse), fill=str(self.Color_1))
                            if self.Objekt_Tempo_gesetzt==1:
                                    vx=String_Number.String_to_Number(self.X_Geschwindigkeit.get())
                                    vy=String_Number.String_to_Number(self.Y_Geschwindigkeit.get())
                                    vz=String_Number.String_to_Number(self.Z_Geschwindigkeit.get())
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>speed or abs(vy)>speed:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>speed or abs(vz)>speed:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>speed or abs(vz)>speed:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                        if self.Se_akt_Pos==1:
                            x=self.Se_akt_X
                            y=self.Se_akt_Y
                            z=self.Se_akt_Z
                            # Bestimmt die Groesse (mind. 1 Pixel):
                            Groesse=String_Number.String_to_Number(self.Radius.get())/Mpp
                            if Groesse<1:
                                Groesse=1
                            # Zeichnet den neuen Punkt ein:
                            pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                            pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_x_xy-Groesse-1>0 and pos_x_xy+Groesse+1<width_x_2 and pos_y_xy-Groesse-1>0 and pos_y_xy+Groesse+1<height_y_2:
                                xy_can=Canvas_xy.create_oval(abs(pos_x_xy-Groesse-1),abs(pos_y_xy-Groesse-1),abs(pos_x_xy+Groesse+1),abs(pos_y_xy+Groesse+1), fill=str(self.Color_1))
                            pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                            pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                            if pos_z_yz-Groesse-1>0 and pos_z_yz+Groesse+1<width_x_2 and pos_y_yz-Groesse-1>0 and pos_y_yz+Groesse+1<height_y_2:
                                yz_can=Canvas_yz.create_oval(abs(pos_z_yz-Groesse-1),abs(pos_y_yz-Groesse-1),abs(pos_z_yz+Groesse+1),abs(pos_y_yz+Groesse+1), fill=str(self.Color_1))
                            pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                            pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                            if pos_x_xz-Groesse-1>0 and pos_x_xz+Groesse+1<width_x_2 and pos_z_xz-Groesse-1>0 and pos_z_xz+Groesse+1<height_y_2:
                                xz_can=Canvas_xz.create_oval(abs(pos_x_xz-Groesse-1),abs(pos_z_xz-Groesse-1),abs(pos_x_xz+Groesse+1),abs(pos_z_xz+Groesse+1), fill=str(self.Color_1))
                            if self.Se_akt_Tem==1:
                                    vx=self.Se_akt_movX
                                    vy=self.Se_akt_movY
                                    vz=self.Se_akt_movZ
                                 # Zeichnet die Gerade der Geschwindigkeit ein:
                                    if abs(vx)>1 or abs(vy)>1:
                                        vx_2=vx/speed
                                        vy_2=-vy/speed
                                        if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                            if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                                vx_can=Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vy)>1 or abs(vz)>1:
                                        vy_2=-vy/speed
                                        vz_2=-vz/speed
                                        if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                            if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                                yz_can=Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                                    if abs(vx)>1 or abs(vz)>1:
                                        vx_2=vx/speed
                                        vz_2=-vz/speed
                                        if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                            if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                                xz_can=Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=str(self.Color_1),arrow=LAST,arrowshape=(5,7,3))
                    # Skript welches den Masstab und Orientierungspunkte Anzeigen soll:
                    # Zuerst werden die Maxima und Minima der Canvases bestimmt:
                    Canvas_coord_yz.delete(ALL)
                    Canvas_coord_xz.delete(ALL)
                    Canvas_coord_xy.delete(ALL)
                        # geg.: Mpp, Mitte_z, Mitte_x, Mitte_y
                    pc=30856776000000000    # 1*Parsec
                    Lj=9460528000000000     # 1*Lichtjahr
                    ae=149597870691         # 1*Astronomische Einheit
                    km=1000                 # 1*Kilometer
                    hm=100                  # 1*Hectometer
                    dam=10                  # 1*Dekameter
                    m=1                     # 1*meter
                    dm=0.1                  # 0.1*meter
                    cm=0.01                 # 0.01*meter

                    # xy, yz - y (height_y_2) - Achsen max und min:
                    max_y=Mitte_y+height_y_2*Mpp/2                              # Oberes Ende!
                    min_y=Mitte_y-height_y_2*Mpp/2                              # Unteres Ende!
                    # Die Skala soll ermitelt werden:
                    # Wir teilen min durch die Längen der einheiten und runden diese zu einer int, dann zeichnen wir alle relevanten einund setzen Einheitenanzahl eins höher
                    e=0                     # Anzeige aus=0, an=1
                    Aktueller_Schritt=8     #0=Parsec, 1=Lj, 2=AE.....

                    if Aktueller_Schritt==8:
                        # 1 cm (cm) = 1 m
                        a=int(round(min_y/cm))
                        stop=0
                        d=0
                        c=abs(((a+1)*cm)/Mpp-(a*cm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*cm>min_y:
                                    if a*cm<max_y:
                                        if Mpp!=0:
                                            y=(a*cm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"cm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==7:
                        # 1 dm (dm) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dm)/Mpp-(a*dm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dm>min_y:
                                    if a*dm<max_y:
                                        if Mpp!=0:
                                            y=(a*dm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"dm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==6:
                        # 1 m (m) = 1 m
                        a=int(round(min_y/m))
                        stop=0
                        d=0
                        c=abs(((a+1)*m)/Mpp-(a*m/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*m>min_y:
                                    if a*m<max_y:
                                        if Mpp!=0:
                                            y=(a*m-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"m", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==5:
                        # 1 dam (dam) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dam)/Mpp-(a*dam/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dam>min_y:
                                    if a*dam<max_y:
                                        if Mpp!=0:
                                            y=(a*dam-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"dam", fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==4:
                        # 1 hm (hm) = 100 m
                        a=int(round(min_y/hm))
                        stop=0
                        d=0
                        c=abs(((a+1)*hm)/Mpp-(a*hm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*hm>min_y:
                                    if a*hm<max_y:
                                        if Mpp!=0:
                                            y=(a*hm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"hm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==3:
                        # 1 km (km) = 1000 m
                        a=int(round(min_y/km))
                        stop=0
                        d=0
                        c=abs(((a+1)*km)/Mpp-(a*km/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*km>min_y:
                                    if a*km<max_y:
                                        if Mpp!=0:
                                            y=(a*km-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"km", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==2:
                        # 1 ae (ae) = 149597870691 m
                        a=int(round(min_y/ae))
                        stop=0
                        d=0
                        c=abs(((a+1)*ae)/Mpp-(a*ae/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*ae>min_y:
                                    if a*ae<max_y:
                                        if Mpp!=0:
                                            y=(a*ae-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"AE", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==1:
                        # 1 Lj (Lj) = 9460528000000000 m
                        a=int(round(min_y/Lj))
                        stop=0
                        d=0
                        c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*Lj>min_y:
                                    if a*Lj<max_y:
                                        if Mpp!=0:
                                            y=(a*Lj-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==0:
                        # 1 pc (Lj) = 30856776000000000 m
                        a=int(round(min_y/pc))
                        stop=0
                        d=0
                        c=abs(((a+1)*pc)/Mpp-(a*pc/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*pc>min_y:
                                    if a*pc<max_y:
                                        if Mpp!=0:
                                            y=(a*pc-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"pc", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==-1:
                        # Format unbekannt:
                        if e==0:
                            f=1
                            g=0
                            stop=0
                            d=0
                            while g==0:
                                h=(int(round(min_y/10**f)+1)*10**f)/Mpp-(int(round(min_y/10**f))*10**f)/Mpp
                                if h>20 and h<height_y_2:
                                    a=int(round(min_y/10**f))
                                    c=abs(((a+1)*10**f)/Mpp-(a*10**f/Mpp))
                                    g=1
                                else:
                                    f=f+1
                            while stop==0:
                                if a*10**f>min_y:
                                    if a*10**f<max_y:
                                        if Mpp!=0:
                                            y=(a*10**f-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"mE"+str(f), fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                    # Rechtes Canvas (yz):
                    e=0                     # Anzeige aus=0, an=1
                    Aktueller_Schritt=8     #0=Parsec, 1=Lj, 2=AE.....

                    if Aktueller_Schritt==8:
                        # 1 cm (cm) = 1 m
                        a=int(round(min_y/cm))
                        stop=0
                        d=0
                        c=abs(((a+1)*cm)/Mpp-(a*cm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*cm>min_y:
                                    if a*cm<max_y:
                                        if Mpp!=0:
                                            y=(a*cm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"cm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==7:
                        # 1 dm (dm) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dm)/Mpp-(a*dm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dm>min_y:
                                    if a*dm<max_y:
                                        if Mpp!=0:
                                            y=(a*dm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"dm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==6:
                        # 1 m (m) = 1 m
                        a=int(round(min_y/m))
                        stop=0
                        d=0
                        c=abs(((a+1)*m)/Mpp-(a*m/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*m>min_y:
                                    if a*m<max_y:
                                        if Mpp!=0:
                                            y=(a*m-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,9,4,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"m", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==5:
                        # 1 dam (dam) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dam)/Mpp-(a*dam/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dam>min_y:
                                    if a*dam<max_y:
                                        if Mpp!=0:
                                            y=(a*dam-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"dam", fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==4:
                        # 1 hm (hm) = 100 m
                        a=int(round(min_y/hm))
                        stop=0
                        d=0
                        c=abs(((a+1)*hm)/Mpp-(a*hm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*hm>min_y:
                                    if a*hm<max_y:
                                        if Mpp!=0:
                                            y=(a*hm-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"hm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==3:
                        # 1 km (km) = 1000 m
                        a=int(round(min_y/km))
                        stop=0
                        d=0
                        c=abs(((a+1)*km)/Mpp-(a*km/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*km>min_y:
                                    if a*km<max_y:
                                        if Mpp!=0:
                                            y=(a*km-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"km", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==2:
                        # 1 ae (ae) = 149597870691 m
                        a=int(round(min_y/ae))
                        stop=0
                        d=0
                        c=abs(((a+1)*ae)/Mpp-(a*ae/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*ae>min_y:
                                    if a*ae<max_y:
                                        if Mpp!=0:
                                            y=(a*ae-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"AE", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==1:
                        # 1 Lj (Lj) = 9460528000000000 m
                        a=int(round(min_y/Lj))
                        stop=0
                        d=0
                        c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*Lj>min_y:
                                    if a*Lj<max_y:
                                        if Mpp!=0:
                                            y=(a*Lj-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==0:
                        # 1 pc (Lj) = 30856776000000000 m
                        a=int(round(min_y/pc))
                        stop=0
                        d=0
                        c=abs(((a+1)*pc)/Mpp-(a*pc/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*pc>min_y:
                                    if a*pc<max_y:
                                        if Mpp!=0:
                                            y=(a*pc-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"pc", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==-1:
                        # Format unbekannt:
                        if e==0:
                            f=1
                            g=0
                            stop=0
                            d=0
                            while g==0:
                                h=(int(round(min_y/10**f)+1)*10**f)/Mpp-(int(round(min_y/10**f))*10**f)/Mpp
                                if h>20 and h<height_y_2:
                                    a=int(round(min_y/10**f))
                                    c=abs(((a+1)*10**f)/Mpp-(a*10**f/Mpp))
                                    g=1
                                else:
                                    f=f+1
                            while stop==0:
                                if a*10**f>min_y:
                                    if a*10**f<max_y:
                                        if Mpp!=0:
                                            y=(a*10**f-Mitte_y)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                                Canvas_coord_yz.create_text(22, b-6, text=str(a)+"mE"+str(f), fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                    # xz - z (height_y_2) - Achsen max und min:
                    max_y=Mitte_z-height_y_2*Mpp/2                                # Oberes Ende!
                    max_y=Mitte_z+height_y_2*Mpp/2                                # Unteres Ende!
                    # Die Skala soll ermitelt werden:
                    # Wir teilen min durch die Längen der einheiten und runden diese zu einer int, dann zeichnen wir alle relevanten einund setzen Einheitenanzahl eins höher
                    e=0                     # Anzeige aus=0, an=1
                    Aktueller_Schritt=8     #0=Parsec, 1=Lj, 2=AE.....
                    if Aktueller_Schritt==8:
                        # 1 cm (cm) = 1 m
                        a=int(round(min_y/cm))
                        stop=0
                        d=0
                        c=abs(((a+1)*cm)/Mpp-(a*cm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*cm>min_y:
                                    if a*cm<max_y:
                                        if Mpp!=0:
                                            y=(a*cm-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"cm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==7:
                        # 1 dm (dm) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dm)/Mpp-(a*dm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dm>min_y:
                                    if a*dm<max_y:
                                        if Mpp!=0:
                                            y=(a*dm-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"dm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==6:
                        # 1 m (m) = 1 m
                        a=int(round(min_y/m))
                        stop=0
                        d=0
                        c=abs(((a+1)*m)/Mpp-(a*m/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*m>min_y:
                                    if a*m<max_y:
                                        if Mpp!=0:
                                            y=(a*m-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xy.create_text(17, b-6, text=str(a)+"m", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==5:
                        # 1 dam (dam) = 10 m
                        a=int(round(min_y/dm))
                        stop=0
                        d=0
                        c=abs(((a+1)*dam)/Mpp-(a*dam/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*dam>min_y:
                                    if a*dam<max_y:
                                        if Mpp!=0:
                                            y=(a*dam-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"dam", fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==4:
                        # 1 hm (hm) = 100 m
                        a=int(round(min_y/hm))
                        stop=0
                        d=0
                        c=abs(((a+1)*hm)/Mpp-(a*hm/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*hm>min_y:
                                    if a*hm<max_y:
                                        if Mpp!=0:
                                            y=(a*hm-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"hm", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==3:
                        # 1 km (km) = 1000 m
                        a=int(round(min_y/km))
                        stop=0
                        d=0
                        c=abs(((a+1)*km)/Mpp-(a*km/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*km>min_y:
                                    if a*km<max_y:
                                        if Mpp!=0:
                                            y=(a*km-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"km", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==2:
                        # 1 ae (ae) = 149597870691 m
                        a=int(round(min_y/ae))
                        stop=0
                        d=0
                        c=abs(((a+1)*ae)/Mpp-(a*ae/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*ae>min_y:
                                    if a*ae<max_y:
                                        if Mpp!=0:
                                            y=(a*ae-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"AE", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==1:
                        # 1 Lj (Lj) = 9460528000000000 m
                        a=int(round(min_y/Lj))
                        stop=0
                        d=0
                        c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*Lj>min_y:
                                    if a*Lj<max_y:
                                        if Mpp!=0:
                                            y=(a*Lj-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==0:
                        # 1 pc (Lj) = 30856776000000000 m
                        a=int(round(min_y/pc))
                        stop=0
                        d=0
                        c=abs(((a+1)*pc)/Mpp-(a*pc/Mpp))
                        if c>20 and c<height_y_2:
                            while stop==0:
                                if a*pc>min_y:
                                    if a*pc<max_y:
                                        if Mpp!=0:
                                            y=(a*pc-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"pc", fill="white",font=("Helvectica", "8"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                        else:
                            Aktueller_Schritt=Aktueller_Schritt-1
                    if Aktueller_Schritt==-1:
                        # Format unbekannt:
                        if e==0:
                            f=1
                            g=0
                            stop=0
                            d=0
                            while g==0:
                                h=(int(round(min_y/10**f)+1)*10**f)/Mpp-(int(round(min_y/10**f))*10**f)/Mpp
                                if h>20 and h<height_y_2:
                                    a=int(round(min_y/10**f))
                                    c=abs(((a+1)*10**f)/Mpp-(a*10**f/Mpp))
                                    g=1
                                else:
                                    f=f+1
                            while stop==0:
                                if a*10**f>min_y:
                                    if a*10**f<max_y:
                                        if Mpp!=0:
                                            y=(a*10**f-Mitte_z)/Mpp
                                            b=height_y_2/2-y
                                            if b>=0 and b<=height_y_2:
                                                Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                                Canvas_coord_xz.create_text(17, b-6, text=str(a)+"mE"+str(f), fill="white",font=("Helvectica", "6"))
                                                d=1
                                                e=1
                                                for i in range(0,5):
                                                    Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                        a=a+1
                                    else:
                                        stop=1
                                        if d==1:
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                                else:
                                    a=a+1
                    # Nun werden alle Werte eingezeichnet die auf die Anforderungen zutreffen:


            def Normalisieren():
                max_min()
                Masstab_berechnen()
                Einzeichnen()
            Normalisieren_Button=Button(frame_22,text='Normalisieren',command=Normalisieren,width=20, bd=2).place(x=700,y=350)

            def Up(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y-5*self.Se_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y-5*self.Se_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Se_Mittelpunkt_z=self.Se_Mittelpunkt_z-5*self.Se_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Control-Up>",Up)

            def Down(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y+5*self.Se_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y+5*self.Se_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Se_Mittelpunkt_z=self.Se_Mittelpunkt_z+5*self.Se_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Control-Down>",Down)

            def Left(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_x=self.Se_Mittelpunkt_x+5*self.Se_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_z=self.Se_Mittelpunkt_z-5*self.Se_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Se_Mittelpunkt_x=self.Se_Mittelpunkt_x+5*self.Se_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Control-Left>",Left)

            def Right(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_x=self.Se_Mittelpunkt_x-5*self.Se_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_z=self.Se_Mittelpunkt_z+5*self.Se_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Se_Mittelpunkt_x=self.Se_Mittelpunkt_x-5*self.Se_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Control-Right>",Right)


            def Up(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y-50*self.Se_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y-50*self.Se_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Se_Mittelpunkt_z=self.Se_Mittelpunkt_z-50*self.Se_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Up>",Up)

            def Down(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y+50*self.Se_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y+50*self.Se_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Se_Mittelpunkt_z=self.Se_Mittelpunkt_z+50*self.Se_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Down>",Down)

            def Left(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_x=self.Se_Mittelpunkt_x+50*self.Se_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_z=self.Se_Mittelpunkt_z-50*self.Se_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Se_Mittelpunkt_x=self.Se_Mittelpunkt_x+50*self.Se_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Left>",Left)

            def Right(event):
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_x=self.Se_Mittelpunkt_x-50*self.Se_Mpp
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        self.Se_Mittelpunkt_z=self.Se_Mittelpunkt_z+50*self.Se_Mpp
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        self.Se_Mittelpunkt_x=self.Se_Mittelpunkt_x-50*self.Se_Mpp
                Einzeichnen()

            Objekt_erstellen_1.bind("<Right>",Right)

            def Zoom_2(event):
                Canvas_xy.focus_set()
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        x_zoom_xy=event.x-57
                        y_zoom_xy=event.y-36
                        if event.delta < 0:
                            self.Se_Mpp=self.Se_Mpp*(0.8)
                            self.Se_Mittelpunkt_x=self.Se_Mittelpunkt_x+0.2*((self.Se_Mittelpunkt_x/self.Se_Mpp+x_zoom_xy-width_x_2/2)*self.Se_Mpp-self.Se_Mittelpunkt_x)
                            self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y+0.2*((self.Se_Mittelpunkt_y/self.Se_Mpp+height_y_2/2-y_zoom_xy)*self.Se_Mpp-self.Se_Mittelpunkt_y)
                        else:
                            self.Se_Mpp=self.Se_Mpp*(1.2)
                            self.Se_Mittelpunkt_x=self.Se_Mittelpunkt_x+0.2*((self.Se_Mittelpunkt_x/self.Se_Mpp+x_zoom_xy-width_x_2/2)*self.Se_Mpp-self.Se_Mittelpunkt_x)
                            self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y+0.2*((self.Se_Mittelpunkt_y/self.Se_Mpp+height_y_2/2-y_zoom_xy)*self.Se_Mpp-self.Se_Mittelpunkt_y)
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        x_zoom_xy=event.x-509
                        y_zoom_xy=event.y-36
                        if event.delta < 0:
                            self.Se_Mpp=self.Se_Mpp*(0.8)
                            self.Se_Mittelpunkt_z=self.Se_Mittelpunkt_z-0.2*((self.Se_Mittelpunkt_z/self.Se_Mpp+x_zoom_xy-width_x_2/2)*self.Se_Mpp-self.Se_Mittelpunkt_z)
                            self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y+0.2*((self.Se_Mittelpunkt_y/self.Se_Mpp+height_y_2/2-y_zoom_xy)*self.Se_Mpp-self.Se_Mittelpunkt_y)
                        else:
                            self.Se_Mpp=self.Se_Mpp*(1.2)
                            self.Se_Mittelpunkt_z=self.Se_Mittelpunkt_z-0.2*((self.Se_Mittelpunkt_z/self.Se_Mpp+x_zoom_xy-width_x_2/2)*self.Se_Mpp-self.Se_Mittelpunkt_z)
                            self.Se_Mittelpunkt_y=self.Se_Mittelpunkt_y+0.2*((self.Se_Mittelpunkt_y/self.Se_Mpp+height_y_2/2-y_zoom_xy)*self.Se_Mpp-self.Se_Mittelpunkt_y)
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        x_zoom_xy=event.x-57
                        y_zoom_xy=event.y-339
                        if event.delta < 0:
                            self.Se_Mpp=self.Se_Mpp*(0.8)
                            #self.Se_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                        else:
                            self.Se_Mpp=self.Se_Mpp*(1.2)
                            #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                Einzeichnen()

            Objekt_erstellen_1.bind("<Control-MouseWheel>",Zoom_2)

            def Zoom(event):
                Canvas_xy.focus_set()
                # xy:
                if event.x>57 and event.x<501:
                    if event.y>36 and event.y<331:
                        x_zoom_xy=event.x-57
                        y_zoom_xy=event.y-36
                        if event.delta < 0:
                            self.Se_Mpp=self.Se_Mpp*(0.8)
                            #self.Se_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                        else:
                            self.Se_Mpp=self.Se_Mpp*(1.2)
                            #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                # yz:
                if event.x>509 and event.x<957:
                    if event.y>36 and event.y<331:
                        x_zoom_xy=event.x-509
                        y_zoom_xy=event.y-36
                        if event.delta < 0:
                            self.Se_Mpp=self.Se_Mpp*(0.8)
                            #self.Se_Mittelpunkt_z=self.Oe_Mittelpunkt_z-0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                            #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                        else:
                            self.Se_Mpp=self.Se_Mpp*(1.2)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                            #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                # xz:
                if event.x>57 and event.x<501:
                    if event.y>339 and event.y<633:
                        x_zoom_xy=event.x-57
                        y_zoom_xy=event.y-339
                        if event.delta < 0:
                            self.Se_Mpp=self.Se_Mpp*(0.8)
                            #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                        else:
                            self.Se_Mpp=self.Se_Mpp*(1.2)
                            #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                            #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                Einzeichnen()

            Objekt_erstellen_1.bind("<MouseWheel>",Zoom)

            def Click_xy(event):
                # xy:
                        self.Se_akt_Tem=0
                        self.Se_akt_movX=0
                        self.Se_akt_movY=0
                        self.Se_akt_movZ=0
                        x_click=event.x#-57
                        y_click=event.y#-36
                        self.Se_akt_X=((self.Se_Mittelpunkt_x/self.Se_Mpp+x_click-width_x_2/2)*self.Se_Mpp)
                        self.Se_akt_Y=((self.Se_Mittelpunkt_y/self.Se_Mpp+height_y_2/2-y_click)*self.Se_Mpp)
                        self.Se_akt_Z=(self.Se_Mittelpunkt_z)
                        self.Se_akt_Pos=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Click_xz(event):
                # xz:
                        self.Se_akt_Tem=0
                        self.Se_akt_movX=0
                        self.Se_akt_movY=0
                        self.Se_akt_movZ=0
                        x_click=event.x#-57
                        y_click=event.y#-339
                        self.Se_akt_X=((self.Se_Mittelpunkt_x/self.Se_Mpp+x_click-width_x_2/2)*self.Se_Mpp)
                        self.Se_akt_Z=((self.Se_Mittelpunkt_z/self.Se_Mpp+height_y_2/2-y_click)*self.Se_Mpp)
                        self.Se_akt_Y=(self.Se_Mittelpunkt_y)
                        self.Se_akt_Pos=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Click_yz(event):
                # yz:
                        self.Se_akt_Tem=0
                        self.Se_akt_movX=0
                        self.Se_akt_movY=0
                        self.Se_akt_movZ=0
                        x_click=event.x#-509
                        y_click=event.y#-36
                        self.Se_akt_Z=((self.Se_Mittelpunkt_z/self.Se_Mpp-x_click+width_x_2/2)*self.Se_Mpp)
                        self.Se_akt_Y=((self.Se_Mittelpunkt_y/self.Se_Mpp+height_y_2/2-y_click)*self.Se_Mpp)
                        self.Se_akt_X=(self.Se_Mittelpunkt_x)
                        self.Se_akt_Pos=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Click_Move_xy(event):
                # xy:
                        self.Se='xy'
                        speed=1000*(String_Number.String_to_Number(self.Geschwindigkeit_pro_Pixel.get()))
                        x_click=event.x#-57
                        y_click=event.y#-36
                        G=String_Number.String_to_Number(self.Gravitationskonstante.get())
                        self.Se_akt_X=((self.Se_Mittelpunkt_x/self.Se_Mpp+x_click-width_x_2/2)*self.Se_Mpp)         # X-position des Körpers
                        self.Se_akt_Y=((self.Se_Mittelpunkt_y/self.Se_Mpp+height_y_2/2-y_click)*self.Se_Mpp)
                        self.Se_akt_Z=(self.Newton_Simulator.Z[se_position][0])
                        delta_x=abs(self.Se_akt_X-self.Newton_Simulator.X[se_position][0])                               # Abstand: Körper und Parent
                        delta_y=abs(self.Se_akt_Y-self.Newton_Simulator.Y[se_position][0])
                        r=((delta_x)**2+(delta_y)**2)**(0.5)                                   # R aus: v=sqrt(G*M/r)
                        Se_akt_moX=-delta_y/r
                        Se_akt_moY=delta_x/r            # Länge von x y und z komponente genau 1
                        self.Se_akt_movZ=0
                        self.Se_akt_movX=Se_akt_moX*sqrt(G*self.Newton_Simulator.Masse_Body[se_position][0]/r)
                        self.Se_akt_movY=Se_akt_moY*sqrt(G*self.Newton_Simulator.Masse_Body[se_position][0]/r)
                        self.Se_akt_Tem=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Click_Move_xz(event):
                # xz:
                        self.Se='xz'
                        speed=1000*(String_Number.String_to_Number(self.Geschwindigkeit_pro_Pixel.get()))
                        x_click=event.x#-57
                        y_click=event.y#-36
                        G=String_Number.String_to_Number(self.Gravitationskonstante.get())
                        self.Se_akt_X=((self.Se_Mittelpunkt_x/self.Se_Mpp+x_click-width_x_2/2)*self.Se_Mpp)         # X-position des Körpers
                        self.Se_akt_Z=((self.Se_Mittelpunkt_z/self.Se_Mpp+height_y_2/2-y_click)*self.Se_Mpp)
                        self.Se_akt_Y=(self.Se_Mittelpunkt_y)
                        delta_x=abs(self.Se_akt_X-self.Newton_Simulator.X[se_position][0])                               # Abstand: Körper und Parent
                        delta_z=abs(self.Se_akt_Z-self.Newton_Simulator.Z[se_position][0])
                        r=((delta_x)**2+(delta_z)**2)**(0.5)                                   # R aus: v=sqrt(G*M/r)
                        Se_akt_moX=-delta_z/r
                        Se_akt_moZ=delta_x/r            # Länge von x y und z komponente genau 1
                        self.Se_akt_movZ=0
                        self.Se_akt_movX=Se_akt_moX*sqrt(G*self.Newton_Simulator.Masse_Body[se_position][0]/r)
                        self.Se_akt_movZ=Se_akt_moZ*sqrt(G*self.Newton_Simulator.Masse_Body[se_position][0]/r)
                        self.Se_akt_Tem=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()


            def Click_Move_yz(event):
                # yz:
                        self.Se='yz'
                        speed=1000*(String_Number.String_to_Number(self.Geschwindigkeit_pro_Pixel.get()))
                        x_click=event.x#-57
                        y_click=event.y#-36
                        G=String_Number.String_to_Number(self.Gravitationskonstante.get())
                        self.Se_akt_Z=((self.Se_Mittelpunkt_z/self.Se_Mpp+x_click-width_x_2/2)*self.Se_Mpp)         # X-position des Körpers
                        self.Se_akt_Y=((self.Se_Mittelpunkt_y/self.Se_Mpp+height_y_2/2-y_click)*self.Se_Mpp)
                        self.Se_akt_X=(self.Se_Mittelpunkt_x)
                        delta_y=abs(self.Se_akt_Y-self.Newton_Simulator.Y[se_position][0])                               # Abstand: Körper und Parent
                        delta_z=abs(self.Se_akt_Z-self.Newton_Simulator.Z[se_position][0])
                        r=((delta_y)**2+(delta_z)**2)**(0.5)                                   # R aus: v=sqrt(G*M/r)
                        Se_akt_moY=-delta_z/r
                        Se_akt_moZ=delta_y/r            # Länge von x y und z komponente genau 1
                        self.Se_akt_movX=0
                        self.Se_akt_movY=Se_akt_moY*sqrt(G*self.Newton_Simulator.Masse_Body[se_position][0]/r)
                        self.Se_akt_movZ=Se_akt_moZ*sqrt(G*self.Newton_Simulator.Masse_Body[se_position][0]/r)
                        self.Se_akt_Tem=1
                        self.Objekt_gesetzt=0
                        self.Tempo_gesetzt=0
                        Einzeichnen()

            def Unclick (event):
                if type(event.widget)==Canvas :
                    if self.Se=="xy":
                        self.X_Geschwindigkeit.set(String_Number.Number_to_String(self.Newton_Simulator.VX[se_position][0]-self.Se_akt_movX))
                        self.Y_Geschwindigkeit.set(String_Number.Number_to_String(self.Newton_Simulator.VY[se_position][0]-self.Se_akt_movY))
                        self.Z_Geschwindigkeit.set(str(0))
                    if self.Se=="xz":
                        self.X_Geschwindigkeit.set(String_Number.Number_to_String(self.Newton_Simulator.VX[se_position][0]-self.Se_akt_movX))
                        self.Y_Geschwindigkeit.set(str(0))
                        self.Z_Geschwindigkeit.set(String_Number.Number_to_String(self.Newton_Simulator.VZ[se_position][0]-self.Se_akt_movZ))
                    if self.Se=="yz":
                        self.Y_Geschwindigkeit.set(String_Number.Number_to_String(self.Newton_Simulator.VY[se_position][0]-self.Se_akt_movY))
                        self.Z_Geschwindigkeit.set(String_Number.Number_to_String(self.Newton_Simulator.VZ[se_position][0]-self.Se_akt_movZ))
                        self.X_Geschwindigkeit.set(str(0))
                    # print(type(event.widget))
                    self.Se_akt_Tem=0
                    self.Se_akt_Pos=0
                    Mpp=self.Se_Mpp
                    speed=1000*(String_Number.String_to_Number(self.Geschwindigkeit_pro_Pixel.get()))
                    self.X_Position.set(String_Number.Number_to_String(self.Se_akt_X))
                    self.Y_Position.set(String_Number.Number_to_String(self.Se_akt_Y))
                    self.Z_Position.set(String_Number.Number_to_String(self.Se_akt_Z))
                    Objekt_gesetzt=1
                    Objekt_Tempo_gesetzt=1
                    self.Se_akt_Tem=0
                    self.Se_akt_Pos=0

            def Mouse_Movement_xy(event):
                if Canvas_xy.canvasx(event.x)>10 and Canvas_xy.canvasy(event.y)>10:
                        self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten1.gif')
                        Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                elif Canvas_xy.canvasx(event.x)<10 or Canvas_xy.canvasy(event.y)<10:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                # Koordinatenanzeige:
                if self.Se_Mpp!=0:
                    self.Se_X.set(String_Number.Number_to_String(round(((self.Se_Mittelpunkt_x/self.Se_Mpp+event.x-width_x_2/2)*self.Se_Mpp),1)))
                    self.Se_Y.set(String_Number.Number_to_String(round(((self.Se_Mittelpunkt_y/self.Se_Mpp+height_y_2/2-event.y)*self.Se_Mpp),1)))
                self.Se_Z.set('0.0')

            def Mouse_Movement_yz(event):
                if Canvas_yz.canvasx(event.x)>0 and Canvas_yz.canvasy(event.y)>10 and not Canvas_yz.canvasx(event.x)>440 and not Canvas_yz.canvasy(event.y)>285:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten2.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                elif Canvas_yz.canvasy(event.y)<10 or Canvas_yz.canvasx(event.x)>440 or Canvas_yz.canvasy(event.y)>285:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                # Koordinatenanzeige:
                if self.Se_Mpp!=0:
                    self.Se_Z.set(String_Number.Number_to_String(round(((self.Se_Mittelpunkt_z/self.Se_Mpp-event.x+width_x_2/2)*self.Se_Mpp),1)))
                    self.Se_Y.set(String_Number.Number_to_String(round(((self.Se_Mittelpunkt_y/self.Se_Mpp+height_y_2/2-event.y)*self.Se_Mpp),1)))
                self.Se_X.set('0.0')

            def Mouse_Movement_xz(event):
                if not Canvas_xz.canvasx(event.x)<10 and Canvas_xz.canvasy(event.y)>0 and not Canvas_xz.canvasx(event.x)>440 and not Canvas_xz.canvasy(event.y)>285:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten3.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                elif Canvas_xz.canvasx(event.x)<10 or Canvas_xz.canvasy(event.y)<10 or Canvas_xz.canvasx(event.x)>440 or Canvas_xz.canvasy(event.y)>285:
                    self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
                    Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
                # Koordinatenanzeige:
                if self.Se_Mpp!=0:
                    self.Se_X.set(String_Number.Number_to_String(round(((self.Se_Mittelpunkt_x/self.Se_Mpp+event.x-width_x_2/2)*self.Se_Mpp),1)))
                    self.Se_Z.set(String_Number.Number_to_String(round(((self.Se_Mittelpunkt_z/self.Se_Mpp+height_y_2/2-event.y)*self.Se_Mpp),1)))
                self.Se_Y.set('0.0')

            Canvas_xy = Canvas (frame_22, width=width_x_2, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_xy.place (x=42,y=5)
            Canvas_xy.bind('<Motion>',Mouse_Movement_xy)
            self.xy_koord = PhotoImage(file = '../Icon/Koordinaten/xy.gif')
            Canvas_xy.create_image(12,height_y_2-39, image = self.xy_koord, anchor = NW)

            Canvas_yz = Canvas (frame_22, width=width_x_2, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_yz.place (x=49+width_x_2,y=5)
            Canvas_yz.bind('<Motion>',Mouse_Movement_yz)
            self.yz_koord = PhotoImage(file = '../Icon/Koordinaten/yz.gif')
            Canvas_yz.create_image(width_x_2-39, height_y_2-39, image = self.yz_koord, anchor = NW)

            Canvas_xz = Canvas (frame_22, width=width_x_2, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_xz.place (x=42,y=12+height_y_2)
            Canvas_xz.bind('<Motion>',Mouse_Movement_xz)
            self.xz_koord = PhotoImage(file = '../Icon/Koordinaten/xz.gif')
            Canvas_xz.create_image(12, height_y_2-39, image = self.xz_koord, anchor = NW)

            Koordinaten = Canvas(frame_22, width = 154, height = 107)
            Koordinaten.place(x=49+width_x_2,y=13+height_y_2)
            self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
            Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)

            Canvas_xy.bind("<Button-1>",Click_xy)
            Canvas_xz.bind("<Button-1>",Click_xz)
            Canvas_yz.bind("<Button-1>",Click_yz)
            Canvas_xy.bind("<B1-Motion>",Click_Move_xy)
            Canvas_xz.bind("<B1-Motion>",Click_Move_xz)
            Canvas_yz.bind("<B1-Motion>",Click_Move_yz)
            Objekt_erstellen_1.bind("<ButtonRelease-1>",Unclick)

            Canvas_coord_yz = Canvas (frame_22, width=33, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_coord_yz.place (x=53+2*width_x_2,y=5)

            Canvas_coord_xz = Canvas (frame_22, width=33, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_coord_xz.place (x=8,y=12+height_y_2)

            Canvas_coord_xy = Canvas (frame_22, width=33, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
            Canvas_coord_xy.place (x=8,y=5)

            label_13_frame_11 = Labelframe(frame_11, width=995, height=180, text='Andere')
            label_13_frame_11.place(x=10, y=10)

            Name_label_1 = Label(label_13_frame_11, text='Name:')
            Name_label_1.place(x=10, y=10)

            self.Name = StringVar()
            self.Name.set (self.Newton_Simulator.Name_Body[se_position]+" "+self.Newton_Simulator.Suche_parallel_Childs(se_position))
            Name_label_2 = Entry(label_13_frame_11, justify=RIGHT, textvariable = self.Name, bd=2)
            Name_label_2.place(x=250, y=10)

            def Random_Name_1 (*args):
                self.Name.set(Namensgenerator.Namensgenerator_Buchstaben())

            Random_Name=Button(label_13_frame_11, text="Random", command=Random_Name_1)
            Random_Name.place (x=475, y=6)

            Acht=Canvas(label_13_frame_11, width = 20, height = 20)
            Acht.place(x=566,y=10)
            self.Alert_1 = PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
            Acht.create_image(2, 2, image = self.Alert_1, anchor = NW)

            self.Name_Analyse=StringVar()
            self.Name_Analyse.set('Dieser Name wurde noch keinem anderen Körper zugeordnet.')
            Name_label_2 = Label(label_13_frame_11, textvariable=self.Name_Analyse)
            Name_label_2.place (x=610,y=10)

            def Name_Verifizieren(*args):
                Get_Name = self.Name.get()
                abc=Verifizieren.Namen_Verifizeren(Get_Name,self.Newton_Simulator.Name_Body)
                if abc==0:
                    self.Alert_1=PhotoImage(file = '../Icon/Alert Icon/16/alert.gif')
                    Acht.create_image(2, 2, image = self.Alert_1, anchor = NW)
                    self.Name_Analyse.set('Bitte geben Sie einen Namen ein.')
                elif abc==1:
                    self.Alert_1=PhotoImage(file = '../Icon/Alert Icon/16/alert.gif')
                    Acht.create_image(2, 2, image = self.Alert_1, anchor = NW)
                    self.Name_Analyse.set('Der von ihnen gewählte Name wird bereits benutzt.')
                elif abc==2:
                    self.Alert_1=PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
                    Acht.create_image(2, 2, image = self.Alert_1, anchor = NW)
                    self.Name_Analyse.set('Dieser Name wurde noch keinem anderen Körper zugeordnet.')
            self.Name.trace("w", Name_Verifizieren)

            Typ_label_1 = Label(label_13_frame_11, text='Typ:')
            Typ_label_1.place(x=10, y=40)

            self.Objekttypen =["Galaxie", "Stern", "Schwarzes-Loch", "Planet", "Zwergplanet", "Planemo", "Mond", "Satellit", "Asteroid", "Komet"]
            self.Typ_label_3=StringVar()
            self.Typ_label_3=''
            Typ_label_2 = ttk.Combobox(label_13_frame_11, justify=RIGHT, values=self.Objekttypen, textvariable=self.Typ_label_3)
            Typ_label_2.config(state=NORMAL)
            Typ_label_2.place(x=250, y=40)

            Parent_1 = Label(label_13_frame_11, text="Parent:")
            Parent_1.place(x=475, y=40)

            self.Parent = StringVar()
            self.Parent.set (str(self.Newton_Simulator.Name_Body[se_position]))
            Ges_Erdmassen_2_label_2_frame_1 = Label(label_13_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Parent, bd=2, width=17, anchor=E)
            Ges_Erdmassen_2_label_2_frame_1.place(x=620, y=40)

            Masse_Label_1 = Label(label_13_frame_11, text='Masse:')
            Masse_Label_1.place(x=10, y=70)

            self.Masse = StringVar()
            self.Masse.set ("1")
            Masse_2_label_2_frame_1 = Entry(label_13_frame_11, justify=RIGHT, textvariable = self.Masse, bd=2)
            Masse_2_label_2_frame_1.place(x=250, y=70)

            def Masse_Verifizieren(*args):
                Get_Masse = self.Masse.get()
                self.Masse.set(Verifizieren.Verifizieren_ohne_Minus(Get_Masse))
                b=String_Number.String_to_Number(Get_Masse)
                a=b/self.Newton_Simulator.Masse_Body[se_position][0]
                self.Erdmassen.set(String_Number.Number_to_String(round(a,4)))
                Dichte_Verifizieren()
            self.Masse.trace("w", Masse_Verifizieren)

            Masse_3_label_1_frame_1 = Label(label_13_frame_11, text="[kg]:")
            Masse_3_label_1_frame_1.place (x=380, y=70)

            Ges_Erdmassen_Label_1 = Label(label_13_frame_11, text=str(self.Newton_Simulator.Name_Body[se_position])+"(n) Massen:")
            Ges_Erdmassen_Label_1.place(x=475, y=70)

            self.Erdmassen = StringVar()
            self.Erdmassen.set ("0.0")
            Ges_Erdmassen_2_label_2_frame_1 = Label(label_13_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Erdmassen, bd=2, width=17, anchor=E)
            Ges_Erdmassen_2_label_2_frame_1.place(x=620, y=70)

            Radius_Label_1 = Label(label_13_frame_11, text='Radius:')
            Radius_Label_1.place(x=10, y=100)

            self.Radius = StringVar()
            self.Radius.set ("1")
            Radius_2_label_2_frame_1 = Entry(label_13_frame_11, justify=RIGHT, textvariable = self.Radius, bd=2)
            Radius_2_label_2_frame_1.place(x=250, y=100)

            def Radius_Verifizieren(*args):
                Get_Radius = self.Radius.get()
                self.Radius.set(Verifizieren.Verifizieren(Get_Radius))
                b=String_Number.String_to_Number(Get_Radius)
                a=b/self.Newton_Simulator.Radius_Body[se_position][0]
                self.Erdradien.set(String_Number.Number_to_String(round(a,4)))
                Dichte_Verifizieren()
            self.Radius.trace("w", Radius_Verifizieren)

            Radius_3_label_1_frame_1 = Label(label_13_frame_11, text="[m]:")
            Radius_3_label_1_frame_1.place (x=380, y=100)

            Ges_Erdradius_Label_1 = Label(label_13_frame_11, text=str(self.Newton_Simulator.Name_Body[se_position])+"(n) Radien:")
            Ges_Erdradius_Label_1.place(x=475, y=100)

            self.Erdradien = StringVar()
            self.Erdradien.set ("0.0")
            Ges_Erdradien_2_label_2_frame_1 = Label(label_13_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Erdradien, bd=2, width=17, anchor=E)
            Ges_Erdradien_2_label_2_frame_1.place(x=620, y=100)

            Dichte_Label_1 = Label(label_13_frame_11, text='Dichte ('+chr(0x03C1)+'):')
            Dichte_Label_1.place(x=10, y=130)

            self.Dichte = StringVar()
            self.Dichte.set ("0.2387")
            Dichte_2_label_2_frame_1 = Label(label_13_frame_11, justify=RIGHT, relief=SUNKEN , textvariable = self.Dichte, bd=2, width=17, anchor=E)
            Dichte_2_label_2_frame_1.place(x=250, y=130)

            def Dichte_Verifizieren(*args):
                Get_Masse = String_Number.String_to_Number(self.Masse.get())
                Get_Radius = String_Number.String_to_Number(self.Radius.get())
                b=Basic_Calculations.Dichte(Get_Masse,Get_Radius)
                c=0
                c=b/(self.Newton_Simulator.Masse_Body[se_position][0]/(4/3*3.141*(self.Newton_Simulator.Radius_Body[se_position][0])**3))
                self.Dichte.set(String_Number.Number_to_String(round(b,4)))
                self.Erddichte.set(String_Number.Number_to_String(round(c,4)))

            Dichte_3_label_1_frame_1 = Label(label_13_frame_11, text="[kg/m³]:")
            Dichte_3_label_1_frame_1.place (x=380, y=130)

            Ges_Erddichte_Label_1 = Label(label_13_frame_11, text=str(self.Newton_Simulator.Name_Body[se_position])+"(n) Dichten:")
            Ges_Erddichte_Label_1.place(x=475, y=130)

            self.Erddichte = StringVar()
            self.Erddichte.set ("0.0")
            Ges_Erddichte_2_label_2_frame_1 = Label(label_13_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Erddichte, bd=2, width=17, anchor=E)
            Ges_Erddichte_2_label_2_frame_1.place(x=620, y=130)

            label_11_frame_11 = Labelframe(frame_11, width=995, height=120, text='Objektposition')
            label_11_frame_11.place(x=10, y=190)

            def Abstand_Verifizieren(*args):
                Get_X = String_Number.String_to_Number(self.X_Position.get())
                Get_Y = String_Number.String_to_Number(self.Y_Position.get())
                Get_Z = String_Number.String_to_Number(self.Z_Position.get())
                b=Basic_Calculations.Abstand_zu(Get_X,Get_Y,Get_Z,self.Newton_Simulator.X[se_position][0],self.Newton_Simulator.Y[se_position][0],self.Newton_Simulator.Z[se_position][0])
                self.Abstand_1.set(String_Number.Number_to_String(b))
                self.Abstand_2.set(String_Number.Number_to_String(round((b/149597870691),4)))

            X_Position_Label_1 = Label(label_11_frame_11, text='X-Position:')
            X_Position_Label_1.place(x=10, y=10)

            self.X_Position = StringVar()
            self.X_Position.set (str(String_Number.Number_to_String(self.Newton_Simulator.X[se_position][0])))
            X_Position_2_label_2_frame_1 = Entry(label_11_frame_11, justify=RIGHT, textvariable = self.X_Position, bd=2)
            X_Position_2_label_2_frame_1.place(x=250, y=10)

            def X_Position_Verifizieren(*args):
                Get_X_Position = self.X_Position.get()
                self.X_Position.set(Verifizieren.Verifizieren_mit_Null(Get_X_Position))
                Abstand_Verifizieren()
                Positionsanalyse()
            self.X_Position.trace("w", X_Position_Verifizieren)

            X_Position_3_label_1_frame_1 = Label(label_11_frame_11, text="[m]:")
            X_Position_3_label_1_frame_1.place (x=380, y=10)

            Y_Position_Label_1 = Label(label_11_frame_11, text='Y-Position:')
            Y_Position_Label_1.place(x=10, y=40)

            self.Y_Position = StringVar()
            self.Y_Position.set (str(String_Number.Number_to_String(self.Newton_Simulator.Y[se_position][0])))
            Y_Position_2_label_2_frame_1 = Entry(label_11_frame_11, justify=RIGHT, textvariable = self.Y_Position, bd=2)
            Y_Position_2_label_2_frame_1.place(x=250, y=40)

            def Y_Position_Verifizieren(*args):
                Get_Y_Position = self.Y_Position.get()
                self.Y_Position.set(Verifizieren.Verifizieren_mit_Null(Get_Y_Position))
                Abstand_Verifizieren()
                Positionsanalyse()
            self.Y_Position.trace("w", Y_Position_Verifizieren)

            Y_Position_3_label_1_frame_1 = Label(label_11_frame_11, text="[m]:")
            Y_Position_3_label_1_frame_1.place (x=380, y=40)

            Z_Position_Label_1 = Label(label_11_frame_11, text='Z-Position:')
            Z_Position_Label_1.place(x=10, y=70)

            self.Z_Position = StringVar()
            self.Z_Position.set (str(String_Number.Number_to_String(self.Newton_Simulator.Z[se_position][0])))
            Z_Position_2_label_2_frame_1 = Entry(label_11_frame_11, justify=RIGHT, textvariable = self.Z_Position, bd=2)
            Z_Position_2_label_2_frame_1.place(x=250, y=70)

            def Z_Position_Verifizieren(*args):
                Get_Z_Position = self.Z_Position.get()
                self.Z_Position.set(Verifizieren.Verifizieren_mit_Null(Get_Z_Position))
                Abstand_Verifizieren()
                Positionsanalyse()
            self.Z_Position.trace("w", Z_Position_Verifizieren)

            Z_Position_3_label_1_frame_1 = Label(label_11_frame_11, text="[m]:")
            Z_Position_3_label_1_frame_1.place (x=380, y=70)

            def Positionsanalyse():
                Get_X_Position = self.X_Position.get()
                Get_X = String_Number.String_to_Number(Get_X_Position)
                Get_Y_Position = self.Y_Position.get()
                Get_Y = String_Number.String_to_Number(Get_Y_Position)
                Get_Z_Position = self.Z_Position.get()
                Get_Z = String_Number.String_to_Number(Get_Z_Position)
                # Vergleich mit anderen Planetenpositionen:
                x=0                             # Kontrollvariabel
                for i in range(0,len(self.Newton_Simulator.Name_Body)):
                    if Get_X==self.Newton_Simulator.X[i][0]:
                        if Get_Y==self.Newton_Simulator.Y[i][0]:
                            if Get_Z==self.Newton_Simulator.Z[i][0]:
                                x=1
                    if x==1:
                        break
                if x==1:
                    self.Posi_2 = PhotoImage(file = '../Icon/Alert Icon/16/alert.gif')
                    Position_2.create_image(2, 2, image = self.Posi_2, anchor = NW)
                    self.Positionsanalyse.set('Andere Körper auf selber Position.')
                if x==0:
                    self.Posi_2 = PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
                    Position_2.create_image(2, 2, image = self.Posi_2, anchor = NW)
                    self.Positionsanalyse.set('Position frei.')
                self.Newton_Simulator.Maximalwertsuche()
                self.Objekt_gesetzt=1
                max_min()
                Masstab_berechnen()
                Einzeichnen()


            Position_2=Canvas(label_11_frame_11, width = 20, height = 20)
            Position_2.place(x=566,y=10)
            self.Posi_2 = PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
            Position_2.create_image(2, 2, image = self.Posi_2, anchor = NW)

            self.Positionsanalyse=StringVar()
            Positionsanalyse()
            Positionsana_label_4 = Label(label_11_frame_11, textvariable=self.Positionsanalyse)
            Positionsana_label_4.place (x=610,y=10)

            Ges_Abstand_Label_1 = Label(label_11_frame_11, text='Abstand zu(r) '+str(self.Newton_Simulator.Name_Body[se_position])+':')
            Ges_Abstand_Label_1.place(x=475, y=40)

            self.Abstand_1 = StringVar()
            self.Abstand_1.set ("0")
            Ges_Abstand_2_label_2_frame_1 = Label(label_11_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Abstand_1, bd=2, width=17, anchor=E)
            Ges_Abstand_2_label_2_frame_1.place(x=620, y=40)

            Ges_Abstand_Label_2 = Label(label_11_frame_11, text='[m]')
            Ges_Abstand_Label_2.place(x=750, y=40)


            Ges_Abstand_Label_2 = Label(label_11_frame_11, text='In AE:')
            Ges_Abstand_Label_2.place(x=475, y=70)

            self.Abstand_2 = StringVar()
            self.Abstand_2.set ("0")
            Ges_Abstand_3_label_2_frame_1 = Label(label_11_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Abstand_2, bd=2, width=17, anchor=E)
            Ges_Abstand_3_label_2_frame_1.place(x=620, y=70)

            Ges_Abstand_Label_3 = Label(label_11_frame_11, text='[AE]')
            Ges_Abstand_Label_3.place(x=750, y=70)


            label_12_frame_11 = Labelframe(frame_11, width=995, height=120, text='Objektgeschwindigkeit')
            label_12_frame_11.place(x=10, y=310)

            X_Geschwindigkeit_Label_1 = Label(label_12_frame_11, text='Geschwindigkeit in X-Richtung:')
            X_Geschwindigkeit_Label_1.place(x=10, y=10)

            self.X_Geschwindigkeit = StringVar()
            self.X_Geschwindigkeit.set (str(String_Number.Number_to_String(self.Newton_Simulator.VX[se_position][0])))
            X_Geschwindigkeit_2_label_2_frame_1 = Entry(label_12_frame_11, justify=RIGHT, textvariable = self.X_Geschwindigkeit, bd=2)
            X_Geschwindigkeit_2_label_2_frame_1.place(x=250, y=10)

            def X_Geschwindigkeit_Verifizieren(*args):
                Get_X_Geschwindigkeit = self.X_Geschwindigkeit.get()
                self.X_Geschwindigkeit.set(Verifizieren.Verifizieren_mit_Null(Get_X_Geschwindigkeit))
                Geschwindigkeit_Verifizieren()
            self.X_Geschwindigkeit.trace("w", X_Geschwindigkeit_Verifizieren)

            X_Geschwindigkeit_3_label_1_frame_1 = Label(label_12_frame_11, text="[m/s]:")
            X_Geschwindigkeit_3_label_1_frame_1.place (x=380, y=10)

            Y_Geschwindigkeit_Label_1 = Label(label_12_frame_11, text='Geschwindigkeit in Y-Richtung:')
            Y_Geschwindigkeit_Label_1.place(x=10, y=40)

            self.Y_Geschwindigkeit = StringVar()
            self.Y_Geschwindigkeit.set (str(String_Number.Number_to_String(self.Newton_Simulator.VY[se_position][0])))
            Y_Geschwindigkeit_2_label_2_frame_1 = Entry(label_12_frame_11, justify=RIGHT, textvariable = self.Y_Geschwindigkeit, bd=2)
            Y_Geschwindigkeit_2_label_2_frame_1.place(x=250, y=40)

            def Y_Geschwindigkeit_Verifizieren(*args):
                Get_Y_Geschwindigkeit = self.Y_Geschwindigkeit.get()
                self.Y_Geschwindigkeit.set(Verifizieren.Verifizieren_mit_Null(Get_Y_Geschwindigkeit))
                Geschwindigkeit_Verifizieren()
            self.Y_Geschwindigkeit.trace("w", Y_Geschwindigkeit_Verifizieren)

            Y_Geschwindigkeit_3_label_1_frame_1 = Label(label_12_frame_11, text="[m/s]:")
            Y_Geschwindigkeit_3_label_1_frame_1.place (x=380, y=40)

            Z_Geschwindigkeit_Label_1 = Label(label_12_frame_11, text='Geschwindigkeit in Z-Richtung:')
            Z_Geschwindigkeit_Label_1.place(x=10, y=70)

            self.Z_Geschwindigkeit = StringVar()
            self.Z_Geschwindigkeit.set (str(String_Number.Number_to_String(self.Newton_Simulator.VZ[se_position][0])))
            Z_Geschwindigkeit_2_label_2_frame_1 = Entry(label_12_frame_11, justify=RIGHT, textvariable = self.Z_Geschwindigkeit, bd=2)
            Z_Geschwindigkeit_2_label_2_frame_1.place(x=250, y=70)

            def Z_Geschwindigkeit_Verifizieren(*args):
                Get_Z_Geschwindigkeit = self.Z_Geschwindigkeit.get()
                self.Z_Geschwindigkeit.set(Verifizieren.Verifizieren_mit_Null(Get_Z_Geschwindigkeit))
                Geschwindigkeit_Verifizieren()
            self.Z_Geschwindigkeit.trace("w", Z_Geschwindigkeit_Verifizieren)

            Z_Geschwindigkeit_3_label_1_frame_1 = Label(label_12_frame_11, text="[m/s]:")
            Z_Geschwindigkeit_3_label_1_frame_1.place (x=380, y=70)

            def Geschwindigkeit_Verifizieren():
                Get_X_Geschwindigkeit = self.X_Geschwindigkeit.get()
                Get_X = String_Number.String_to_Number(Get_X_Geschwindigkeit)
                Get_Y_Geschwindigkeit = self.Y_Geschwindigkeit.get()
                Get_Y = String_Number.String_to_Number(Get_Y_Geschwindigkeit)
                Get_Z_Geschwindigkeit = self.Z_Geschwindigkeit.get()
                Get_Z = String_Number.String_to_Number(Get_Z_Geschwindigkeit)
                b=Basic_Calculations.Abstand(Get_X,Get_Y,Get_Z)
                self.Geschwindigkeit_1.set(String_Number.Number_to_String(b))
                if b>=self.Newton_Simulator.Lichtgeschwindigkeit:
                    self.Alert_2 = PhotoImage(file = '../Icon/Alert Icon/16/alert.gif')
                    Acht_2.create_image(2, 2, image = self.Alert_2, anchor = NW)
                    self.Name_Analyse_2.set('Geschwindigkeit ist größer als die gewählte Lichtgeschwindigkeit.')
                elif b<self.Newton_Simulator.Lichtgeschwindigkeit:
                    self.Alert_2 = PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
                    Acht_2.create_image(2, 2, image = self.Alert_2, anchor = NW)
                    self.Name_Analyse_2.set('Geschwindigkeit im grünen Bereich.')
                self.Geschwindigkeit_2.set(Basic_Calculations.Geschwindigkeit_zu(Get_X,Get_Y,Get_Z,self.Newton_Simulator.VX[se_position][0],self.Newton_Simulator.VY[se_position][0],self.Newton_Simulator.VZ[se_position][0]))
                self.Objekt_Tempo_gesetzt=1
                max_min()
                Masstab_berechnen()
                Einzeichnen()


            Acht_2=Canvas(label_12_frame_11, width = 20, height = 20)
            Acht_2.place(x=566,y=10)
            self.Alert_2 = PhotoImage(file = '../Icon/OK Icon/16/ok.gif')
            Acht_2.create_image(2, 2, image = self.Alert_2, anchor = NW)

            self.Name_Analyse_2=StringVar()
            self.Name_Analyse_2.set('Geschwindigkeit im grünen Bereich.')
            Name_label_4 = Label(label_12_frame_11, textvariable=self.Name_Analyse_2)
            Name_label_4.place (x=610,y=10)


            Ges_Geschwindigkeit_Label_1 = Label(label_12_frame_11, text='Geschwindigkeit:')
            Ges_Geschwindigkeit_Label_1.place(x=475, y=40)

            self.Geschwindigkeit_1 = StringVar()
            self.Geschwindigkeit_1.set ("0")
            Ges_Geschwindigkeit_2_label_2_frame_1 = Label(label_12_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Geschwindigkeit_1, bd=2, width=17, anchor=E)
            Ges_Geschwindigkeit_2_label_2_frame_1.place(x=620, y=40)

            Ges_Geschwindigkeit_Label_2 = Label(label_12_frame_11, text='[m/s]')
            Ges_Geschwindigkeit_Label_2.place(x=750, y=40)

            Ges_Geschwindigkeit_Label_2 = Label(label_12_frame_11, text=str(self.Newton_Simulator.Name_Body[se_position])+'(n) Geschwindigkeiten:')
            Ges_Geschwindigkeit_Label_2.place(x=475, y=70)

            self.Geschwindigkeit_2 = StringVar()
            self.Geschwindigkeit_2.set ("1")
            Ges_Geschwindigkeit_3_label_2_frame_1 = Label(label_12_frame_11, justify=RIGHT, relief=SUNKEN, textvariable = self.Geschwindigkeit_2, bd=2, width=17, anchor=E)
            Ges_Geschwindigkeit_3_label_2_frame_1.place(x=663, y=70)

            label_14_frame_11 = Labelframe(frame_11, width=995, height=60, text='Objektfarbe')
            label_14_frame_11.place(x=10, y=430)

            Color_Label_1 = Label(label_14_frame_11, text='Farbe:')
            Color_Label_1.place(x=10, y=10)

            Object_Color = Canvas(label_14_frame_11, width=20, height=20, background=self.Color_1)
            Object_Color.place(x=130, y=6)

            self.Color_2 = StringVar()
            self.Color_2.set(self.Color_1)
            Color_2_label_2_frame_1 = Label(label_14_frame_11, justify=RIGHT, textvariable = self.Color_2, relief=SUNKEN, bd=2,width=17, anchor=E)
            Color_2_label_2_frame_1.place(x=250, y=10)


            def Random_Color_1 (*args):
                self.Color_1=Randomcolor.Randomcolor()
                self.Color_2.set(self.Color_1)
                Object_Color.config(background=self.Color_1)

            Random_Color_1_Label=Button(label_14_frame_11, text="Random", command=Random_Color_1)
            Random_Color_1_Label.place (x=475, y=6)

            def Pick_Color_1 (*args):
                triple, hexstr = colorchooser.askcolor(parent=Objekt_erstellen_1)
                if hexstr!=None:
                    self.Color_1=hexstr
                    self.Color_2.set(self.Color_1)
                    Object_Color.config(background=self.Color_1)

            Pick_Color_2_Label=Button(label_14_frame_11, text="Farbe Auswählen", command=Pick_Color_1)
            Pick_Color_2_Label.place (x=625, y=6)

            def Mouse_Movement_11(event):
                modi=0
                Typ_label_2.config(state=NORMAL)
            def Mouse_Movement_22(event):
                modi=1
                Typ_label_2.config(state=DISABLED)
            frame_11.bind('<Enter>',Mouse_Movement_11)
            frame_22.bind('<Enter>',Mouse_Movement_22)
            Canvas_xy.bind('<Enter>',Mouse_Movement_22)
            Canvas_yz.bind('<Enter>',Mouse_Movement_22)
            Canvas_xz.bind('<Enter>',Mouse_Movement_22)
            label_13_frame_11.bind('<Enter>',Mouse_Movement_11)
            label_11_frame_11.bind('<Enter>',Mouse_Movement_11)
            label_12_frame_11.bind('<Enter>',Mouse_Movement_11)

                #   Hinzufügen Button:
            def Hinzufuegen():
                print('Hinzufügen')
                Name_2=''
                Name_2=Name_2+str(self.Name.get())
                Typ_2=''
                Typ_2=Typ_2+str(Typ_label_2.get())
                Masse_2=0.0
                Masse_2=0.0+String_Number.String_to_Number(self.Masse.get())
                Radius_2=0.0
                Radius_2=0.0+String_Number.String_to_Number(self.Radius.get())
                X_Geschwindigkeit_2=0.0
                X_Geschwindigkeit_2=X_Geschwindigkeit_2+String_Number.String_to_Number(self.X_Geschwindigkeit.get())
                Y_Geschwindigkeit_2=0.0
                Y_Geschwindigkeit_2=Y_Geschwindigkeit_2+String_Number.String_to_Number(self.Y_Geschwindigkeit.get())
                Z_Geschwindigkeit_2=0.0
                Z_Geschwindigkeit_2=Z_Geschwindigkeit_2+String_Number.String_to_Number(self.Z_Geschwindigkeit.get())
                X_Position_2=0.0
                X_Position_2=X_Position_2+String_Number.String_to_Number(self.X_Position.get())
                Y_Position_2=0.0
                Y_Position_2=Y_Position_2+String_Number.String_to_Number(self.Y_Position.get())
                Z_Position_2=0.0
                Z_Position_2=Z_Position_2+String_Number.String_to_Number(self.Z_Position.get())
                Color_3=''
                Color_3=Color_3+str(self.Color_2.get())
                Parent_2=str(self.Parent.get())
                # Elemente in die Gui-Listen Hinzufügen:
                self.pos=self.pos+1
                # Elemente in die Liste Hinzufügen (bei simplen Hinzufügen heist das nichts anderes, als es hinten ran zu hängen:
                ab=self.Tree.insert(self.ID[se_position], self.pos, text=Name_2, values=(Typ_2, Verifizieren.Verifizieren_mit_Null(Masse_2), Verifizieren.Verifizieren_mit_Null(Radius_2), Verifizieren.Verifizieren_mit_Null(X_Geschwindigkeit_2), Verifizieren.Verifizieren_mit_Null(Y_Geschwindigkeit_2), Verifizieren.Verifizieren_mit_Null(Z_Geschwindigkeit_2), Verifizieren.Verifizieren_mit_Null(X_Position_2), Verifizieren.Verifizieren_mit_Null(Y_Position_2), Verifizieren.Verifizieren_mit_Null(Z_Position_2)))
                self.ID.append(ab)
                self.Name_13.append(Name_2)
                self.Newton_Simulator.Objekt_Hinzufuegen_2(Name_2,Typ_2,Masse_2,Radius_2,X_Geschwindigkeit_2,Y_Geschwindigkeit_2,Z_Geschwindigkeit_2,X_Position_2,Y_Position_2,Z_Position_2,Color_3,Parent_2)
                # Toplevel beenden jucheee:
                Objekt_erstellen_1.destroy()

            def Hinzufuegen_2():
                Name_2=''
                Name_2=Name_2+str(self.Name.get())
                abc=Verifizieren.Namen_Verifizeren(Name_2,self.Newton_Simulator.Name_Body)
                if abc==0:
                    Ausruf = Canvas(frame_11, width = 66, height = 66)
                    Ausruf.place(x=340, y=525)
                    self.Ausruf_2 = PhotoImage(file = '../Icon/Alert Icon/64/alert.gif')
                    Ausruf.create_image(0, 0, image = self.Ausruf_2, anchor = NW)
                    Warnung_Label=Label(frame_11, text="Bitte geben Sie einen Namen ein!")
                    Warnung_Label.place (x=415, y=545)
                if abc==1:
                    Ausruf = Canvas(frame_11, width = 66, height = 66)
                    Ausruf.place(x=340, y=525)
                    self.Ausruf_2 = PhotoImage(file = '../Icon/Alert Icon/64/alert.gif')
                    Ausruf.create_image(0, 0, image = self.Ausruf_2, anchor = NW)
                    Warnung_Label=Label(frame_11, text="Der von ihnen gewählte Name wird bereits benutzt.")
                    Warnung_Label.place (x=415, y=545)
                if abc==2:
                    Hinzufuegen()

#-------------------------------------------------------------------

            Hinzufuegen_2 = Button(Objekt_erstellen_1, text="Hinzufügen", command=Hinzufuegen_2)
            Hinzufuegen_2.place (x=475, y=700)

        Satellit_erstellen = Button (label_1_frame_2, text="Satellit erstellen", state=DISABLED, command=Satellit_erstellen)
        Satellit_erstellen.place(x=580, y=12)

                # Erstellt Treeview:

        self.Tree = ttk.Treeview(frame_2, height=29, selectmode='browse', columns=('Art', 'Masse', 'Radius', 'v x', 'v y', 'v z', 'x', 'y', 'z'))      # Kreiert eine Liste mit den genannten Spalten (columns) selectmode=browse sorgt dafür, dass nur ein Element anwählbar ist
        self.Tree.place(x=8,y=100)

                    # Spalten:

        self.Tree.column('#0', width=200, anchor='w')                                # Spricht die Spalte an welche das Widget trägt
        self.Tree.heading('#0', text='Name')

        self.Tree.column('Art', width=115, anchor='w')
        self.Tree.heading('Art', text='Art')

        self.Tree.column('Masse', width=100, anchor='w')
        self.Tree.heading('Masse', text='Masse')

        self.Tree.column('Radius', width=100, anchor='w')
        self.Tree.heading('Radius', text='Radius')

        self.Tree.column('v x', width=80, anchor='w')
        self.Tree.heading('v x', text='v x')

        self.Tree.column('v y', width=80, anchor='w')
        self.Tree.heading('v y', text='v y')

        self.Tree.column('v z', width=80, anchor='w')
        self.Tree.heading('v z', text='v z')

        self.Tree.column('x', width=80, anchor='w')
        self.Tree.heading('x', text='x')

        self.Tree.column('y', width=80, anchor='w')
        self.Tree.heading('y', text='y')

        self.Tree.column('z', width=80, anchor='w')
        self.Tree.heading('z', text='z')

        self.ID[0]=self.Tree.insert('', 0, text='Sonne', values=('Stern', '1.989E30', '1.3914E9', '0.0', '0.0', '0.0', '0.0', '0.0','0.0'))

        self.ID[1]=self.Tree.insert(self.ID[0], 1, text='Erde', values=('Planet', '5.974E24', '6.37E6', '0.0','29.78E3', '0.0', '1.496E11', '0.0','0.0'))

        self.ID[2]=self.Tree.insert(self.ID[1], 2, text='Mond', values=('Mond', '7.349E22', '1.738E6', '0.0', '30.803E3', '0.0','1.499844E11', '0.0','0.0'))


        def Print_focus(*args):
            if self.Tree.focus()=="":
                Objekt_bearbeiten.config(state=DISABLED)
                Satellit_erstellen.config(state=DISABLED)
                Objekt_loeschen.config(state=DISABLED)
            else:
                if self.Tree.focus()!="":
                    Objekt_bearbeiten.config(state=NORMAL)
                    Satellit_erstellen.config(state=NORMAL)
                    Objekt_loeschen.config(state=NORMAL)
        self.Tree.bind("<Button-1>", Print_focus)

            #   3. Frame:

        label_1_frame_3 = Frame(root, width=1012, height=714)                            # Auswertung

        label_1_frame_4 = Labelframe(label_1_frame_3, width=250, height=95, text='Berechnen:')
        label_1_frame_4.place (x=10, y=615)

        label_1_frame_5 = Labelframe(label_1_frame_3, width=735, height=95)
        label_1_frame_5.place (x=270, y=615)

        label_1_frame_6 = Labelframe(label_1_frame_3, width=500, height=200, text='Anzeige:')
        label_1_frame_6.place (x=505, y=417)

                        # Startbutton:

        modi=0

        def Start(*args):
            self.Start(self.Gravitationskonstante.get(),self.Berechnungsart.get(),self.Lichtgeschwindigkeit.get(),self.Iterationsanzahl.get(),self.Iterationsintervall.get(),self.Speicherintervall.get())
            Einzeichnen()

        Start = Button (label_1_frame_4, text="Start", command=Start, width=20, bd=4)
        Start.place (x=45, y=20)

        width_x_2=450
        height_y_2=295

        self.Objekt_gesetzt=0
        self.Objekt_Tempo_gesetzt=0

        self.Color_1 = Randomcolor.Randomcolor()

        # Weiterführende Einstellungen der Anzeige:
        self.Zeichenmodus = IntVar()
        self.Zeichenmodus.set(1)
        self.Groesse_Bd_Kugeln=StringVar()
        self.Groesse_Bd_Kugeln.set('3')
        self.Groesse_Bd_Kugeln_2=StringVar()
        self.Groesse_Bd_Kugeln_2.set('10')
        self.Groesse_Bd_text_1=StringVar()
        self.Groesse_Bd_text_1.set("Größe:")
        Kugeln_Bd_1=Radiobutton(label_1_frame_6, text="Kugeln gleicher Größe", variable=self.Zeichenmodus, value=1).place(x=10,y=10)#.place(x=59+width_x_2,y=123+height_y_2)
        Kugeln_Bd_2=Radiobutton(label_1_frame_6, text="Kugeln nach Radius", variable=self.Zeichenmodus, value=2).place(x=10,y=40)#.place(x=59+width_x_2,y=123+height_y_2+30)
        Kugeln_Bd_3=Radiobutton(label_1_frame_6, text="Kugeln nach Entfernung", variable=self.Zeichenmodus, value=3).place(x=10,y=70)#.place(x=59+width_x_2,y=123+height_y_2+60)
        Kugeln_Bd_4=Radiobutton(label_1_frame_6, text="Tatsächliche Größe", variable=self.Zeichenmodus, value=4).place(x=10,y=100)#.place(x=59+width_x_2,y=123+height_y_2+90)

        def Kugeln_Bd_1_Angewaehlt(*args):
            if self.Zeichenmodus.get()==1:
                self.Groesse_Bd_text_1.set("Größe:")
                Groesse_Bd_2.config(state=DISABLED)
                Groesse_Bd_1_Label_2.config(state=NORMAL)
                Groesse_Bd_1_Label.config(state=NORMAL)
                Groesse_Bd_1.config(state=NORMAL)
                Groesse_Bd_2_Label_2.config(state=DISABLED)
                Groesse_Bd_2_Label.config(state=DISABLED)
            elif self.Zeichenmodus.get()==2:
                self.Groesse_Bd_text_1.set("Von:")
                Groesse_Bd_2.config(state=NORMAL)
                Groesse_Bd_1_Label_2.config(state=NORMAL)
                Groesse_Bd_1_Label.config(state=NORMAL)
                Groesse_Bd_1.config(state=NORMAL)
                Groesse_Bd_2_Label_2.config(state=NORMAL)
                Groesse_Bd_2_Label.config(state=NORMAL)
            elif self.Zeichenmodus.get()==3:
                self.Groesse_Bd_text_1.set("Von:")
                Groesse_Bd_2.config(state=NORMAL)
                Groesse_Bd_1_Label_2.config(state=NORMAL)
                Groesse_Bd_1_Label.config(state=NORMAL)
                Groesse_Bd_1.config(state=NORMAL)
                Groesse_Bd_2_Label_2.config(state=NORMAL)
                Groesse_Bd_2_Label.config(state=NORMAL)
            elif self.Zeichenmodus.get()==4:
                self.Groesse_Bd_text_1.set("Groesse:")
                Groesse_Bd_2.config(state=DISABLED)
                Groesse_Bd_1_Label_2.config(state=DISABLED)
                Groesse_Bd_1_Label.config(state=DISABLED)
                Groesse_Bd_1.config(state=DISABLED)
                Groesse_Bd_2_Label_2.config(state=DISABLED)
                Groesse_Bd_2_Label.config(state=DISABLED)
            Einzeichnen()
        self.Zeichenmodus.set(1)
        self.Zeichenmodus.trace("w", Kugeln_Bd_1_Angewaehlt)

        self.Anzeigesp = StringVar()
        self.Anzeigesp.set ("J")
        SpeedAnzeige = Checkbutton(label_1_frame_5, text="Anzeige der Geschwindigkeit", variable=self.Anzeigesp, onvalue="J", offvalue="N")
        SpeedAnzeige.place (x=45, y=10)

        def Speed_rel(*args):                                        # Aktiviert und Deaktiviert die Lichtgeschwindigkeitseingabe
            if self.Anzeigesp.get() == "N":
                self.Bd_Speed               =0
            else:
                self.Bd_Speed               =1
            Einzeichnen()
        self.Anzeigesp.trace("w", Speed_rel)

        self.Anzeigeku = StringVar()
        self.Anzeigeku.set ("J")
        SpeedAnzeige = Checkbutton(label_1_frame_5, text="Anzeige der Körper", variable=self.Anzeigeku, onvalue="J", offvalue="N")
        SpeedAnzeige.place (x=270, y=10)

        def ku_rel(*args):                                        # Aktiviert und Deaktiviert die Lichtgeschwindigkeitseingabe
            if self.Anzeigeku.get() == "N":
                self.Bd_Kugeln              =0
            else:
                self.Bd_Kugeln              =1
            Einzeichnen()
        self.Anzeigeku.trace("w", ku_rel)

        self.Anzeigeli = StringVar()
        self.Anzeigeli.set ("N")
        SpeedAnzeige = Checkbutton(label_1_frame_5, text="Anzeige der approximierten Flugbahnen", variable=self.Anzeigeli, onvalue="J", offvalue="N")
        SpeedAnzeige.place (x=495, y=10)

        def li_rel(*args):                                        # Aktiviert und Deaktiviert die Lichtgeschwindigkeitseingabe
            if self.Anzeigeli.get() == "N":
                self.Linien              =0
            else:
                self.Linien             =1
            Einzeichnen()
        self.Anzeigeli.trace("w", li_rel)

        Groesse_Bd_1_Label=Label(label_1_frame_6,textvariable=self.Groesse_Bd_text_1)
        Groesse_Bd_1_Label.place(x=199,y=10)
        Groesse_Bd_1_Label.config(state=NORMAL)
        Groesse_Bd_1=Spinbox(label_1_frame_6,from_=1, to=100,textvariable=self.Groesse_Bd_Kugeln,width=7,bd=2)
        Groesse_Bd_1.place(x=279,y=10)
        Groesse_Bd_1.config(state=NORMAL)
        Groesse_Bd_1_Label_2=Label(label_1_frame_6,text="[Pixel]")
        Groesse_Bd_1_Label_2.place(x=355,y=10)
        Groesse_Bd_2_Label=Label(label_1_frame_6,text="Bis:")
        Groesse_Bd_2_Label.place(x=199,y=40)
        Groesse_Bd_2_Label.config(state=DISABLED)
        Groesse_Bd_2=Spinbox(label_1_frame_6,from_=1, to=100,textvariable=self.Groesse_Bd_Kugeln_2,width=7,bd=2)
        Groesse_Bd_2.place(x=279,y=40)
        Groesse_Bd_2.config(state=DISABLED)
        Groesse_Bd_2_Label_2=Label(label_1_frame_6,text="[Pixel]")
        Groesse_Bd_2_Label_2.place(x=355,y=40)
        Groesse_Bd_2_Label_2.config(state=DISABLED)
        Geschwindigkeit_Bd_1_Label_1=Label(label_1_frame_6, text='Geschwindigkeit:')
        Geschwindigkeit_Bd_1_Label_1.place(x=10,y=145)
        self.Geschwindigkeit_pro_Pixel=StringVar()
        self.Geschwindigkeit_pro_Pixel.set('1.0')
        Geschwindigkeit_Bd_1_Label_2=Entry(label_1_frame_6, textvariable=self.Geschwindigkeit_pro_Pixel,bd=2,justify=RIGHT,width=17)
        Geschwindigkeit_Bd_1_Label_2.place(x=192,y=145)
        Geschwindigkeit_Bd_1_Label_3=Label(label_1_frame_6, text='[1000*(m/s)/Pixel]')
        Geschwindigkeit_Bd_1_Label_3.place(x=350,y=145)

        def Geschwindigkeit_Verifizieren(*args):
            Get_Geschwindigkeit = self.Geschwindigkeit_pro_Pixel.get()
            a=Verifizieren.Verifizieren_ohne_Minus(Get_Geschwindigkeit)
            self.Geschwindigkeit_pro_Pixel.set(a)
            max_min()
            Masstab_berechnen()
            Einzeichnen()
        self.Geschwindigkeit_pro_Pixel.trace("w", Geschwindigkeit_Verifizieren)

        self.Bd_X=StringVar()
        self.Bd_X.set('0')
        X_Label_label_1_frame_3=Label(label_1_frame_5, text='X:').place(x=50,y=45)
        X_Label_label_1_frame_3_1=Label(label_1_frame_5, textvariable=self.Bd_X, relief=SUNKEN,bd=2,width=15).place(x=100,y=45)

        self.Bd_Y=StringVar()
        self.Bd_Y.set('0')
        Y_Label_label_1_frame_3=Label(label_1_frame_5, text='Y:').place(x=275,y=45)
        Y_Label_label_1_frame_3_1=Label(label_1_frame_5, textvariable=self.Bd_Y, relief=SUNKEN,bd=2,width=15).place(x=325,y=45)

        self.Bd_Z=StringVar()
        self.Bd_Z.set('0')
        Z_Label_label_1_frame_3=Label(label_1_frame_5, text='Z:').place(x=500,y=45)
        Z_Label_label_1_frame_3_1=Label(label_1_frame_5, textvariable=self.Bd_Z, relief=SUNKEN,bd=2,width=15).place(x=550,y=45)

        def max_min():
            # Startwerte für die kleinsten und größten x,y und z Werte der Liste:
            self.Newton_Simulator.Maximalwertsuche()
            self.minX=self.Newton_Simulator.MinX
            self.minY=self.Newton_Simulator.MinY
            self.minZ=self.Newton_Simulator.MinZ
            self.maxX=self.Newton_Simulator.MaxX
            self.maxY=self.Newton_Simulator.MaxY
            self.maxZ=self.Newton_Simulator.MaxZ
            if self.Objekt_gesetzt==1:
                x=String_Number.String_to_Number(self.X_Position.get())
                y=String_Number.String_to_Number(self.Y_Position.get())
                z=String_Number.String_to_Number(self.Z_Position.get())
                if x>self.maxX:
                    self.minX=x
                elif x<self.minX:
                    self.minX=x
                if y>self.maxY:
                    self.maxY=y
                elif y<self.minY:
                    self.minY=y
                if z>self.maxZ:
                    self.maxZ=z
                elif z<self.minZ:
                    self.minZ=z

        def Masstab_berechnen():
            x_diff=self.maxX-self.minX
            y_diff=self.maxY-self.minY
            z_diff=self.maxZ-self.minZ
            if x_diff==0 and y_diff==0 and z_diff==0:
                x_diff=100
                y_diff=100
                z_diff=100
            # Für xy:
            if y_diff!=0:
                if x_diff!=0:
                    Mpp_y_xy=y_diff/height_y_2
                    Mpp_x_xy=x_diff/width_x_2
                    if Mpp_y_xy>=Mpp_x_xy:
                        self.Bd_Mpp_xy=Mpp_y_xy
                    else:
                        self.Bd_Mpp_xy=Mpp_x_xy
                elif x_diff==0:
                     self.Bd_Mpp_xy=y_diff/height_y_2
            elif y_diff==0:
                if x_diff!=0:
                    self.Bd_Mpp_xy=x_diff/width_x_2
                elif x_diff==0:
                    self.Bd_Mpp_xy=0
            # Für yz:
            if z_diff!=0:
                if y_diff!=0:
                    Mpp_y_yz=y_diff/height_y_2
                    Mpp_z_yz=z_diff/width_x_2
                    if Mpp_y_yz>=Mpp_z_yz:
                        self.Bd_Mpp_yz=Mpp_y_yz
                    else:
                        self.Bd_Mpp_yz=Mpp_z_yz
                elif y_diff==0:
                     self.Bd_Mpp_yz=z_diff/width_x_2
            elif z_diff==0:
                if y_diff!=0:
                    self.Bd_Mpp_yz=y_diff/height_y_2
                elif y_diff==0:
                    self.Bd_Mpp_yz=0
            # Für xz:
            if z_diff!=0:
                if x_diff!=0:
                    Mpp_z_xz=z_diff/height_y_2
                    Mpp_x_xz=x_diff/width_x_2
                    if Mpp_z_xz>=Mpp_x_xz:
                        self.Bd_Mpp_xz=Mpp_z_xz
                    else:
                        self.Bd_Mpp_xz=Mpp_x_xz
                elif x_diff==0:
                     self.Bd_Mpp_xz=z_diff/height_y_2
            elif z_diff==0:
                if x_diff!=0:
                    self.Bd_Mpp_xz=x_diff/width_x_2
                elif x_diff==0:
                    self.Bd_Mpp_xz=0
            # Vergleich der Mpp's (meiste Meter pro Pixel gesucht):
            self.Bd_Mpp=self.Bd_Mpp_xy
            if self.Bd_Mpp_xz>self.Bd_Mpp:
                self.Bd_Mpp=self.Bd_Mpp_xz
            if self.Bd_Mpp_yz>self.Bd_Mpp:
                self.Bd_Mpp=self.Bd_Mpp_yz
            if self.Bd_Mpp==0:
                self.Bd_Mpp=0.1
            # Vergrößern von Mpp um 10% pro Seite:
            self.Bd_Mpp=self.Bd_Mpp*1.2
            # Mittelpunkte_bestimmen:
            self.Bd_Mittelpunkt_x=self.minX+x_diff/2
            self.Bd_Mittelpunkt_y=self.minY+y_diff/2
            self.Bd_Mittelpunkt_z=self.minZ+z_diff/2


        def Einzeichnen():
            # Hinzufügen der Punkte / Kreise auf die beschriebenen Arten und Weisen erst in Richtung :
                Canvas_xy.delete(ALL)
                Canvas_yz.delete(ALL)
                Canvas_xz.delete(ALL)
                self.xy_koord = PhotoImage(file = '../Icon/Koordinaten/xy.gif')
                Canvas_xy.create_image(12,height_y_2-39, image = self.xy_koord, anchor = NW)
                self.yz_koord = PhotoImage(file = '../Icon/Koordinaten/yz.gif')
                Canvas_yz.create_image(width_x_2-39, height_y_2-39, image = self.yz_koord, anchor = NW)
                self.xz_koord = PhotoImage(file = '../Icon/Koordinaten/xz.gif')
                Canvas_xz.create_image(12, height_y_2-39, image = self.xz_koord, anchor = NW)
                Mpp=self.Bd_Mpp
                if Mpp==0:
                    Mpp=0.1
                Mitte_x=self.Bd_Mittelpunkt_x
                Mitte_y=self.Bd_Mittelpunkt_y
                Mitte_z=self.Bd_Mittelpunkt_z
                speed=1000*(String_Number.String_to_Number(self.Geschwindigkeit_pro_Pixel.get()))
                if len(self.Newton_Simulator.Name_Body)>0:
                    if self.Linien==1:
                        for k in range(0,len(self.Newton_Simulator.Name_Body)):
                            for l in range(0,len(self.Newton_Simulator.VZ[k])-1):
                                x=self.Newton_Simulator.X[k][l]
                                y=self.Newton_Simulator.Y[k][l]
                                z=self.Newton_Simulator.Z[k][l]
                                x2=self.Newton_Simulator.X[k][l+1]
                                y2=self.Newton_Simulator.Y[k][l+1]
                                z2=self.Newton_Simulator.Z[k][l+1]
                                # Zeichnet die Geraden ein:
                                pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                                pos_x_xy2=width_x_2/2+(x2-Mitte_x)/Mpp
                                pos_y_xy2=height_y_2/2-(y2-Mitte_y)/Mpp
                                if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                    Canvas_xy.create_line(pos_x_xy,pos_y_xy,pos_x_xy2,pos_y_xy2, fill=self.Newton_Simulator.Color[k])
                                pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                                pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                                pos_z_yz2=width_x_2/2-(z2-Mitte_z)/Mpp
                                pos_y_yz2=height_y_2/2-(y2-Mitte_y)/Mpp
                                if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                    Canvas_yz.create_line(pos_z_yz,pos_y_yz,pos_z_yz2,pos_y_yz2, fill=self.Newton_Simulator.Color[k])
                                pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                                pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_z_xz2=height_y_2/2-(z2-Mitte_z)/Mpp
                                pos_x_xz2=width_x_2/2+(x2-Mitte_x)/Mpp
                                if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                    Canvas_xz.create_line(pos_x_xz,pos_z_xz,pos_x_xz2,pos_z_xz2, fill=self.Newton_Simulator.Color[k])
                    if self.Zeichenmodus.get()==1:
                        Groesse=String_Number.String_to_Number(self.Groesse_Bd_Kugeln.get())
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            if self.Bd_Kugeln==1:
                                # Zeichnet die Punkte ein:
                                pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                                if pos_x_xy-Groesse>0 and pos_x_xy+Groesse<width_x_2 and pos_y_xy-Groesse>0 and pos_y_xy+Groesse<height_y_2:
                                    Canvas_xy.create_oval(abs(pos_x_xy-Groesse),abs(pos_y_xy-Groesse),abs(pos_x_xy+Groesse),abs(pos_y_xy+Groesse), fill=self.Newton_Simulator.Color[i])
                                pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                                pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                                if pos_z_yz-Groesse>0 and pos_z_yz+Groesse<width_x_2 and pos_y_yz-Groesse>0 and pos_y_yz+Groesse<height_y_2:
                                    Canvas_yz.create_oval(abs(pos_z_yz-Groesse),abs(pos_y_yz-Groesse),abs(pos_z_yz+Groesse),abs(pos_y_yz+Groesse), fill=self.Newton_Simulator.Color[i])
                                pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                                pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                                if pos_x_xz-Groesse>0 and pos_x_xz+Groesse<width_x_2 and pos_z_xz-Groesse>0 and pos_z_xz+Groesse<height_y_2:
                                    Canvas_xz.create_oval(abs(pos_x_xz-Groesse),abs(pos_z_xz-Groesse),abs(pos_x_xz+Groesse),abs(pos_z_xz+Groesse), fill=self.Newton_Simulator.Color[i])
                            if self.Bd_Speed==1:
                                x=self.Newton_Simulator.X[i][0]
                                y=self.Newton_Simulator.Y[i][0]
                                z=self.Newton_Simulator.Z[i][0]
                                vx=self.Newton_Simulator.VX[i][0]
                                vy=self.Newton_Simulator.VY[i][0]
                                vz=self.Newton_Simulator.VZ[i][0]
                                pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                                pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                                pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                                pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                                # Zeichnet die Geraden der Geschwindigkeit ein:
                                if abs(vx)>speed or abs(vy)>speed:
                                    vx_2=vx/speed
                                    vy_2=-vy/speed
                                    if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                        if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                            Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                                if abs(vy)>speed or abs(vz)>speed:
                                    vy_2=-vy/speed
                                    vz_2=-vz/speed
                                    if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                        if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                            Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                                if abs(vx)>speed or abs(vz)>speed:
                                    vx_2=vx/speed
                                    vz_2=-vz/speed
                                    if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                        if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                            Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                    if self.Zeichenmodus.get()==2:
                        Groesse_1=String_Number.String_to_Number(self.Groesse_Bd_Kugeln.get())
                        Groesse_2=String_Number.String_to_Number(self.Groesse_Bd_Kugeln_2.get())
                        Groesse=[]
                        Groesse=self.Newton_Simulator.Radius_Anteil(Groesse_1,Groesse_2,String_Number.String_to_Number(String_Number.Number_to_String(self.Newton_Simulator.Radius_Body[0][0])))
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            if self.Bd_Kugeln==1:
                                # Zeichnet die Punkte ein:
                                pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                                if pos_x_xy-Groesse[i]>0 and pos_x_xy+Groesse[i]<width_x_2 and pos_y_xy-Groesse[i]>0 and pos_y_xy+Groesse[i]<height_y_2:
                                    Canvas_xy.create_oval(abs(pos_x_xy-Groesse[i]),abs(pos_y_xy-Groesse[i]),abs(pos_x_xy+Groesse[i]),abs(pos_y_xy+Groesse[i]), fill=self.Newton_Simulator.Color[i])
                                pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                                pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                                if pos_z_yz-Groesse[i]>0 and pos_z_yz+Groesse[i]<width_x_2 and pos_y_yz-Groesse[i]>0 and pos_y_yz+Groesse[i]<height_y_2:
                                    Canvas_yz.create_oval(abs(pos_z_yz-Groesse[i]),abs(pos_y_yz-Groesse[i]),abs(pos_z_yz+Groesse[i]),abs(pos_y_yz+Groesse[i]), fill=self.Newton_Simulator.Color[i])
                                pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                                pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                                if pos_x_xz-Groesse[i]>0 and pos_x_xz+Groesse[i]<width_x_2 and pos_z_xz-Groesse[i]>0 and pos_z_xz+Groesse[i]<height_y_2:
                                    Canvas_xz.create_oval(abs(pos_x_xz-Groesse[i]),abs(pos_z_xz-Groesse[i]),abs(pos_x_xz+Groesse[i]),abs(pos_z_xz+Groesse[i]), fill=self.Newton_Simulator.Color[i])
                            if self.Bd_Speed==1:
                                x=self.Newton_Simulator.X[i][0]
                                y=self.Newton_Simulator.Y[i][0]
                                z=self.Newton_Simulator.Z[i][0]
                                vx=self.Newton_Simulator.VX[i][0]
                                vy=self.Newton_Simulator.VY[i][0]
                                vz=self.Newton_Simulator.VZ[i][0]
                                pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                                pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                                pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                                pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                                # Zeichnet die Geraden der Geschwindigkeit ein:
                                if abs(vx)>speed or abs(vy)>speed:
                                    vx_2=vx/speed
                                    vy_2=-vy/speed
                                    if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                        if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                            Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                                if abs(vy)>speed or abs(vz)>speed:
                                    vy_2=-vy/speed
                                    vz_2=-vz/speed
                                    if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                        if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                            Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                                if abs(vx)>speed or abs(vz)>speed:
                                    vx_2=vx/speed
                                    vz_2=-vz/speed
                                    if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                        if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                            Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                    if self.Zeichenmodus.get()==3:
                        # Nach entfernung:
                        Groesse_1=String_Number.String_to_Number(self.Groesse_Bd_Kugeln.get())
                        Groesse_2=String_Number.String_to_Number(self.Groesse_Bd_Kugeln_2.get())
                        Groesse=[]
                        Groesse_x=self.Newton_Simulator.Entfernung_Anteil_x(Groesse_1,Groesse_2,String_Number.String_to_Number((String_Number.Number_to_String(self.Newton_Simulator.X[0][0]))))
                        Groesse_y=self.Newton_Simulator.Entfernung_Anteil_y(Groesse_1,Groesse_2,String_Number.String_to_Number((String_Number.Number_to_String(self.Newton_Simulator.Y[0][0]))))
                        Groesse_z=self.Newton_Simulator.Entfernung_Anteil_z(Groesse_1,Groesse_2,String_Number.String_to_Number((String_Number.Number_to_String(self.Newton_Simulator.Z[0][0]))))
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            if self.Bd_Kugeln==1:
                                # Zeichnet die Punkte ein:
                                pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                                if pos_x_xy-Groesse_z[i]>0 and pos_x_xy+Groesse_z[i]<width_x_2 and pos_y_xy-Groesse_z[i]>0 and pos_y_xy+Groesse_z[i]<height_y_2:
                                    Canvas_xy.create_oval(abs(pos_x_xy-Groesse_z[i]),abs(pos_y_xy-Groesse_z[i]),abs(pos_x_xy+Groesse_z[i]),abs(pos_y_xy+Groesse_z[i]), fill=self.Newton_Simulator.Color[i])
                                pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                                pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                                if pos_z_yz-Groesse_x[i]>0 and pos_z_yz+Groesse_x[i]<width_x_2 and pos_y_yz-Groesse_x[i]>0 and pos_y_yz+Groesse_x[i]<height_y_2:
                                    Canvas_yz.create_oval(abs(pos_z_yz-Groesse_x[i]),abs(pos_y_yz-Groesse_x[i]),abs(pos_z_yz+Groesse_x[i]),abs(pos_y_yz+Groesse_x[i]), fill=self.Newton_Simulator.Color[i])
                                pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                                pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                                if pos_x_xz-Groesse_y[i]>0 and pos_x_xz+Groesse_y[i]<width_x_2 and pos_z_xz-Groesse_y[i]>0 and pos_z_xz+Groesse_y[i]<height_y_2:
                                    Canvas_xz.create_oval(abs(pos_x_xz-Groesse_y[i]),abs(pos_z_xz-Groesse_y[i]),abs(pos_x_xz+Groesse_y[i]),abs(pos_z_xz+Groesse_y[i]), fill=self.Newton_Simulator.Color[i])
                            if self.Bd_Speed==1:
                                x=self.Newton_Simulator.X[i][0]
                                y=self.Newton_Simulator.Y[i][0]
                                z=self.Newton_Simulator.Z[i][0]
                                vx=self.Newton_Simulator.VX[i][0]
                                vy=self.Newton_Simulator.VY[i][0]
                                vz=self.Newton_Simulator.VZ[i][0]
                                pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                                pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                                pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                                pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                                # Zeichnet die Geraden der Geschwindigkeit ein:
                                if abs(vx)>speed or abs(vy)>speed:
                                    vx_2=vx/speed
                                    vy_2=-vy/speed
                                    if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                        if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                            Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                                if abs(vy)>speed or abs(vz)>speed:
                                    vy_2=-vy/speed
                                    vz_2=-vz/speed
                                    if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                        if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                            Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                                if abs(vx)>speed or abs(vz)>speed:
                                    vx_2=vx/speed
                                    vz_2=-vz/speed
                                    if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                        if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                            Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                    if self.Zeichenmodus.get()==4:
                        for i in range(0,len(self.Newton_Simulator.Name_Body)):
                            x=self.Newton_Simulator.X[i][0]
                            y=self.Newton_Simulator.Y[i][0]
                            z=self.Newton_Simulator.Z[i][0]
                            vx=self.Newton_Simulator.VX[i][0]
                            vy=self.Newton_Simulator.VY[i][0]
                            vz=self.Newton_Simulator.VZ[i][0]
                            if self.Bd_Kugeln==1:
                                # Zeichnet die Punkte ein:
                                pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                                # Bestimmt die Groesse (mind. 1 Pixel):
                                Groesse=self.Newton_Simulator.Radius_Body[i][0]/Mpp
                                if Groesse<1:
                                    Groesse=1
                                if pos_x_xy-Groesse>0 and pos_x_xy+Groesse<width_x_2 and pos_y_xy-Groesse>0 and pos_y_xy+Groesse<height_y_2:
                                    Canvas_xy.create_oval(abs(pos_x_xy-Groesse),abs(pos_y_xy-Groesse),abs(pos_x_xy+Groesse),abs(pos_y_xy+Groesse), fill=self.Newton_Simulator.Color[i])
                                pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                                pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                                if pos_z_yz-Groesse>0 and pos_z_yz+Groesse<width_x_2 and pos_y_yz-Groesse>0 and pos_y_yz+Groesse<height_y_2:
                                    Canvas_yz.create_oval(abs(pos_z_yz-Groesse),abs(pos_y_yz-Groesse),abs(pos_z_yz+Groesse),abs(pos_y_yz+Groesse), fill=self.Newton_Simulator.Color[i])
                                pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                                pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                                if pos_x_xz-Groesse>0 and pos_x_xz+Groesse<width_x_2 and pos_z_xz-Groesse>0 and pos_z_xz+Groesse<height_y_2:
                                    Canvas_xz.create_oval(abs(pos_x_xz-Groesse),abs(pos_z_xz-Groesse),abs(pos_x_xz+Groesse),abs(pos_z_xz+Groesse), fill=self.Newton_Simulator.Color[i])
                            if self.Bd_Speed==1:
                                x=self.Newton_Simulator.X[i][0]
                                y=self.Newton_Simulator.Y[i][0]
                                z=self.Newton_Simulator.Z[i][0]
                                vx=self.Newton_Simulator.VX[i][0]
                                vy=self.Newton_Simulator.VY[i][0]
                                vz=self.Newton_Simulator.VZ[i][0]
                                pos_z_xz=height_y_2/2-(z-Mitte_z)/Mpp
                                pos_x_xz=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_x_xy=width_x_2/2+(x-Mitte_x)/Mpp
                                pos_y_xy=height_y_2/2-(y-Mitte_y)/Mpp
                                pos_z_yz=width_x_2/2-(z-Mitte_z)/Mpp
                                pos_y_yz=height_y_2/2-(y-Mitte_y)/Mpp
                                # Zeichnet die Geraden der Geschwindigkeit ein:
                                if abs(vx)>speed or abs(vy)>speed:
                                    vx_2=vx/speed
                                    vy_2=-vy/speed
                                    if pos_x_xy+vx_2>0 and pos_x_xy+vx_2<width_x_2 and pos_y_xy+vx_2>0 and pos_y_xy+vx_2<height_y_2:
                                        if pos_x_xy>0 and pos_x_xy<width_x_2 and pos_y_xy>0 and pos_y_xy<height_y_2:
                                            Canvas_xy.create_line(abs(pos_x_xy),abs(pos_y_xy),abs(pos_x_xy+vx_2),abs(pos_y_xy+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                                if abs(vy)>speed or abs(vz)>speed:
                                    vy_2=-vy/speed
                                    vz_2=-vz/speed
                                    if pos_z_yz+vz_2>0 and pos_z_yz+vz_2<width_x_2 and pos_y_yz+vy_2>0 and pos_y_yz+vy_2<height_y_2:
                                        if pos_z_yz>0 and pos_z_yz<width_x_2 and pos_y_yz>0 and pos_y_yz<height_y_2:
                                            Canvas_yz.create_line(abs(pos_z_yz),abs(pos_y_yz),abs(pos_z_yz+vz_2),abs(pos_y_yz+vy_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                                if abs(vx)>speed or abs(vz)>speed:
                                    vx_2=vx/speed
                                    vz_2=-vz/speed
                                    if pos_x_xz+vx_2>0 and pos_x_xz+vx_2<width_x_2 and pos_z_xz+vz_2>0 and pos_z_xz+vz_2<height_y_2:
                                        if pos_x_xz>0 and pos_x_xz<width_x_2 and pos_z_xz>0 and pos_z_xz<height_y_2:
                                            Canvas_xz.create_line(abs(pos_x_xz),abs(pos_z_xz),abs(pos_x_xz+vx_2),abs(pos_z_xz+vz_2), fill=self.Newton_Simulator.Color[i],arrow=LAST,arrowshape=(5,7,3))
                # Skript welches den Masstab und Orientierungspunkte Anzeigen soll:
                # Zuerst werden die Maxima und Minima der Canvases bestimmt:
                Canvas_coord_yz.delete(ALL)
                Canvas_coord_xz.delete(ALL)
                Canvas_coord_xy.delete(ALL)
                    # geg.: Mpp, Mitte_z, Mitte_x, Mitte_y
                pc=30856776000000000    # 1*Parsec
                Lj=9460528000000000     # 1*Lichtjahr
                ae=149597870691         # 1*Astronomische Einheit
                km=1000                 # 1*Kilometer
                hm=100                  # 1*Hectometer
                dam=10                  # 1*Dekameter
                m=1                     # 1*meter
                dm=0.1                  # 0.1*meter
                cm=0.01                 # 0.01*meter

                # xy, yz - y (height_y_2) - Achsen max und min:
                max_y=Mitte_y+height_y_2*Mpp/2                              # Oberes Ende!
                min_y=Mitte_y-height_y_2*Mpp/2                              # Unteres Ende!
                # Die Skala soll ermitelt werden:
                # Wir teilen min durch die Längen der einheiten und runden diese zu einer int, dann zeichnen wir alle relevanten einund setzen Einheitenanzahl eins höher
                e=0                     # Anzeige aus=0, an=1
                Aktueller_Schritt=8     #0=Parsec, 1=Lj, 2=AE.....

                if Aktueller_Schritt==8:
                    # 1 cm (cm) = 1 m
                    a=int(round(min_y/cm))
                    stop=0
                    d=0
                    c=abs(((a+1)*cm)/Mpp-(a*cm/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*cm>min_y:
                                if a*cm<max_y:
                                    if Mpp!=0:
                                        y=(a*cm-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"cm", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==7:
                    # 1 dm (dm) = 10 m
                    a=int(round(min_y/dm))
                    stop=0
                    d=0
                    c=abs(((a+1)*dm)/Mpp-(a*dm/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*dm>min_y:
                                if a*dm<max_y:
                                    if Mpp!=0:
                                        y=(a*dm-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"dm", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==6:
                    # 1 m (m) = 1 m
                    a=int(round(min_y/m))
                    stop=0
                    d=0
                    c=abs(((a+1)*m)/Mpp-(a*m/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*m>min_y:
                                if a*m<max_y:
                                    if Mpp!=0:
                                        y=(a*m-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"m", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==5:
                    # 1 dam (dam) = 10 m
                    a=int(round(min_y/dm))
                    stop=0
                    d=0
                    c=abs(((a+1)*dam)/Mpp-(a*dam/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*dam>min_y:
                                if a*dam<max_y:
                                    if Mpp!=0:
                                        y=(a*dam-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"dam", fill="white",font=("Helvectica", "6"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==4:
                    # 1 hm (hm) = 100 m
                    a=int(round(min_y/hm))
                    stop=0
                    d=0
                    c=abs(((a+1)*hm)/Mpp-(a*hm/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*hm>min_y:
                                if a*hm<max_y:
                                    if Mpp!=0:
                                        y=(a*hm-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"hm", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==3:
                    # 1 km (km) = 1000 m
                    a=int(round(min_y/km))
                    stop=0
                    d=0
                    c=abs(((a+1)*km)/Mpp-(a*km/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*km>min_y:
                                if a*km<max_y:
                                    if Mpp!=0:
                                        y=(a*km-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"km", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==2:
                    # 1 ae (ae) = 149597870691 m
                    a=int(round(min_y/ae))
                    stop=0
                    d=0
                    c=abs(((a+1)*ae)/Mpp-(a*ae/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*ae>min_y:
                                if a*ae<max_y:
                                    if Mpp!=0:
                                        y=(a*ae-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"AE", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==1:
                    # 1 Lj (Lj) = 9460528000000000 m
                    a=int(round(min_y/Lj))
                    stop=0
                    d=0
                    c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*Lj>min_y:
                                if a*Lj<max_y:
                                    if Mpp!=0:
                                        y=(a*Lj-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==1:
                    # 1 Lj (Lj) = 9460528000000000 m
                    a=int(round(min_y/Lj))
                    stop=0
                    d=0
                    c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*Lj>min_y:
                                if a*Lj<max_y:
                                    if Mpp!=0:
                                        y=(a*Lj-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==0:
                    # 1 pc (Lj) = 30856776000000000 m
                    a=int(round(min_y/pc))
                    stop=0
                    d=0
                    c=abs(((a+1)*pc)/Mpp-(a*pc/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*pc>min_y:
                                if a*pc<max_y:
                                    if Mpp!=0:
                                        y=(a*pc-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"pc", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==-1:
                    # Format unbekannt:
                    if e==0:
                        f=1
                        g=0
                        stop=0
                        d=0
                        while g==0:
                            h=(int(round(min_y/10**f)+1)*10**f)/Mpp-(int(round(min_y/10**f))*10**f)/Mpp
                            if h>20 and h<height_y_2:
                                a=int(round(min_y/10**f))
                                c=abs(((a+1)*10**f)/Mpp-(a*10**f/Mpp))
                                g=1
                            else:
                                f=f+1
                        while stop==0:
                            #print(a)
                            if a*10**f>min_y:
                                if a*10**f<max_y:
                                    if Mpp!=0:
                                        y=-(a*10**f-Mitte_y)/Mpp
                                        b=height_y_2/2+y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"mE"+str(f), fill="white",font=("Helvectica", "6"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xy.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xy.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                # Rechtes Canvas (yz):
                e=0                     # Anzeige aus=0, an=1
                Aktueller_Schritt=8     #0=Parsec, 1=Lj, 2=AE.....

                if Aktueller_Schritt==8:
                    # 1 cm (cm) = 1 m
                    a=int(round(min_y/cm))
                    stop=0
                    d=0
                    c=abs(((a+1)*cm)/Mpp-(a*cm/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*cm>min_y:
                                if a*cm<max_y:
                                    if Mpp!=0:
                                        y=(a*cm-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                            Canvas_coord_yz.create_text(22, b-6, text=str(a)+"cm", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==7:
                    # 1 dm (dm) = 10 m
                    a=int(round(min_y/dm))
                    stop=0
                    d=0
                    c=abs(((a+1)*dm)/Mpp-(a*dm/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*dm>min_y:
                                if a*dm<max_y:
                                    if Mpp!=0:
                                        y=(a*dm-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                            Canvas_coord_yz.create_text(22, b-6, text=str(a)+"dm", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==6:
                    # 1 m (m) = 1 m
                    a=int(round(min_y/m))
                    stop=0
                    d=0
                    c=abs(((a+1)*m)/Mpp-(a*m/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*m>min_y:
                                if a*m<max_y:
                                    if Mpp!=0:
                                        y=(a*m-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_yz.create_line(19,b,9,4,fill='white')
                                            Canvas_coord_yz.create_text(22, b-6, text=str(a)+"m", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==5:
                    # 1 dam (dam) = 10 m
                    a=int(round(min_y/dm))
                    stop=0
                    d=0
                    c=abs(((a+1)*dam)/Mpp-(a*dam/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*dam>min_y:
                                if a*dam<max_y:
                                    if Mpp!=0:
                                        y=(a*dam-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                            Canvas_coord_yz.create_text(22, b-6, text=str(a)+"dam", fill="white",font=("Helvectica", "6"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==4:
                    # 1 hm (hm) = 100 m
                    a=int(round(min_y/hm))
                    stop=0
                    d=0
                    c=abs(((a+1)*hm)/Mpp-(a*hm/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*hm>min_y:
                                if a*hm<max_y:
                                    if Mpp!=0:
                                        y=(a*hm-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                            Canvas_coord_yz.create_text(22, b-6, text=str(a)+"hm", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==3:
                    # 1 km (km) = 1000 m
                    a=int(round(min_y/km))
                    stop=0
                    d=0
                    c=abs(((a+1)*km)/Mpp-(a*km/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*km>min_y:
                                if a*km<max_y:
                                    if Mpp!=0:
                                        y=(a*km-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                            Canvas_coord_yz.create_text(22, b-6, text=str(a)+"km", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==2:
                    # 1 ae (ae) = 149597870691 m
                    a=int(round(min_y/ae))
                    stop=0
                    d=0
                    c=abs(((a+1)*ae)/Mpp-(a*ae/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*ae>min_y:
                                if a*ae<max_y:
                                    if Mpp!=0:
                                        y=(a*ae-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                            Canvas_coord_yz.create_text(22, b-6, text=str(a)+"AE", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==1:
                    # 1 Lj (Lj) = 9460528000000000 m
                    a=int(round(min_y/Lj))
                    stop=0
                    d=0
                    c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*Lj>min_y:
                                if a*Lj<max_y:
                                    if Mpp!=0:
                                        y=(a*Lj-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                            Canvas_coord_yz.create_text(22, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==0:
                    # 1 pc (Lj) = 30856776000000000 m
                    a=int(round(min_y/pc))
                    stop=0
                    d=0
                    c=abs(((a+1)*pc)/Mpp-(a*pc/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*pc>min_y:
                                if a*pc<max_y:
                                    if Mpp!=0:
                                        y=(a*pc-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                            Canvas_coord_yz.create_text(22, b-6, text=str(a)+"pc", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==-1:
                    # Format unbekannt:
                    if e==0:
                        f=1
                        g=0
                        stop=0
                        d=0
                        while g==0:
                            h=(int(round(min_y/10**f)+1)*10**f)/Mpp-(int(round(min_y/10**f))*10**f)/Mpp
                            if h>20 and h<height_y_2:
                                a=int(round(min_y/10**f))
                                c=abs(((a+1)*10**f)/Mpp-(a*10**f/Mpp))
                                g=1
                            else:
                                f=f+1
                        while stop==0:
                            if a*10**f>min_y:
                                if a*10**f<max_y:
                                    if Mpp!=0:
                                        y=(a*10**f-Mitte_y)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_yz.create_line(19,b,4,b,fill='white')
                                            Canvas_coord_yz.create_text(22, b-6, text=str(a)+"mE"+str(f), fill="white",font=("Helvectica", "6"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_yz.create_line(9,b+i*c/5,4,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_yz.create_line(9,b-i*c/5,4,b-i*c/5,fill='white')
                            else:
                                a=a+1
                # xz - z (height_y_2) - Achsen max und min:
                min_y=Mitte_z-height_y_2*Mpp/2                                # Oberes Ende!
                max_y=Mitte_z+height_y_2*Mpp/2                                # Unteres Ende!
                # Die Skala soll ermitelt werden:
                # Wir teilen min durch die Längen der einheiten und runden diese zu einer int, dann zeichnen wir alle relevanten einund setzen Einheitenanzahl eins höher
                e=0                     # Anzeige aus=0, an=1
                Aktueller_Schritt=8     #0=Parsec, 1=Lj, 2=AE.....
                if Aktueller_Schritt==8:
                    # 1 cm (cm) = 1 m
                    a=int(round(min_y/cm))
                    stop=0
                    d=0
                    c=abs(((a+1)*cm)/Mpp-(a*cm/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*cm>min_y:
                                if a*cm<max_y:
                                    if Mpp!=0:
                                        y=(a*cm-Mitte_z)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xz.create_text(17, b-6, text=str(a)+"cm", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==7:
                    # 1 dm (dm) = 10 m
                    a=int(round(min_y/dm))
                    stop=0
                    d=0
                    c=abs(((a+1)*dm)/Mpp-(a*dm/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*dm>min_y:
                                if a*dm<max_y:
                                    if Mpp!=0:
                                        y=(a*dm-Mitte_z)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xz.create_text(17, b-6, text=str(a)+"dm", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==6:
                    # 1 m (m) = 1 m
                    a=int(round(min_y/m))
                    stop=0
                    d=0
                    c=abs(((a+1)*m)/Mpp-(a*m/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*m>min_y:
                                if a*m<max_y:
                                    if Mpp!=0:
                                        y=(a*m-Mitte_z)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xy.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xy.create_text(17, b-6, text=str(a)+"m", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==5:
                    # 1 dam (dam) = 10 m
                    a=int(round(min_y/dm))
                    stop=0
                    d=0
                    c=abs(((a+1)*dam)/Mpp-(a*dam/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*dam>min_y:
                                if a*dam<max_y:
                                    if Mpp!=0:
                                        y=(a*dam-Mitte_z)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xz.create_text(17, b-6, text=str(a)+"dam", fill="white",font=("Helvectica", "6"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==4:
                    # 1 hm (hm) = 100 m
                    a=int(round(min_y/hm))
                    stop=0
                    d=0
                    c=abs(((a+1)*hm)/Mpp-(a*hm/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*hm>min_y:
                                if a*hm<max_y:
                                    if Mpp!=0:
                                        y=(a*hm-Mitte_z)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xz.create_text(17, b-6, text=str(a)+"hm", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==3:
                    # 1 km (km) = 1000 m
                    a=int(round(min_y/km))
                    stop=0
                    d=0
                    c=abs(((a+1)*km)/Mpp-(a*km/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*km>min_y:
                                if a*km<max_y:
                                    if Mpp!=0:
                                        y=(a*km-Mitte_z)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xz.create_text(17, b-6, text=str(a)+"km", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==2:
                    # 1 ae (ae) = 149597870691 m
                    a=int(round(min_y/ae))
                    stop=0
                    d=0
                    c=abs(((a+1)*ae)/Mpp-(a*ae/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*ae>min_y:
                                if a*ae<max_y:
                                    if Mpp!=0:
                                        y=(a*ae-Mitte_z)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xz.create_text(17, b-6, text=str(a)+"AE", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==1:
                    # 1 Lj (Lj) = 9460528000000000 m
                    a=int(round(min_y/Lj))
                    stop=0
                    d=0
                    c=abs(((a+1)*Lj)/Mpp-(a*Lj/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*Lj>min_y:
                                if a*Lj<max_y:
                                    if Mpp!=0:
                                        y=(a*Lj-Mitte_z)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xz.create_text(17, b-6, text=str(a)+"Lj", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==0:
                    # 1 pc (Lj) = 30856776000000000 m
                    a=int(round(min_y/pc))
                    stop=0
                    d=0
                    c=abs(((a+1)*pc)/Mpp-(a*pc/Mpp))
                    if c>20 and c<height_y_2:
                        while stop==0:
                            if a*pc>min_y:
                                if a*pc<max_y:
                                    if Mpp!=0:
                                        y=(a*pc-Mitte_z)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xz.create_text(17, b-6, text=str(a)+"pc", fill="white",font=("Helvectica", "8"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                    else:
                        Aktueller_Schritt=Aktueller_Schritt-1
                if Aktueller_Schritt==-1:
                    # Format unbekannt:
                    if e==0:
                        f=1
                        g=0
                        stop=0
                        d=0
                        while g==0:
                            h=(int(round(min_y/10**f)+1)*10**f)/Mpp-(int(round(min_y/10**f))*10**f)/Mpp
                            if h>20 and h<height_y_2:
                                a=int(round(min_y/10**f))
                                c=abs(((a+1)*10**f)/Mpp-(a*10**f/Mpp))
                                g=1
                            else:
                                f=f+1
                        while stop==0:
                            if a*10**f>min_y:
                                if a*10**f<max_y:
                                    if Mpp!=0:
                                        y=(a*10**f-Mitte_z)/Mpp
                                        b=height_y_2/2-y
                                        if b>=0 and b<=height_y_2:
                                            Canvas_coord_xz.create_line(21,b,36,b,fill='white')
                                            Canvas_coord_xz.create_text(17, b-6, text=str(a)+"mE"+str(f), fill="white",font=("Helvectica", "6"))
                                            d=1
                                            e=1
                                            for i in range(0,5):
                                                Canvas_coord_xz.create_line(31,b+i*c/5,36,b+i*c/5,fill='white')
                                    a=a+1
                                else:
                                    stop=1
                                    if d==1:
                                        for i in range(0,5):
                                            Canvas_coord_xz.create_line(31,b-i*c/5,36,b-i*c/5,fill='white')
                            else:
                                a=a+1
                # Nun werden alle Werte eingezeichnet die auf die Anforderungen zutreffen:

        def Normalisieren():
            max_min()
            Masstab_berechnen()
            Einzeichnen()

        Normalisieren_Button=Button(label_1_frame_3,text='Normalisieren',command=Normalisieren,width=20, bd=2).place(x=700,y=350)

        def Up(event):
            # xy:
            if event.x>57 and event.x<501:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y-5*self.Bd_Mpp
            # yz:
            if event.x>509 and event.x<957:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y-5*self.Bd_Mpp
            # xz:
            if event.x>57 and event.x<501:
                if event.y>339 and event.y<633:
                    self.Bd_Mittelpunkt_z=self.Bd_Mittelpunkt_z-5*self.Bd_Mpp
            Einzeichnen()

        root.bind("<Control-Up>",Up)

        def Down(event):
            # xy:
            if event.x>57 and event.x<501:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y+5*self.Bd_Mpp
            # yz:
            if event.x>509 and event.x<957:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y+5*self.Bd_Mpp
            # xz:
            if event.x>57 and event.x<501:
                if event.y>339 and event.y<633:
                    self.Bd_Mittelpunkt_z=self.Bd_Mittelpunkt_z+5*self.Bd_Mpp
            Einzeichnen()

        root.bind("<Control-Down>",Down)

        def Left(event):
            # xy:
            if event.x>57 and event.x<501:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_x=self.Bd_Mittelpunkt_x+5*self.Bd_Mpp
            # yz:
            if event.x>509 and event.x<957:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_z=self.Bd_Mittelpunkt_z-5*self.Bd_Mpp
            # xz:
            if event.x>57 and event.x<501:
                if event.y>339 and event.y<633:
                    self.Bd_Mittelpunkt_x=self.Bd_Mittelpunkt_x+5*self.Bd_Mpp
            Einzeichnen()

        root.bind("<Control-Left>",Left)

        def Right(event):
            # xy:
            if event.x>57 and event.x<501:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_x=self.Bd_Mittelpunkt_x-5*self.Bd_Mpp
            # yz:
            if event.x>509 and event.x<957:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_z=self.Bd_Mittelpunkt_z+5*self.Bd_Mpp
            # xz:
            if event.x>57 and event.x<501:
                if event.y>339 and event.y<633:
                    self.Bd_Mittelpunkt_x=self.Bd_Mittelpunkt_x-5*self.Bd_Mpp
            Einzeichnen()

        root.bind("<Control-Right>",Right)


        def Up(event):
            # xy:
            if event.x>57 and event.x<501:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y-50*self.Bd_Mpp
            # yz:
            if event.x>509 and event.x<957:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y-50*self.Bd_Mpp
            # xz:
            if event.x>57 and event.x<501:
                if event.y>339 and event.y<633:
                    self.Bd_Mittelpunkt_z=self.Bd_Mittelpunkt_z-50*self.Bd_Mpp
            Einzeichnen()

        root.bind("<Up>",Up)

        def Down(event):
            # xy:
            if event.x>57 and event.x<501:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y+50*self.Bd_Mpp
            # yz:
            if event.x>509 and event.x<957:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y+50*self.Bd_Mpp
            # xz:
            if event.x>57 and event.x<501:
                if event.y>339 and event.y<633:
                    self.Bd_Mittelpunkt_z=self.Bd_Mittelpunkt_z+50*self.Bd_Mpp
            Einzeichnen()

        root.bind("<Down>",Down)

        def Left(event):
            # xy:
            if event.x>57 and event.x<501:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_x=self.Bd_Mittelpunkt_x+50*self.Bd_Mpp
            # yz:
            if event.x>509 and event.x<957:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_z=self.Bd_Mittelpunkt_z-50*self.Bd_Mpp
            # xz:
            if event.x>57 and event.x<501:
                if event.y>339 and event.y<633:
                    self.Bd_Mittelpunkt_x=self.Bd_Mittelpunkt_x+50*self.Bd_Mpp
            Einzeichnen()

        root.bind("<Left>",Left)

        def Right(event):
            # xy:
            if event.x>57 and event.x<501:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_x=self.Bd_Mittelpunkt_x-50*self.Bd_Mpp
            # yz:
            if event.x>509 and event.x<957:
                if event.y>36 and event.y<331:
                    self.Bd_Mittelpunkt_z=self.Bd_Mittelpunkt_z+50*self.Bd_Mpp
            # xz:
            if event.x>57 and event.x<501:
                if event.y>339 and event.y<633:
                    self.Bd_Mittelpunkt_x=self.Bd_Mittelpunkt_x-50*self.Bd_Mpp
            Einzeichnen()

        root.bind("<Right>",Right)

        def Zoom_2(event):
            Canvas_xy.focus_set()
            # xy:
            if event.x>57 and event.x<501:
                if event.y>36 and event.y<331:
                    x_zoom_xy=event.x-57
                    y_zoom_xy=event.y-36
                    if event.delta < 0:
                        self.Bd_Mpp=self.Bd_Mpp*(0.8)
                        self.Bd_Mittelpunkt_x=self.Bd_Mittelpunkt_x+0.2*((self.Bd_Mittelpunkt_x/self.Bd_Mpp+x_zoom_xy-width_x_2/2)*self.Bd_Mpp-self.Bd_Mittelpunkt_x)
                        self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y+0.2*((self.Bd_Mittelpunkt_y/self.Bd_Mpp+height_y_2/2-y_zoom_xy)*self.Bd_Mpp-self.Bd_Mittelpunkt_y)
                    else:
                        self.Bd_Mpp=self.Bd_Mpp*(1.2)
                        self.Bd_Mittelpunkt_x=self.Bd_Mittelpunkt_x+0.2*((self.Bd_Mittelpunkt_x/self.Bd_Mpp+x_zoom_xy-width_x_2/2)*self.Bd_Mpp-self.Bd_Mittelpunkt_x)
                        self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y+0.2*((self.Bd_Mittelpunkt_y/self.Bd_Mpp+height_y_2/2-y_zoom_xy)*self.Bd_Mpp-self.Bd_Mittelpunkt_y)
            # yz:
            if event.x>509 and event.x<957:
                if event.y>36 and event.y<331:
                    x_zoom_xy=event.x-509
                    y_zoom_xy=event.y-36
                    if event.delta < 0:
                        self.Bd_Mpp=self.Bd_Mpp*(0.8)
                        self.Bd_Mittelpunkt_z=self.Bd_Mittelpunkt_z-0.2*((self.Bd_Mittelpunkt_z/self.Bd_Mpp+x_zoom_xy-width_x_2/2)*self.Bd_Mpp-self.Bd_Mittelpunkt_z)
                        self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y+0.2*((self.Bd_Mittelpunkt_y/self.Bd_Mpp+height_y_2/2-y_zoom_xy)*self.Bd_Mpp-self.Bd_Mittelpunkt_y)
                    else:
                        self.Bd_Mpp=self.Bd_Mpp*(1.2)
                        self.Bd_Mittelpunkt_z=self.Bd_Mittelpunkt_z-0.2*((self.Bd_Mittelpunkt_z/self.Bd_Mpp+x_zoom_xy-width_x_2/2)*self.Bd_Mpp-self.Bd_Mittelpunkt_z)
                        self.Bd_Mittelpunkt_y=self.Bd_Mittelpunkt_y+0.2*((self.Bd_Mittelpunkt_y/self.Bd_Mpp+height_y_2/2-y_zoom_xy)*self.Bd_Mpp-self.Bd_Mittelpunkt_y)
            # xz:
            if event.x>57 and event.x<501:
                if event.y>339 and event.y<633:
                    x_zoom_xy=event.x-57
                    y_zoom_xy=event.y-339
                    if event.delta < 0:
                        self.Bd_Mpp=self.Bd_Mpp*(0.8)
                        #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                        #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                    else:
                        self.Bd_Mpp=self.Bd_Mpp*(1.2)
                        #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                        #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
            Einzeichnen()

        root.bind("<Control-MouseWheel>",Zoom_2)

        def Zoom(event):
            Canvas_xy.focus_set()
            # xy:
            if event.x>57 and event.x<501:
                if event.y>36 and event.y<331:
                    x_zoom_xy=event.x-57
                    y_zoom_xy=event.y-36
                    if event.delta < 0:
                        self.Bd_Mpp=self.Bd_Mpp*(0.8)
                        #self.Bd_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                        #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                    else:
                        self.Bd_Mpp=self.Bd_Mpp*(1.2)
                        #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                        #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
            # yz:
            if event.x>509 and event.x<957:
                if event.y>36 and event.y<331:
                    x_zoom_xy=event.x-509
                    y_zoom_xy=event.y-36
                    if event.delta < 0:
                        self.Bd_Mpp=self.Bd_Mpp*(0.8)
                        #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                        #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
                    else:
                        self.Bd_Mpp=self.Bd_Mpp*(1.2)
                        #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z-0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                        #self.Oe_Mittelpunkt_y=self.Oe_Mittelpunkt_y+0.2*((self.Oe_Mittelpunkt_y/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_y)
            # xz:
            if event.x>57 and event.x<501:
                if event.y>339 and event.y<633:
                    x_zoom_xy=event.x-57
                    y_zoom_xy=event.y-339
                    if event.delta < 0:
                        self.Bd_Mpp=self.Bd_Mpp*(0.8)
                        #self.Bd_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                        #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
                    else:
                        self.Bd_Mpp=self.Bd_Mpp*(1.2)
                        #self.Oe_Mittelpunkt_x=self.Oe_Mittelpunkt_x+0.2*((self.Oe_Mittelpunkt_x/self.Oe_Mpp+x_zoom_xy-width_x_2/2)*self.Oe_Mpp-self.Oe_Mittelpunkt_x)
                        #self.Oe_Mittelpunkt_z=self.Oe_Mittelpunkt_z+0.2*((self.Oe_Mittelpunkt_z/self.Oe_Mpp+height_y_2/2-y_zoom_xy)*self.Oe_Mpp-self.Oe_Mittelpunkt_z)
            Einzeichnen()

        root.bind("<MouseWheel>",Zoom)

        def Mouse_Movement_xy(event):
            if Canvas_xy.canvasx(event.x)>10 and Canvas_xy.canvasy(event.y)>10:
                self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten1.gif')
                Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
            elif Canvas_xy.canvasx(event.x)<10 or Canvas_xy.canvasy(event.y)<10:
                self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
                Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
            # Koordinatenanzeige:
            if self.Bd_Mpp!=0:
                self.Bd_X.set(String_Number.Number_to_String(round(((self.Bd_Mittelpunkt_x/self.Bd_Mpp+event.x-width_x_2/2)*self.Bd_Mpp),1)))
                self.Bd_Y.set(String_Number.Number_to_String(round(((self.Bd_Mittelpunkt_y/self.Bd_Mpp+height_y_2/2-event.y)*self.Bd_Mpp),1)))
            self.Bd_Z.set('0.0')

        def Mouse_Movement_yz(event):
            if Canvas_yz.canvasx(event.x)>0 and Canvas_yz.canvasy(event.y)>10 and not Canvas_yz.canvasx(event.x)>440 and not Canvas_yz.canvasy(event.y)>285:
                self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten2.gif')
                Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
            elif Canvas_yz.canvasy(event.y)<10 or Canvas_yz.canvasx(event.x)>440 or Canvas_yz.canvasy(event.y)>285:
                self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
                Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
            # Koordinatenanzeige:
            if self.Bd_Mpp!=0:
                self.Bd_Z.set(String_Number.Number_to_String(round(((self.Bd_Mittelpunkt_z/self.Bd_Mpp-event.x+width_x_2/2)*self.Bd_Mpp),1)))
                self.Bd_Y.set(String_Number.Number_to_String(round(((self.Bd_Mittelpunkt_y/self.Bd_Mpp+height_y_2/2-event.y)*self.Bd_Mpp),1)))
            self.Bd_X.set('0.0')

        def Mouse_Movement_xz(event):
            if not Canvas_xz.canvasx(event.x)<10 and Canvas_xz.canvasy(event.y)>0 and not Canvas_xz.canvasx(event.x)>440 and not Canvas_xz.canvasy(event.y)>285:
                self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten3.gif')
                Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
            elif Canvas_xz.canvasx(event.x)<10 or Canvas_xz.canvasy(event.y)<10 or Canvas_xz.canvasx(event.x)>440 or Canvas_xz.canvasy(event.y)>285:
                self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
                Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)
            # Koordinatenanzeige:
            if self.Bd_Mpp!=0:
                self.Bd_X.set(String_Number.Number_to_String(round(((self.Bd_Mittelpunkt_x/self.Bd_Mpp+event.x-width_x_2/2)*self.Bd_Mpp),1)))
                self.Bd_Z.set(String_Number.Number_to_String(round(((self.Bd_Mittelpunkt_z/self.Bd_Mpp+height_y_2/2-event.y)*self.Bd_Mpp),1)))
            self.Bd_Y.set('0.0')

        Canvas_xy = Canvas (label_1_frame_3, width=width_x_2, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
        Canvas_xy.place (x=42,y=5)
        Canvas_xy.bind('<Motion>',Mouse_Movement_xy)
        self.xy_koord = PhotoImage(file = '../Icon/Koordinaten/xy.gif')
        #Canvas_xy.create_image(12,height_y_2-39, image = self.xy_koord, anchor = NW)

        Canvas_yz = Canvas (label_1_frame_3, width=width_x_2, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
        Canvas_yz.place (x=49+width_x_2,y=5)
        Canvas_yz.bind('<Motion>',Mouse_Movement_yz)
        self.yz_koord = PhotoImage(file = '../Icon/Koordinaten/yz.gif')
        #Canvas_yz.create_image(width_x_2-39, height_y_2-39, image = self.yz_koord, anchor = NW)

        Canvas_xz = Canvas (label_1_frame_3, width=width_x_2, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
        Canvas_xz.place (x=42,y=12+height_y_2)
        Canvas_xz.bind('<Motion>',Mouse_Movement_xz)
        self.xz_koord = PhotoImage(file = '../Icon/Koordinaten/xz.gif')
        #Canvas_xz.create_image(12, height_y_2-39, image = self.xz_koord, anchor = NW)

        Koordinaten = Canvas(label_1_frame_3, width = 154, height = 107)
        Koordinaten.place(x=49+width_x_2,y=13+height_y_2)
        self.Koordinaten_2 = PhotoImage(file = '../Icon/Koordinaten/koordinaten.gif')
        Koordinaten.create_image(0, 0, image = self.Koordinaten_2, anchor = NW)

        Canvas_coord_yz = Canvas (label_1_frame_3, width=33, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
        Canvas_coord_yz.place (x=53+2*width_x_2,y=5)

        Canvas_coord_xz = Canvas (label_1_frame_3, width=33, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
        Canvas_coord_xz.place (x=8,y=12+height_y_2)

        Canvas_coord_xy = Canvas (label_1_frame_3, width=33, height=height_y_2, background='black', borderwidth=2, cursor='tcross')
        Canvas_coord_xy.place (x=8,y=5)

        Normalisieren()

        #   Spalten:

        notebook.add(frame_1, text="Einstellungen")
        notebook.add(frame_2, text="Körper")
        notebook.add(label_1_frame_3, text="Auswertung")

        #   Anzeigen des Notebooks:

        notebook.place(x=5,y=5)

#-----------------------INIT Ende-----------------------------------
#-------------------------------------------------------------------

        #   Kommandos des 1. Pulldown Menüs: (Datei)

    def neu(self):
        self.Newton_Simulator.new_file()
        self.Iterationsanzahl.set ("10,000")
        self.Gravitationskonstante.set ("6.67428E-11")
        self.Berechnungsart.set ("N")
        self.Lichtgeschwindigkeit.set ("299,792,458")
        self.Iterationsintervall.set ("1,800")
        self.Speicherintervall.set ("10")
        print ('new')
        self.pos            =           0
        self.minX                =           0
        self.maxX                =           0
        self.minY                =           0
        self.maxY                =           0
        self.minZ                =           0
        self.maxZ                =           0
        self.Oe_Mpp              =           0
        self.Oe_Mpp_xy           =           0
        self.Oe_Mpp_yz           =           0
        self.Oe_Mpp_xz           =           0
        self.Oe_Mittelpunkt_x    =           0
        self.Oe_Mittelpunkt_y    =           0
        self.Oe_Mittelpunkt_z    =           0
        self.Oe_akt_X            =           0
        self.Oe_akt_Y            =           0
        self.Oe_akt_Z            =           0
        self.Oe_akt_Pos          =           0
        self.Oe_akt_movX         =           0
        self.Oe_akt_movY         =           0
        self.Oe_akt_movZ         =           0
        self.Oe_akt_Tem          =           0
        self.Se_Mpp              =           0
        self.Se_Mpp_xy           =           0
        self.Se_Mpp_yz           =           0
        self.Se_Mpp_xz           =           0
        self.Se_Mittelpunkt_x    =           0
        self.Se_Mittelpunkt_y    =           0
        self.Se_Mittelpunkt_z    =           0
        self.Se_akt_X            =           0
        self.Se_akt_Y            =           0
        self.Se_akt_Z            =           0
        self.Se_akt_Pos          =           0
        self.Se_akt_movX         =           0
        self.Se_akt_movY         =           0
        self.Se_akt_movZ         =           0
        self.Se_akt_Tem          =           0
        self.Se_position         =           0
        for i in range(0,len(self.ID)):
            try:
                self.Tree.delete(self.ID[len(self.ID)-1-i])
            except:
                print('.')
        self.ID             =           []
        self.Name_13           =        []
        self.Tree.delete()
        self.filename.set("")

    def open(self):
        self.filename.set(askopenfilename(initialdir="../Sternsysteme", title="Öffnen", filetypes=[("All files","*"),("Text files","*.txt")]))			# Öffnet ein Fenster in welchem man die zu öffnende Datei auswählen kann und gibt den absoluten Pfad an.
        if not self.filename.get() == "":                                             # Falls das Auswählen einer Datei gelungen ist, der filename, "string", also nicht leer ist (...)
            a=self.Newton_Simulator.open_file(self.filename.get())
            if a==1:
                print("Daten erfolgreich eingelesen!")
                # Alte Dateien löschen:
                self.pos                 =           0
                self.minX                =           0
                self.maxX                =           0
                self.minY                =           0
                self.maxY                =           0
                self.minZ                =           0
                self.maxZ                =           0
                self.Oe_Mpp              =           0
                self.Oe_Mpp_xy           =           0
                self.Oe_Mpp_yz           =           0
                self.Oe_Mpp_xz           =           0
                self.Oe_Mittelpunkt_x    =           0
                self.Oe_Mittelpunkt_y    =           0
                self.Oe_Mittelpunkt_z    =           0
                self.Oe_akt_X            =           0
                self.Oe_akt_Y            =           0
                self.Oe_akt_Z            =           0
                self.Oe_akt_Pos          =           0
                self.Oe_akt_movX         =           0
                self.Oe_akt_movY         =           0
                self.Oe_akt_movZ         =           0
                self.Oe_akt_Tem          =           0
                self.Se_Mpp              =           0
                self.Se_Mpp_xy           =           0
                self.Se_Mpp_yz           =           0
                self.Se_Mpp_xz           =           0
                self.Se_Mittelpunkt_x    =           0
                self.Se_Mittelpunkt_y    =           0
                self.Se_Mittelpunkt_z    =           0
                self.Se_akt_X            =           0
                self.Se_akt_Y            =           0
                self.Se_akt_Z            =           0
                self.Se_akt_Pos          =           0
                self.Se_akt_movX         =           0
                self.Se_akt_movY         =           0
                self.Se_akt_movZ         =           0
                self.Se_akt_Tem          =           0
                self.Se_position         =           0
                for i in range(0,len(self.ID)):
                    try:
                        self.Tree.delete(self.ID[len(self.ID)-1-i])
                    except:
                        print('.')
                self.ID             =           []
                self.Name_13           =        []
                self.Tree.delete()
                self.filename.set("")
                # Variabeln einlesen aus Fachklasse:
                self.Gravitationskonstante.set(str(self.Newton_Simulator.Gravitationskonstante))
                self.Berechnungsart.set(str(self.Newton_Simulator.Berechnungsart))                                         # self.Berechnungsart = J -> Relativistische Berechnung, self.Berechnungsart = N -> Rein Newtonsche Berechnung
                self.Lichtgeschwindigkeit.set(str(self.Newton_Simulator.Lichtgeschwindigkeit))
                self.Iterationsanzahl.set(str(self.Newton_Simulator.Iterationsanzahl))
                self.Iterationsintervall.set(str(self.Newton_Simulator.Iterationsintervall))                                      # in Sekunden
                self.Speicherintervall.set(str(self.Newton_Simulator.Speicherintervall))
                for i in range(0,len(self.Newton_Simulator.Name_Body)):
                    namen=self.Newton_Simulator.Name_Body[i]
                    typen=self.Newton_Simulator.Typ_Body[i]
                    zugehoerigkeit=self.Newton_Simulator.Zugehoerigkeit_Body[i]
                    radien=String_Number.Number_to_String(self.Newton_Simulator.Radius_Body[i][0])
                    massen=String_Number.Number_to_String(self.Newton_Simulator.Masse_Body[i][0])
                    vxen=String_Number.Number_to_String(self.Newton_Simulator.VX[i][0])
                    vyen=String_Number.Number_to_String(self.Newton_Simulator.VY[i][0])
                    vzen=String_Number.Number_to_String(self.Newton_Simulator.VZ[i][0])
                    xen=String_Number.Number_to_String(self.Newton_Simulator.X[i][0])
                    yen=String_Number.Number_to_String(self.Newton_Simulator.Y[i][0])
                    zen=String_Number.Number_to_String(self.Newton_Simulator.Z[i][0])

                    # In die Liste einfügen:

                    Name_2=str(namen)
                    Typ_2=str(typen)
                    Masse_2=String_Number.String_to_Number(str(massen))
                    Radius_2=String_Number.String_to_Number(str(radien))
                    X_Geschwindigkeit_2=str(vxen)
                    Y_Geschwindigkeit_2=str(vyen)
                    Z_Geschwindigkeit_2=str(vzen)
                    X_Position_2=str(xen)
                    Y_Position_2=str(yen)
                    Z_Position_2=str(zen)
                    # Elemente in die Gui-Listen Hinzufügen:
                    self.pos=self.pos+1
                    # Suche nach der ID für die Zugehörigkeit:
                    asdf=0
                    bdgf=''
                    if zugehoerigkeit!="":
                        for l in range(0,len(self.ID)):
                            if self.Newton_Simulator.Name_Body[l]==zugehoerigkeit:
                                asdf=l
                                bdgf=str(self.ID[asdf])
                    # Elemente in die Liste Hinzufügen (bei simplen Hinzufügen heist das nichts anderes, als es hinten ran zu hängen:
                    ab=self.Tree.insert(bdgf, self.pos, text=Name_2, values=(Typ_2, Verifizieren.Verifizieren_mit_Null(Masse_2), Verifizieren.Verifizieren_mit_Null(Radius_2), Verifizieren.Verifizieren_mit_Null(X_Geschwindigkeit_2), Verifizieren.Verifizieren_mit_Null(Y_Geschwindigkeit_2), Verifizieren.Verifizieren_mit_Null(Z_Geschwindigkeit_2), Verifizieren.Verifizieren_mit_Null(X_Position_2), Verifizieren.Verifizieren_mit_Null(Y_Position_2), Verifizieren.Verifizieren_mit_Null(Z_Position_2)))
                    self.ID.append(ab)
                    self.Name_13.append(Name_2)
                    self.Berechnungsart.set ("N")
            elif a==0:
                print('Datei konnte nicht eingelesen werden!')
        else:
            print('Es wurde keine Datei zum öffnen gewählt!')

    def save(self):
        # Daten aktualisieren!
        Gravitationskonstante_2=0.0+String_Number.String_to_Number(self.Gravitationskonstante.get())
        Berechnungsart=self.Berechnungsart.get()
        Lichtgeschwindigkeit_2=0.0+String_Number.String_to_Number(self.Lichtgeschwindigkeit.get())
        Iterationsanzahl_2=0.0+String_Number.String_to_Number(self.Iterationsanzahl.get())
        Iterationsintervall_2=0.0+String_Number.String_to_Number(self.Iterationsintervall.get())
        Speicherintervall_2=0.0+String_Number.String_to_Number(self.Speicherintervall.get())
        self.Newton_Simulator.hole_GBLIIS(Gravitationskonstante_2,Berechnungsart,Lichtgeschwindigkeit_2,Iterationsanzahl_2,Iterationsintervall_2,Speicherintervall_2,0)

        if self.filename.get()!="":
            a=self.Newton_Simulator.save_file(self.filename.get())
            if a==1:
                print('Datei gespeichert!')
            elif a==0:
                print('Datei konnte nicht gespeichert werden!')
        else:
            print('Es wurde keine Datei zum öffnen gewählt!')

    def save_as(self):
        # Daten aktualisieren!
        Gravitationskonstante_2=0.0+String_Number.String_to_Number(self.Gravitationskonstante.get())
        Berechnungsart=self.Berechnungsart.get()
        Lichtgeschwindigkeit_2=0.0+String_Number.String_to_Number(self.Lichtgeschwindigkeit.get())
        Iterationsanzahl_2=0.0+String_Number.String_to_Number(self.Iterationsanzahl.get())
        Iterationsintervall_2=0.0+String_Number.String_to_Number(self.Iterationsintervall.get())
        Speicherintervall_2=0.0+String_Number.String_to_Number(self.Speicherintervall.get())
        self.Newton_Simulator.hole_GBLIIS(Gravitationskonstante_2,Berechnungsart,Lichtgeschwindigkeit_2,Iterationsanzahl_2,Iterationsintervall_2,Speicherintervall_2,0)

        self.filename.set(asksaveasfilename(initialdir="../Sternsysteme", title="Speichern", filetypes=[("All files","*"),("Text files","*.txt")]))
        if not self.filename.get() == "":
            a=self.Newton_Simulator.save_file(self.filename.get())
            if a==1:
                print('Datei gespeichert!')
            elif a==0:
                print('Datei konnte nicht gespeichert werden!')
        else:
            print('Es wurde keine Datei zum öffnen gewählt!')

        #   Kommandos des 2. Pulldown Menüs: (Über)

    #def documentation(self):           # Zur Zeit erstmal irrelevant, gibt so viel interessantere Dinge für das Programm
        #print ('documentation')

    def about(self):
        #   Fenstername, Größe und Icon: (rbot_2)

        bbout = Toplevel(root, width=590, height=350)
        bbout.title ("Newton Simulator   v."+version)
        bbout.resizable(width = False, height = False)
        bbout.wm_iconbitmap('../Icon/Window Icon/Window Icon.ico')
        about = Frame(bbout, width=590, height=400)
        about.place(x=0,y=0)
        Titel = Canvas(about, width = 588, height = 198)
        Titel.place (x=0,y=0)
        self.Titel_2 = PhotoImage(file = '../Icon/Newton Simulator/titel.gif')
        Titel.create_image(0, 0, image = self.Titel_2, anchor = NW)
        Zuletzt = Label(about, text='Zuletzt geändert:                          '+Zuletzt_Geendert)
        Zuletzt.place(x=50, y=210)
        Versio = Label(about, text= 'Version:                                         '+version)
        Versio.place(x=50, y=240)
        Mitwirkende = Label(about, text='Mitwirkende:                                Michael Schilling')
        Mitwirkende.place(x=50,y=270)
        Dank = Label(about, text='Dank gilt insbesondere:              Galileo Galilei, Johannes Kepler, Isaac Newton, Albert Einstein')
        Dank.place(x=50,y=310)


    def Start(self,Gravitationskonstante,Berechnungsart,Lichtgeschwindigkeit,Iterationsanzahl,Iterationsintervall,Speicherintervall):
        Gravitationskonstante_2=0.0+String_Number.String_to_Number(Gravitationskonstante)
        Lichtgeschwindigkeit_2=0.0+String_Number.String_to_Number(Lichtgeschwindigkeit)
        Iterationsanzahl_2=0.0+String_Number.String_to_Number(Iterationsanzahl)
        Iterationsintervall_2=0.0+String_Number.String_to_Number(Iterationsintervall)
        Speicherintervall_2=0.0+String_Number.String_to_Number(Speicherintervall)
        self.Newton_Simulator.hole_GBLIIS(Gravitationskonstante_2,Berechnungsart,Lichtgeschwindigkeit_2,Iterationsanzahl_2,Iterationsintervall_2,Speicherintervall_2,1)
        self.Newton_Simulator.Berechnung()
        self.Newton_Simulator.Maximalwertsuche()
        self.minX=self.Newton_Simulator.MinX
        self.minY=self.Newton_Simulator.MinY
        self.minZ=self.Newton_Simulator.MinZ
        self.maxX=self.Newton_Simulator.MaxX
        self.maxY=self.Newton_Simulator.MaxY
        self.maxZ=self.Newton_Simulator.MaxZ


#-------------------------------------------------------------------

root = Tk()

main = Main(root)

root.mainloop()
