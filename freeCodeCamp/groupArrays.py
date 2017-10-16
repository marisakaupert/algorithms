import unittest


class Algorithm:
    def chuck_array_in_groups(self, input_array, num):
        overall_2d_array = []
        if input_array == [] or num < 0:
            return []
        else:
            for i in range(0, len(input_array), num):
                overall_2d_array.append(input_array[i:i + num])

        return overall_2d_array


class TestPath(unittest.TestCase):
    def test_array_of_strings(self):
        practice = Algorithm()
        self.assertEqual(
            [["a", "b"], ["c", "d"]],
            practice.chuck_array_in_groups(["a", "b", "c", "d"], 2))

    def test_array_of_ints_1(self):
        practice = Algorithm()
        self.assertEqual(
            [[0, 1, 2], [3, 4, 5]],
            practice.chuck_array_in_groups([0, 1, 2, 3, 4, 5], 3))

    def test_array_of_ints_2(self):
        practice = Algorithm()
        self.assertEqual(
            [[0, 1], [2, 3], [4, 5]],
            practice.chuck_array_in_groups([0, 1, 2, 3, 4, 5], 2))

    def test_array_of_ints_3(self):
        practice = Algorithm()
        self.assertEqual(
            [[0, 1, 2, 3], [4, 5]],
            practice.chuck_array_in_groups([0, 1, 2, 3, 4, 5], 4))

    def test_array_of_ints_4(self):
        practice = Algorithm()
        self.assertEqual(
            [[0, 1, 2], [3, 4, 5], [6]],
            practice.chuck_array_in_groups([0, 1, 2, 3, 4, 5, 6], 3))

    def test_array_of_ints_5(self):
        practice = Algorithm()
        self.assertEqual(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8]],
            practice.chuck_array_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4))

    def test_array_of_ints_6(self):
        practice = Algorithm()
        self.assertEqual(
            [[0, 1], [2, 3], [4, 5], [6, 7], [8]],
            practice.chuck_array_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2))

    def test_empty_array(self):
        practice = Algorithm()
        self.assertEqual([], practice.chuck_array_in_groups([], 4))

    def test_negative_input(self):
        practice = Algorithm()
        self.assertEqual(
            [],
            practice.chuck_array_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], -7))

if __name__ == '__main__':
    unittest.main()
