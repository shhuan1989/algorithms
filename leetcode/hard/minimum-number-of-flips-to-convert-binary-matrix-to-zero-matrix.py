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
created by shhuan at 2019/12/8 10:39

"""


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        N, M = len(mat), len(mat[0])
        def state(m):
            s = ''.join([''.join(map(str, row)) for row in m])
            return int(s, 2)

        def flip(s, i):
            b = list(bin(s)[2:])
            if len(b) < N * M:
                b = ['0'] * (N*M-len(b)) + b

            b[i] = '1' if b[i] == '0' else '0'
            r, c = i // M, i % M
            for nr, nc in [(r+1, c), (r-1, c), (r, c+ 1), (r, c-1)]:
                if 0 <= nr < N and 0 <= nc < M:
                    j = nr * M + nc
                    b[j] = '1' if b[j] == '0' else '0'

            return int(''.join(b), 2)

        q = [state(mat)]
        vis = [False] * (1 << (N*M))
        step = 0
        while q:
            nq = []
            for s in q:
                if s == 0:
                    return step
                for i in range(N*M):
                    ns = flip(s, i)
                    if not vis[ns]:
                        vis[ns] = True
                        nq.append(ns)

            q = nq
            step += 1

        return -1


s = Solution()
print(s.minFlips(mat = [[0,0],[0,1]]))
print(s.minFlips([[0]]))
print(s.minFlips([[1,1,1],[1,0,1],[0,0,0]]))
print(s.minFlips( [[1,0,0],[1,0,0]]))