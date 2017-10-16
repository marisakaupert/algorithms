import unittest


class Algorithm:
    def find_longest_word(self, input_string):
        split_string = input_string.split(' ')
        length_of_words_list = []
        for word in split_string:
            length_of_words_list.append(len(word))

        return max(length_of_words_list)


class TestPath(unittest.TestCase):
    def test_check_all_letters_alphabet_phrase(self):
        practice = Algorithm()
        self.assertEqual(
            6, practice.find_longest_word(
                "The quick brown fox jumped over the lazy dog"
                ))

    def test_check_star_wars_credo(self):
        practice = Algorithm()
        self.assertEqual(
            5, practice.find_longest_word(
                "May the force be with you"
                ))

    def test_check_google_action(self):
        practice = Algorithm()
        self.assertEqual(
            6, practice.find_longest_word(
                "Google do a barrel roll"
                ))

    def test_check_monty_python_quote(self):
        practice = Algorithm()
        self.assertEqual(
            8, practice.find_longest_word(
                "What is the average airspeed velocity of an unladen swallow"
                ))

    def test_check_long_words(self):
        practice = Algorithm()
        self.assertEqual(
            19, practice.find_longest_word(
                "What if we try a super-long word such as otorhinolaryngology"
                ))

if __name__ == '__main__':
    unittest.main()