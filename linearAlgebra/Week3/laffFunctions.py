import numpy as np


class Week3Functions(object):
    def setToZero(self, vector_x):
        x_out = []
        if vector_x is None:
            return 'FAILED'

        for item in vector_x:
            if isinstance(item, str):
                return 'FAILED'
            else:
                x_out.append(0)

        return x_out

    def set_to_zero_unb(self, matrix_A):
        if matrix_A is None:
            return 'FAILED'

        A_left = []
        while len(A_left) < len(matrix_A):
            pivot = 0
            current_vector = []
            for item in np.nditer(matrix_A[pivot], order='F'):
                item = 0
                current_vector.append(item)
                np.delete(matrix_A, item)
            A_left.append(current_vector)
            pivot = pivot + 1

        zero_matrix = A_left
        return zero_matrix
