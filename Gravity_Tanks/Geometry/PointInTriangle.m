function res=PointInTriangle(p,a,b,c)
    if SameSide(p,a,b,c) && SameSide(p,b,a,c) && SameSide(p,c, a,b)
        res=1;
    else 
        res=0;
    end
end