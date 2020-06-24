%Elektrostatisches Potential in 3 Dimensionen
clc;
clear all;
close all;

%% Ausgangsparameter
typer='paul_papercl';    %Typ des Systems
sizer=256;              %Auflösung 
iter_steps=8192*64;       %Iterationsschritte (in der Zeit)
dt=0.01;
omega=1.0;                %Frequenz der Wechselspannung
q=-0.0000005;                %Ladung der Teilchen
m=0.000005;                  %Masse der Teilchen 
visc=0.25;
g_const=0.00025;              %Gravity Acceleration constant
fun=@(omega,t) cos(omega*t)+0.01;    %Voltage Signal

n_q=10;
n_posx=randn(n_q,1)*0.05+0.5;          %Positionsn der Ladungsträger
n_posy=randn(n_q,1)*0.05+0.5;   
n_posz=randn(n_q,1)*0.05+0.6;   
%n_q=2;
%n_posx=[0.45 0.55];
%n_posy=[0.5 0.5];
%n_posz=[0.5 0.5];

abbruch=[1e-4,1];       %1 mittlere Abweichung, 2 maximale Abweichung
w=1.5;                  %Überrelaxationskonstante

plot_rec_step=200;
ausgangsplot=128;
trajectories=1000;         %Zeige Trajektorien?

%Create filename
savename=[typer '_' num2str(sizer) '.mat'];

%% 1. Berechne Potential ohne Ladungsträger (Initialisierung der Rechnung)
if exist(savename,'file')~=2
    %Erzeuge die Ausgangsbedingungen
    [phi,A ]=phirand_3d(sizer,typer);
    %Plotte Struktur des Systems
    X=((1:sizer)-1)'/(sizer-1);
    Y=X; Z=X;
    iso_1=isosurface(X,Y,Z,phi,10);
    iso_2=isosurface(X,Y,Z,-phi,10);
    p_1=patch(iso_1);
    hold on;
    p_2=patch(iso_2);
    isonormals(X,Y,Z,phi,p_1);
    isonormals(X,Y,Z,-phi,p_2);
    p_1.FaceColor = 'blue';
    p_1.EdgeColor = 'none';
    p_2.FaceColor = 'red';
    p_2.EdgeColor = 'none';
    daspect([1,1,1]);view(3);
    camlight 
    %lighting gouraud
    xlabel('x'); ylabel('y'); zlabel ('z');
    title('System Setup');
    axis([0 1 0 1 0 1])
    rotate3d on;
    drawnow;

    %Berechne das Potential
    phi=estatsolveseid_3d(A,phi,sizer,w,abbruch,typer);   %Rekursiv von kleinem zu großem Gitter

    %Save data
    save(savename,'phi','A');
else
    load(savename);
end

%% Plotte die feinere Struktur und löse Feld auf 
hold off;
X=((1:sizer)-1)'/(sizer-1);
Y=X; Z=X;
iso_1=isosurface(X,Y,Z,phi,10);
iso_2=isosurface(X,Y,Z,-phi,10);
p_1=patch(iso_1);
hold on;
p_2=patch(iso_2);
isonormals(X,Y,Z,phi,p_1);
isonormals(X,Y,Z,-phi,p_2);
p_1.FaceColor = 'blue';
p_1.EdgeColor = 'none';
p_2.FaceColor = 'red';
p_2.EdgeColor = 'none';
daspect([1,1,1]);view(3);
camlight 
%lighting gouraud
xlabel('x'); ylabel('y'); zlabel ('z');
title('Potential');
axis([0 1 0 1 0 1])
rotate3d on;
drawnow;
%Plotte die Ergebnisse
if ausgangsplot>=1
    %close all;
    for i=1:sizer
        if i>1
             delete(g_prev);
        end
        Z=ones(sizer)*(i-1)/(sizer-1);
        g=surf(X,Y,Z,-phi(:,:,i));
        set(g,'edgecolor','none')
        colormap('jet');
        caxis([-10 10]);
        pause(0.05);
        g_prev=g;
        if ausgangsplot>1 && ausgangsplot==i
            pause();
        end
    end
end


%% Berechne Trajecktorien von Ladungsträgern 
nx=zeros(n_q,iter_steps+1);
ny=zeros(n_q,iter_steps+1);
nz=zeros(n_q,iter_steps+1);
nx(:,1)=n_posx;
ny(:,1)=n_posy;
nz(:,1)=n_posz;
vx=zeros(n_q,iter_steps+1);
vy=zeros(n_q,iter_steps+1);
vz=zeros(n_q,iter_steps+1);
r_jk=zeros(n_q,n_q);

