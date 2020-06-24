function [ C b ] = nrmatrix_3d( A , D , Phi , T , size )
%nrmatrix erzeugt eine Matrix C für die Lösung eines linearen
%Gleichungssystems
%   Phi_{i,j,k}=1/4*(Phi_{i,j+1,k}+Phi_{i,j-1,k}+Phi_{i+1,j,k}+Phi_{i-1,j,k}+Phi_{i,j,k+1}+Phi_{i,j,k-1})
%   C*x=b;
%Matrix C, Vektor b ist duenn besiedelt daher zunaechst
leng=length(T); 
C=zeros(leng);     %Variiere nur die Nachbarkomponenten und setze Randkomponenten in 
b=zeros(leng,1);
for k=1:leng
    %Ermittle i,j mit Hilfe von T
    i=T(k,1); j=T(k,2); h=T(k,3);
    %Suche benachbarte Punkte
    % i-1,j ; i+1,j ; i,j-1 ; i,j+1 ;
    %Ueberpruefe zuerst auf nicht Randpunkte
    count=0;
    for l=1:leng
        if (abs(T(l,1)-i)==1 & abs(T(l,2)-j)==0 & abs(T(l,3)-j)==0)
            C(k,l)=-1;
            count=count+1;
        elseif (abs(T(l,1)-i)==0 & abs(T(l,2)-j)==1 & abs(T(l,3)-k)==0)
            C(k,l)=-1;
            count=count+1;
        elseif (abs(T(l,1)-i)==0 & abs(T(l,2)-j)==0 & abs(T(l,3)-k)==1)
            C(k,l)=-1;
            count=count+1;
        elseif l==k
            C(l,l)=6;
            count=count+1;
        end
    end
    if count<7
        %Ueberpruefe nun auf Randpunkte
        if A(i-1,j,h)==1
            b(k)=b(k)+Phi(i-1,j,h);
        end
        if A(i+1,j,h)==1
            b(k)=b(k)+Phi(i+1,j,h);
        end
        if A(i,j-1,h)==1
            b(k)=b(k)+Phi(i,j-1,h);
        end
        if A(i,j+1,h)==1
            b(k)=b(k)+Phi(i,j+1,h);
        end
        if A(i,j,h+1)==1
            b(k)=b(k)+Phi(i,j,h-1);
        end
        if A(i,j,h-1)==1
            b(k)=b(k)+Phi(i,j,h-1);
        end
    end
    if D(i,j,h)~=0
            b(k)=b(k)-D(i,j,h);
    end
end
end