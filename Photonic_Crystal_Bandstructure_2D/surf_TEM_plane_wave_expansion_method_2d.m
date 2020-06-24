%surf_TEM_plane_wave_expansion_photonic_crystal_hexa.m
%Determine the Bandstructure of a hexagonal lattice photonic crystal
%TEM_plane_wave_expansion_method_2d.m
%Determine the Bandstructure of a hexagonal lattice photonic crystal
%Gamma-Kappa-M-Gamma
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
how_fine=5;        %How much Detail per Zone?
plot_how_many=4;   %Plot How many Bands?
plotting=[1,0];     %E, B


%Create a filename
filename=filename_generator('Surf_TEM',d,a,eps_1,eps_2,n_max,how_fine);
%Save Startparameters
appdata_save(f,'d',d,'a',a,'eps_1',eps_1,'eps_2',eps_2,'n_max',n_max,'how_fine',how_fine);

%% Determine K_Matrix
%Preparation for fast matrix generation
area=a^2*sqrt(3);
pw=(2*n_max+1)^2;
b1=2*pi/a*(1-sqrt(3)/3*1i);                  %Primitie reciprocal lattice   -> real part is         x-axis    
b2=2*pi/a*2*sqrt(3)/3*1i;                    %Primitie reciprocal lattice   -> imaginary part is    y-axis

k_x=-2*pi/a:pi/(how_fine*a):+2*pi/a;
k_y=-2*pi/(sqrt(3)*a):pi/(how_fine*a*sqrt(3)):+2*pi/(sqrt(3)*a);
how_many=length(k_x)*length(k_y);

freqs_TE=zeros(length(k_x),length(k_y),pw);
freqs_TM=zeros(length(k_x),length(k_y),2*pw);

%Create some empty matrizes to fill
prefactor=2/area*pi*d;  %Prefactor for Fourier Transform
K=ones(pw,pw)*prefactor*(eps_1-eps_2);  %K_list
TE=zeros(pw,pw);
TM=zeros(2*pw,2*pw); 
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

save('f',f,'K',K,'k_x',k_x,'k_y',k_y);


%% Main Part of the Calculation
%Determine Q(k_z)
s=1; %counts the k_x and k_y components that have been calculated +1 
x=0;
y=0;
fprintf(['-> Calculating: ' num2str(s) '/' num2str(how_many) '\n'])
for k_x=-2*pi/a:pi/(how_fine*a):2*pi/a
    y=0;
    %k_x=0;
    x=x+1;
    for k_y=-2*pi/(sqrt(3)*a):pi/(how_fine*a*sqrt(3)):+2*pi/(sqrt(3)*a)
        y=y+1;
        %Generate Left Side K_nq
        t=tic();
        for l=1:(2*n_max+1)^2   %Vector components of field representing fourier components
            for m=1:(2*n_max+1)^2   %q and n components
                alpha=2*pi/(sqrt(3)*a)*(2*q(m)-n(m))+k_y;
                beta=2*pi/a*n(m)+k_x;
                TE(l,m)=K(l,m)*(alpha^2+beta^2);
                TM(l+(2*n_max+1)^2*[0 1],m+(2*n_max+1)^2*[0 1])=K(l,m)*[alpha^2       -alpha*beta;...
                                                                        -alpha*beta   beta^2];
            end
        end
        t_K=toc(t);
        fprintf(['\b\t K-Matrix: ' datestr(datenum(0,0,0,0,0,t_K),'HH:MM:SS') '\n']);
        %Determine eigenvalues via
        t=tic();
        omega_k_TE=eig(TE);
        omega_k_TM=eig(TM);
        t_eig=toc(t);
        fprintf(['\b\t Eigenvalues: ' datestr(datenum(0,0,0,0,0,t_eig),'HH:MM:SS') '\n']);
        omega_k_TE=sort(sqrt(omega_k_TE));
        omega_k_TM=sort(sqrt(omega_k_TM));
        freqs_TE(y,x,:)=omega_k_TE;
        freqs_TM(y,x,:)=omega_k_TM;
        fprintf(['\b\t Remaining: ' datestr(datenum(0,0,0,0,0,(t_eig+t_K)*(how_many-s)),'HH:MM:SS') '  (HH:MM:SS)\n']);
        s=s+1;     
        if s<=how_many
            fprintf(['-> Calculating: ' num2str(s) '/' num2str(how_many) '\n'])
        end
    end
end


%% Plotting
fprintf('-> Plotting\n')
k_x=-2*pi/a:pi/(how_fine*a):+2*pi/a;
k_y=-2*pi/(sqrt(3)*a):pi/(how_fine*a*sqrt(3)):+2*pi/(sqrt(3)*a);

%Plot Bands
ax1=subplot(1,1,1);
appdata_save(f,'ax1',ax1);

%Plot Bands
counter_E=1;
counter_M=1;
s=1;
if plotting(1)==1
    while counter_E<=plot_how_many
        if counter_E<=plot_how_many
            if max(max(real(freqs_TE(:,:,s))))>1e-5
                surf(k_x,k_y,real(freqs_TE(:,:,s)))
                counter_E=counter_E+1;
                if counter_E==2
                    hold on;
                end
                s_E=s;
            end
        end
        s=s+1;
    end
end
s=1;
if plotting(2)==1
    while counter_M<=plot_how_many
        if counter_M<=plot_how_many
            if max(max(real(freqs_TM(:,:,s))))>1e-5
                surf(k_x,k_yreal(freqs_TM(:,:,s)))
                counter_M=counter_M+1;
                if counter_M==2 && counter_E<2
                    hold on;
                end
                s_M=s;
            end
        end
        s=s+1;
    end
end

hold off;
set(gca,'xlim',[min(k_x) max(k_x)]);
set(gca,'ylim',[min(k_y) max(k_y)]);
xlabel('k_x')
ylabel('k_y')
zlabel('\omega/c')

%% Create MouseMovement Option
%set(f,'WindowButtonMotionFcn',{@MouseMovement_1D,f,h});