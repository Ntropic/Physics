# -*- coding: latin-1 -*-


#   Name:       Basic_Calculations.py
#   Author:     Michael Schilling
#   Edited:     27.03.2010 - 12.12.2011
#   Version:    1.0.0

from math import sqrt

class Basic_Calculations:

    def Abstand(X,Y,Z):
        #print(X)
        #print(Y)
        #print(Z)
        b=X**2+Y**2+Z**2
        Abstand=sqrt(b)
        return(Abstand)

    def Abstand_zu(X,Y,Z,x_2,y_2,z_2):
        b=(X-x_2)**2+(Y-y_2)**2+(Z-z_2)**2
        Abstand=sqrt(b)
        return(Abstand)

    def Geschwindigkeit_zu(VX,VY,VZ,vx,vy,vz):
        va=sqrt(VX**2+VY**2+VZ**2)
        vb=sqrt(vx**2+vy**2+vz**2)
        if vb!=0:
            c=va/vb
            return(str(c))
        else:
            return('Parent in Ruhe')

    def Dichte(Masse, Radius):
        #print(Masse)
        #print(Radius)
        b=Masse/(4/3*3.141*Radius**3)
        return(b)