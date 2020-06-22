#!/usr/bin/env python3

from typing import List

class Solution:
    keyMap = {
       "2": "abc",
       "3": "def",
       "4": "ghi",
       "5": "jkl",
       "6": "mno",
       "7": "pqrs",
       "8": "tuv",
       "9": "wxyz"
    }

    def __init__(self):
        self.result = []

    def validateInput(self, input):
        if type(input) != str:
            raise TypeError("Input should be a string")
        for digit in input:
            if (digit < "2") or (digit > "9"):
                raise TypeError("Input digits should be in a range between 2 and 9")

    def letterCombinationsHelper(self, string: str, digits: str):
        if len(digits) == 0:
            return

        if len(digits) == 1:
            for letter in self.keyMap[digits]:
                self.result.append(string + letter)
            return

        for letter in self.keyMap[digits[0]]:
            self.letterCombinationsHelper(string + letter, digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        self.validateInput(digits)
        self.letterCombinationsHelper("", digits)
        return self.result