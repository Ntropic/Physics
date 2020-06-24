%basis_draw.m
clc;
clear all;
close all;

windowsize=400;
w=windowsize-100;
g=figure('Name','Hole Structure','Position',[100 100 windowsize*2+50 w*sqrt(3)+100]); 

a=1;
d=0.5*a;
eps_1=1; 
eps_2=12;

set(gca, 'Units', 'pixels', 'Position', [60, 60, w, w*sqrt(3)]);
%Background
patch('XData',[-a/2 a/2 a/2 -a/2],'YData',sqrt(3)*a/2*[-1 -1 1 1],'FaceColor','white','EdgeColor','none');
hold on;
%Holes
rectangle('Position',[-d/2 -d/2 d d],'Curvature',[1 1],'FaceColor','black','LineStyle','none');
rectangle('Position',[-d/2-a/2 -d/2-a*sqrt(3)/2 d d],'Curvature',[1 1],'FaceColor','black','LineStyle','none');
rectangle('Position',[-d/2+a/2 -d/2-a*sqrt(3)/2 d d],'Curvature',[1 1],'FaceColor','black','LineStyle','none');
rectangle('Position',[-d/2-a/2 -d/2+a*sqrt(3)/2 d d],'Curvature',[1 1],'FaceColor','black','LineStyle','none');
rectangle('Position',[-d/2+a/2 -d/2+a*sqrt(3)/2 d d],'Curvature',[1 1],'FaceColor','black','LineStyle','none');
text(0,0,['\epsilon_2=' num2str(eps_2,'	%u')],'Color','white','HorizontalAlignment','center')
text(d/2,d/sqrt(3),['\epsilon_1=' num2str(eps_2,'	%u')],'Color','black','HorizontalAlignment','center')
hold off;

axis(a/2*[-1 1 -sqrt(3) sqrt(3)])
xlabel('x')
ylabel('y')