function [ T ] = nrnum_3d( A, sizes )
%nrnum nummeriert die nicht Randelemente und ordnet Sie den i's und j's zu
%   T=[ i1 , j1 , k1;
%       i2 , j2 , k2;
%        .    .   . ;
%        .    .   . ;
%        .    .   . ;
%       in , jn , kn]

fprintf('Erzeuge Koordinatenmatrix: \n')

A_i=sum(A(:));
T=zeros(sizes^3-A_i,3);

j_m=zeros(sizes,sizes);
h_m=zeros(sizes,sizes);
for j=1:sizes
    for h=1:sizes
        j_m(j,h)=j;
        h_m(j,h)=h;
    end
end

k=0;
for i=1:sizes
    fprintf('\t %d/%d \r',i,sizes)
    A_i=sizes^2-sum(sum(A(i,:,:)));
    T(k+1:k+A_i,1)=i*ones(A_i,1);
    el_j=j_m(A(i,:,:)~=1);
    el_h=h_m(A(i,:,:)~=1);
    T(k+1:k+A_i,2)=el_j(:);
    T(k+1:k+A_i,3)=el_h(:);
    k=k+A_i;
    
    %for j=1:sizes
    %    for h=1:sizes
    %        if A(i,j,h)==0;
    %            k=k+1;
    %            T(k,:)=[i,j,h];
    %        end
    %    end
    %end
end
end