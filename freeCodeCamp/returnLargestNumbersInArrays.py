import unittest


class Algorithm:
    def find_largest_of_four_arrays(self, input_array):
        result_array = []
        for indiviual_array in input_array:
            result_array.append(max(indiviual_array))

        return result_array


class TestPath(unittest.TestCase):
    def test_find_max_of_smaller_numbers(self):
        practice = Algorithm()
        self.assertEqual(
            [27, 5, 39, 1001],
            practice.find_largest_of_four_arrays(
                [[13, 27, 18, 26],
                 [4, 5, 1, 3],
                 [32, 35, 37, 39],
                 [1000, 1001, 857, 1]]))

    def test_find_max_of_large_numbers(self):
        practice = Algorithm()
        self.assertEqual(
            [9, 35, 97, 1000000],
            practice.find_largest_of_four_arrays(
                [[4, 9, 1, 3],
                 [13, 35, 18, 26],
                 [32, 35, 97, 39],
                 [1000000, 1001, 857, 1]]))

    def test_find_max_of_same_numbers(self):
        practice = Algorithm()
        self.assertEqual(
            [2, 2, 2, 2],
            practice.find_largest_of_four_arrays(
                [[2, 2, 2, 2],
                 [2, 2, 2, 2],
                 [2, 2, 2, 2],
                 [2, 2, 2, 2]]))

    def test_find_max_of_all_zeroes(self):
        practice = Algorithm()
        self.assertEqual(
            [0, 0, 0, 0],
            practice.find_largest_of_four_arrays(
                [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]))

    def test_find_max_of_arrays_with_negatives(self):
        practice = Algorithm()
        self.assertEqual(
            [5, -136, -3, 27],
            practice.find_largest_of_four_arrays(
                [[1, 3, 5, 0],
                 [-549, -136, -287, -300],
                 [-3, -10, -34, -66],
                 [2, 19, 7, 27]]))

    def test_find_max_of_arrays_with_duplicate_max(self):
        practice = Algorithm()
        self.assertEqual(
            [10, -10, 10, 50],
            practice.find_largest_of_four_arrays(
                [[2, 10, 5, 10],
                 [-10, -10, -65, -43],
                 [10, 0, 0, 10],
                 [-49, 49, 50, 50]]))


if __name__ == '__main__':
    unittest.main()
