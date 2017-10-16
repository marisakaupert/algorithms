import unittest


class Algorithm:
    def truncate_string(self, input_string, num):
        if input_string == "" or num < 0:
            return ""
        elif len(input_string) <= 3 or num <= 3:
            return input_string[:num] + '...'
        else:
            return input_string[:(num-3)] + '...'


class TestPath(unittest.TestCase):
    def test_phrase_1(self):
        practice = Algorithm()
        self.assertEqual(
            "A-tisket...",
            practice.truncate_string(
                "A-tisket a-tasket A green and yellow basket", 11))

    def test_phrase_2(self):
        practice = Algorithm()
        self.assertEqual(
            "Peter Piper...",
            practice.truncate_string(
                "Peter Piper picked a peck of pickled peppers", 14))

    def test_phrase_3(self):
        practice = Algorithm()
        self.assertEqual("A...", practice.truncate_string("A-", 1))

    def test_phrase_4(self):
        practice = Algorithm()
        self.assertEqual(
            "Ab...", practice.truncate_string("Absolutely Longer", 2))

    def test_single_word(self):
        practice = Algorithm()
        self.assertEqual("Ballr...", practice.truncate_string("Ballroom", 8))

    def test_single_short_word(self):
        practice = Algorithm()
        self.assertEqual("It...", practice.truncate_string("It", 2))

    def test_empty_string(self):
        practice = Algorithm()
        self.assertEqual("", practice.truncate_string("", 5))

    def test_negative_input(self):
        practice = Algorithm()
        self.assertEqual("", practice.truncate_string("", -3))

if __name__ == '__main__':
    unittest.main()
