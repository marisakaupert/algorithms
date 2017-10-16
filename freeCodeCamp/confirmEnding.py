import unittest


class Algorithm:
    def confirm_ending(self, input_string, target_string):
        split_input = input_string.split(' ')
        if input_string == "":
            return True
        elif len(split_input) > 1:
            if target_string == split_input[-1]:
                return True
            elif target_string in split_input[-1]:
                return True
            else:
                return False
        else:
            if input_string[-1] == target_string:
                return True
            else:
                return False


class TestPath(unittest.TestCase):
    def test_confirm_ending_single_word_true(self):
        practice = Algorithm()
        self.assertTrue(practice.confirm_ending("Bastain", "n"))

    def test_confirm_ending_single_word_false(self):
        practice = Algorithm()
        self.assertFalse(practice.confirm_ending("Connor", "n"))

    def test_confirm_ending_long_phrase_1_false(self):
        practice = Algorithm()
        self.assertFalse(
            practice.confirm_ending(
                "Walking on water and developing software from a specification are easy if both are frozen",
                "specification"))

    def test_confirm_ending_short_phrase_1_true(self):
        practice = Algorithm()
        self.assertTrue(practice.confirm_ending(
            "He has to give me a new name", "name"))

    def test_confirm_ending_short_phrase_2_true(self):
        practice = Algorithm()
        self.assertTrue(practice.confirm_ending(
            "Open sesame", "same"))

    def test_confirm_ending_short_phrase_2_false(self):
        practice = Algorithm()
        self.assertFalse(practice.confirm_ending(
            "Open sesame", "pen"))

    def test_confirm_ending_long_phrase_2_false(self):
        practice = Algorithm()
        self.assertFalse(
            practice.confirm_ending(
                "If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing",
                "mountain"))

    def test_confirm_ending_empty_string(self):
        practice = Algorithm()
        self.assertTrue(practice.confirm_ending("", ""))

if __name__ == '__main__':
    unittest.main()

