function [ phi ] = kleinnachgross_3d( phi , A , phi2 , size2 , size )
%kleinnachgross setzt bessere Ausgangswerte für das Gauss-Seidel Verfahren
faktor=size2/size;
for i=1:size
    for j=1:size
        for k=1:size
            if A(i,j,k)==0
                phi(i,j,k)=phi2(ceil(i*faktor),ceil(j*faktor),ceil(k*faktor));
            end
        end
    end
end
end

