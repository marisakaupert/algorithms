import unittest
import string


class Algorithm:
    def ceasar_cipher(self, input_string):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        first_section_alphabet = alphabet[13:]
        second_section_alphabet = alphabet[:14]
        result_string = ""
        for index, item in enumerate(input_string):
            if item in alphabet:
                encoded_index = alphabet.index(item) % 13
                if alphabet.index(item) < 13:
                    result_string = result_string + first_section_alphabet[
                        encoded_index]
                else:
                    result_string = result_string + second_section_alphabet[
                        encoded_index]
            else:
                result_string = result_string + item

        return result_string


class TestPath(unittest.TestCase):
    def test_single_word(self):
        practice = Algorithm()
        self.assertEqual("HELLO", practice.ceasar_cipher("URYYB"))

    def test_normal_phrase(self):
        practice = Algorithm()
        self.assertEqual(
            "FREE CODE CAMP", practice.ceasar_cipher("SERR PBQR PNZC"))

    def test_phrase_with_exclamation(self):
        practice = Algorithm()
        self.assertEqual("FREE PIZZA!", practice.ceasar_cipher("SERR CVMMN!"))

    def test_phrase_with_question(self):
        practice = Algorithm()
        self.assertEqual("FREE LOVE?", practice.ceasar_cipher("SERR YBIR?"))

    def test_long_sentence(self):
        practice = Algorithm()
        self.assertEqual(
            "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX.",
            practice.ceasar_cipher(
                "GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK."))

    def test_word_with_digit(self):
        practice = Algorithm()
        self.assertEqual("C3P0", practice.ceasar_cipher("P3C0"))

    def test_empty_string(self):
        practice = Algorithm()
        self.assertEqual("", practice.ceasar_cipher(""))

if __name__ == '__main__':
    unittest.main()
