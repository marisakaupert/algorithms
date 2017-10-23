import unittest


class Algorithm:
    def sum_all_numbers(self, input_array):
        result = 0
        sorted_array = sorted(input_array)
        if sorted_array == []:
            return 0
        elif sorted_array[0] == sorted_array[1]:
            return sorted_array[0]
        else:
            for i in range(sorted_array[0], (sorted_array[1]+1)):
                result = result + i

        return result


class TestPath(unittest.TestCase):
    def test_sorted_int_array_1(self):
        practice = Algorithm()
        self.assertEqual(10, practice.sum_all_numbers([1, 4]))

    def test_sorted_int_array_2(self):
        practice = Algorithm()
        self.assertEqual(45, practice.sum_all_numbers([5, 10]))

    def test_unsorted_int_array_1(self):
        practice = Algorithm()
        self.assertEqual(10, practice.sum_all_numbers([4, 1]))

    def test_unsorted_int_array_2(self):
        practice = Algorithm()
        self.assertEqual(45, practice.sum_all_numbers([10, 5]))

    def test_zero_array(self):
        practice = Algorithm()
        self.assertEqual(0, practice.sum_all_numbers([0, 0]))

    def test_same_number_array(self):
        practice = Algorithm()
        self.assertEqual(1, practice.sum_all_numbers([1, 1]))

    def test_empty_array(self):
        practice = Algorithm()
        self.assertEqual(0, practice.sum_all_numbers([]))

if __name__ == '__main__':
    unittest.main()
