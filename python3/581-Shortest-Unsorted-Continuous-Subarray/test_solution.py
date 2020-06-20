#!/usr/bin/env python3

import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_validateInput(self):
        inputs = [
            True,
            "string",
            {},
            1,
            [True, 1],
            ["string", 1],
            [{}]
        ]
        for input in inputs:
            self.assertRaises(TypeError, Solution().validateInput, input)

    def test_findUnsortedSubarray(self):
        inputs = [
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 
                []
            ],
            [
                [2, 6, 4, 8, 10, 9, 15],
                [6, 4, 8, 10, 9]
            ],
            [
                [1, 3, 4, 5, 6, 7, 8, 9, 2],
                [3, 4, 5, 6, 7, 8, 9, 2]
            ],
            [
                [5, 4, 3, 2, 1],
                [5, 4, 3, 2, 1]
            ],
            [
                [1,3,2,2,2],
                [3,2,2,2]
            ],
            [
                [1,2,3,3,3],
                []
            ],
            [
                [2,3,3,2,4],
                [3,3,2]
            ],
            [
                [1,2,5,3,4],
                [5,3,4]
            ],
            [
                [2,7,8,9,4,1,5,0,6,3],
                [2,7,8,9,4,1,5,0,6,3]
            ]
        ]
        for input in inputs:
            self.assertEqual(Solution().findUnsortedSubarray(input[0]), len(input[1]))


if __name__ == "__main__":
    unittest.main()