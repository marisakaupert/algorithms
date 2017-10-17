import unittest


class Algorithm:
    def remove_same_values(self, input_array, *args):
        if input_array == []:
            return []
        else:
            for arg in args:
                while arg in input_array:
                    input_array.remove(arg)

        return input_array


class TestPath(unittest.TestCase):
    def test_array_of_ints_1(self):
        practice = Algorithm()
        self.assertEqual(
            [1, 1], practice.remove_same_values([1, 2, 3, 1, 2, 3], 2, 3))

    def test_array_of_ints_2(self):
        practice = Algorithm()
        self.assertEqual(
            [1, 5, 1], practice.remove_same_values(
                [1, 2, 3, 5, 1, 2, 3], 2, 3))

    def test_array_of_ints_3(self):
        practice = Algorithm()
        self.assertEqual(
            [1], practice.remove_same_values([3, 5, 1, 2, 2], 2, 3, 5))

    def test_removing_all_elements_of_array(self):
        practice = Algorithm()
        self.assertEqual([], practice.remove_same_values([2, 3, 2, 3], 2, 3))

    def test_mix_of_strings_and_ints(self):
        practice = Algorithm()
        self.assertEqual(
            ["hamburger"], practice.remove_same_values(
                ["tree", "hamburger", 53], "tree", 53))

    def test_array_with_no_similar_values(self):
        practice = Algorithm()
        self.assertEqual(
            [1, 2, 3, 1, 2, 3], practice.remove_same_values(
                [1, 2, 3, 1, 2, 3], 7, 9))

    def test_no_arguments_to_remove_given(self):
        practice = Algorithm()
        self.assertEqual([2, 3], practice.remove_same_values([2, 3]))

    def test_empty_array(self):
        practice = Algorithm()
        self.assertEqual([], practice.remove_same_values([], 3, 4, 5))

if __name__ == '__main__':
    unittest.main()
