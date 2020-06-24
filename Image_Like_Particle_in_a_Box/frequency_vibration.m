%frequency_evolution.m
%2d version
clc;
clear all;
close all;

%% Parameters
len=100;                %Size of resulting image
A=imread('tree.png');
t=linspace(0,5,500);

%% Program
c=1;
B=A(:,:,1);
vidfile = VideoWriter('tree_waveprobability_2.mp4','MPEG-4');

fn=image_center(len,B,0.4);
[fftz x y]=sinus_decomposition2_image(fn,len);

M=cell(len,len);
for j=1:1:len
    for k=1:1:len
        M{j,k}=sin(y*pi*(k-1)).*sin(x*pi*(j-1));
    end
end
open(vidfile);
for i=1:length(t)
    z=zeros(size(x));
    for j=1:1:len
        for k=1:1:len
            z=z+M{j,k}.*fftz(j,k)*exp(1i*t(i)*sqrt((j-1)^2+(k-1)^2)*c);
        end
    end
    a=sqrt(z.*conj(z))';
    h=pcolor(a(end:-1:1,:)/sum(a(:)));
    h.EdgeColor='none';
    axis tight;
    axis equal;
    %caxis([0 1]);
   % colorbar()
    drawnow()
    F=getframe(gcf); 
    writeVideo(vidfile,F);
end
close(vidfile)