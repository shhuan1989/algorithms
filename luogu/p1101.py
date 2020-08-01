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
created by shhuan at 2020/7/13 19:44

"""

def solve(N, A):
    mark = [[False for _ in range(N)] for _ in range(N)]
    word = 'yizhong'
    for r in range(N):
        for c in range(N):
            if A[r][c] == 'y':
                for dxy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    dx, dy = dxy
                    s = []
                    xys = []
                    for i in range(len(word)):
                        x, y = r + i * dx, c + i * dy
                        if x < 0 or x >= N or y < 0 or y >= N:
                            break
                        s.append(A[x][y])
                        xys.append((x, y))
                    # s = [A[r + i * dx][c + i * dy] for i in range(len(word)) if
                    #      0 <= r + i * dx < N and 0 <= c + i * dy < N]
                    if ''.join(s) == word:
                        for x, y in xys:
                            mark[x][y] = True

    for r in range(N):
        for c in range(N):
            if not mark[r][c]:
                A[r][c] = '*'

    for row in A:
        print(''.join(row))


if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(input()))

    solve(N, A)


