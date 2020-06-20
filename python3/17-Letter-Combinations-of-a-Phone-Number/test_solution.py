#!/usr/bin/env python3

import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_validateInput(self):
        self.assertRaises(TypeError, Solution().validateInput, 123)
        self.assertRaises(TypeError, Solution().validateInput, True)
        self.assertRaises(TypeError, Solution().validateInput, "12b")
        self.assertRaises(TypeError, Solution().validateInput, ["1", 1])
    
    def test_letterCombinations(self):
        inputs = [
            ["2", ["a", "b", "c"]],
            ["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
            ["234", ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]]
        ]
        for input in inputs:
            self.assertEqual(Solution().letterCombinations(input[0]), input[1])

if __name__ == "__main__":
    unittest.main()