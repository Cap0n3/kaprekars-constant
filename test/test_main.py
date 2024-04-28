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
        for input_nb in range(1000, 9999):
            if len(set(str(input_nb))) > 1:
                self.assertEqual(kaprekar_routine(input_nb, len(str(input_nb))), 6174)
        for input_nb in range(100, 999):
            if len(set(str(input_nb))) > 1:
                self.assertEqual(kaprekar_routine(input_nb, len(str(input_nb))), 495)
        
if __name__ == "__main__":
    unittest.main()