from unittest import TestCase


class MyTestCases():
    def test_check_number_odd_number(self):
        self.assertEqual(odd_number(5),"1,3,5")
        self.assertEqual(odd_number(7),"1,3,5,7")

    def test_check_number_even_number(self):
        self.assertEqual(even_range_2_to_5(5),"1,3,5")
        self.assertEqual(even_range_2_to_5(7),"1,3,5,7")
        

    def test_check_number_negative_even_number(self):
        self.assertEqual(even_range_2_to_5(5),"1,3,5")
        self.assertEqual(even_range_2_to_5(7),"1,3,5,7")


    def test_check_number_negative_odd_number(self):
        self.assertEqual(even_range_2_to_5(5),"1,3,5")
        self.assertEqual(even_range_2_to_5(7),"1,3,5,7")

    def test_check_number_neutral(self):
        self.assertEqual(even_range_2_to_5(5),"1,3,5")
        self.assertEqual(even_range_2_to_5(7),"1,3,5,7")

    def test_check_number_even_greater_than_20(self):
        self.assertEqual(even_range_2_to_5(5),"1,3,5")
        self.assertEqual(even_range_2_to_5(7),"1,3,5,7")