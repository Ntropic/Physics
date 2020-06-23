%magnetic_pendulum.m
%Top view onto a pendulum with a magnetic head. The pendulum is released
%with zero velocity and 
clc;
clear all;
close all;

how_many_trajectories=100;
boundaries=8;     %How large are the boundaries of the starting positions

%Magnet Positions
x_i=0.66*[1,-1,1,-1];
y_i=0.66*[1,1,-1,-1];

%Magnet Colors
rgb=[255,0,0;0,255,0;0,0,255;255,255,0];

%Physics Parameters
R=0.5; %Strength of friction (German: R for Reibung)
d=0.1; %inverse strength of the pendulum
C=0.5; %Strength of gravity (drives pendulum to the center)

%Differential equation
fun=@(t,x) [x(2);
            -C*x(1)-R*x(2)+(y_i(1)-x(1))/sqrt((x_i(1)-x(3))^2+(y_i(1)-x(1))^2+d^2)^3+(y_i(2)-x(1))/sqrt((x_i(2)-x(3))^2+(y_i(2)-x(1))^2+d^2)^3+(y_i(3)-x(1))/sqrt((x_i(3)-x(3))^2+(y_i(3)-x(1))^2+d^2)^3+(y_i(4)-x(1))/sqrt((x_i(4)-x(3))^2+(y_i(4)-x(1))^2+d^2)^3;
            x(4);
            -C*x(3)-R*x(4)+(x_i(1)-x(3))/sqrt((x_i(1)-x(3))^2+(y_i(1)-x(1))^2+d^2)^3+(x_i(2)-x(3))/sqrt((x_i(2)-x(3))^2+(y_i(2)-x(1))^2+d^2)^3+(x_i(3)-x(3))/sqrt((x_i(3)-x(3))^2+(y_i(3)-x(1))^2+d^2)^3+(x_i(4)-x(3))/sqrt((x_i(4)-x(3))^2+(y_i(4)-x(1))^2+d^2)^3];
      
%Trajectories
for j=1:how_many_trajectories
    x0=[rand(1)*boundaries-0.5,0,rand(1)*boundaries-0.5,0]; %[y vy,x,vx]
    tspan=[0,10];
    [t,y]=ode45(fun,tspan,x0);

    %Plot trajectories
    steps=30;
    for i=1:steps
        l=min([size(y,1) ceil(size(y,1)/steps*i)]);
        plot(y(1:l,3),y(1:l,1),'k')
        hold on;
        plot(x_i(1),y_i(1),'or')
        plot(x_i(2),y_i(2),'og')
        plot(x_i(3),y_i(3),'oy')
        plot(x_i(4),y_i(4),'ob')
        hold off;
        axis equal;
        axis(boundaries*[-1 1 -1 1])
        drawnow;
    end
end