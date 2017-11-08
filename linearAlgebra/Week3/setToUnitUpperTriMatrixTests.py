import unittest
import numpy as np
from laffFunctions import Week3Functions


class SetToUnitUpperTriMatrixUnblockedTests(unittest.TestCase):
    def setUp(self):
        self.matrix_A = np.matrix('1 2 3; -1 -2 -3; 3 2 1')
        self.zero_matrix = np.matrix('0 0 0; 0 0 0; 0 0 0')

    def test_set_to_unit_upper_tri_matrix_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[1, 2, 3], [0, 1, -3], [0, 0, 1]],
            practice.set_to_unit_upper_triangle_matrix(self.matrix_A))

    def test_zero_matrix_set_to_unit_upper_tri_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            practice.set_to_unit_upper_triangle_matrix(self.zero_matrix))

    def test_empty_matrix_set_to_unit_upper_tri_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [], practice.set_to_unit_upper_triangle_matrix([]))

    def test_illegal_matrix_set_to_unit_upper_tri_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            'FAILED', practice.set_to_unit_upper_triangle_matrix(None))


if __name__ == '__main__':
    unittest.main()
