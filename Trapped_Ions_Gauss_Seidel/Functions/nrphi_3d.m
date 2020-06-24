function [ phi,n ] = nrphi_3d( phi , T , w , abbruch )
%nrphi berechnet phi nach dem Gauss Seidel Verfahren
n=0;
abruch=abbruch(1);
if abbruch(2)==1    %mittlere Aenderung
len=length(T);
abruch=abruch*len;
a=abruch+0.1;
fprintf('Loese elektrostatisches Problem (der Größe %d):\n',size(phi,1))
while a>abruch
    fprintf('\t Iteration # %d ',n)
    if n>=1
        fprintf(' - %2.3f <-> %2.3f \r',a,abruch)
    else
        fprintf('\r')
    end
    a=0;
    n=n+1;
    for k=1:len
        i=T(k,1); j=T(k,2); h=T(k,3);
        phi2=1/6*(phi(i+1,j,h)+phi(i-1,j,h)+phi(i,j-1,h)+phi(i,j+1,h)+phi(i,j,h-1)+phi(i,j,h+1));
        abw=w*(phi2-phi(i,j,h));
        a=a+abs(abw);
        phi(i,j,h)=phi(i,j,h)+abw;
    end
    %surf(phi)  %Somit laesst sich die Funktionsweise des Programms zeigen
    %pause;
end
elseif abbruch(2)==2    %maximale Aenderung
a=abruch+0.1;
len=length(T);
while a>abruch
    fprintf('\t Iteration # %d \r',n)
    if n>=1
        fprintf(' - %2.3f <-> %2.3f \r',a,abruch)
    else
        fprintf('\r')
    end
    a=0;
    n=n+1;
    for k=1:len
        i=T(k,1); j=T(k,2); h=T(k,3);
        phi2=1/6*(phi(i+1,j,h)+phi(i-1,j,h)+phi(i,j-1,h)+phi(i,j+1,h)+phi(i,j,h-1)+phi(i,j,h+1));
        abw=w*(phi2-phi(i,j));
        if abs(abw)>a
            a=a+abs(abw);
        end
        phi(i,j,h)=phi(i,j,h)+abw;
    end
    %surf(phi)  %Somit laesst sich die Funktionsweise des Programms zeigen
    %pause;
end
end