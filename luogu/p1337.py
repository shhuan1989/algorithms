# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/10 21:11

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
    N = int(input())
    A = []
    for _ in range(N):
        x, y, m = map(int, input().strip().split())
        A.append((x, y, m))

    cx, cy = sum([x for x, y, m in A])/N, sum([y for x, y, m in A]) / N

    r = 0.9
    for _ in range(1000):
        dx, dy = 0, 0
        for x, y, m in A:
            px = math.sqrt((x-cx)**2 + (y-cy)**2)
            if px > 0:
                dx += m * (x-cx) / px
            py = math.sqrt((x-cx)**2 + (y-cy)**2)
            if py > 0:
                dy += m * (y-cy) / py

        cx += dx * r
        cy += dy * r
        r *= 0.99

    print('{:.3f} {:.3f}'.format(cx, cy))