%asp_ratio_magnetic_pendulum.m
clc;
clear all;
close all;
gcp %Start Parallel computing pool

%% Parameters:
resolution=1920;
asp_ratio=[16,9];
origin=[0,0];
region=8;  %How large are the boundaries of the starting positions

%Magnet positions and colors
x_i=0.66*[1,-1,1,-1];
y_i=0.66*[1,1,-1,-1];
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


%% Program Code
res=round(resolution*asp_ratio/max(asp_ratio));
ratio=asp_ratio(1)/asp_ratio(2);
if asp_ratio(1)>asp_ratio(2)
    min_x=origin(1)-region;
    max_x=origin(1)+region;
    min_y=origin(2)-region/ratio;
    max_y=origin(2)+region/ratio;
else
    min_x=origin(1)-region*ratio;
    max_x=origin(1)+region*ratio;
    min_y=origin(2)-region;
    max_y=origin(2)+region;  
end
x_map=linspace(min_x,max_x,res(1));
y_map=linspace(min_y,max_y,res(2));
dx=x_map(2)-x_map(1);
dy=y_map(2)-y_map(1);

rgb_map=zeros(res(2),res(1),3);
y_end=zeros(res(1),res(2));
x_end=zeros(res(1),res(2));
tspan=[0,10];
opts=odeset('RelTol',1e-3,'AbsTol',1e-3);
t2=0;
t_last=0;
for i=1:res(1)
    timer=tic();
    parfor j=1:res(2) %Parallelize the trajectories
        rem_time=t2/((i-1))*((res(1)-i)+(res(2)-j)/res(2));
        fprintf('Calculating trajectory i=%1d, j=%1d,  rem: %1ds\n',i,j,rem_time)
        x0=[y_map(j),0,x_map(i),0];
        
        [t,y]=ode113(fun,tspan,x0,opts);
        x_end(i,j)=y(size(y,1),3);
        y_end(i,j)=y(size(y,1),1);
        rgb_i=zeros(1,1,3);
        for k=1:4
            z=sqrt((x_i(k)-x_end(i,j))^2+(y_i(k)-y_end(i,j))^2);
            rgb_i(1,1,:)=max([0,1-z])*(1-z)*rgb(k,:);
            rgb_map(j,i,:)=rgb_map(j,i,:)+rgb_i;
        end
    end
    t_last=toc(timer);
    t2=t2+t_last;
    rem_time=t2/(i-1)*(res(1)-i);
    if mod(i,1)==0
        fid=fopen('rem_time.txt','w');
            tstr=datestr(datetime('now'));
            str_str=['Calculating trajectory i=%1d, R=%1.2f, C=%1.2f  rem: %1ds curr: ' tstr '\n'];
            fprintf(fid,str_str,i,R,C,rem_time);
        fclose(fid);
    end
end
%Save file
filename=['magnetic_pendulum_attractor_' num2str(res(1)) '_' num2str(res(2)) '_' num2str(origin(1)) '_' num2str(origin(2)) '_' num2str(region) '_' num2str(R) '_' num2str(d) '_' num2str(C)];
imwrite(rgb_map/255,[filename '.png']);
save([filename '.mat'],'rgb_map','x_end','y_end','R','d','C','resolution','asp_ratio','origin','region');

delete(gcp);