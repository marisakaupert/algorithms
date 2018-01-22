import unittest
import numpy as np
from laffFunctions import Week3Functions


class SymmetricMatrixTests(unittest.TestCase):
    def setUp(self):
        self.matrix_A = np.matrix('2 -2 -1; 5 1 -3; -10 -20 -1')
        self.matrix_B = np.matrix('2 5 -10; 1 1 20; -1 -3 -1')
        self.diagonal_matric = np.matrix('1 0 0; 0 1 0; 0 0 1')
        self.zero_matrix = np.matrix('0 0 0; 0 0 0; 0 0 0')

    def test_upper_tri_symmetric_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[2, -2, -1], [-2, 1, -3], [-1, -3, -1]],
            practice.set_symmetric_matrix(self.matrix_A))

    def test_lower_tri_symmetric_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[2, 1, -1], [1, 1, -3], [-1, -3, -1]],
            practice.set_symmetric_matrix(self.matrix_B))

    def test_diagonal_symmetric_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            practice.set_symmetric_matrix(self.diagonal_matric))

    def test_zero_matrix_symmetric_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            practice.set_symmetric_matrix(self.zero_matrix))

    def test_empty_matrix_symmetric_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual([], practice.set_symmetric_matrix([]))

    def test_illegal_matrix_symmetric_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual('FAILED', practice.set_symmetric_matrix(None))


if __name__ == '__main__':
    unittest.main()
