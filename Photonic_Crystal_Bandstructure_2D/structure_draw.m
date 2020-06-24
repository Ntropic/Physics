%structure_draw.m
clc;
clear all;
close all;

a=1;
d=0.5*a;

how_many_x=6;
how_many_y=3;

plot_eps=1;
plot_wigner_seitz=2;

eps_1=1; 
eps_2=12;


w=300;
g=figure('Name','Hole Structure','Position',[100 100 w*how_many_x/how_many_y+100 w*sqrt(3)+100]); 
set(gca, 'Units', 'pixels', 'Position', [60, 60, w*how_many_x/how_many_y, w*sqrt(3)]);

%Background
n=(how_many_x);
for i=-n:n
    if mod(i,2)==1
        plot(i*a/2*[1 1],how_many_y*a/2*[-sqrt(3) sqrt(3)],'k:');
        if i==-n 
            hold on;
        end
        if i==-n+1
            hold on;
        end
    end
end
m=(how_many_y);
for i=-m:m
    if mod(i,2)==1
        plot(how_many_x*a/2*[1 -1],i*a/2*[sqrt(3) sqrt(3)],'k:');
    end
end

%Holes
for i=-n:n
    for j=-m:m
        if mod(i,2)==1 && mod(j,2)==1
            rectangle('Position',[-d/2+i*a/2 -d/2+j*a/2*sqrt(3) d d],'Curvature',[1 1],'FaceColor','black','LineStyle','none');
        elseif mod(i,2)==0 && mod(j,2)==0
            rectangle('Position',[-d/2+i*a/2 -d/2+j*a/2*sqrt(3) d d],'Curvature',[1 1],'FaceColor','black','LineStyle','none');
        end
    end
end
%Primitive
rectangle('Position',[-a/2 -a/2*sqrt(3) a a*sqrt(3)],'Curvature',[0 0],'FaceColor','none','EdgeColor','k');
%Wigner Seitz Cell
if plot_wigner_seitz>=1
    x_wig=a/2*[1 0 -1 -1 0 1];
    y_max=a/sqrt(3);
    y_min=a/2/sqrt(3)
    y_wig=[y_min y_max y_min -y_min -y_max -y_min];
    patch('XData',x_wig,'YData',y_wig,'FaceColor','black','FaceAlpha',0.15,'EdgeColor','red','LineStyle',':')
    for i=-n:n
        for j=-m:m
            kappa=1/(1/a*(sqrt((i*a/2)^2+(sqrt(3)*j/2)^2)));
            if i==0 && j==0
                pause(0.00001)
            elseif mod(i,2)==1 && mod(j,2)==1
                patch('XData',x_wig+i*a/2,'YData',y_wig+j*a/2*sqrt(3),'FaceColor','black','FaceAlpha',0.1*kappa,'EdgeColor','red','LineStyle',':')
            elseif mod(i,2)==0 && mod(j,2)==0
                patch('XData',x_wig+i*a/2,'YData',y_wig+j*a/2*sqrt(3),'FaceColor','black','FaceAlpha',0.1*kappa,'EdgeColor','red','LineStyle',':')
            end
        end
    end
end
%Text
if plot_eps==1
    text(0,0,['\epsilon_2=' num2str(eps_2,'	%u')],'Color','white','HorizontalAlignment','center')
    text(d/2,d/sqrt(3),['\epsilon_1=' num2str(eps_2,'	%u')],'Color','black','HorizontalAlignment','center')
end
hold off;


axis(a/2*[-1*how_many_x 1*how_many_x -how_many_y*sqrt(3) how_many_y*sqrt(3)])
xlabel('x')
ylabel('y')