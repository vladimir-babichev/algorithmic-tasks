#!/usr/bin/env python3

import unittest
from solution import Solution

class TestFlippingImage(unittest.TestCase):

    def test_validateInput(self):
        self.assertRaises(TypeError, Solution().validateInput, "string")
        self.assertRaises(TypeError, Solution().validateInput, 123)
        self.assertRaises(TypeError, Solution().validateInput, True)
        self.assertRaises(TypeError, Solution().validateInput, [])
        self.assertRaises(TypeError, Solution().validateInput, ["asd"])
        self.assertRaises(TypeError, Solution().validateInput, [[]])
        self.assertRaises(TypeError, Solution().validateInput, [[[]]])

    def test_flipHorizontally(self):
        lines = [
            [ [0,1], [1,0] ],
            [ [0,1,1], [1,1,0] ],
            [ [0,0,1,1], [1,1,0,0] ]
        ]
        for line in lines:
            Solution().flipHorizontally(line[0])
            self.assertEqual(line[0], line[1])

    def test_invertLine(self):
        lines = [
            [ [0], [1] ],
            [ [0,0], [1,1] ],
            [ [0,1], [1,0] ],
            [ [0,0,1,1,0,1], [1,1,0,0,1,0] ]
        ]
        for line in lines:
            Solution().invertLine(line[0])
            self.assertEqual(line[0], line[1])

    def test_flipAndInvertImage(self):
        inputs = [
            [ [[1,1,0],[1,0,1],[0,0,0]], [[1,0,0],[0,1,0],[1,1,1]] ],
            [ [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]], [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]]
        ]
        for input in inputs:
            self.assertEqual(Solution().flipAndInvertImage(input[0]), input[1])

if __name__ == "__main__":
    unittest.main()