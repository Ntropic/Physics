function Movements
    clear all;
    close all;
    clc;
    
    global world dt
    
    figure('MenuBar','none','Color','black',...
    'name','Planet Busters','position',[50,50,800,800],...
    'keypressfcn',@keypress,...
    'KeyReleaseFcn',@keyrelease);
    
    %Parameters
    n_obj=4;    %Number of objects
    dr=0.2;
    how_many=9;
    max_dist=15;
    min_dist=2;
    %% Start of Code

    %Mass distribution
    mass_prob=[0,0,0,1,10,2,0,0,0,0,0,1,4,5,3,1,0];
    pol_width=0.4;

    world=World(n_obj,max_dist,min_dist,how_many,mass_prob,pol_width,dr,dt);

    world=world.Add_Tank(1,pi/2);
    world.Plot()
    axis equal;
    axis off;
    
    %Define update interval (this can be adjust to faster computers)
    dt=0.05;
    
    while true
        world=world.Evolve_System();
        world.Plot() %Repeatedly update plots
        pause(dt)
    end

end


function keypress(varargin)
    global world
    key=get(gcbf,'CurrentKey');
    if any(strcmp(world.key,key))==0
        world.key={world.key{:} key}; %This way multiple keys can be registered at the same time -> multiplayer
    end
end

 function keyrelease(varargin)
     global world
     key=get(gcbf,'CurrentKey');
     if any(strcmp(world.key,key))
        world.key={world.key{find(1-strcmp(world.key,key))}};
    end
 end