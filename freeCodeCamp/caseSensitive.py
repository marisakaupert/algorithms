import unittest


class Algorithm:
    def make_title_case_sensitive(self, input_string):
        split_string = input_string.split(' ')
        case_sensitive_list = []
        for word in split_string:
            if len(word) == 0:
                return
            else:
                case_sensitive_list.append(word[0].upper() + word[1:].lower())

        return ' '.join(case_sensitive_list)


class TestPath(unittest.TestCase):
    def test_check_normal_string_with_symbol(self):
        practice = Algorithm()
        self.assertEqual(
            "I'm A Little Tea Pot",
            practice.make_title_case_sensitive("I'm a little tea pot"))

    def test_check_inverse_string(self):
        practice = Algorithm()
        self.assertEqual(
            "Short And Stout",
            practice.make_title_case_sensitive("sHoRt AnD sToUt"))

    def test_check_all_caps(self):
        practice = Algorithm()
        self.assertEqual(
            "Here Is My Handle Here Is My Spout",
            practice.make_title_case_sensitive(
                "HERE IS MY HANDLE HERE IS MY SPOUT"))

if __name__ == '__main__':
    unittest.main()
