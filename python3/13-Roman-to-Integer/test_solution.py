#!/usr/bin/env python3

import unittest
from solution import Solution

class TestRomanToInt(unittest.TestCase):

    def test_input_type(self):
        # Test input type
        self.assertRaises(TypeError, Solution().romanToInt, 3)
        self.assertRaises(TypeError, Solution().romanToInt, True)

    def test_conversion(self):
        # Test conversion
        self.assertEqual(Solution().romanToInt("III"), 3)
        self.assertEqual(Solution().romanToInt("IV"), 4)
        self.assertEqual(Solution().romanToInt("IX"), 9)
        self.assertEqual(Solution().romanToInt("LVIII"), 58)
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)

if __name__ == '__main__':
    unittest.main()
