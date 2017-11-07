import unittest
import numpy as np
from laffFunctions import Week3Functions


class SetToZeroTests(unittest.TestCase):
    def setUp(self):
        self.vector_x = [1, 2, 3]

    def test_set_to_zero_function(self):
        practice = Week3Functions()
        self.assertEqual([0, 0, 0], practice.setToZero(self.vector_x))

    def test_already_zero_vector_set_to_zero_function(self):
        practice = Week3Functions()
        self.assertEqual([0, 0, 0, 0], practice.setToZero([0, 0, 0, 0]))

    def test_empty_vector_set_to_zero_function(self):
        practice = Week3Functions()
        self.assertEqual([], practice.setToZero([]))

    def test_illegal_vector_set_to_zero_function(self):
        practice = Week3Functions()
        self.assertEqual('FAILED', practice.setToZero(None))

    def test_string_vector_set_to_zero_function(self):
        practice = Week3Functions()
        self.assertEqual('FAILED', practice.setToZero(['a', 'b', 'c']))


class SetToZeroUnblockedTests(unittest.TestCase):
    def setUp(self):
        self.matrix_A = np.matrix('1 2 3; 0 -1 -2')
        self.zero_matrix = np.matrix('0 0; 0 0')

    def test_set_to_zero_function_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[0, 0, 0], [0, 0, 0]], practice.set_to_zero_unb(self.matrix_A))

    def test_already_zero_vector_set_to_zero_function_unb(self):
        practice = Week3Functions()
        self.assertEqual(
            [[0, 0], [0, 0]], practice.set_to_zero_unb(self.zero_matrix))

    def test_empty_vector_set_to_zero_function_unb(self):
        practice = Week3Functions()
        self.assertEqual([], practice.set_to_zero_unb([]))

    def test_illegal_vector_set_to_zero_function_unb(self):
        practice = Week3Functions()
        self.assertEqual('FAILED', practice.set_to_zero_unb(None))


if __name__ == '__main__':
    unittest.main()
