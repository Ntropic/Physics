function [ phi,n ] = littlesolveseidel_3d( size , w , abbruch , typer )
%Create smaller system setup
[phi,A]=phirand_3d(size,typer);
%Berechne die Loesungen von nicht Randpunkten
[phi,n]=estatsolveseid_3d(A,phi,size,w,abbruch,typer);
end