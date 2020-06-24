%plane_wave_expansion_photonic_crystal_hexa.m
%Determine the Bandstructure of a hexagonal lattice photonic crystal
clc;
clear all;
close all;

windowsize=800;
f=figure('Name','Dispersion Diagram','Position',[200 200 windowsize*16/9 windowsize]); 
%% Startparameters
%System
d=0.8; 
a=1; 
eps_1=1; 
eps_2=13;

n_max=5;           %How Many Fourier Components?
how_many_ks=1;      %How many Brilluin Zones?
how_fine=20;        %How much Detail per Zone?
plot_how_many=10;   %Plot How many Bands?

%Save Startparameters
appdata_save(f,'d',d,'a',a,'eps_1',eps_1,'eps_2',eps_2,'n_max',n_max,'how_many_ks',how_many_ks,'how_fine',how_fine,'plot_before',0);

%% Determine K_Matrix
k_x=-how_many_ks*pi/a:pi/(how_fine*a):+how_many_ks*pi/a;
k_y=-how_many_ks*pi/(sqrt(3)*a):pi/(how_fine*a*sqrt(3)):+how_many_ks*pi/(a*sqrt(3));
pw=(2*n_max+1)^2;

freqs=zeros(length(k_x),length(k_y),(2*n_max+1)^2*3);
%freqs=zeros(1,length(k_y),pw*3);

%Preparation for fast matrix generation
area=a^2*sqrt(3);
pw=(2*n_max+1)^2;
prefactor=(1/eps_1-1/eps_2)*1/area*pi*d;  %Prefactor for Fourier Transform
b1=2*pi/a*(1-sqrt(3)/3*1i);                  %Primitie reciprocal lattice   -> real part is         x-axis    
b2=2*pi/a*2*sqrt(3)/3*1i;                    %Primitie reciprocal lattice   -> imaginary part is    y-axis

%Create some empty matrizes to fill
K=ones(pw,pw)*prefactor; 
dK=zeros(pw,pw);          
K_nq=zeros(pw,pw);
G=zeros(pw,1);

fprintf('-> Create K Matrix \n')

n=zeros(pw,1); %Index Positions in Matrizes of n
q=zeros(pw,1); %Index Positions in Matrizes of q
for i=1:pw
     n(i)=floor(mod(i-1,pw)/(2*n_max+1))-n_max;
     q(i)=mod(i-1,2*n_max+1)-n_max;
     G(i)=n(i)*b1+q(i)*b2;
end
%Do the bulk of the calculation
for i=1:pw
    for j=i+1:pw
        K(i,j)=K(i,j)*besselj(1,d/2*abs(G(i)-G(j)))/abs(G(i)-G(j));
        K(j,i)=K(i,j);          %Use symmetry :D I <3 Symmetry
    end
    K(i,i)=(1-prefactor*d/4)*eps_2+prefactor*eps_1*d/4;   %Add the constant background factor
end
K=inv(K);

appdata_save(f,'K',K,'k_x',k_x,'k_y',k_y);


%% Main Part of the Calculation
%Determine Q(k_z)
s=1; %counts the k_x and k_y components that have been calculated +1 
x=0;
y=0;
how_many=length(k_x)*length(k_y);
fprintf(['-> Calculating: ' num2str(s) '/' num2str(how_many) '\n'])
for k_x=-how_many_ks*pi/a:pi/(how_fine*a):+how_many_ks*pi/a
    y=0;
    %k_x=0;
    x=x+1;
    for k_y=-how_many_ks*pi/(sqrt(3)*a):pi/(how_fine*a*sqrt(3)):+how_many_ks*pi/(sqrt(3)*a)
        y=y+1;
        %Generate Left Side K_nq
        t=tic();
        for l=1:(2*n_max+1)^2   %Vector components of field representing fourier components
            for m=1:(2*n_max+1)^2   %q and n components
                alpha=2*pi/(sqrt(3)*a)*(2*q(m)-n(m))+k_y;
                beta=2*pi/a*n(m)+k_x;
                K_nq(l+(2*n_max+1)^2*[0 1 2],m+(2*n_max+1)^2*[0 1 2])=K(l,m)*[alpha^2       -alpha*beta         0;...
                                                                              -alpha*beta   beta^2              0;...
                                                                              0             0                   alpha^2+beta^2];
            end
        end
        t_K=toc(t);
        fprintf(['\b\t K-Matrix: ' datestr(datenum(0,0,0,0,0,t_K),'HH:MM:SS') '\n']);
        %Determine eigenvalues via
        t=tic();
        omega_k=eig(K_nq);
        t_eig=toc(t);
        fprintf(['\b\t Eigenvalues: ' datestr(datenum(0,0,0,0,0,t_eig),'HH:MM:SS') '\n']);
        omega_k=sort(sqrt(omega_k));
        freqs(x,y,:)=omega_k;
        fprintf(['\b\t Remaining: ' datestr(datenum(0,0,0,0,0,(t_eig+t_K)*(how_many-s)),'HH:MM:SS') '  (HH:MM:SS)\n']);
        s=s+1;     
        if s<=how_many
            fprintf(['-> Calculating: ' num2str(s) '/' num2str(how_many) '\n'])
        end
    end
end


%% Plotting

k_x=-how_many_ks*pi/a:pi/(how_fine*a):+how_many_ks*pi/a;
k_y=-how_many_ks*pi/(sqrt(3)*a):pi/(how_fine*a*sqrt(3)):+how_many_ks*pi/(a*sqrt(3));
fprintf('-> Plotting\n')
%Plot Bands
ax1=subplot(1,1,1);
appdata_save(f,'ax1',ax1);

counter=1;
s=1;
while counter<=plot_how_many
    if max(max(real(freqs(:,:,s))))>1e-5
        %plot(k_y,real(freqs(:,:,s)))
        surf(k_x,k_y,real(freqs(:,:,s)))
        counter=counter+1;
        if counter==2
            hold on;
        end
    end
    s=s+1;
end

hold off;
xlabel('k_x')
ylabel('k_y')
zlabel('\omega/c')
rotate3d on;


%% Create MouseMovement Option
%set(f,'WindowButtonMotionFcn',{@MouseMovement_1D,f,h});
