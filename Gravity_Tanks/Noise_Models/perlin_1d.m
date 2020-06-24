function [ perlin ] = perlin_1d( s_max )
b=3;    %exp(1);
s0=4;
sizle=2^(s_max);
amp_fun=@(s) b^s/factorial(s)*exp(-b);%exp(-(s-s0).^2/b^2);%(1/b)^(s); %Distribution of frequencies
interp=@(x) 6*x.^5-15*x.^4+10*x.^3; %Smoothstep (Ken Perlin's suggestion -> 1st and 2nd derivatives are zero at x=0,1
interp1d=@(x,a,b) ((1-interp(x)).*a+interp(x).*b);%a+interp(x)*(b-a);

seed=rand(1,sizle);

p_x=0:(sizle-1);
perlin=zeros(1,sizle);

for s=0:s_max
    %Determine interpolation indexes and fractions
    inter_size=2^(s_max-s);
    index_x=(floor(p_x/inter_size))*inter_size+1;
    index_x2=mod((floor(p_x/inter_size)+1)*inter_size,sizle)+1;

    frac_x=mod(p_x/inter_size,1);
    
    %Interpolate between the random points
    perlin=perlin+amp_fun(s)*interp1d(frac_x,seed(index_x),seed(index_x2));
end
perlin=perlin-mean(perlin);
end

