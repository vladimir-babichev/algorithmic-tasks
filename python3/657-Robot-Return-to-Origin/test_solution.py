#!/usr/bin/env python3

import unittest
from solution import Solution

class TestRobotReturnToorigin(unittest.TestCase):
    def test_input_type(self):
        self.assertRaises(TypeError, Solution().judgeCircle, 1)
        self.assertRaises(TypeError, Solution().judgeCircle, True)
        self.assertRaises(TypeError, Solution().judgeCircle, [])

    def test_leetcode(self):
        self.assertEqual(Solution().judgeCircle("LL"), False)
        self.assertEqual(Solution().judgeCircle("UD"), True)
        self.assertEqual(Solution().judgeCircle("RLUURDDDLU"), True)

if __name__ == '__main__':
    unittest.main()
