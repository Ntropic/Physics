%gray_scott_test.m
%Add colors via three components of chemical
clc;
clear all;
close all;

%% Parameters
n=256; %Size of grid
m=256; %Size of grid 2
plot_many=25;

n_its=100; %Starting points
sizles=5; %Size of starting points
mode=3;
%Rates
if mode==1 %Stripes
    f=0.055; %Rate of process that feeds U and drains V and P
    k=0.063; %Conversion rate of V to P
elseif mode==2 %Dots and Stripes
    f=0.06; %Rate of process that feeds U and drains V and P
    k=0.065; %Conversion rate of V to P
elseif mode==3 %Dots and Stripes
    f=0.03; %Rate of process that feeds U and drains V and P
    k=0.065; %Conversion rate of V to P
elseif mode==4 %Explosions
    f=0.018; %Rate of process that feeds U and drains V and P
    k=0.051; %Conversion rate of V to P
elseif mode==5 %Inverse Dots
    f=0.026; %Rate of process that feeds U and drains V and P
    k=0.053; %Conversion rate of V to P
elseif mode==6 %Explore new modes
    f=0.040; %Rate of process that feeds U and drains V and P
    k=0.060; %Conversion rate of V to P
end

r_u=1; %Diffusion rate u
r_v=0.5; %Diffusion rate v
dt=0.25;
dx=1;

its=100000; %Iterations

%% Setup
U=ones(n,m);
V=zeros(n,m);
for i=1:n_its
    init=ceil(rand(1,2).*[n-sizles,m-sizles]);
    V(init(1)+(0:sizles-1),init(2)+(0:sizles-1))=1;
end

subplot(1,3,1)
imagesc(V);
axis equal;
axis tight;
subplot(1,3,2)
imagesc(U);
axis equal;
axis tight;
title('t=0');
%caxis([0,1]);
%colorbar()
drawnow;
for i=1:its

    ddU=laplace(U,dx);
    ddV=laplace(V,dx);
    
    dU=r_u*ddU-U.*V.^2+f*(1-U);
    dV=r_v*ddV+U.*V.^2-(f+k)*V;
    
    U=(U+dU*dt);
    V=(V+dV*dt);
    
    if mod(i,plot_many)==0
        subplot(1,3,1)
        imagesc(V);
        axis equal;
        axis tight;
        subplot(1,3,2)
        imagesc(U);
        axis equal;
        axis tight;
        title(['t=' num2str(i)]);
        subplot(1,3,3)
        imagesc(1-U-V);
        axis equal;
        axis tight;
        %caxis([0,1]);
        %colorbar()
        drawnow;
    end
end