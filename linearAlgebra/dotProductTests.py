import unittest
import numpy as np
from laffFunctions import Week1Functions


class TestingClass(unittest.TestCase):
    def setUp(self):
        self.vector_x = [1, 2, 3]
        self.vector_y = [0, -1, -2]
        self.vector_z = [4, 3, 2, 1]

    def test_column_with_column_vector_dot_product(self):
        practice = Week1Functions()
        self.assertEqual(-8, practice.dotProduct(self.vector_x, self.vector_y))

    def test_column_with_row_vector_dot_product(self):
        practice = Week1Functions()
        self.assertEqual(-8, practice.dotProduct(self.vector_x, np.transpose(self.vector_y)))

    def test_row_with_column_vector_dot_product(self):
        practice = Week1Functions()
        self.assertEqual(-8, practice.dotProduct(np.transpose(self.vector_x), self.vector_y))

    def test_row_with_row_vector_dot_product(self):
        practice = Week1Functions()
        self.assertEqual(-8, practice.dotProduct(np.transpose(self.vector_x), np.transpose(self.vector_y)))

    def test_column_with_column_vector_wrong_size_dot_product(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.dotProduct(self.vector_x, self.vector_z))

    def test_column_with_row_vector_dot_wrong_size_product(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.dotProduct(self.vector_x, np.transpose(self.vector_z)))

    def test_row_with_column_vector_wrong_size_dot_product(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.dotProduct(np.transpose(self.vector_x), self.vector_z))

    def test_row_with_row_vector_wrong_size_dot_product(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.dotProduct(np.transpose(self.vector_x), np.transpose(self.vector_z)))

    def test_empty_vectors_dot_product(self):
        practice = Week1Functions()
        self.assertEqual(0, practice.dotProduct([], []))

    def test_empty_vector_x_dot_product(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.dotProduct([], self.vector_y))

    def test_empty_vector_y_dot_product(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.dotProduct(self.vector_x, []))

    def test_zero_vector_dot_product(self):
        practice = Week1Functions()
        self.assertEqual(0, practice.dotProduct([0, 0, 0], [0, 0, 0]))


if __name__ == '__main__':
    unittest.main()
