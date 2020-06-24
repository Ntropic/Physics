classdef Tank
    %Creates a default tank
    
    properties
        %HP
        f_wheel=150;
        b_wheel=150;
        main=500;
        barrel=300;
        
        %Fuel
        fuel=300;
        consumption=20;
        friction=5;
        force=40;
        
        %Velocity
        vel=0;
        
        %Location
        x=0;
        y=0;
        %Angles
        angle=0; %Rotation of tank
        %Barrel Location
        wheel_angle=0;
        barrel_angle=pi/4;%0;
        barrel_vel=0.5;
        
        %Parent
        parent=[];
        parent_angle=0; %Position of tank on planet
        
       %Explosion Radius
        b_r=1;
    end
    
    methods
        function obj=Tank(planet,planet_index,ang)
            if nargin==3
                obj.parent_angle=ang;
                [x,y,ang]=planet.Location(ang);
                obj.x=x;
                obj.y=y;
                obj.angle=ang;
                obj.parent=planet_index;
            elseif nargin==1
                obj.angle=planet;
            end
        end
        
        function obj=Reposition(obj,planet,parent_angle_change)
            if nargin==3
                obj.parent_angle=mod(obj.parent_angle+parent_angle_change,2*pi);
            end
            
            ang=obj.parent_angle;
            [x,y,ang]=planet.Location(ang);
            obj.x=x;
            obj.y=y;
            obj.angle=ang;
        end
        
        function obj=ReBarrel(obj,angle_change)
            new_ang=obj.barrel_angle+angle_change;
            if new_ang>pi
                new_ang=new_ang-2*pi;
            end
            if new_ang<=-pi/2
                new_ang=-pi/2;
            elseif new_ang>pi/2
                new_ang=pi/2;
            end
            obj.barrel_angle=new_ang;
        end
        
        function obj=Barrel_Strength(obj,strength_change)
            vel=obj.barrel_vel+strength_change;
            if vel<=0.5
                vel=0.5;
            elseif vel>20
                vel=20;
            end
            obj.barrel_vel=vel;
            fprintf(['Strength: ' num2str(vel) '/' num2str(5) '\n']);
        end
        
        function [x y x_vel y_vel]=Barrel_Tip(obj)
            wheel_size=0.1;
            wheel_dist=0.4;
            chassis_dist=0.02;
            barrel_size=[0.04,0.03,0.15];
            
            %Get Barrel position
            x=obj.x;
            y=obj.y;
            angle=obj.angle;
            barrel=[0; barrel_size(3)]; %1st
            b_phi=obj.barrel_angle;
            barrel=vector_rotator(barrel,b_phi);
            barrel=[barrel(1,:);barrel(2,:)+wheel_size*9/3];
            barrel=vector_rotator(barrel,angle,x,y);
            
            x=barrel(1);
            y=barrel(2);
            vel=obj.barrel_vel;
            ang=b_phi+angle-pi/2;

            x_vel=-vel*cos(ang);
            y_vel=-vel*sin(ang);
        end
        
        function Plot(obj)
            wheel_size=0.1;
            wheel_dist=0.4;
            chassis_dist=0.02;
            barrel_size=[0.04,0.03,0.15];
            
            theta=linspace(0,2*pi,11);
            %theta=theta(1:end-1);
            angler=obj.wheel_angle;
            wheel=[cos(theta+angler);sin(theta+angler)+1];
            wheel(2,:)=wheel(2,:)-min(wheel(2,:)); %On the floor
            
            x=obj.x;
            y=obj.y;
            angle=obj.angle;
            
            %Object vectors
            barrel=[-barrel_size(1)/2,barrel_size(1)/2,barrel_size(2)/2,-barrel_size(2)/2;
                   0,0,barrel_size(3),barrel_size(3)]; %1st
            b_phi=obj.barrel_angle;
            barrel=vector_rotator(barrel,b_phi);
            barrel=[barrel(1,:);barrel(2,:)+wheel_size*9/3];
            
            upper_chassis=[-wheel_dist/2,wheel_dist/2,wheel_dist/2-wheel_size,-wheel_dist/2+wheel_size ;
                          wheel_size,wheel_size,wheel_size*9.5/3,wheel_size*9.5/3]; %2nd
            chassis=[wheel_dist/2    ,wheel_dist/2+wheel_size+chassis_dist,wheel_dist/2+wheel_size+chassis_dist,wheel_dist/2  ;
                     wheel_size*2/3,wheel_size                      ,wheel_size*6/3                      ,wheel_size*7/3]; %3rd
            chassis=[chassis(1,:),-chassis(1,end:-1:1);chassis(2,:),chassis(2,end:-1:1)];
            front_wheel=[wheel_dist/2+wheel(1,:)*wheel_size;wheel(2,:)*wheel_size]; %5th
            back_wheel=[-wheel_dist/2+wheel(1,:)*wheel_size;wheel(2,:)*wheel_size];  %6th
            wx=wheel(1,:)*wheel_size;
            wx(wx>0)=wx(wx>0)+wheel_dist;
            wx=wx-wheel_dist/2;
            chain=wheel*wheel_size; %4th
            chain(1,:)=wx;    
            
            %Rotate
            barrel=vector_rotator(barrel,angle,x,y);
            upper_chassis=vector_rotator(upper_chassis,angle,x,y);
            chassis=vector_rotator(chassis,angle,x,y);
            chain=vector_rotator(chain,angle,x,y);
            front_wheel=vector_rotator(front_wheel,angle,x,y);
            back_wheel=vector_rotator(back_wheel,angle,x,y);
            %Plot vectors
            b=fill(barrel(1,:),barrel(2,:),0.35*ones(1,3));
            set(b,'EdgeColor','none')
            hold on;
            fill(upper_chassis(1,:),upper_chassis(2,:),0.45*ones(1,3));
            fill(chassis(1,:),chassis(2,:),0.4*ones(1,3));
            plot(chain(1,:),chain(2,:),'Color',0.0*ones(1,3),'LineWidth',1);
            fill(front_wheel(1,:),front_wheel(2,:),0.3*ones(1,3));
            fill(back_wheel(1,:),back_wheel(2,:),0.3*ones(1,3));
            
            axis equal;
        end
    end
    
end

