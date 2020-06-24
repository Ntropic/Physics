function [ v ] = vector_rotator( v,phi,x,y )
%VECTOR_ROTATOR rotates 2D vectors
len=size(v,2);
for i=1:len
    v(:,i)=[cos(phi),-sin(phi);sin(phi),cos(phi)]*v(:,i);
end
if nargin==4
    v(1,:)=v(1,:)+x;
    v(2,:)=v(2,:)+y;
end
end

