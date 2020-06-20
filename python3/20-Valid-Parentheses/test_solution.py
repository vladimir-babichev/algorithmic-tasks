#!/usr/bin/env python3

import unittest

from solution import Solution

class TestSolution(unittest.TestCase):
    def test_validateInputType(self):
        inputs = [
            1,
            True,
            [],
        ]
        for input in inputs:
            self.assertRaises(TypeError, Solution().validateInput, input)

    def test_validateInputValue(self):
        inputs = [
            "abc",
            "[]()[]()2[]()"
        ]
        for input in inputs:
            self.assertRaises(ValueError, Solution().validateInput, input)

    def test_isValid(self):
        inputs = [
            [ "()", True ],
            [ "()[]{}", True ],
            [ "(]", False ],
            [ "([)]", False ],
            [ "{[]}", True ],
            [ "[", False]
        ]
        for input in inputs:
            self.assertEqual(Solution().isValid(input[0]), input[1])

if __name__ == "__main__":
    unittest.main()