%eig_scale.m

size_A=21^3;
for i=1:10
    A=rand(size_A);
    t=tic();
    [v,d]=eig(A);
    time(i)=toc(t)
    plot(time(1:i),'o');
    pause(0.01);
end

%Last time: mean(time)=469.6013s