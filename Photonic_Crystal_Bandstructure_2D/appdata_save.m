function [ ] = appdata_save( h, varargin )
%APPDATA_SAVE saves your variables in the appdata of figure h, so that it
%can be accessed by different callback functions without having to pass all
%the variables and parameters all the time, except for this once
%Input:
%   h                       -   figure handle of figure to save the appdata
%   'VariableName',Variable -   Nametag for saving, and the Variable
if mod(nargin,2)==0
    error('Input length must be uneven.')
end
for i=1:(nargin-1)/2
    name_tag=varargin{2*i-1};
    if isstr(name_tag)==0
        error('The Order needs to be str(Variablename) and then type(Variable).')
    end
    variable=varargin{2*i};
    setappdata(h,name_tag,variable);
end
end

