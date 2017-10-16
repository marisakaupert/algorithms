import unittest
import re


class Algorithm:
    def palindrome(self, input_string):
        input_string = input_string.lower()
        parsed_string = re.sub(r'[^A-Za-z0-9]+', '', input_string)
        reversed_string = parsed_string[::-1]
        if parsed_string == reversed_string:
            return True
        else:
            return False


class TestPath(unittest.TestCase):
    def test_check_1(self):
        practice = Algorithm()
        self.assertTrue(practice.palindrome("eye"))

    def test_check_2(self):
        practice = Algorithm()
        self.assertTrue(practice.palindrome("_eye"))

    def test_check_3(self):
        practice = Algorithm()
        self.assertTrue(practice.palindrome("race car"))

    def test_check_4(self):
        practice = Algorithm()
        self.assertFalse(practice.palindrome("not a palindrome"))

    def test_check_5(self):
        practice = Algorithm()
        self.assertTrue(practice.palindrome("A man, a plan, a canal. Panama"))

    def test_check_6(self):
        practice = Algorithm()
        self.assertTrue(practice.palindrome("never odd or even"))

    def test_check_7(self):
        practice = Algorithm()
        self.assertFalse(practice.palindrome("nope"))

    def test_check_8(self):
        practice = Algorithm()
        self.assertFalse(practice.palindrome("almostomla"))

    def test_check_9(self):
        practice = Algorithm()
        self.assertTrue(practice.palindrome("My age is 0, 0 si ega ym."))

    def test_check_10(self):
        practice = Algorithm()
        self.assertFalse(practice.palindrome("1 eye for of 1 eye."))

    def test_check_11(self):
        practice = Algorithm()
        self.assertTrue(practice.palindrome("0_0 (: /-\ :) 0-0"))

    def test_check_12(self):
        practice = Algorithm()
        self.assertFalse(practice.palindrome("five|\_/|four"))

if __name__ == '__main__':
    unittest.main()