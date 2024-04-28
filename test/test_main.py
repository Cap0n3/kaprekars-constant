import unittest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from kaprekar.utils import *
from kaprekar.kaprekar_routine import kaprekar_routine

class TestKaprekarRoutine(unittest.TestCase):
    def test_transform_four_digit(self):
        self.assertEqual(transform_four_digits(1234), (1234, 4321))
        self.assertEqual(transform_four_digits(1111), (1111, 1111))
        self.assertEqual(transform_four_digits(9876), (6789, 9876))
        self.assertEqual(transform_four_digits(999), (999, 9990))

    def test_transform_three_digit(self):
        self.assertEqual(transform_three_digits(123), (123, 321))
        self.assertEqual(transform_three_digits(111), (111, 111))
        self.assertEqual(transform_three_digits(987), (789, 987))
        self.assertEqual(transform_three_digits(568), (568, 865))
    
    def test_is_four_digits(self):
        self.assertTrue(is_four_digits(1234))
        self.assertTrue(is_four_digits(9876))
        self.assertFalse(is_four_digits(1111))
        self.assertFalse(is_four_digits(123))
        self.assertFalse(is_four_digits(12345))

    def test_is_three_digits(self):
        self.assertTrue(is_three_digits(123))
        self.assertTrue(is_three_digits(987))
        self.assertFalse(is_three_digits(111))
        self.assertFalse(is_three_digits(12))
        self.assertFalse(is_three_digits(1234))
    
    def test_kaprekar_routine(self):
        self.assertEqual(kaprekar_routine(1234, 4), 6174)
        self.assertEqual(kaprekar_routine(123, 3), 495)
        self.assertEqual(kaprekar_routine(2111, 4), 6174)
        self.assertEqual(kaprekar_routine(576, 3), 495)
        self.assertEqual(kaprekar_routine(495, 3), 495)
        

if __name__ == "__main__":
    unittest.main()