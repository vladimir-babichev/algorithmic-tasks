#!/usr/bin/env python3

import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_validateInputType(self):
        inputs = [1, True, ["str"], {"a": "b"}]
        for input in inputs:
            self.assertRaises(TypeError, Solution().validateInput, input)
    
    def test_validateInputValue(self):
        inputs = ["abcdef", "ABCDEF", "ididiidddiii"]
        for input in inputs:
            self.assertRaises(ValueError, Solution().validateInput, input)

    def test_buildIncreasingSequence(self):
        inputs = [
            [0, 0, [1]], 
            [0, 2, [1, 2, 3]], 
            [0, 5, [1, 2, 3, 4, 5, 6]]
        ]
        for input in inputs:
            sequence = Solution()
            sequence.buildIncreasingSequence(input[0], input[1])
            self.assertEqual(sequence.number, input[2])

    def test_buildDecreasingSequence(self):
        inputs = [
            [0, 0, [1]], 
            [0, 2, [3, 2, 1]], 
            [0, 5, [6, 5, 4, 3, 2, 1]]
        ]
        for input in inputs:
            sequence = Solution()
            sequence.buildDecreasingSequence(input[0], input[1])
            self.assertEqual(sequence.number, input[2])

    def test_minimumNumber(self):
        inputs = [
            ["D", "21"], 
            ["I", "12"], 
            ["DD", "321"],
            ["II", "123"],
            ["DIDI", "21435"],
            ["IIDDD", "126543"],
            ["DDIDDIID", "321654798"]
        ]
        for input in inputs:
            sequence = Solution()
            self.assertEqual(sequence.minimumNumber(input[0]), input[1])

if __name__ == "__main__":
    unittest.main()