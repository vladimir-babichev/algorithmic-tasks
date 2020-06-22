#!/usr/bin/env python3

from typing import List

class Solution:
    def validateInput(self, R: int, C: int, r0: int, c0: int):
        for param in [R, C, r0, c0]:
            if type(param) != int:
                raise TypeError("Input parameters should be integer")
        
        if (R < 1) or (R > 100):
            raise ValueError("R must be: 1 <= R <= 100")
        if (C < 1) or (C > 100):
            raise ValueError("C must be: 1 <= C <= 100")
        if (r0 < 0) or (r0 >= R):
            raise ValueError("r0 must be: 0 <= r0 < R")
        if (c0 < 0) or (c0 >= C):
            raise ValueError("c0 must be: 0 <= c0 < C")

    def printMap(self, R: int, C: int, r0: int, c0: int):
        print(f"r0 = {r0}, c0 = {c0}")
        for c in range(C-1,-1,-1):
            for r in range(R):
                if r == r0 and c == c0:
                    print("X", end =" ")
                else:
                    print(".", end =" ")
                if r+1 == R:
                    print()
            

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        self.validateInput(R, C, r0, c0)

        distanceMap = {}
        res = []
        for r in range(R):
            for c in range(C):
                dist = abs(r-r0) + abs(c-c0)
                if dist in distanceMap:
                    distanceMap[dist].append([r,c])
                else:
                    distanceMap[dist] = [[r,c]]

        for elem in sorted(distanceMap.items()):
            res.extend(elem[1])

        return res
