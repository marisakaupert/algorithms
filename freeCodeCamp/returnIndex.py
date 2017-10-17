import unittest


class Algorithm:
    def return_correct_index(self, input_array, input_num):
        if input_num is None:
            return None
        else:
            input_array.append(input_num)
            sorted_array = sorted(input_array)
            for index, value in enumerate(sorted_array):
                if input_num == value:
                    return index


class TestPath(unittest.TestCase):
    def test_sorted_int_array_1(self):
        practice = Algorithm()
        self.assertEqual(
            3, practice.return_correct_index([10, 20, 30, 40, 50], 35))

    def test_sorted_int_array_2(self):
        practice = Algorithm()
        self.assertEqual(1, practice.return_correct_index([40, 60], 50))

    def test_sorted_int_array_3(self):
        practice = Algorithm()
        self.assertEqual(3, practice.return_correct_index([2, 5, 10], 15))

    def test_value_already_in_array(self):
        practice = Algorithm()
        self.assertEqual(
            2, practice.return_correct_index([10, 20, 30, 40, 50], 30))

    def test_unsorted_int_array_1(self):
        practice = Algorithm()
        self.assertEqual(0, practice.return_correct_index([3, 10, 5], 3))

    def test_unsorted_int_array_2(self):
        practice = Algorithm()
        self.assertEqual(2, practice.return_correct_index([5, 3, 20, 3], 5))

    def test_unsorted_int_array_3(self):
        practice = Algorithm()
        self.assertEqual(2, practice.return_correct_index([2, 20, 10], 19))

    def test_adding_to_an_empty_array_(self):
        practice = Algorithm()
        self.assertEqual(0, practice.return_correct_index([], 5))

    def test_empty_array_with_no_argument(self):
        practice = Algorithm()
        self.assertEqual(None, practice.return_correct_index([], None))

if __name__ == '__main__':
    unittest.main()
