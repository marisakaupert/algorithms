import unittest
from itertools import zip_longest
from collections import OrderedDict



class Algorithm:
    def diff_two_arrays(self, array_1, array_2):
        result = []
        master_list = array_1 + array_2
        if array_1 == []:
            return array_2
        elif array_2 == []:
            return array_1
        elif array_1 == array_2:
            return []
        else:
            first_check = []
            if len(array_1) == len(array_2):
                for index, value in enumerate(array_1):
                    if value != array_2[index]:
                        first_check.extend([value, array_2[index]])
                for element in first_check:
                    if first_check.count(element) == 1:
                        result.append(element)
            else:
                for element in master_list:
                    if master_list.count(element) == 1:
                        result.append(element)

        return result


class TestPath(unittest.TestCase):
    def test_lists_of_strings_1(self):
        practice = Algorithm()
        self.assertEqual(
            ["pink wool"], practice.diff_two_arrays(
                ["diorite", "andesite", "grass",
                    "dirt", "pink wool", "dead shrub"],
                ["diorite", "andesite", "grass", "dirt", "dead shrub"]))

    def test_lists_of_strings_2(self):
        practice = Algorithm()
        self.assertEqual(["diorite", "pink wool"], practice.diff_two_arrays(
            ["andesite", "grass", "dirt", "pink wool", "dead shrub"],
            ["diorite", "andesite", "grass", "dirt", "dead shrub"]))

    def test_lists_of_all_similar_elements(self):
        practice = Algorithm()
        self.assertEqual([], practice.diff_two_arrays(
            ["andesite", "grass", "dirt", "dead shrub"],
            ["andesite", "grass", "dirt", "dead shrub"]))

    def test_lists_of_sorted_ints(self):
        practice = Algorithm()
        self.assertEqual([4], practice.diff_two_arrays(
            [1, 2, 3, 5], [1, 2, 3, 4, 5]))

    def test_lists_of_mixed_strings_and_ints(self):
        practice = Algorithm()
        self.assertEqual(["piglet", 4], practice.diff_two_arrays(
            [1, "calf", 3, "piglet"], [1, "calf", 3, 4]))

    def test_one_empty_list(self):
        practice = Algorithm()
        self.assertEqual(
            ["snuffleupagus", "cookie monster", "elmo"],
            practice.diff_two_arrays(
                [], ["snuffleupagus", "cookie monster", "elmo"]))

    def test_lists_with_no_similar_elements(self):
        practice = Algorithm()
        self.assertEqual(
            [1, "calf", 3, "piglet", 7, "filly"],
            practice.diff_two_arrays([1, "calf", 3, "piglet"], [7, "filly"]))

    def test_empty_lists(self):
        practice = Algorithm()
        self.assertEqual([], practice.diff_two_arrays([], []))

    def test_lists_of_unsorted_ints(self):
        practice = Algorithm()
        self.assertEqual([1, 3, 2, -3, 4], practice.diff_two_arrays(
            [1, -1, 3, -5], [-1, 2, -3, 4, -5]))

if __name__ == '__main__':
    unittest.main()
