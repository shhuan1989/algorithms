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
created by shhuan at 2020/1/8 22:42

"""


def solve(A, s):
    chv = {chr(ord('a') + i): v for i, v in enumerate(A)}
    presum = []
    chindx = collections.defaultdict(list)
    p = 0
    for i, ch in enumerate(s):
        v = chv[ch]
        p += v
        presum.append(p)
        chindx[ch].append(i)

    ans = 0
    for ch, idx in chindx.items():
        ps = collections.defaultdict(list)
        for i in idx:
            ps[presum[i]].append(i)

        if chv[ch] == 0:
            for w in ps.values():
                nw = len(w)
                if nw > 1:
                    ans += nw * (nw - 1) // 2
        else:
            for u, idx in ps.items():
                v = u + chv[ch]
                if v in ps:
                    w = ps[v]
                    for i in idx:
                        ans += len(w) - bisect.bisect_right(w, i)
    print(ans)

# solve([0 for _ in range(26)], 'v' * 1000000)

A = [int(x) for x in input().split()]
s = input()
solve(A, s)
