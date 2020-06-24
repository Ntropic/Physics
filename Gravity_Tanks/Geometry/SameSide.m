function res=SameSide(p1,p2,a,b)
    cp1=cross(b-a,p1-a);
    cp2=cross(b-a,p2-a);
    if (cp1'*cp2) >= 0
        res=1;
    else
        res=0;
    end
end