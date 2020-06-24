function MouseMovement_2D_TEM_Toggle(obj,dontknow,f,h,kind)
    movement=appdata_load(f,'movement');
    if movement==1
        fprintf('    -> Calculating high Resolution fields (and interpolating)\n')
        movement=0;
        set(f,'WindowButtonMotionFcn','');
        appdata_save(f,'movement',movement);
        if kind=='TE'
            MouseMovement_2D_TEM(1,1,f,h,'TE',1);
        else
            MouseMovement_2D_TEM(1,1,f,h,'TM',1);
        end
        fprintf('    -> Finished HD Calculation\n')
    else
        fprintf('-> Moving again\n')
        movement=1;
        appdata_save(f,'movement',movement);
        if kind=='TE'
            set(f,'WindowButtonMotionFcn',{@MouseMovement_2D_TEM,f,h,'TE'});
        else
            set(f,'WindowButtonMotionFcn',{@MouseMovement_2D_TEM,f,h,'TM'});
        end
    end
end