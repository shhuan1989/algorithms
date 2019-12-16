# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/15 10:00

"""

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
    def __init__(self):
        self.room = [
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.x = 1
        self.y = 3
        self.d = 0
        self.n = len(self.room)
        self.m = len(self.room[0])
        self.cleaned = []

    def dxy(self):
        delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dx, dy = delta[self.d]
        return dx, dy

    def move(self):
        dx, dy = self.dxy()
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < self.n and 0 <= ny < self.m and self.room[nx][ny] == 1:
            self.x = nx
            self.y = ny
            return True
        return False

    def turnLeft(self):
       self.d = (self.d - 1) % 4

    def turnRight(self):
       self.d = (self.d + 1) % 4

    def clean(self):
        self.cleaned.append((self.x, self.y))


class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()



robot = Robot()
s = Solution()
print(s.cleanRoom(robot))

