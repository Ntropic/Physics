function [ phi A ] = phirand_3d( sizes, type )
% erzeugt eine Matrix phi und eine Matrix A für ein
%Gitterdiskretisiertes System der Größe size x size

% Erzeuge Matrizen der Größe size x size x size
phi=zeros(sizes,sizes,sizes); A=zeros(sizes,sizes,sizes); D=zeros(sizes,sizes,sizes);
%Ermittle Maßstabsvrhaeltnis
%Setze die aeusseren Randwerte entsprechend randfun
A(:,:,1)=1; A(:,1,:)=1; A(1,:,:)=1; A(:,sizes,:)=1; A(sizes,:,:)=1; A(:,:,sizes)=1;
i=1:sizes;
phi(:,:,1)=0; phi(:,1,:)=0; phi(1,:,:)=0; phi(:,sizes,sizes)=0; phi(sizes,:,sizes)=0; phi(sizes,sizes,:)=0;
%Ergänze nun die inneren Randwerte
fprintf('Erzeuge System \n')
if type=='paul_classic'
    %Erzeuge Paul Falle mit Torus mit Radien r_1 und r_2 und 2 Halbkugeln bei
    %r_3 auf dem Potential Phi0 und -Phi0
    r_1=0.3;
    r_2=0.05;
    r_3=0.3;
    z0=(r_1-r_2)/sqrt(2)+r_3;
    Phi0=10;
    for i=1:sizes
        for j=1:sizes
            for k=1:sizes
                pos=[(i-1)/(sizes-1)-0.5,(j-1)/(sizes-1)-0.5,(k-1)/(sizes-1)-0.5];
                r=sqrt(pos(1)^2+pos(2)^2);
                z=pos(3);
                %Torus
                if (r-r_1)^2+z^2<r_2^2 %In Torus
                    A(i,j,k)=1;
                    phi(i,j,k)=Phi0+0.5*(r_2^2-(r-r_1)^2+z^2);
                elseif (r)^2+(z0-abs(z))^2<r_3^2 && (z0-abs(z))>=0%In Halbkugel
                    A(i,j,k)=1;
                    phi(i,j,k)=-Phi0-0.5*(r_3^2-(r)^2+(z0-abs(z))^2);
                end
            end
        end
    end
elseif type=='paul_papercl'
    %Erzeuge PaperClip Falle
    angle=pi/4;
    f=1;
    
    r_1=0.18*f;
    r_2=0.03*f;
    r_3=0.25*f;
    x0=-0.3*f;
    x1=0.2*f;
    
    Phi0=10;
    for i=1:sizes
        for j=1:sizes
            for k=1:sizes
                pos1=[(i-1)/(sizes-1)-0.5,(j-1)/(sizes-1)-0.5,(k-1)/(sizes-1)-0.5];
                pos=[pos1(1)*cos(angle)-pos1(2)*sin(angle),pos1(1)*sin(angle)+pos1(2)*cos(angle),pos1(3)]; %Rotation
                
                r_inner=sqrt(pos(1)^2+pos(2)^2);
                r_i2o=sqrt((pos(1)-x0)^2+(pos(2)+r_2)^2);
                r_outer=sqrt((pos(1)-x1)^2+(pos(2))^2);
                
                if (r_inner-r_1)^2+pos(3)^2<r_2^2 && pos(1)>=0 %Inner 1/2 Torus
                    A(i,j,k)=1;
                    phi(i,j,k)=Phi0+0.5*(r_2^2-(r_inner-r_1)^2);
                elseif pos(1)<=0 && pos(1)>=x0 && (r_1-abs(pos(2)))^2+pos(3)^2<r_2^2  %Inner cables
                    A(i,j,k)=1;
                    phi(i,j,k)=Phi0+0.5*(r_2^2-(r_1-abs(pos(2)))^2-pos(3)^2);
                elseif pos(1)<=x1 && pos(1)>=x0 && (r_1+2*r_2-abs(pos(2)))^2+pos(3)^2<r_2^2  %Outer cables
                    A(i,j,k)=1;
                    phi(i,j,k)=Phi0+0.5*(r_2^2-(r_1+2*r_2-abs(pos(2)))^2-pos(3)^2);
                elseif pos(1)<=x0 && (r_i2o-(r_1+r_2))^2+pos(3)^2<r_2^2 %Inner to Outer 1/2 Torus
                    A(i,j,k)=1;
                    phi(i,j,k)=Phi0+0.5*(r_2^2-(r_i2o-(r_1+r_2))^2-pos(3)^2);
                elseif (r_outer-r_1-2*r_2)^2+pos(3)^2<r_2^2 && pos(1)>=0 && pos(1)>=x1 %Outer 1/2 Torus
                    A(i,j,k)=1;
                    phi(i,j,k)=Phi0+0.5*(r_2^2-(r_outer-r_1-2*r_2)^2);
                end
            end
        end
    end
