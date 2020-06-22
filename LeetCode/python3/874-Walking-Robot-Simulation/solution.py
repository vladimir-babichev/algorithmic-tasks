#!/usr/bin/env python3

from typing import List

class Solution:

    def __init__(self):
        self.direction = 0
        self.directions = [
            [0,1],  # UP    / NORTH
            [1,0],  # RIGHT / EAST
            [0,-1], # DOWN  / SOUTH
            [-1,0]  # LEFT  / WEST
        ]
        self.posX = 0
        self.posY = 0
        self.maxDistance = 0


    def validateInput(self, commands, obstacles):
        if type(commands) != list:
            raise TypeError("Commands input should be a list.")
        for command in commands:
            if type(command) != int:
                raise TypeError("The command should be an integer.")

        if type(obstacles) != list:
            raise TypeError("Obstacles input should be a list.")
        for obstacle in obstacles:
            if type(obstacle) != list:
                raise TypeError("An onstacle should be a list.")
            if len(obstacle) != 2:
                raise TypeError("An onstacle should have only 2 coordinates.")
            for coordinate in obstacle:
                if type(coordinate) != int:
                    raise TypeError("An onstacle coordinate should be an integer.")


    def setDirection(self, command: int):
        if command == -2:
            self.direction -= 1
        if command == -1:
            self.direction += 1
        self.direction %= 4


    def getDistance(self) -> int:
        return self.posX * self.posX + self.posY * self.posY


    def makeMove(self, command: int, obstacles: set):
        for step in range(command):
            self.posX += 1 * self.directions[self.direction][0]
            self.posY += 1 * self.directions[self.direction][1]
            if (self.posX, self.posY) in obstacles:
                self.posX -= 1 * self.directions[self.direction][0]
                self.posY -= 1 * self.directions[self.direction][1]
                break
            self.maxDistance = max(self.maxDistance, self.getDistance())


    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.validateInput(commands, obstacles)

        obstacleSet = set(map(tuple, obstacles))
        for command in commands:
            if command < 0:
                self.setDirection(command)
            else:
                self.makeMove(command, obstacleSet)

        return self.maxDistance
