#!/usr/bin/env python3

import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_validateInput(self):
        inputs = [
            1,
            True,
            [1],
            {"a":"a"}
        ]
        for input in inputs:
            self.assertRaises(TypeError, Solution().validateInput, input)

    def test_longestPalindrome(self):
        inputs = [
            [ "babad", "bab" ],
            [ "baabdas", "baab" ],
            [ "cbbd", "bb"],
            [ "", "" ],
            [ "asd", "a"],
            [ "ccd", "cc"]
        ]
        for input in inputs:
            self.assertEqual(Solution().longestPalindrome(input[0]), input[1])


if __name__ == "__main__":
    unittest.main()