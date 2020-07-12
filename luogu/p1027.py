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
created by shhuan at 2020/7/8 22:56

"""


import math


def pointdist(p1, p2):
    return dist(p1[0], p1[1], p2[0], p2[1])

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def getpoint(x1, y1, x2, y2, x3, y3):
    ab = (x1-x2)**2 + (y1-y2)**2
    ac = (x1-x3)**2 + (y1-y3)**2
    bc = (x2-x3)**2 + (y2-y3)**2

    x4, y4 = 0, 0
    if ab + ac == bc:
        x4 = x2+x3-x1
        y4 = y2+y3-y1
    elif ab + bc == ac:
        x4 = x1+x3-x2
        y4 = y1+y3-y2
    elif ac + bc == ab:
        x4 = x1+x2-x3
        y4 = y1+y2-y3

    return x4, y4


if __name__ == '__main__':
    TT = int(input())
    for ti in range(TT):
        S, T, A, B = map(int, input().split())

        starts, ends = [], []
        points = []
        MAXN = 500
        cost = [[float('inf') for _ in range(MAXN)] for _ in range(MAXN)]
        for si in range(S):
            x1, y1, x2, y2, x3, y3, t = map(int, input().split())
            i1 = len(points)
            i2 = i1 + 1
            i3 = i2 + 1
            i4 = i3 + 1
            if si + 1 == A:
                starts = [i1, i2, i3, i4]
            if si + 1 == B:
                ends = [i1, i2, i3, i4]
            points.append((x1, y1))
            points.append((x2, y2))
            points.append((x3, y3))
            x4, y4 = getpoint(x1, y1, x2, y2, x3, y3)
            points.append((x4, y4))

            for i in range(i1, i4+1):
                for j in range(i1, i4+1):
                    if i != j:
                        cost[i][j] = pointdist(points[i], points[j]) * t
                    else:
                        cost[i][j] = 0

        # print(points)
        # print(starts, ends)
        NP = len(points)
        for i in range(NP):
            for j in range(NP):
                if i != j and cost[i][j] >= float('inf'):
                    cost[i][j] = pointdist(points[i], points[j]) * T
                if i == j:
                    cost[i][j] = 0

        for k in range(NP):
            for i in range(NP):
                for j in range(NP):
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

        ans = float('inf')
        for s in starts:
            for e in ends:
                ans = min(ans, cost[s][e])
        print('{:.1f}'.format(ans))



