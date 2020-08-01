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
created by shhuan at 2020/7/17 23:10

"""


def online(a, b, c):
    return (c[1]-a[1]) * (b[0]-a[0]) == (b[1]-a[1]) * (c[0]-a[0])

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().strip().split())
        points.append((x, y))

    ans = 1
    for ci, center in enumerate(points):
        ans = max(ans, len([1 for i in range(N) if points[i][0] == center[0]]))
        others = [((points[i][1]-center[1])/(points[i][0]-center[0]), points[i]) for i in range(N) if i != ci and points[i][0] != center[0]]
        if others:
            others.sort()
            oi, oj = 0, 0
            while oj < len(others):
                while oj < len(others) and online(center, others[oi][1], others[oj][1]):
                    oj += 1
                ans = max(ans, oj-oi+1)
                oi = oj
            ans = max(ans, oj - oi + 1)
    print(ans)