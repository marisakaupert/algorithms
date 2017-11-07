import numpy as np
import math


class Week1Functions(object):
    def axpy(self, alpha, vector_x, vector_y):
        if len(vector_x) != len(vector_y):
            return 'FAILED'

        if isinstance(alpha, str) or alpha is None:
            return 'FAILED'

        scaled_x = np.multiply(alpha, vector_x)
        y_out = list(np.add(scaled_x, vector_y))
        return y_out

    def axpy_unb(self, alpha, vector_x, vector_y):
        if len(vector_x) != len(vector_y):
            return 'FAILED'

        if alpha is None or isinstance(alpha, str):
            return 'FAILED'

        x_top = []
        vector_x = list(vector_x)
        vector_y = list(vector_y)
        while len(x_top) < len(vector_x):
            for index, val in enumerate(vector_x):
                out_axpy = alpha * val + vector_y[index]
                x_top.append(out_axpy)
            vector_x.remove(val)

        y_out = x_top
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

    def dot_product_unb(self, vector_x, vector_y):
        if len(vector_x) != len(vector_y):
            return 'FAILED'

        x_top = []
        alpha = 0
        vector_x = list(vector_x)
        vector_y = list(vector_y)
        while len(x_top) < len(vector_x):
            for index, val in enumerate(vector_x):
                alpha = val * vector_y[index] + alpha
                x_top.append(alpha)
            vector_x.remove(val)

        alpha_out = alpha
        return alpha_out

    def length(self, vector_x):
        if vector_x is None:
            return 'FAILED'
        
        for item in vector_x:
            if isinstance(item, str):
                return 'FAILED'

        alpha = math.sqrt(self.dotProduct(vector_x, vector_x))
        return round(alpha, 4)

    def scale(self, alpha, vector_x):
        if alpha is None or isinstance(alpha, str):
            return 'FAILED'

        if vector_x is None:
            return 'FAILED'

        for item in vector_x:
            if isinstance(item, str):
                return 'FAILED'

        x_out = list(np.multiply(alpha, vector_x))
        return x_out