phi_0=-phi;
[Ex Ey Ez]=gradient(phi_0); Ex=-Ex*sizer/128; Ey=-Ey*sizer/128; Ez=-Ez*sizer/128;   %Separate into potential by Klammer and electric field by other charges (to increase speed and get rid of self-interaction)

fprintf('\n')
if ausgangsplot==1
    delete(g_prev);
end
hold off;
X=((1:sizer)-1)'/(sizer-1);
Y=X; Z=X;
iso_1=isosurface(X,Y,Z,phi,10);
iso_2=isosurface(X,Y,Z,-phi,10);
p_1=patch(iso_1);
hold on;
p_2=patch(iso_2);
isonormals(X,Y,Z,phi,p_1);
isonormals(X,Y,Z,-phi,p_2);
p_1.FaceColor = 'blue';
p_1.EdgeColor = 'none';
p_2.FaceColor = 'red';
p_2.EdgeColor = 'none';
daspect([1,1,1]);view(3);
camlight 
%lighting gouraud
xlabel('x'); ylabel('y'); zlabel ('z');
title('Potential');
axis([0 1 0 1 0 1])
rotate3d on;
drawnow;

counter=0;
for i=1:iter_steps      %Iterationsschritte
    t=dt*(i-1);
    for j=1:n_q
        x_i(j)=nx(j,i);
        y_i(j)=ny(j,i);
        z_i(j)=nz(j,i);
    end   
    %Change Positions
    %Create map of Coulomb force interactions by the particles
    %Lorentzforce (electric field) and gravity 
    for j=1:n_q
        if x_i(j)>0 && x_i(j)<1 && y_i(j)>0 && y_i(j)<1 && z_i(j)>0 && z_i(j)<1
            E_q_x=0; E_q_y=0; E_q_z=0;
            for k=1:n_q
                if k~=j
                    E_q_x=E_q_x+q*(x_i(j)-x_i(k))/(sqrt((x_i(j)-x_i(k))^2+(y_i(j)-y_i(k))^2+(z_i(j)-z_i(k))^2))^3;
                    E_q_y=E_q_y+q*(y_i(j)-y_i(k))/(sqrt((x_i(j)-x_i(k))^2+(y_i(j)-y_i(k))^2+(z_i(j)-z_i(k))^2))^3;
                    E_q_z=E_q_z+q*(z_i(j)-z_i(k))/(sqrt((x_i(j)-x_i(k))^2+(y_i(j)-y_i(k))^2+(z_i(j)-z_i(k))^2))^3;
                end
            end
            vx(j,i+1)=vx(j,i)*(1-visc*dt)+q/m*dt*(Ex(1+floor(y_i(j)*(sizer-1)),1+floor(x_i(j)*(sizer-1)),1+floor(z_i(j)*(sizer-1)))*fun(omega,t)+E_q_x);
            vy(j,i+1)=vy(j,i)*(1-visc*dt)+q/m*dt*(Ey(1+floor(y_i(j)*(sizer-1)),1+floor(x_i(j)*(sizer-1)),1+floor(z_i(j)*(sizer-1)))*fun(omega,t)+E_q_y);
            vz(j,i+1)=vz(j,i)*(1-visc*dt)+q/m*dt*(Ez(1+floor(y_i(j)*(sizer-1)),1+floor(x_i(j)*(sizer-1)),1+floor(z_i(j)*(sizer-1)))*fun(omega,t)+E_q_z)-g_const*dt;
            nx(j,i+1)=nx(j,i)+vx(j,i)*dt;
            ny(j,i+1)=ny(j,i)+vy(j,i)*dt;
            nz(j,i+1)=nz(j,i)+vz(j,i)*dt;
        else
            nx(j,i+1)=nx(j,i)+vx(j,i)*dt;
            ny(j,i+1)=ny(j,i)+vy(j,i)*dt;
            nz(j,i+1)=nz(j,i)+vz(j,i)*dt;
        end
    end
    
    if mod(i,plot_rec_step)==1
        if i>1
            delete(trajic);
        end
        %axis equal;
        for j=1:n_q
            %Charge
            if trajectories>=1
                k=max([i-trajectories,1]);
                hold on;
                trajic(j)=plot3(nx(j,k:i),ny(j,k:i),nz(j,k:i),'k-','LineWidth',0.5);
            elseif trajectories==-1
                hold on;
                trajic(j)=plot3(nx(j,i),ny(j,i),nz(j,k:i),'ko');
            end
        end
        title(['t=' num2str(t)])
        drawnow;
    end
end