# function [ x_out ] = laff_scal( alpha, x )
# % x = copy ( alpha , x ) scales vector x by alpha and reassigns it to x
# %   Vector x can be a mixture of column and/or row vectors. In other
# %   words, x can be a nx1 or 1xn array. However, its size must equal n


# % Extract the row and column sizes of x
# [m_x, n_x] = size(x);


# % Make sure alpha is a scalar and x is a vector
# if ~isscalar(alpha)
#     x_out = 'FAILED';
#     return
# end

# if ~isvector(x)
#     x_out = 'FAILED';
#     return
# end

# if (n_x == 1) % x is a column vector
#     for i=1:m_x
#         x(i, 1) = alpha * x(i, 1);
#     end
# else % x is a row vector
#     for i=1:n_x
#         x(1, i) = alpha * x(1, i);
#     end
# end


# % Return the updated x in x_out
# x_out = x;

# return
# end