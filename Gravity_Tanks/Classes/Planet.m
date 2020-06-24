classdef Planet
    %PLANET Creates a plentary object
    
    properties
        %Location
        x=0;
        y=0;
        
        xs=0; %Schwerpunkt
        ys=0;
        %Radius
        how_many=5;
        r=ones(2^5,1);
        r0=[1,1];
        phi=0;
        m=pi;
        color=[0.3 0.3 0.3];
        density=1;
    end
    
    methods
        function obj=Planet(x,y,how_many,radius,color)
            obj.x=x;
            obj.y=y;
            obj.xs=x;
            obj.ys=y;
            obj.how_many=how_many;
            perl=perlin_1d(how_many);
            perl=perl/(max(perl));
            phi=linspace(0,2*pi,2^how_many+1);
            phi=phi(1:end-1);
            obj.r=radius(1)*ones(1,2^how_many)+(radius(2)-radius(1))*perl;
            obj.density=1;
            obj=obj.Mass;
            obj.r0=[min(obj.r) max(obj.r)];
            if nargin==5
                obj.color=color;
            end
        end
        
        function Plot(obj)
            phis=obj.phi+linspace(0,2*pi,2^(obj.how_many)+1);
            phis=phis(1:end-1);
            r=obj.r;
            x=obj.x+cos(phis).*r;
            y=obj.y+sin(phis).*r;
            fill(x,y,obj.color);
        end
        
        function obj=Mass(obj)
            obj.m=(sum(obj.r)/(2^obj.how_many))^2*pi*obj.density;
        end
        
        function obj=Mass_Center(obj)
            x=obj.x;
            y=obj.y;
            r=obj.r;
            phis=obj.phi+linspace(0,2*pi,2^(obj.how_many)+1);
            phis=phis(1:end-1);
            x_p=x+r.*cos(phis);
            y_p=y+r.*sin(phis);
            obj.xs=sum(x_p)*2/3/length(x_p)+x*1/3; %Geometrischer Schwerpunkt
            obj.ys=sum(y_p)*2/3/length(y_p)+y*1/3;
        end
        
        function [xt,yt,ang]=Location(obj,ang)
            %Returns the Location 
            how_many=obj.how_many;
            x=obj.x;
            y=obj.y;
            r=obj.r;
            r=r;
            
            ang=mod(ang,2*pi);
            if ang==0
                ang=10^-15;
            end
            comp_phi=linspace(0,2*pi,2^(obj.how_many)+1);
            phis=sort([ang comp_phi(1:end-1)]);
            pos=find(phis==ang);
            pos=min(pos);
            pos=pos+[-1 0];
            
            if pos(2)==length(r)+1
                pos(2)=1;
            end
            
            %Find position
            phis=linspace(0,2*pi,2^(obj.how_many)+1);
            r0=r(pos(1))+(r(pos(2))-r(pos(1)))*(ang-phis(pos(1)))/(phis(2)-phis(1));
            xt=x+cos(obj.phi+ang)*r0;
            yt=y+sin(obj.phi+ang)*r0;

            %Find angle
            phis=obj.phi+linspace(0,2*pi,2^(obj.how_many)+1);
            xi=x+r(pos).*cos(phis(pos));
            yi=y+r(pos).*sin(phis(pos));
            dx=xi(2)-xi(1);
            dy=yi(2)-yi(1);

            ang=angle(-dx-1i*dy);
        end
        
        function [r0 ang]=Radius(obj,angle)
            phi=obj.phi;
            ang=angle-phi;
            %Returns the Radius at an angle
            how_many=obj.how_many;
            x=obj.x;
            y=obj.y;
            r=obj.r;
            r=r;
            
            ang=mod(ang,2*pi);
            if ang==0
                ang=10^-15;
            end
            comp_phi=linspace(0,2*pi,2^(obj.how_many)+1);
            phis=sort([ang comp_phi(1:end-1)]);
            pos=find(phis==ang);
            pos=min(pos);
            pos=pos+[-1 0];
            
            if pos(2)==length(r)+1
                pos(2)=1;
            end
            
            %Find position
            phis=linspace(0,2*pi,2^(obj.how_many)+1);
            r0=r(pos(1))+(r(pos(2))-r(pos(1)))*(ang-phis(pos(1)))/(phis(2)-phis(1));
        end
        
        function ang=Angle(obj,angle)
            phi=obj.phi;
            ang=angle-phi;
        end
        
        function obj=Bomb_Explosion(obj,angle,rb)
            rand_str=0.025;
            %rb is the radius of the crater
            %angle is the angle at which the bomb hits the planet
            
            %The radius at angle
            [r1 ang]=obj.Radius(angle);
            
            %The planet is affected for a radius of alpha_max
            alpha_max=2*asin(rb/2/r1);
            
            %Find angles that can be affected
            phis=linspace(0,2*pi,2^(obj.how_many)+1);
            phis(end)=[];
            ang_diff=mod(phis-ang,2*pi);
            point_list=find(ang_diff<alpha_max);
            point_list=[point_list find(ang_diff>2*pi-alpha_max)];
            
            alpha=ang_diff(point_list);
            %Reduce the radius at these points
            r=obj.r;
            r2=r;

            r2(point_list)=r1*cos(alpha)-sqrt(r1^2*cos(alpha).^2-r1^2+rb^2)+rand(1,length(point_list))*rand_str;
            r=min([r;r2]);
            r=max([r;zeros(size(r))]);
            
            obj.r=r;
            obj.r0=[min(r) max(r)];
            
            %Recalculate Mass
            obj=obj.Mass;
            
            %Recalculate Center
            obj=obj.Mass_Center;
        end
    end
    
end

