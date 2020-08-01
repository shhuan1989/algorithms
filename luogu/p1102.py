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
created by shhuan at 2020/7/13 21:11

"""


if __name__ == '__main__':
    N, C = map(int, input().split())
    A = []
    while len(A) < N:
        A += [int(x) for x in input().split()]

    wc = collections.defaultdict(int)
    for i, v in enumerate(A):
        wc[v] += 1


    ans = 0
    for a in list(wc.keys()):
        b = a-C
        if b == a:
            ans += wc[a] * (wc[a] - 1) // 2
        else:
            ans += wc[a] * wc[b]

    print(ans)
