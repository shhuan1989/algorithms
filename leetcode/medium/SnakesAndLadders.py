# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2018/10/14 16:35

"""


class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """


        N = len(board)
        M = N * N
        B = [-1 for _ in range(M+1)]

        leftToRight = True
        num = M
        for row in range(N):
            if leftToRight:
                for col in range(N):
                    B[num] = board[row][col]
                    num -= 1
            else:
                for col in range(N-1, -1, -1):
                    B[num] = board[row][col]
                    num -= 1

            leftToRight = not leftToRight


        steps = [float('inf') for _ in range(M+1)]

        steps[-1] = 0

        Q = [M]
        while Q:
            num = Q.pop()
            for i in range(1, 7):
                v = num - i
                if v > 0:
                    if B[v] == -1:
                        steps[v] = min(steps[v], steps[num] + 1)
                    else:
                        pass

                else:
                    break









s = Solution()
print(s.snakesAndLadders(
 [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1]
 ]
))