elseif type=='paul_linears'
    %Erzeuge lineare Paul-Falle
    a=0.3;  %width
    b=0.4;  %length
    r=0.05;
    Phi0=10;
    for i=1:sizes
        for j=1:sizes
            for k=1:sizes
                pos=[(i-1)/(sizes-1)-0.5,(j-1)/(sizes-1)-0.5,(k-1)/(sizes-1)-0.5];
                z=pos(3);
                if (abs(pos(1))-a)^2+(abs(pos(3))-a)^2<=r^2 && abs(pos(2))<=b
                    A(i,j,k)=1;
                    if pos(1)<0 && pos(3)>0
                        phi(i,j,k)=Phi0+0.5*((abs(pos(1))-a)^2+(abs(pos(3)-a)^2));
                    elseif pos(1)>0 && pos(3)<0
                        phi(i,j,k)=Phi0+0.5*((abs(pos(1))-a)^2+(abs(pos(3)-a)^2));
                    else
                        phi(i,j,k)=-Phi0-0.5*((abs(pos(1))-a)^2+(abs(pos(3)-a)^2));
                    end
                end
            end
        end
    end
elseif type=='paul_lineari'
    %Erzeuge lineare Paul-Falle
    a=0.2;  %width
    b=0.15;  %length
    r=0.05;
    Phi0=10;
    for i=1:sizes
        for j=1:sizes
            for k=1:sizes
                pos=[(i-1)/(sizes-1)-0.5,(j-1)/(sizes-1)-0.5,(k-1)/(sizes-1)-0.5];
                z=pos(3);
                if (abs(pos(1))-a)^2+(abs(pos(3))-a)^2<=r^2 && abs(pos(2))<=b
                    A(i,j,k)=1;
                    if pos(1)<0 && pos(3)>0
                        phi(i,j,k)=Phi0+0.5*((abs(pos(1))-a)^2+(abs(pos(3)-a)^2));
                    elseif pos(1)>0 && pos(3)<0
                        phi(i,j,k)=Phi0+0.5*((abs(pos(1))-a)^2+(abs(pos(3)-a)^2));
                    else
                        phi(i,j,k)=-Phi0-0.5*((abs(pos(1))-a)^2+(abs(pos(3)-a)^2));
                    end
                elseif (abs(pos(1))-a)^2+(abs(pos(3))-a)^2<=r^2 && abs(pos(2))>=b
                    A(i,j,k)=1;
                    if pos(1)<0 && pos(3)>0
                        phi(i,j,k)=1.5*Phi0+0.5*((abs(pos(1))-a)^2+(abs(pos(3)-a)^2));
                    elseif pos(1)>0 && pos(3)<0
                        phi(i,j,k)=1.5*Phi0+0.5*((abs(pos(1))-a)^2+(abs(pos(3)-a)^2));
                    else
                        phi(i,j,k)=-1.5*Phi0-0.5*((abs(pos(1))-a)^2+(abs(pos(3)-a)^2));
                    end
                end
            end
        end
    end
end
end