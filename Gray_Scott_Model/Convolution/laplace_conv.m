function [ ddA ] = laplace_conv( A,dx )
%Laplace operator (finite difference) of matrix with repeating boundary
%conditions with convolution matrix
c_mat=[0.25 0.5 0.25; 0.5 -3 0.5; 0.25 0.5 0.25]/dx^2;
len=size(A);

%Padding curcular boundary conditions
A2=padarray(A,[1 1],'circular');
    
ddA2=conv2(A2,c_mat);
ddA=ddA2(3:len(1)+2,3:len(2)+2);

end

