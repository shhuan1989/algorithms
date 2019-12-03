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
created by shhuan at 2019/12/1 10:33

"""

from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        A = [[0 for _ in range(3)] for _ in range(3)]

        def check():
            for row in A:
                if all([x == row[0] for x in row]) and row[0] != 0:
                    return True
            for c in range(3):
                col = [A[r][c] for r in range(3)]
                if all([col[0] == x for x in col]) and col[0] != 0:
                    return True

            if A[0][0] != 0 and A[0][0] == A[1][1] == A[2][2]:
                return True
            if A[0][2] != 0 and A[0][2] == A[1][1] == A[2][0]:
                return True
            return False

        for i, m in enumerate(moves):
            p = 1 if i % 2 == 0 else 2
            r, c = m
            A[r][c] = p

            if check():
                return 'A' if p == 1 else 'B'

        return 'Draw' if all([all([x != 0 for x in row]) for row in A]) else 'Pending'

s = Solution()
print(s.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(s.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(s.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
print(s.tictactoe([[0,0],[1,1]]))