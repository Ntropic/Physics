%gray_scott_map.m
%Add colors via three components of chemical
clc;
clear all;
close all;

%% Parameters
n=2000; %Size of grid
m=2000; %Size of grid 2
plot_many=10;

n_its=2000; %Starting points
sizles=10; %Size of starting points

k=[0.0 0.08];
f=[0.0 0.08];
r_u=1; %Diffusion rate u
r_v=0.5; %Diffusion rate v
dt=0.125;
dx=1.5;

its=15000; %Iterations

%% Setup
filename=['f_' num2str(f(1)) '_' num2str(f(2)) '_k_' num2str(k(1)) '_' num2str(k(2)) '_res' num2str(n) '_' num2str(m) '.png'];
U=ones(n,m);
V=zeros(n,m);
for i=1:n_its
    init=ceil(rand(1,2).*[n-sizles,m-sizles]);
    V(init(1)+(0:sizles-1),init(2)+(0:sizles-1))=1;
end
c_mat=[0.25 0.5 0.25; 0.5 -3 0.5; 0.25 0.5 0.25]/dx^2;

k=linspace(k(1),k(2),n);
kl=k;
k=repmat(k',1,m);
f=linspace(f(1),f(2),m);
fl=f;
f=repmat(f,n,1);

for i=1:its
    ddU=convolve2(U,c_mat,'circular');
    ddV=convolve2(V,c_mat,'circular');
    
    dU=r_u*ddU-U.*V.^2+f.*(1-U);
    dV=r_v*ddV+U.*V.^2-(f+k).*V;
    
    U=(U+dU*dt);
    V=(V+dV*dt);
    
    if mod(i,plot_many)==0
        A=U;%zeros(n,m,3);
        %P=(1-U-V);
        %maxi=max([U(:); V(:)]);%;U(:)+P(:)]);
        %A(:,:,1)=V/maxi;
        %A(:,:,3)=(U/maxi);
        %A(:,:,2)=(P)/maxi;
        %image(fl,kl,A)
        imagesc(fl,kl,A)
        set(gca,'YDir','normal')
        title(['t=' num2str(i)]);
        xlabel('f')
        ylabel('k')
        axis equal;
        axis tight;
        grid;
        %caxis([0,1]);
        %colorbar()
        drawnow;
        
    end
end
F = getframe(gcf);
[A, Map] = frame2im(F);
imwrite(A,filename);
%imwrite(uint8(round(A*255)),filename);