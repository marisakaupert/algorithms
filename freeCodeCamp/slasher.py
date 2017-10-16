import unittest


class Algorithm:
    def slasher(self, input_array, num):
        if input_array == [] or num > len(input_array):
            return []
        elif num < 0:
            return input_array[:num]
        else:
            return input_array[num:]


class TestPath(unittest.TestCase):
    def test_array_of_ints(self):
        practice = Algorithm()
        self.assertEqual([3], practice.slasher([1, 2, 3], 2))

    def test_no_slicing(self):
        practice = Algorithm()
        self.assertEqual([1, 2, 3], practice.slasher([1, 2, 3], 0))

    def test_slicing_off_more_than_length(self):
        practice = Algorithm()
        self.assertEqual([], practice.slasher([1, 2, 3], 9))

    def test_slicing_off_all_elements(self):
        practice = Algorithm()
        self.assertEqual([], practice.slasher([1, 2, 3], 4))

    def test_array_of_strings(self):
        practice = Algorithm()
        self.assertEqual(
            ["fries", "shake"],
            practice.slasher(["burgers", "fries", "shake"], 1))

    def test_mixed_array(self):
        practice = Algorithm()
        self.assertEqual(
            ["cheese", 4],
            practice.slasher([1, 2, "chicken", 3, "potatoes", "cheese", 4], 5))

    def test_empty_array(self):
        practice = Algorithm()
        self.assertEqual([], practice.slasher([], 10))

    def test_negative_input(self):
        practice = Algorithm()
        self.assertEqual([1, 2], practice.slasher([1, 2, 3], -1))

if __name__ == '__main__':
    unittest.main()
