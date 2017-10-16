import unittest


class Algorithm:
    def repeat_string_num_times(self, input_string, num):
        repeated_strings_list = []
        if input_string == "" or input_string == " " or num < 0:
            return ""
        else:
            for i in range(num):
                repeated_strings_list.append(input_string)

        return ''.join(repeated_strings_list)


class TestPath(unittest.TestCase):
    def test_string_of_letters_1_time(self):
        practice = Algorithm()
        self.assertEqual(
            "abc", practice.repeat_string_num_times("abc", 1))

    def test_string_of_letters_3_times(self):
        practice = Algorithm()
        self.assertEqual(
            "abcabcabc", practice.repeat_string_num_times("abc", 3))

    def test_string_of_letters_4_times(self):
        practice = Algorithm()
        self.assertEqual(
            "abcabcabcabc", practice.repeat_string_num_times("abc", 4))

    def test_symbols_3_times(self):
        practice = Algorithm()
        self.assertEqual("***", practice.repeat_string_num_times("*", 3))

    def test_symbols_8_times(self):
        practice = Algorithm()
        self.assertEqual("********", practice.repeat_string_num_times("*", 8))

    def test_empty_string(self):
        practice = Algorithm()
        self.assertEqual("", practice.repeat_string_num_times("", 3))

    def test_string_with_some_spaces(self):
        practice = Algorithm()
        self.assertEqual(
            "m jm jm jm jm jm jm jm jm j",
            practice.repeat_string_num_times("m j", 9))

    def test_neagtive_num_input(self):
        practice = Algorithm()
        self.assertEqual("", practice.repeat_string_num_times("abc", -2))

if __name__ == '__main__':
    unittest.main()
