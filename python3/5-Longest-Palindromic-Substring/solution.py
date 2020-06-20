class Solution:
    def validateInput(self, input: str):
        if type(input) != str:
            raise TypeError("Input parameter should be a string")

    def findLongestPalindrome(self, s, pos) -> str:
        l, r = pos, pos
        for i in range(pos+1, len(s)):
            if s[pos] != s[i]:
                break
            r = i

        while (l >= 0) and (r < len(s)):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        l += 1
        r -= 1
        return s[l:r+1]

    def longestPalindrome(self, s: str) -> str:
        self.validateInput(s)
        if len(s) == 0:
            return ""

        result = s[0]
        for i in range(len(s)):
            palindrome = self.findLongestPalindrome(s, i)
            if len(palindrome) > len(result):
                result = palindrome

        return result
