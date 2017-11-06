import unittest
import numpy as np
from laffFunctions import Week1Functions


class CopyTests(unittest.TestCase):
    def setUp(self):
        self.vector_x = [1, 2, 3]
        self.vector_y = [0, -1, -2]
        self.vector_z = [4, 3, 2, 1]

    def test_column_column_copy(self):
        practice = Week1Functions()
        self.assertEqual(
            [1, 2, 3], practice.copy(self.vector_x, self.vector_y))

    def test_column_row_copy(self):
        practice = Week1Functions()
        self.assertEqual(
            [1, 2, 3],
            practice.copy(self.vector_x, np.transpose(self.vector_y)))

    def test_row_column_copy(self):
        practice = Week1Functions()
        self.assertEqual(
            [1, 2, 3],
            practice.copy(np.transpose(self.vector_x), self.vector_y))

    def test_row_row_copy(self):
        practice = Week1Functions()
        self.assertEqual(
            [1, 2, 3],
            practice.copy(
                np.transpose(self.vector_x), np.transpose(self.vector_y)))

    def test_column_column_wrong_size_copy(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.copy(self.vector_x, self.vector_z))

    def test_column_row_wrong_size_copy(self):
        practice = Week1Functions()
        self.assertEqual(
            'FAILED',
            practice.copy(self.vector_x, np.transpose(self.vector_z)))

    def test_row_column_wrong_size_copy(self):
        practice = Week1Functions()
        self.assertEqual(
            'FAILED',
            practice.copy(np.transpose(self.vector_x), self.vector_z))

    def test_row_row_wrong_size_copy(self):
        practice = Week1Functions()
        self.assertEqual(
            'FAILED',
            practice.copy(
                np.transpose(self.vector_x), np.transpose(self.vector_z)))

    def test_empty_vector_x_copy(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.copy([], self.vector_y))

    def test_empty_vector_y_copy(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.copy(self.vector_x, []))

    def test_both_empty_vectors_copy(self):
        practice = Week1Functions()
        self.assertEqual([], practice.copy([], []))

    def test_both_zero_vectors_copy(self):
        practice = Week1Functions()
        self.assertEqual([0, 0, 0], practice.copy([0, 0, 0], [0, 0, 0]))

    def test_false_vector_x_copy(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.copy(None, self.vector_y))

    def test_false_vector_y_copy(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.copy(self.vector_x, None))


if __name__ == '__main__':
    unittest.main()
