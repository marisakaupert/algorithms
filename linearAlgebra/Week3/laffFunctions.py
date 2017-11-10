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
            A_left.append(current_vector)
            pivot = pivot + 1

        zero_matrix = A_left
        return zero_matrix

    def set_to_diagonal_unb(self, matrix_A, vector_x):
        if matrix_A is None or vector_x is None:
            return 'FAILED'

        if len(matrix_A) == 0 or len(vector_x) == 0:
            return []

        out_matrix = []
        matrix_A = matrix_A.tolist()
        pivot = 0
        while len(out_matrix) < len(matrix_A):
            for inner_vector_index, inner_vector in enumerate(matrix_A):
                current_vector = []
                for index, val in enumerate(inner_vector):
                    if index == pivot:
                        current_vector.append(vector_x[index])
                    else:
                        current_vector.append(0)
                out_matrix.append(current_vector)
                pivot = pivot + 1

        return out_matrix

    def set_to_upper_triangle_matrix(self, matrix_A):
        if matrix_A is None:
            return 'FAILED'

        if len(matrix_A) == 0:
            return []

        out_matrix = []
        matrix_A = matrix_A.tolist()
        pivot = 0
        while len(out_matrix) < len(matrix_A):
            for inner_vector_index, inner_vector in enumerate(matrix_A):
                current_vector = []
                for index, val in enumerate(inner_vector):
                    if index < pivot:
                        current_vector.append(0)
                    else:
                        current_vector.append(val)
                out_matrix.append(current_vector)
                pivot = pivot + 1

        return out_matrix

    def set_to_strictly_upper_triangle_matrix(self, matrix_A):
        if matrix_A is None:
            return 'FAILED'

        if len(matrix_A) == 0:
            return []

        out_matrix = []
        matrix_A = matrix_A.tolist()
        pivot = 0
        while len(out_matrix) < len(matrix_A):
            for inner_vector_index, inner_vector in enumerate(matrix_A):
                current_vector = []
                for index, val in enumerate(inner_vector):
                    if index <= pivot:
                        current_vector.append(0)
                    else:
                        current_vector.append(val)
                out_matrix.append(current_vector)
                pivot = pivot + 1

        return out_matrix

    def set_to_unit_upper_triangle_matrix(self, matrix_A):
        if matrix_A is None:
            return 'FAILED'

        if len(matrix_A) == 0:
            return []

        out_matrix = []
        matrix_A = matrix_A.tolist()
        pivot = 0
        while len(out_matrix) < len(matrix_A):
            for inner_vector_index, inner_vector in enumerate(matrix_A):
                current_vector = []
                for index, val in enumerate(inner_vector):
                    if index == pivot:
                        current_vector.append(1)
                    elif index < pivot:
                        current_vector.append(0)
                    else:
                        current_vector.append(val)
                out_matrix.append(current_vector)
                pivot = pivot + 1

        return out_matrix

    def set_to_strictly_lower_triangle_matrix(self, matrix_A):
        if matrix_A is None:
            return 'FAILED'

        if len(matrix_A) == 0:
            return []

        out_matrix = []
        matrix_A = matrix_A.tolist()
        pivot = 0
        while len(out_matrix) < len(matrix_A):
            for inner_vector_index, inner_vector in enumerate(matrix_A):
                current_vector = []
                for index, val in enumerate(inner_vector):
                    if index >= pivot:
                        current_vector.append(0)
                    else:
                        current_vector.append(val)
                out_matrix.append(current_vector)
                pivot = pivot + 1

        return out_matrix

    def set_to_unit_lower_triangle_matrix(self, matrix_A):
        if matrix_A is None:
            return 'FAILED'

        if len(matrix_A) == 0:
            return []

        out_matrix = []
        matrix_A = matrix_A.tolist()
        pivot = 0
        while len(out_matrix) < len(matrix_A):
            for inner_vector_index, inner_vector in enumerate(matrix_A):
                current_vector = []
                for index, val in enumerate(inner_vector):
                    if index == pivot:
                        current_vector.append(1)
                    elif index > pivot:
                        current_vector.append(0)
                    else:
                        current_vector.append(val)
                out_matrix.append(current_vector)
                pivot = pivot + 1

        return out_matrix

    def transpose(self, matrix_A, matrix_B):
        if matrix_A is None or matrix_B is None:
            return 'FAILED'

        if len(matrix_A) == 0 or len(matrix_B) == 0:
            return []

        A = matrix_A.tolist()
        B_out_matrix = []
        pivot = 0
        while len(B_out_matrix) < len(matrix_B):
            B_top = []
            for index, inner_vector in enumerate(A):
                B_top.append(inner_vector[pivot])
            pivot = pivot + 1
            B_out_matrix.append(B_top)

        return B_out_matrix

    def set_symmatric_matrix(self):
        pass

    def scale_marix(self, matrix_A, alpha):
        if matrix_A is None or alpha is None:
            return 'FAILED'

        if len(matrix_A) == 0:
            return []

        A = matrix_A.tolist()
        out_matrix = []
        for inner_vector_index, inner_vector in enumerate(A):
            current_vector = []
            for index, value in enumerate(inner_vector):
                scaled_value = value * alpha
                current_vector.append(scaled_value)
            out_matrix.append(current_vector)

        return out_matrix
