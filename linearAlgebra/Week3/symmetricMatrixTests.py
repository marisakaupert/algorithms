import unittest
import numpy as np
from laffFunctions import Week3Functions


class SymmetricMatrixTests(unittest.TestCase):
    def setUp(self):
        self.matrix_A = np.matrix('2 -2 -1; 5 1 -3; -10 -20 0')
        self.matrix_B = np.matrix('2 5 -10; 1 1 20; -1 -3 -1')
        self.zero_matrix = np.matrix('0 0 0; 0 0 0; 0 0 0')

    def test_symmetric_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual()

    # def test_zero_matrix_A_transpose_unb(self):
    #     practice = Week3Functions()
    #     self.assertEqual(
    #         [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    #         practice.transpose(self.zero_matrix_A, self.matrix_B))

    # def test_zero_matrix_B_transpose_unb(self):
    #     practice = Week3Functions()
    #     self.assertEqual(
    #         [[1, -1, 100], [2, -5, 90], [3, -10, 80], [4, -20, 3]],
    #         practice.transpose(self.matrix_A, self.zero_matrix_B))

    # def test_empty_matrix_A_transpose_unb(self):
    #     practice = Week3Functions()
    #     self.assertEqual([], practice.transpose([], self.matrix_B))

    # def test_empty_matrix_B_transpose_unb(self):
    #     practice = Week3Functions()
    #     self.assertEqual([], practice.transpose(self.matrix_A, []))

    # def test_illegal_matrix_A_transpose_unb(self):
    #     practice = Week3Functions()
    #     self.assertEqual('FAILED', practice.transpose(None, self.matrix_B))

    # def test_illegal_matrix_B_transpose_unb(self):
    #     practice = Week3Functions()
    #     self.assertEqual('FAILED', practice.transpose(self.matrix_A, None))


if __name__ == '__main__':
    unittest.main()
