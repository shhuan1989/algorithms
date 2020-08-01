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
created by shhuan at 2020/7/17 23:22

"""

if __name__ == '__main__':
    N, M = map(int, input().split())

    A = []
    for i in range(N):
        row = [int(x) for x in list(input().strip())]
        A.append(row)

    id = 2
    size = collections.defaultdict(int)
    for r in range(N):
        for c in range(N):
            if A[r][c] in {0, 1}:
                id += 1
                q = [(A[r][c], r, c)]
                A[r][c] = id
                size[id] += 1
                while q:
                    v, x, y = q.pop()
                    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if 0 <= nx < N and 0 <= ny < N and A[nx][ny] == 1 ^ v:
                            A[nx][ny] = id
                            size[id] += 1
                            q.append((1^v, nx, ny))

    # for row in A:
    #     print(row)

    ans = []
    for i in range(M):
        r, c = map(int, input().strip().split())
        ans.append(size[A[r-1][c-1]])

    print('\n'.join(map(str, ans)))
