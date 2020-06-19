#!/usr/bin/env python3

class Solution:
    ROMAN_TO_INT_DICT = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        if type(s) != str:
            raise TypeError("The input should be a string.")

        res = 0
        lookBack = False
        i = 0
        while i < len(s):
            if i == len(s)-1:
                res += self.ROMAN_TO_INT_DICT[s[i]]
            else:
                if self.ROMAN_TO_INT_DICT[s[i]] >= self.ROMAN_TO_INT_DICT[s[i+1]]:
                    res += self.ROMAN_TO_INT_DICT[s[i]]
                else:
                    res += self.ROMAN_TO_INT_DICT[s[i+1]] - self.ROMAN_TO_INT_DICT[s[i]]
                    i += 1
            i += 1
        return res

if __name__ == '__main__':
    print(Solution().romanToInt("XL"))
