import numpy as np
import math


class Week1Functions(object):
    def axpy(self, vector_x, vector_y, alpha):
        if len(vector_x) != len(vector_y):
            return 'FAILED'

        if isinstance(alpha, str) or alpha is None:
            return 'FAILED'

        scaled_x = np.multiply(alpha, vector_x)
        y_out = list(np.add(scaled_x, vector_y))
        return y_out

    def copy(self, vector_x, vector_y):
        if vector_x is None or vector_y is None:
            return 'FAILED'

        if len(vector_x) != len(vector_y):
            return 'FAILED'

        y_out = list(vector_x)
        return y_out

    def dotProduct(self, vector_x, vector_y):
        if len(vector_x) != len(vector_y):
            return 'FAILED'

        alpha = 0
        multiplied_vectors = np.multiply(vector_x, vector_y)
        alpha = int(np.sum(multiplied_vectors) + alpha)
        return alpha

    def length(self, vector_x):
        if vector_x is None or isinstance(vector_x, str):
            return 'FAILED'

        alpha = math.sqrt(self.dotProduct(vector_x, vector_x))
        return round(alpha, 4)




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