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
created by shhuan at 2019/12/22 23:03

"""

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        N, M = len(board), len(board[0])

        def crash():
            shouldCrash = set()
            for r in range(N):
                c = 0
                while c < M:
                    if board[r][c] != 0:
                        # right
                        nc = c
                        while nc < M and board[r][nc] == board[r][c]:
                            nc += 1
                        if nc - c >= 3:
                            shouldCrash |= {(r, y) for y in range(c, nc)}
                        c = nc
                    else:
                        c += 1
            for c in range(M):
                r = 0
                while r < N:
                    if board[r][c] != 0:
                        nr = r
                        while nr < N and board[nr][c] == board[r][c]:
                            nr += 1
                        if nr - r >= 3:
                            shouldCrash |= {(x, c) for x in range(r, nr)}
                        r = nr
                    else:
                        r += 1

            for r, c in shouldCrash:
                board[r][c] = 0

            for c in {c for r, c in shouldCrash}:
                rd, ru = N-1, N-1
                while ru >= 0:
                    if board[ru][c] != 0:
                        board[rd][c] = board[ru][c]
                        rd -= 1
                    ru -= 1
                for r in range(rd, -1, -1):
                    board[r][c] = 0

            return len(shouldCrash) > 0

        while crash():
            continue

        return board


s = Solution()
b = s.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]])
for row in b:
    print(row)


