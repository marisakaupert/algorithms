import unittest


class Algorithm:
    def reverse_string(self, input_string):
        return input_string[::-1]


class TestPath(unittest.TestCase):
    def test_reverse_string_hello(self):
        practice = Algorithm()
        self.assertEqual("olleh", practice.reverse_string("hello"))

    def test_reverse_string_Howdy(self):
        practice = Algorithm()
        self.assertEqual("ydwoH", practice.reverse_string("Howdy"))

    def test_reverse_string_phrase(self):
        practice = Algorithm()
        self.assertEqual(
            "htraE morf sgniteerG",
            practice.reverse_string("Greetings from Earth")
            )

if __name__ == '__main__':
    unittest.main()

