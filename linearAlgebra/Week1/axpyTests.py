import unittest
import numpy as np
from laffFunctions import Week1Functions


class AxpyTests(unittest.TestCase):
    def setUp(self):
        self.vector_x = [1, 2, 3]
        self.vector_y = [0, -1, -2]
        self.alpha = -2

    def test_column_column_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            [-2, -5, -8],
            practice.axpy( self.alpha, self.vector_x, self.vector_y))

    def test_column_row_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            [-2, -5, -8],
            practice.axpy(
                 self.alpha, self.vector_x, np.transpose(self.vector_y)))

    def test_row_column_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            [-2, -5, -8],
            practice.axpy(
                 self.alpha, np.transpose(self.vector_x), self.vector_y))

    def test_row_row_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            [-2, -5, -8],
            practice.axpy(
                self.alpha, np.transpose(
                    self.vector_x), np.transpose(self.vector_y)))

    def test_vector_x_wrong_size_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            'FAILED', practice.axpy(self.alpha, [-1], self.vector_y))

    def test_vector_y_wrong_size_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            'FAILED', practice.axpy(self.alpha, self.vector_x, [4, 3, 2, 1]))

    def test_vector_x_zeroes_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            [0, -1, -2], practice.axpy(self.alpha, [0, 0, 0], self.vector_y))

    def test_vector_y_zeroes_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            [-2, -4, -6], practice.axpy(self.alpha, self.vector_x, [0, 0, 0]))

    def test_all_vectors_zeroes_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            [0, 0, 0], practice.axpy(self.alpha, [0, 0, 0], [0, 0, 0]))

    def test_vector_x_empty_and_wrong_size_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            'FAILED', practice.axpy(self.alpha, [], self.vector_y))

    def test_vector_y_empty_and_wrong_size_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            'FAILED', practice.axpy(self.alpha, self.vector_x, []))

    def test_empty_vectors_axpy(self):
        practice = Week1Functions()
        self.assertEqual([], practice.axpy(self.alpha, [], []))

    def test_zero_alpha_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            [0, -1, -2], practice.axpy(0, self.vector_x, self.vector_y))

    def test_false_alpha_axpy(self):
        practice = Week1Functions()
        self.assertEqual(
            'FAILED', practice.axpy(None, self.vector_x, self.vector_y))

if __name__ == '__main__':
    unittest.main()
