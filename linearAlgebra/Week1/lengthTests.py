import unittest
import numpy as np
from laffFunctions import Week1Functions


class TestingClass(unittest.TestCase):
    def setUp(self):
        self.vector_x = [1, 2, 3]

    def test_column_vector(self):
        practice = Week1Functions()
        self.assertEqual(3.7417, practice.length(self.vector_x))

    def test_row_vector(self):
        practice = Week1Functions()
        self.assertEqual(3.7417, practice.length(np.transpose(self.vector_x)))

    def test_row_vector(self):
        practice = Week1Functions()
        self.assertEqual(3.7417, practice.length(np.transpose(self.vector_x)))

    def test_empty_vector(self):
        practice = Week1Functions()
        self.assertEqual(0, practice.length([]))

    def test_zero_vector(self):
        practice = Week1Functions()
        self.assertEqual(0, practice.length([0, 0, 0]))

    def test_illegal_vector(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.length(None))


if __name__ == '__main__':
    unittest.main()
