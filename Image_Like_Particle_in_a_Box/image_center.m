function fn = image_center( n,B,r )
% Rescale Image to size nxn and cutting off the border by 0.5-r
    x=linspace(0,1,n);
    y=linspace(0,1,n);
    [X,Y]=meshgrid(x,y);

    sB=size(B);
    rx=r;
    ry=r*sB(1)/sB(2);
    x_in=abs(X-0.5)<rx;
    y_in=abs(Y-0.5)<ry;

    [indy indx]=find(x_in);
    dx=max(indx)-min(indx);
    [indy2 indx2]=find(y_in);
    dy=max(indy2)-min(indy2);

    fn=zeros(size(X));
    B=B/max(B(:));
    B=1-B;
    B(end:-1:1,:)=B;
    b=imresize(B,[dy,dx]);
    fn(min(indy2):max(indy2)-1,min(indx):max(indx)-1)=b;
end

