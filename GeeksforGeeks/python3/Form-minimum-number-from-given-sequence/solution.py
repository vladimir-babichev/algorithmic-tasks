'''
https://www.geeksforgeeks.org/form-minimum-number-from-given-sequence/
Form minimum number from given sequence
Given a pattern containing only I’s and D’s. I for increasing and D for decreasing. Devise an algorithm to print the minimum number following that pattern. Digits from 1-9 and digits can’t repeat.

Examples:
   Input: D        Output: 21
   Input: I        Output: 12
   Input: DD       Output: 321
   Input: II       Output: 123
   Input: DIDI     Output: 21435
   Input: IIDDD    Output: 126543
   Input: DDIDDIID Output: 321654798 
'''

from typing import List

class Solution:
    def __init__(self):
        self.numbers = []
        self.number = [1]
        for i in range(2,10):
            self.numbers.append(i)

    def validateInput(self, input):
        if type(input) != str:
            raise TypeError("Input should be a string")

        for char in input:
            if char not in ("D", "I"):
                raise ValueError("Input string should consist only of I's and D's")

    def buildIncreasingSequence(self, numberIdx: int, count: int):
        self.number.extend(self.numbers[:count])
        del self.numbers[:count]

    def buildDecreasingSequence(self, numberIdx: int, count: int):
        k = self.number.pop()
        self.number.extend(sorted(self.numbers[:count], reverse=True))
        self.number.append(k)
        del self.numbers[:count]

    def minimumNumber(self, sequence: str) -> str:
        self.validateInput(sequence)
        i = 0
        while i < len(sequence): 
            start = i  
            while (i+1 < len(sequence)) and (sequence[i] == sequence[i+1]):
                i += 1
            if sequence[i] == "D":
                self.buildDecreasingSequence(start, i-start+1)
            else:
                self.buildIncreasingSequence(start, i-start+1)

            i += 1
        return ''.join(map(str, self.number))