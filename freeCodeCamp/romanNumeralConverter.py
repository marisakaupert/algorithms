import unittest


class Algorithm:
    def convert_to_roman(self, num):
        ints = [1000, 900, 500, 400, 100,  90, 50,  40, 10,  9, 5, 4, 1]
        roman_nums = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ""
        for i in range(len(ints)):
            count = int(num / ints[i])
            result += roman_nums[i] * count
            num -= ints[i] * count
        return result


class TestPath(unittest.TestCase):
    def test_roman_numerals_2(self):
        practice = Algorithm()
        self.assertEqual("II", practice.convert_to_roman(2))

    def test_roman_numerals_3(self):
        practice = Algorithm()
        self.assertEqual("III", practice.convert_to_roman(3))

    def test_roman_numerals_4(self):
        practice = Algorithm()
        self.assertEqual("IV", practice.convert_to_roman(4))

    def test_roman_numerals_5(self):
        practice = Algorithm()
        self.assertEqual("V", practice.convert_to_roman(5))

    def test_roman_numerals_9(self):
        practice = Algorithm()
        self.assertEqual("IX", practice.convert_to_roman(9))

    def test_roman_numerals_12(self):
        practice = Algorithm()
        self.assertEqual("XII", practice.convert_to_roman(12))

    def test_roman_numerals_16(self):
        practice = Algorithm()
        self.assertEqual("XVI", practice.convert_to_roman(16))

    def test_roman_numerals_29(self):
        practice = Algorithm()
        self.assertEqual("XXIX", practice.convert_to_roman(29))

    def test_roman_numerals_44(self):
        practice = Algorithm()
        self.assertEqual("XLIV", practice.convert_to_roman(44))

    def test_roman_numerals_45(self):
        practice = Algorithm()
        self.assertEqual("XLV", practice.convert_to_roman(45))

    def test_roman_numerals_68(self):
        practice = Algorithm()
        self.assertEqual("LXVIII", practice.convert_to_roman(68))

    def test_roman_numerals_83(self):
        practice = Algorithm()
        self.assertEqual("LXXXIII", practice.convert_to_roman(83))

    def test_roman_numerals_97(self):
        practice = Algorithm()
        self.assertEqual("XCVII", practice.convert_to_roman(97))

    def test_roman_numerals_99(self):
        practice = Algorithm()
        self.assertEqual("XCIX", practice.convert_to_roman(99))

    def test_roman_numerals_500(self):
        practice = Algorithm()
        self.assertEqual("D", practice.convert_to_roman(500))

    def test_roman_numerals_501(self):
        practice = Algorithm()
        self.assertEqual("DI", practice.convert_to_roman(501))

    def test_roman_numerals_649(self):
        practice = Algorithm()
        self.assertEqual("DCXLIX", practice.convert_to_roman(649))

    def test_roman_numerals_798(self):
        practice = Algorithm()
        self.assertEqual("DCCXCVIII", practice.convert_to_roman(798))

    def test_roman_numerals_891(self):
        practice = Algorithm()
        self.assertEqual("DCCCXCI", practice.convert_to_roman(891))

    def test_roman_numerals_1000(self):
        practice = Algorithm()
        self.assertEqual("M", practice.convert_to_roman(1000))

    def test_roman_numerals_1004(self):
        practice = Algorithm()
        self.assertEqual("MIV", practice.convert_to_roman(1004))

    def test_roman_numerals_1006(self):
        practice = Algorithm()
        self.assertEqual("MVI", practice.convert_to_roman(1006))

    def test_roman_numerals_1023(self):
        practice = Algorithm()
        self.assertEqual("MXXIII", practice.convert_to_roman(1023))

    def test_roman_numerals_2014(self):
        practice = Algorithm()
        self.assertEqual("MMXIV", practice.convert_to_roman(2014))

    def test_roman_numerals_3999(self):
        practice = Algorithm()
        self.assertEqual("MMMCMXCIX", practice.convert_to_roman(3999))

if __name__ == '__main__':
    unittest.main()
