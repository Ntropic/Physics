%TE_plane_wave_expansion_method_2d.m
%Determine the Bandstructure of a hexagonal lattice photonic crystal
%Gamma-Kappa-M-Gamma
clc;
clear all;
close all;

%% Startparameters
%System
d=0.8; 
a=1; 
eps_1=1; 
eps_2=13;

n_max=20;           %How Many Fourier Components?
how_fine=30;        %How much Detail per Zone?
plot_how_many=7;   %Plot How many Bands?
plot_light_cone=0;


%% Initialize Windows
%First Draw Structure
windowsize=400;
w=windowsize-100;
h=figure('Name','Hole Structure','Position',[100 100 windowsize+2*w+160 w*sqrt(3)+100]); 

%Create axis for field distributions
axh1=axes(h, 'Units', 'pixels', 'Position', [60, 60, w, w*sqrt(3)]);
axh2=axes(h, 'Units', 'pixels', 'Position', [60+w+50, 60, w, w*sqrt(3)]);
axh3=axes(h, 'Units', 'pixels', 'Position', [60+w*2+100, 60, w, w*sqrt(3)]);
axh4=axes(h, 'Units', 'pixels', 'Position', [60+w*3+110, 60, 150, w*sqrt(3)]);
axis off;

%Create Band-Structure Window
windowsize=500; 
f=figure('Name','Band Structure','Position',[300 300 windowsize*16/9 windowsize]); 



%Save Startparameters in Window
filename=filename_generator('Surf_TE',d,a,eps_1,eps_2,n_max,how_fine,plot_how_many);
appdata_save(f,'axh1',axh1,'axh2',axh2,'axh3',axh3,'axh4',axh4,'d',d,'a',a,'eps_1',eps_1,'eps_2',eps_2,'n_max',n_max,'how_fine',how_fine,'plot_how_many',plot_how_many);

%% Determine K_Matrix
%Preparation for fast matrix generation
area=a^2*sqrt(3);
pw=(2*n_max+1)^2;
b1=2*pi/a*(1-sqrt(3)/3*1i);                  %Primitie reciprocal lattice   -> real part is         x-axis    
b2=2*pi/a*2*sqrt(3)/3*1i;                    %Primitie reciprocal lattice   -> imaginary part is    y-axis

%The path of k -> high symmetry points
%Gamma to Kappa
k_x_0=0:2*pi/a*1/3/how_fine:2*pi/a*1/3;             
k_y_0=0:2*pi/a*1/sqrt(3)/how_fine:2*pi/a*1/sqrt(3);
%Kappa to M
k_x_1=2*pi/a*1/3:-2*pi/a*1/3/how_fine:0;
k_y_1=2*pi/a*1/sqrt(3)*ones(1,how_fine);
%M to Gamma
k_x_2=zeros(1,how_fine);
k_y_2=2*pi/a*1/sqrt(3):-2*pi/a*1/sqrt(3)/how_fine:0;

k_x=[k_x_0 k_x_1(2:length(k_x_1)) k_x_2];
k_y=[k_y_0 k_y_1(2:length(k_y_1)) k_y_2];
freqs=zeros(length(k_x),pw);

    %Create some empty matrizes to fill
    prefactor=2/area*pi*d;  %Prefactor for Fourier Transform
    K=ones(pw,pw)*prefactor*(eps_1-eps_2);  %K_list
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

    appdata_save(f,'K',K,'k_x',k_x,'k_y',k_y,'q',q,'n',n,'G',G,'n_10',0);

if exist([filename '.mat'])==0
    %% Main Part of the Calculation
    %Determine Q(k_z)
    s=1; %counts the k_x and k_y components that have been calculated +1 
    x=0;
    y=0;
    how_many=length(k_x);
    fprintf(['-> Calculating: ' num2str(s) '/' num2str(how_many) '\n'])
    for i=1:length(k_x)
        %Generate Left Side K_nq
        t=tic();
        for l=1:(2*n_max+1)^2   %Vector components of field representing fourier components
            for m=1:(2*n_max+1)^2   %q and n components
                alpha=2*pi/(sqrt(3)*a)*(2*q(m)-n(m))+k_y(i);
                beta=2*pi/a*n(m)+k_x(i);
                K_nq(l,m)=K(l,m)*(alpha^2+beta^2);
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
        freqs(i,:)=omega_k;
        fprintf(['\b\t Remaining: ' datestr(datenum(0,0,0,0,0,(t_eig+t_K)*(how_many-s)),'HH:MM:SS') '  (HH:MM:SS)\n']);
        s=s+1;     
        if s<=how_many
            fprintf(['-> Calculating: ' num2str(s) '/' num2str(how_many) '\n'])
        end
    end
    save([filename '.mat'],'freqs');
else
    fprintf('-> Loading Data\n')
    load([filename '.mat']);
end

%% Plotting
fprintf('-> Plotting\n')
%Plot Bands
ax1=subplot(1,1,1);
appdata_save(f,'ax1',ax1);

%Plot Bands
counter=1;
s=1;
while counter<=plot_how_many 
    if max(real(freqs(:,s)))>1e-5
        plot(1:length(k_x),real(freqs(:,s)),'ButtonDownFcn',{@MouseMovement_2D_TEM_Toggle,f,h,'TE'})
        counter=counter+1;
        if counter==2
            hold on;
        end
    end
    s=s+1;
end
set(gca,'XTick',[1:how_fine:length(k_x)]') 
set(gca,'XTickLabel',{'\Lambda';'K';'M';'\Lambda'})
set(gca,'xlim',[1 length(k_x)])

%Plot Light Cone
if plot_light_cone==1
    w_c_max=get(gca,'ylim');
    k_abs=sqrt(k_x.^2+k_y.^2);
    x_en=[1:length(k_x),length(k_x):-1:1]';
    y_en=[k_abs,w_c_max(2)*ones(1,length(k_x))]';
    patch('XData',x_en,'YData',y_en,'FaceColor','black','FaceAlpha',0.5,'EdgeColor','none')
end

hold off;
xlabel('k')
ylabel('\omega/c')

%% Create MouseMovement Option
set(f,'WindowButtonMotionFcn',{@MouseMovement_2D_TEM,f,h,'TE'});
appdata_save(f,'movement',1);
set(f,'ButtonDownFcn',{@MouseMovement_2D_TEM_Toggle,f,h,'TE'});
