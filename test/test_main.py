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
    def test_sort_digits(self):
        self.assertEqual(sort_digits(1234, 4), (1234, 4321))
        self.assertEqual(sort_digits(123, 3), (123, 321))
        self.assertEqual(sort_digits(9876, 4), (6789, 9876))
        self.assertEqual(sort_digits(568, 3), (568, 865))

    def test_is_three_or_four_digits(self):
        self.assertTrue(is_three_or_four_digits(123))
        self.assertTrue(is_three_or_four_digits(987))
        self.assertTrue(is_three_or_four_digits(1234))
        self.assertFalse(is_three_or_four_digits(111))
        self.assertFalse(is_three_or_four_digits(12))
        self.assertFalse(is_three_or_four_digits(34565))
    
    def test_kaprekar_routine(self):
        self.assertEqual(kaprekar_routine(1234, 4), 6174)
        self.assertEqual(kaprekar_routine(123, 3), 495)
        self.assertEqual(kaprekar_routine(2111, 4), 6174)
        self.assertEqual(kaprekar_routine(576, 3), 495)
        self.assertEqual(kaprekar_routine(495, 3), 495)
        
if __name__ == "__main__":
    unittest.main()