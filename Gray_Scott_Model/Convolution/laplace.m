function [ ddA ] = laplace( A,dx )
%Laplace operator (finite difference) of matrix with repeating boundary
%conditions
    %Use 9 point stencil for smooth fields
    ddA=0.5*(circshift(A,1,2)+circshift(A,-1,2)+circshift(A,1,1)+circshift(A,-1,1)) ...
       +0.25*(circshift(A,[1 1])+circshift(A,[-1 1])+circshift(A,[1 -1])+circshift(A,[-1 -1]))-3*A;
    ddA=ddA/dx^2;
end

