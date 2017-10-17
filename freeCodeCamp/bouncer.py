import unittest


class Algorithm:
    def bouncer(self, input_array):
        false_values = [None, 0, False, ""]
        if input_array == []:
            return []
        else:
            for index, value in enumerate(false_values):
                if value in input_array:
                    input_array.remove(value)

        return input_array


class TestPath(unittest.TestCase):
    def test_mixed_values(self):
        practice = Algorithm()
        self.assertEqual(
            [7, "ate", 9], practice.bouncer([7, "ate", "", False, 9]))

    def test_no_false_values(self):
        practice = Algorithm()
        self.assertEqual(["a", "b", "c"], practice.bouncer(["a", "b", "c"]))

    def test_all_false_values(self):
        practice = Algorithm()
        self.assertEqual([], practice.bouncer([False, 0, None, ""]))

    def test_empty_array(self):
        practice = Algorithm()
        self.assertEqual([], practice.bouncer([]))

    def test_mixed_ints(self):
        practice = Algorithm()
        self.assertEqual([1, 2], practice.bouncer([1, None, 2]))

if __name__ == '__main__':
    unittest.main()
