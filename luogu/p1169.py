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
created by shhuan at 2020/7/19 14:14

"""


def check(heights, width):
    l, r, minh = 0, 0, 100000
    while r < len(heights):
        minh = min(minh, heights[r])
        if minh < width:
            minh = 100000
            l = r + 1

        if r-l+1 >= width and minh >= width:
            return True

        r += 1

    return False

def findMaxSquare(heights):
    n = len(heights)
    lo, hi = 1, n
    while lo <= hi:
        w = (lo + hi) // 2
        if check(heights, w):
            lo = w + 1
        else:
            hi = w - 1

    return hi * hi


def fingMaxRectangle(heights, start, end, orderinex):
    if start > end:
        return 0

    w = end - start + 1
    if w == 1:
        return heights[start]

    while orderinex and orderinex[0] < start or orderinex[0] > end:
        orderinex.pop(0)

    area = w * heights[orderinex[0]]
    area = max(area, fingMaxRectangle(heights, start, orderinex[0]-1, orderinex.copy()))
    area = max(area, fingMaxRectangle(heights, orderinex[0]+1, end, orderinex.copy()))

    return area





if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = []
    for i in range(N):
        row = [int(x) for x in input().strip().split()]
        A.append(row)

    # N, M = 20, 10
    # A = []
    # for i in range(N):
    #     row = [random.randint(0, 1) for _ in range(M)]
    #     A.append(row)

    H = [0 for _ in range(M)]
    a1, a2 = 1, 1
    for ri, row in enumerate(A):
        H[0] = (H[0] + 1) if (ri == 0 or A[ri-1][0] != row[0]) else 1
        l, r = 0, 1
        segs = []
        while r < M:
            H[r] = (H[r] + 1) if (ri == 0 or A[ri-1][r] != row[r]) else 1
            if row[r] == row[r-1]:
                segs.append((l, r-1))
                l = r
            r += 1
        segs.append((l, r-1))
        for l, r in segs:
            hi = [(H[i], i) for i in range(l, r + 1)]
            hi.sort()
            a1 = max(a1, findMaxSquare(H[l: r + 1]))
            a2 = max(a2, fingMaxRectangle(H, l, r, [i for h, i in hi]))

    print(a1)
    print(a2)
