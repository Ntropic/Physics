function [ filename ] = filename_generator( name , varargin )
%Creates filenames
filename=name;
for i=1:length(varargin)
    if isstring(varargin{i})
        filename=[filename '_' varargin{i}];
    else
        filename=[filename '_' num2str(varargin{i})];
    end
end
end

