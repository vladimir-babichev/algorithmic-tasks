#!/usr/bin/env python3

class Solution:
    bracketsMap = {
        '(': ')', 
        '{': '}',
        '[': ']'
    }
    def validateInput(self, input):
        if type(input) != str:
            raise TypeError("Input should be a string")
        
        for char in input:
            if char not in "(){}[]":
                raise ValueError("Input should consist only of '(', ')', '{', '}', '[' and ']'")

    def isValid(self, s: str) -> bool:
        self.validateInput(s)

        stack = []
        for char in s:
            if char in self.bracketsMap:
                stack.append(self.bracketsMap[char])
            else:
                if len(stack) == 0:
                    return False
                if char != stack.pop():
                    return False

        return (len(stack) == 0)