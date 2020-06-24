classdef World
    %WORLD keeps all objects, and makes sure that they are drawn onto the
    %screen
    properties
        n=0;
        Planets=Planet.empty;
        Tanks=Tank.empty;
        Bullets=Bullet.empty;
        dt=0.05;
        
        trajectories=0;
        key={};
        time=datetime();
    end
    
    methods
        function obj=World(n,max_dist,min_dist,how_many,mass_prob,pol_width,dr,dt)
            if nargin==3
                mass_prob=[0,0,0,1,10,2,0,0,0,0,0,1,4,5,3,1,0];
                pol_width=0.2;
            end
            if nargin<=7
                obj.dt=0.05;
            end
            
            i=1;
            r(i)=Rand_Dist(1,mass_prob,pol_width,'');

            x(i)=rand(1)*max_dist;
            y(i)=rand(1)*max_dist;
            p(i)=Planet(x(i),y(i),how_many,r(i)+[0,dr],[0.4,0.3,0.2]+rand(1,3)*0.3);

            m_D=max_dist;
            p_W=pol_width;
            for i=2:n
                dxi=-1;
                counter=0;
                while min(dxi)<0
                    counter=counter+1;
                    
                    if floor(counter/50)>0
                        max_dist=m_D*0.8^(floor(counter/50));
                        if counter>200
                            pol_width=p_W*0.8^floor(counter/200);
                        end
                    end
                    
                    r(i)=Rand_Dist(1,mass_prob,pol_width,'');

                    x(i)=rand(1)*max_dist;
                    y(i)=rand(1)*max_dist;

                    %Check for overlaps
                    for j=1:i-1
                        dxi(j)=norm([x(j)-x(i);y(j)-y(i)])-r(j)-r(i)-2*dr-min_dist;
                    end
                end

                p(i)=Planet(x(i),y(i),5,r(i)+[0,dr],[0.4,0.3,0.2]+rand(1,3)*0.3);
            end
            obj.Planets=p;
        end
        
        function [coll coll_ang]=Bullet_Collision(obj)
            %Check for collisions
            b=obj.Bullets;
            p=obj.Planets;
            bx=[];
            by=[];
            for i=1:length(p)
                px(i)=p(i).x;
                py(i)=p(i).y;
                pr0(i,:)=p(i).r0;
            end
            for i=1:length(b)
                bx(i)=b(i).x;
                by(i)=b(i).y;
            end
            coll=zeros(length(b),1);
            coll_ang=zeros(length(b),1);
            for i=1:length(bx)
                for j=1:length(px)
                    r_diff=[bx(i)-px(j);by(i)-py(j)];
                    dr=norm(r_diff);
                    if dr<pr0(j,1)
                        coll(i)=j;
                    elseif dr<pr0(j,2)
                        %Maybe a collision
                        alpha=angle(r_diff(1)+1i*r_diff(2));
                        [r0 ang]=p(j).Radius(alpha);
                        if dr<r0
                            coll(i)=j;
                            coll_ang(i)=ang;
                        end
                    end
                end
            end
        end
        
        function obj=Toggle_Trajectory(obj)
            obj.trajectories=mod(obj.trajectories+1,2);
        end
        
        function obj=Add_Tank(obj,planet_index,ang)
            t=obj.Tanks;
            if nargin==3
                t(length(t)+1)=Tank(obj.Planets(planet_index),planet_index,ang);
            elseif nargin==2
                t(length(t)+1)=Tank(obj.Planets(planet_index),planet_index,rand()*2*pi);
            elseif nargin==1
                planet_index=ceil(rand()*length(obj.Planets));
                t(length(t)+1)=Tank(obj.Planets(planet_index),planet_index,rand()*2*pi);
            end 
            obj.Tanks=t;
        end
        
        function obj=Rotate_Planet(obj,planet_index,ang)
            p=obj.Planets;
            p(planet_index).phi=mod(p(planet_index).phi+ang,2*pi);
            obj.Planets=p;
            %Recalculate Tank Positions
            t=obj.Tanks;
            for i=1:length(t)
                if t(i).parent==planet_index
                    t(i)=t(i).Reposition(p(planet_index));
                end
            end
            obj.Tanks=t;
        end
        
        function obj=Evolve_System(obj)
            %Check key presses
            key=obj.key;
            if any(strcmp(key,'space'))
                obj=obj.Shoot(1);
            end
            if any(strcmp(key,'a'))
                obj=obj.Drive_Left(1);
            end
            if any(strcmp(key,'d'))
                obj=obj.Drive_Right(1);
            end
            if any(strcmp(key,'q')) || any(strcmp(key,'w'))
                obj=obj.Barrel_Left(1);
            end
            if any(strcmp(key,'e')) || any(strcmp(key,'s'))
                obj=obj.Barrel_Right(1);
            end
            if any(strcmp(key,'shift'))
                obj=obj.Barrel_Increase(1);
            end
            if any(strcmp(key,'control'))
                obj=obj.Barrel_Decrease(1);    
            end
            if any(strcmp(key,'r'))
                obj=obj.Toggle_Trajectory;
                obj.key={obj.key{find(1-strcmp(obj.key,'r'))}}; 
            end
            
            %Evolve positions
            G=1;
            dt=obj.dt;
            %Evolve System -> Euler method
            %Evolve Bullets
            p=obj.Planets;
            for i=1:length(p)
                px(i)=p(i).x;
                py(i)=p(i).y;
                m(i)=p(i).m;
            end
            b=obj.Bullets;
            for i=1:length(b)
                bx=b(i).x;
                by=b(i).y;
                bvx=b(i).vx;
                bvy=b(i).vy;
                
                F=[0;0];
                for j=1:length(px)
                    nr=[bx-px(j);by-py(j)];
                    len_r=norm(nr);
                    nr=nr/len_r;
                    
                    F=F-nr*m(j)/len_r^2;
                end
                bxn=bx+bvx*dt+1/2*F(1)*dt^2;
                byn=by+bvy*dt+1/2*F(2)*dt^2;

                bxnv=bvx+F(1)*dt;
                bynv=bvy+F(2)*dt;
                
                b(i).x=bxn;
                b(i).y=byn;
                b(i).vx=bxnv;
                b(i).vy=bynv;
            end
            
            %Detect collisions
            [coll coll_ang]=obj.Bullet_Collision;
            %coll tells us which bullet collided with which planet
            %coll ang the angle at which this happens

            for i=1:length(coll)
                if coll(i)>0
                    p(coll(i))=p(coll(i)).Bomb_Explosion(coll_ang(i),b(i).b_r);
                end
            end
            b(find(coll))=[];
            obj.Bullets=b;
            obj.Planets=p;
        end
        
        function [x y coll coll_ang]=Evolve_Trajectories(obj,tank)
            t=obj.Tanks;
            b=Bullet(t(tank));
            
            G=1;
            dt=obj.dt;
            %Evolve System -> Euler method
            %Evolve Bullets
            p=obj.Planets;
            for i=1:length(p)
                px(i)=p(i).x;
                py(i)=p(i).y;
                m(i)=p(i).m;
                pr0(i,:)=p(i).r0;
                pr{i}=p(i).r;
            end
           
            bx=b.x;
            by=b.y;
            bvx=b.vx;
            bvy=b.vy;
            
            steps=500;
            x=zeros(steps,1);
            y=zeros(steps,1);
            i=0;
            coll=0;
            coll_ang=0;
            while i<steps && coll==0
                i=i+1;
                F=[0;0];
                for j=1:length(px)
                    nr=[bx-px(j);by-py(j)];
                    len_r=norm(nr);
                    
                    if len_r<pr0(j,1)
                        coll=j;
                    elseif len_r<pr0(j,2)
                        %Maybe a collision
                        alpha=angle(nr(1)+1i*nr(2));
                        [r0 ang]=p(j).Radius(alpha);
                        if len_r<r0
                            coll=j;
                            coll_ang=ang;
                        end
                    end
                    
                    nr=nr/len_r;

                    F=F-nr*m(j)/len_r^2;
                end
                bx=bx+bvx*dt+1/2*F(1)*dt^2;
                by=by+bvy*dt+1/2*F(2)*dt^2;

                bvx=bvx+F(1)*dt;
                bvy=bvy+F(2)*dt;
                
                x(i)=bx;
                y(i)=by;
            end
            if coll>0
                x(i:end)=[];
                y(i:end)=[];
            end
        end
        
        function obj=Shoot(obj,tank)
            t1=obj.time;
            t2=datetime();
            if seconds(t2-t1)>0.5
                t=obj.Tanks;
                b=obj.Bullets;
                b(length(b)+1)=Bullet(t(tank));
                obj.Bullets=b;
                obj.time=t2;
            end
        end
        
        function obj=Drive_Left(obj,tank)
            t=obj.Tanks;
            par=t(tank).parent;
            p=obj.Planets;
            t(tank)=t(tank).Reposition(p(par),0.025);
            obj.Tanks=t;
        end
        
        function obj=Drive_Right(obj,tank)
            t=obj.Tanks;
            par=t(tank).parent;
            p=obj.Planets;
            t(tank)=t(tank).Reposition(p(par),-0.025);
            obj.Tanks=t;
        end
        
        function obj=Barrel_Left(obj,tank)
            t=obj.Tanks;
            t(tank)=t(tank).ReBarrel(0.05);
            obj.Tanks=t;
        end
        
        function obj=Barrel_Right(obj,tank)
            t=obj.Tanks;
            t(tank)=t(tank).ReBarrel(-0.05);
            obj.Tanks=t;
        end
        
        function obj=Barrel_Increase(obj,tank)
            t=obj.Tanks;
            t(tank)=t(tank).Barrel_Strength(+0.125);
            obj.Tanks=t;
        end
        
        function obj=Barrel_Decrease(obj,tank)
            t=obj.Tanks;
            t(tank)=t(tank).Barrel_Strength(-0.125);
            obj.Tanks=t;
        end
        
        function Plot(obj)
            p=obj.Planets;
            t=obj.Tanks;
            b=obj.Bullets;
            for i=1:length(p)
                p(i).Plot();
                hold on;
            end
            for j=1:length(t)
                t(j).Plot();
                hold on;
            end
            for k=1:length(b)
                b(k).Plot();
                hold on;
            end
            
            axis equal;
            axis tight;
            
            x_lim=get(gca,'xlim');
            x_lim=mean(x_lim)+[-diff(x_lim)*0.7 diff(x_lim)*0.7];
            y_lim=get(gca,'ylim');
            y_lim=mean(y_lim)+[-diff(y_lim)*0.7 diff(y_lim)*0.7];
            
            if obj.trajectories==1
                [x y coll coll_ang]=obj.Evolve_Trajectories(1);
                plot(x,y,':w');
                hold on;
                
                if coll>0
                    r_b=t(1).b_r;
                    phis=linspace(0,2*pi,32);
                    plot(x(end)+r_b*cos(phis),y(end)+r_b*sin(phis),':w');
                end
            end
            set(gca,'xlim',x_lim);
            set(gca,'ylim',y_lim);
            axis off;
            set(gca,'color',[0 0 0])
            
            hold off;
        end
    end
    
end

