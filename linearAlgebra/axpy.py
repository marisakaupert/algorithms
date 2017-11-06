import unittest
import numpy as np


class LAFF(object):
    def axpy(self, vector_x, vector_y, alpha):
        if len(vector_x) != len(vector_y):
            return 'FAILED'

        if isinstance(alpha, str) or alpha is None:
            return 'FAILED'

        scaled_x = np.multiply(alpha, vector_x)
        y_out = list(np.add(scaled_x, vector_y))
        return y_out


class TestingClass(unittest.TestCase):
    def setUp(self):
        self.vector_x = [1, 2, 3]
        self.vector_y = [0, -1, -2]
        self.alpha = -2

    def test_column_column_axpy(self):
        practice = LAFF()
        self.assertEqual(
            [-2, -5, -8],
            practice.axpy(self.vector_x, self.vector_y, self.alpha))

    def test_column_row_axpy(self):
        practice = LAFF()
        self.assertEqual(
            [-2, -5, -8],
            practice.axpy(
                self.vector_x, np.transpose(self.vector_y), self.alpha))

    def test_row_column_axpy(self):
        practice = LAFF()
        self.assertEqual(
            [-2, -5, -8],
            practice.axpy(
                np.transpose(self.vector_x), self.vector_y, self.alpha))

    def test_row_row_axpy(self):
        practice = LAFF()
        self.assertEqual(
            [-2, -5, -8],
            practice.axpy(
                np.transpose(
                    self.vector_x), np.transpose(self.vector_y), self.alpha))

    def test_vector_x_wrong_size_axpy(self):
        practice = LAFF()
        self.assertEqual(
            'FAILED', practice.axpy([-1], self.vector_y, self.alpha))

    def test_vector_y_wrong_size_axpy(self):
        practice = LAFF()
        self.assertEqual(
            'FAILED', practice.axpy(self.vector_x, [4, 3, 2, 1], self.alpha))

    def test_vector_x_zeroes_axpy(self):
        practice = LAFF()
        self.assertEqual(
            [0, -1, -2], practice.axpy([0, 0, 0], self.vector_y, self.alpha))

    def test_vector_y_zeroes_axpy(self):
        practice = LAFF()
        self.assertEqual(
            [-2, -4, -6], practice.axpy(self.vector_x, [0, 0, 0], self.alpha))

    def test_all_vectors_zeroes_axpy(self):
        practice = LAFF()
        self.assertEqual(
            [0, 0, 0], practice.axpy([0, 0, 0], [0, 0, 0], self.alpha))

    def test_vector_x_empty_and_wrong_size_axpy(self):
        practice = LAFF()
        self.assertEqual(
            'FAILED', practice.axpy([], self.vector_y, self.alpha))

    def test_vector_y_empty_and_wrong_size_axpy(self):
        practice = LAFF()
        self.assertEqual(
            'FAILED', practice.axpy(self.vector_x, [], self.alpha))

    def test_empty_vectors_axpy(self):
        practice = LAFF()
        self.assertEqual([], practice.axpy([], [], self.alpha))

    def test_zero_alpha_axpy(self):
        practice = LAFF()
        self.assertEqual(
            [0, -1, -2], practice.axpy(self.vector_x, self.vector_y, 0))

    def test_false_alpha_axpy(self):
        practice = LAFF()
        self.assertEqual(
            'FAILED', practice.axpy(self.vector_x, self.vector_y, None))

if __name__ == '__main__':
    unittest.main()
