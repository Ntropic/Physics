# -*- coding: latin-1 -*-


#   Name:       Randomcolor.py
#   Author:     Michael Schilling
#   Edited:     27.03.2010 - 10.11.2010
#   Version:    1.0.0


from Newton_Simulator import *
from random import randint

class Randomcolor:

    def Randomcolor():

        # Erzeugt einen zufälligen Farbton (Als Hexstring)
        string  = "#"
        string_2=""
        a = 0
        for i in range(0,3):
            a = randint(0,255)
            string_2=str(hex(a)[2:])
            if len(string_2)==1:
                string = string+string_2+"0"
            elif len(string_2)==0:
                string = string+"00"
            else:
                string = string +string_2
        return(string)

#print(Randomcolor.Randomcolor())