# function [ alpha ] = laff_norm2( x )
# % alpha = length(x) gets the length of a vector
# %   Since the length of a vector is the sqare root of the dot
# %   product with itself, the function calls the dot
# %   product function of itself. To deal with illegal entries
# %   it checks if x is a vector before proceding

# % Checking if x is a vector
# if ~isvector(x)
#     alpha = 'FAILED';
#     return
# end
    
# alpha = sqrt( laff_dot(x, x) );

# end