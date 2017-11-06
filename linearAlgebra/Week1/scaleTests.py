import unittest
import numpy as np
from laffFunctions import Week1Functions


class TestingClass(unittest.TestCase):
    def setUp(self):
        self.vector_x = [1, 2, 3]
        self.alpha = -2

    def test_column_vector_scale(self):
        practice = Week1Functions()
        self.assertEqual([-2, -4, -6], practice.scale(self.alpha, self.vector_x))

    def test_row_vector_scale(self):
        practice = Week1Functions()
        self.assertEqual([-2, -4, -6], practice.scale(self.alpha, np.transpose(self.vector_x)))

    def test_illegal_alpha_scale(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.scale('Scale', self.vector_x))

    def test_none_value_alpha_scale(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.scale(None, self.vector_x))

    def test_0_alpha_scale(self):
        practice = Week1Functions()
        self.assertEqual([0, 0, 0], practice.scale(0, self.vector_x))

    def test_illegal_vector_x_scale(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.scale(self.alpha, ['a', 'b', 'c']))

    def test_None_vector_x_scale(self):
        practice = Week1Functions()
        self.assertEqual('FAILED', practice.scale(self.alpha, None))

    def test_empty_vector_x_scale(self):
        practice = Week1Functions()
        self.assertEqual([], practice.scale(self.alpha, []))

    def test_zero_vector_x_scale(self):
        practice = Week1Functions()
        self.assertEqual([0, 0, 0], practice.scale(self.alpha, [0, 0, 0]))


if __name__ == '__main__':
    unittest.main()
