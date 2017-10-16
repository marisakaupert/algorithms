import unittest


class Algorithm:
    def mutation(self, input_array):
        comparable_list = [str(i).lower() for i in input_array]

        original = set(comparable_list[0])
        comparison = set(comparable_list[1])

        if comparison.difference(original) == set():
            return True
        else:
            return False


class TestPath(unittest.TestCase):
    def test_case_1(self):
        practice = Algorithm()
        self.assertFalse(practice.mutation(["hello", "hey"]))

    def test_case_2(self):
        practice = Algorithm()
        self.assertTrue(practice.mutation(["hello", "Hello"]))

    def test_case_3(self):
        practice = Algorithm()
        self.assertTrue(practice.mutation(
            ["zyxwvutsrqponmlkjihgfedcba", "qrstu"]))

    def test_case_4(self):
        practice = Algorithm()
        self.assertTrue(practice.mutation(["Mary", "Army"]))

    def test_case_5(self):
        practice = Algorithm()
        self.assertTrue(practice.mutation(["Mary", "Aarmy"]))

    def test_case_6(self):
        practice = Algorithm()
        self.assertTrue(practice.mutation(["Alien", "line"]))

    def test_case_7(self):
        practice = Algorithm()
        self.assertTrue(practice.mutation(["floor", "for"]))

    def test_case_8(self):
        practice = Algorithm()
        self.assertFalse(practice.mutation(["hello", "neo"]))

    def test_case_9(self):
        practice = Algorithm()
        self.assertFalse(practice.mutation(["voodoo", "no"]))

    def test_empty_string(self):
        practice = Algorithm()
        self.assertTrue(practice.mutation(["", ""]))

    def test_empty_string_against_actual_string(self):
        practice = Algorithm()
        self.assertFalse(practice.mutation(["hello", " "]))

    def test_digits_in_string(self):
        practice = Algorithm()
        self.assertTrue(practice.mutation(["12345", "12"]))

    def test_ints_against_string(self):
        practice = Algorithm()
        self.assertTrue(practice.mutation(["12345", 34]))

    def test_symbols(self):
        practice = Algorithm()
        self.assertTrue(practice.mutation(["Eureka!", "!"]))

if __name__ == '__main__':
    unittest.main()
