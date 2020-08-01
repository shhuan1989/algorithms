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
created by shhuan at 2020/7/25 18:41

"""


if __name__ == '__main__':
    M, S, C = map(int, input().split())

    room = [0 for _ in range(S+1)]

    for i in range(C):
        x = int(input())
        room[x] = 1

    l, r = 0, 0
    segs = []
    while r <= S:
        if room[r] == 0:
            if l < r:
                segs.append((l, r-1))
            l = r + 1
        r += 1
    if l < r:
        segs.append((l, r-1))
    while len(segs) > M:
        mind = S
        mini = -1
        for i in range(len(segs)-1):
            d = segs[i+1][0] - segs[i][1]
            if d < mind:
                mind = d
                mini = i

        segs = segs[:mini] + [(segs[mini][0], segs[mini+1][1])]+ segs[mini+2:]

    print(sum([r - l + 1 for l, r in segs]) or [0])



