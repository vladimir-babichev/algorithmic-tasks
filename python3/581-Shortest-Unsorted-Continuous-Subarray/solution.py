from typing import List

class Solution:
    def validateInput(self, input: List[int]):
        if type(input) != list:
            raise TypeError("Input must be a list of integers")
        if len(input) == 0:
            raise ValueError("Input can't be an empty list")
        for item in input:
            if type(item) != int:
                raise TypeError("Input must be a list of integers")

    def findElementIndex(self, nums, element):
        for i, num in enumerate(nums):
            if num <= element:
                continue
            return i

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        self.validateInput(nums)
        startIdx = None
        minNum = None
        finishIdx = None
        maxNum = None

        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                if (minNum is None) or (nums[i] < minNum):
                    startIdx = self.findElementIndex(nums, nums[i])
                    minNum = nums[i]
                if (not maxNum) or (nums[i-1] > maxNum):
                    maxNum = nums[i-1]

            if (maxNum) and (nums[i] < maxNum):
                finishIdx = i

            i += 1

        if startIdx == finishIdx:
            length = 0
        else:
            length = finishIdx - startIdx + 1
        return length