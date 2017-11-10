import unittest
import numpy as np
from laffFunctions import Week3Functions


class TransposeTests(unittest.TestCase):
    def setUp(self):
        self.matrix_A = np.matrix('1 2 3 4; -1 -5 -10 -20; 100 90 80 3')
        self.matrix_B = np.matrix('10 20 30; 0 -100 -500; 50 50 50; 1 1 1')
        self.zero_matrix_A = np.matrix('0 0 0 0; 0 0 0 0; 0 0 0 0')
        self.zero_matrix_B = np.matrix('0 0 0; 0 0 0; 0 0 0; 0 0 0')

    def test_transpose_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[1, -1, 100], [2, -5, 90], [3, -10, 80], [4, -20, 3]],
            practice.transpose(self.matrix_A, self.matrix_B))

    def test_zero_matrix_A_transpose_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            practice.transpose(self.zero_matrix_A, self.matrix_B))

    def test_zero_matrix_B_transpose_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[1, -1, 100], [2, -5, 90], [3, -10, 80], [4, -20, 3]],
            practice.transpose(self.matrix_A, self.zero_matrix_B))

    def test_empty_matrix_A_transpose_unb(self):
        practice = Week3Functions()
        self.assertEqual([], practice.transpose([], self.matrix_B))

    def test_empty_matrix_B_transpose_unb(self):
        practice = Week3Functions()
        self.assertEqual([], practice.transpose(self.matrix_A, []))

    def test_illegal_matrix_A_transpose_unb(self):
        practice = Week3Functions()
        self.assertEqual('FAILED', practice.transpose(None, self.matrix_B))

    def test_illegal_matrix_B_transpose_unb(self):
        practice = Week3Functions()
        self.assertEqual('FAILED', practice.transpose(self.matrix_A, None))


if __name__ == '__main__':
    unittest.main()
