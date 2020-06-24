function [ projection ] = Rand_Dist( n_obj,mass_prob,pol_width,plotting )
%Creates random values of distribution defined in the list mass_prob
if nargin==2
    pol_width=0.2
    plotting='';
elseif nargin==3
    plotting='';
end

mass=1:length(mass_prob);
xq=0:pol_width:length(mass_prob);
pdf=interp1(mass,mass_prob,xq,'pchip');
pdf(pdf<0)=0;
pdf=pdf/sum(pdf);
cdf=cumsum(pdf);
[cdf,mask]=unique(cdf);
xq2=xq(mask);

randomValues=rand(1,n_obj);
projection=interp1(cdf,xq2,randomValues);

if any(strfind(plotting,'mass_dist'))
    a=figure();
    hist(projection,length(mass_prob)*1/pol_width);
    hold on;
    plot(xq,pdf*n_obj);
    title('Mass distribution')
    hold off;
end
projection=projection*pol_width;
end

