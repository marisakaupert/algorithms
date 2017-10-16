import unittest
import math


class Algorithm:
    def factorializa_a_number(self, input_num):
        if input_num == 0:
            return 1
        else:
            return input_num * self.factorializa_a_number(input_num - 1)

        # another way of doing this with a library:
        # return math.factorial(input_num)


class TestPath(unittest.TestCase):
    def test_factorialize_5(self):
        practice = Algorithm()
        self.assertEqual(120, practice.factorializa_a_number(5))

    def test_factorializa_10(self):
        practice = Algorithm()
        self.assertEqual(3628800, practice.factorializa_a_number(10))

    def test_factorializa_20(self):
        practice = Algorithm()
        self.assertEqual(
            2432902008176640000,
            practice.factorializa_a_number(20)
            )

    def test_factorializa_0(self):
        practice = Algorithm()
        self.assertEqual(1, practice.factorializa_a_number(0))

if __name__ == '__main__':
    unittest.main()