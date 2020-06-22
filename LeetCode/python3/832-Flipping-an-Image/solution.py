#!/usr/bin/env python3

from typing import List

class Solution:
    def validateInput(self, input: List[List[int]]):
        if type(input) != list:
            raise TypeError("Input should be a list")
        if len(input) < 1:
            raise TypeError("Input can't be an empty list")
        for line in input:
            if type(line) != list:
                raise TypeError("Input should be a list of lists")
            if len(line) < 1:
                raise TypeError("Line of the input can't be an empty list")
            for pix in line:
                if type(pix) != int:
                    raise TypeError("Pixel should be integer")
                if pix != 0 and pix != 1:
                    raise TypeError("Pixel can be either 0 or 1 ")

    def flipHorizontally(self, line):
        line.reverse()

    def invertLine(self, line):
        i = 0
        while i < len(line):
            line[i] = 1 - line[i]
            i += 1

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        self.validateInput(A)    

        i = 0
        while i < len(A): 
            self.flipHorizontally(A[i])
            self.invertLine(A[i])
            i += 1

        return A