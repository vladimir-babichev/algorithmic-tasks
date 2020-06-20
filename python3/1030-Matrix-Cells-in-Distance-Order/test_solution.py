#!/usr/bin/env python3

import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_validateInputType(self):
        inputs = [
            [True, False, True, False],
            ["asd", 1, 2, 3],
            [[], {}, [], {}]
        ]
        for input in inputs:
            self.assertRaises(TypeError, Solution().validateInput, *input)

    def test_validateInputValue(self):
        inputs = [
            [0, 100, 1, 1],
            [101, 100, 1, 1],
            [1, 0, 1, 1],
            [1, 101, 1, 1],
            [3, 3, -1, 1],
            [3, 3, 3, 1],
            [3, 3, 1, -1],
            [3, 3, 1, 3],
        ]
        for input in inputs:
            self.assertRaises(ValueError, Solution().validateInput, *input)

    def test_allCellsDistOrder(self):
        inputs = [
            [ [1,2,0,0], [[0,0],[0,1]] ],
            [ [2,2,0,1], [[0,1],[0,0],[1,1],[1,0]] ],
            [ [2,3,1,2], [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]] ]
        ]
        for input in inputs:
            self.assertEqual(Solution().allCellsDistOrder(*input[0]), input[1])

if __name__ == "__main__":
    unittest.main()