function [ varargout ] = appdata_load( h, varargin )
%APPDATA_LOAD loads your variables from the appdata of figure h
%Input:
%   h                       -   figure handle of figure from which to load
%   'VariableName'          -   Nametag for loading
for i=1:(nargin-1)
    name_tag=varargin{i};
    if isstr(name_tag)==0
        error('Nametags need to be strings.')
    end
    varargout{i}=getappdata(h,name_tag);
end