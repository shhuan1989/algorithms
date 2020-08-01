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
created by shhuan at 2020/7/20 21:00

"""

if __name__ == '__main__':

    N = int(input())
    A = []

    for i in range(N):
        row = [int(x) for x in input().strip().split()]
        A.append(row)



    id = 3
    edge = set()
    for r in range(N):
        for c in range(N):
            if A[r][c] == 0:
                A[r][c] = id
                q = [(r, c)]
                while q:
                    x, y = q.pop()
                    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if 0 <= nx < N and 0 <= ny < N:
                            if A[nx][ny] == 0:
                                A[nx][ny] = id
                                q.append((nx, ny))
                        else:
                            edge.add(id)
                id += 1

    for r in range(N):
        for c in range(N):
            if A[r][c] != 1:
                if A[r][c] in edge:
                    A[r][c] = 0
                else:
                    A[r][c] = 2

    for row in A:
        print(' '.join(map(str, row)))

