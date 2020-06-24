classdef Bullet
    %Creates a default tank
    
    properties
        
        %Velocity
        vx=0;
        vy=0;
        
        %Location
        x=0;
        y=0;
              
        %Explosion Radius
        b_r=1;
    end
    
    methods
        function obj=Bullet(tank)
            [x y x_vel y_vel]=tank.Barrel_Tip;
            obj.x=x;
            obj.y=y;
            obj.vx=x_vel;
            obj.vy=y_vel;
        end
        
        function obj=Reposition(obj,x,y,vx,vy)
            obj.x=x;
            obj.y=y;
            obj.vx=vx;
            obj.vy=vy;
        end
        
        function Plot(obj)
            bullet_size=0.1;
            x=obj.x;
            y=obj.y;
            
            plot(x,y,'wo')
            axis equal;
        end
    end
    
end

