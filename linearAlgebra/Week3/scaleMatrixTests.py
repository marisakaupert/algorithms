import unittest
import numpy as np
from laffFunctions import Week3Functions


class SymmetricMatrixTests(unittest.TestCase):
    def setUp(self):
        self.matrix_A = np.matrix('2 -2 -1; 5 1 -3; -10 -20 0')
        self.alpha = 2
        self.zero_matrix = np.matrix('0 0 0; 0 0 0; 0 0 0')

    def test_scale_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[4, -4, -2], [10, 2, -6], [-20, -40, 0]],
            practice.scale_marix(self.matrix_A, self.alpha))

    def test_zero_matrix_A_scale_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            practice.scale_marix(self.zero_matrix, self.alpha))

    def test_zero_alpha_scale_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            practice.scale_marix(self.matrix_A, 0))

    def test_empty_matrix_A_scale_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual([], practice.scale_marix([], self.alpha))

    def test_illegal_matrix_A_scale_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual('FAILED', practice.scale_marix(None, self.alpha))

    def test_illegal_matrix_B_scale_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual('FAILED', practice.scale_marix(self.matrix_A, None))

if __name__ == '__main__':
    unittest.main()
