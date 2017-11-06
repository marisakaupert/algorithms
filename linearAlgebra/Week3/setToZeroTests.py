import unittest
from laffFunctions import Week3Functions


class ScaleTests(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
