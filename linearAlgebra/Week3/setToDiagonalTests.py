import unittest
import numpy as np
from laffFunctions import Week3Functions


class SetToDiagonalUnblockedTests(unittest.TestCase):
    def setUp(self):
        self.matrix_A = np.matrix('1 2 3; 0 -1 -2; 3 2 1')
        self.zero_matrix = np.matrix('0 0 0; 0 0 0; 0 0 0')
        self.vector_x = [1, -2, 10]

    def test_set_to_diagonal_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[1, 0, 0], [0, -2, 0], [0, 0, 10]],
            practice.set_to_diagonal_unb(self.matrix_A, self.vector_x))

    def test_zero_vector_x_set_to_diagonal_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            practice.set_to_diagonal_unb(self.matrix_A, [0, 0, 0]))

    def test_zero_matrix_set_to_diagonal_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[1, 0, 0], [0, -2, 0], [0, 0, 10]],
            practice.set_to_diagonal_unb(self.zero_matrix, self.vector_x))

    def test_empty_vector_x_set_to_diagonal_unb(self):
        practice = Week3Functions()
        self.assertEqual([], practice.set_to_diagonal_unb(self.matrix_A, []))

    def test_empty_matrix_set_to_diagonal_unb(self):
        practice = Week3Functions()
        self.assertEqual([], practice.set_to_diagonal_unb([], self.vector_x))

    def test_illegal_vector_x_set_to_diagonal_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            'FAILED', practice.set_to_diagonal_unb(self.matrix_A, None))

    def test_illegal_matrix_set_to_diagonal_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            'FAILED', practice.set_to_diagonal_unb(None, self.vector_x))


if __name__ == '__main__':
    unittest.main()
