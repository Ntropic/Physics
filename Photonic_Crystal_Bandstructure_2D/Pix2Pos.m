function [ pos inside ] = Pix2Pos( fig , axe , pix , borders)
%Pix2Pos translates Pixel Positions (pix or mouse position) into a axis
%position
%% Input:
%   fig         -   figure of position that shall be determined
%   axe         -   axes handle in the figure
%   pix         -   (optional) pixel position
% If pix is not an Input, pix will be determined via mouse position
%% Output:
%   pos         - position corresponding to the pix Information
%   inside      - 1=pos is in axes handle, 0=else

if nargin==2
    %Determine Mouse Position
    mpos=get(fig,'CurrentPoint'); %Get current mouse Position on screen (starting at 1,1)
    mx=mpos(1); %x-position
    my=mpos(2); %y-position   
elseif nargin>=3
    mx=pix(:,1);
    my=pix(:,2);
end
    fpos=get(fig,'position');  %Get figures Position on screen
    if any(ismember(axe,findobj(fig,'Type','axes')))==0
        error('Axes Object not found')
    end
    plotPos=get(axe,'position'); % get the position of the plots axes
    sizes(1:2)=get(axe,'xlim');
    sizes(3:4)=get(axe,'ylim');
    Mx=(mx-fpos(3)*plotPos(1))/(fpos(3)*plotPos(3))*(sizes(2)-sizes(1))+sizes(1);
    My=(my-fpos(4)*plotPos(2))/(fpos(4)*plotPos(4))*(sizes(4)-sizes(3))+sizes(3);
    pos=[Mx,My];
    if nargin~=4
        if (pos(1)>sizes(1)) && (pos(1)<sizes(2)) && (pos(2)>sizes(3)) && (pos(2)<sizes(4))
            inside=1;
        else
            inside=0;
        end
    else 
        if (pos(1)>borders(1,1)) && (pos(1)<borders(2,1)) && (pos(2)>borders(1,2)) && (pos(2)<borders(2,2))
            inside=1;
        else
            inside=0;
        end
    end
end