import unittest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from kaprekar.utils import transform_number, is_valid_number
from kaprekar.kaprekar_routine import kaprekar_routine

class TestKaprekarRoutine(unittest.TestCase):
    def test_transform_number(self):
        self.assertEqual(transform_number(1234), (1234, 4321))
        self.assertEqual(transform_number(1111), (1111, 1111))
        self.assertEqual(transform_number(9876), (6789, 9876))
        self.assertEqual(transform_number(999), (999, 9990))
    
    def test_is_valid_number(self):
        self.assertTrue(is_valid_number(1234))
        self.assertTrue(is_valid_number(9876))
        self.assertFalse(is_valid_number(1111))
        self.assertFalse(is_valid_number(123))
        self.assertFalse(is_valid_number(12345))
    
    def test_kaprekar_routine(self):
        pass

if __name__ == "__main__":
    unittest.main()