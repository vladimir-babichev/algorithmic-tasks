#!/usr/bin/env python3

class Solution:
    def __init__(self):
        self.posX = 0
        self.posY = 0

    def validateInput(self, moves):
        if type(moves) != str:
            raise TypeError("Moves shoud be string.")

    def judgeCircle(self, moves: str) -> bool:
        self.validateInput(moves)

        for move in moves:
            if move == 'U':
                self.posY += 1
            elif move == 'D':
                self.posY -= 1
            elif move == 'R':
                self.posX += 1
            elif move == 'L':
                self.posX -= 1

        return (self.posX == 0) and (self.posY == 0)
