import numpy as np


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
