# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/13 23:01

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


def distance(x0, y0, x1, y1):
    return math.sqrt((x0-x1)**2 + (y0-y1)**2)


if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        x, y = map(int, input().split())
        A.append((x, y))

    dist = [distance(A[0][0], A[0][1], A[i][0], A[i][1]) for i in range(N)]
    ans = 0
    dist[0] = 0

    vis = [False for _ in range(N)]
    vis[0] = True
    # Prim
    for _ in range(N-1):
        mindist = float('inf')
        mi = -1
        for j in range(N):
            if not vis[j] and dist[j] < mindist:
                mindist = dist[j]
                mi = j
        vis[mi] = True
        ans += mindist
        for j in range(N):
            if not vis[j]:
                dist[j] = min(dist[j], distance(A[mi][0], A[mi][1], A[j][0], A[j][1]))

    print('{:.2f}'.format(ans))




