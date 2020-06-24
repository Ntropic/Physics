function  [fftz X Y ]= sinus_decomposition2_image( fn,n )
%2d version
%f is function defined on 0 to 1 (and zero at the edges)
%n is sampling points

x=linspace(0,1,n);
y=linspace(0,1,n);
[X,Y]=meshgrid(x,y);
fz=fn;
fz(1,:)=0;
fz(end,:)=0;
fz(:,1)=0;
fz(:,end)=0;


fz2=fz(end:-1:1,:);
fftz=zeros(size(fz2));
for i=1:size(fftz,1)
    for j=1:size(fftz,2)
        fftz(i,j)=sum(sum(sin((j-1)*pi*X).*sin((i-1)*pi.*Y).*fz2));
    end
end

fftz=fftz(1:n,1:n); %Cut 
fftz=fftz/sqrt(sum(fftz(:).^2)); %Normalize
end