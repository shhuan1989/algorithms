# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/11 23:05

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        row = [int(x) for x in input().strip()]
        A.append(row)

    dist = [[M+N for _ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if A[r][c] == 1:
                dist[r][c] = 0
                q = collections.deque([(r, c)])
                while q:
                    x, y = q.popleft()
                    for nx, ny in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
                        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] > dist[x][y] + 1:
                            dist[nx][ny] = dist[x][y] + 1
                            q.append((nx, ny))

    for row in dist:
        print(' '.join(map(str, row)))