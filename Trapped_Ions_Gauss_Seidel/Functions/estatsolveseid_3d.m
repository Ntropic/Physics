function [ phi , n ] = estatsolveseid_3d(A , phi , size , w , abbruch , typer)
%estatsolveseid loest das elektrostatische System mit Hilfe des
%Gauss-Seidel Verfahrens mit sukzessiver Ueberrelaxation
%   Erzeuge Ausgangsvektor der inneren Punkte T
T=nrnum_3d(A,size);
%   Berechnung nach Gauss-Seidel
m=0;
if size>=32
    fprintf('Berechne kleineres System fuer Startparameter \n')
    size2=round(size/2);
    [ phi2 n ]=littlesolveseidel_3d( size2 , w , abbruch , typer );
    phi=kleinnachgross_3d(phi,A,phi2,size2,size);
    m=m+n;
end
%   Fuer grosse size wird ein kleineres System Berechnet und für die
%   Startphi eingesetzt
[phi,n]=nrphi_3d(phi,T,w,abbruch);
m=m+n;
end