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
created by shhuan at 2020/7/25 12:06

"""


if __name__ == '__main__':
    sys.stdin = open('p1213_6.in', 'r')
    ops = [
        [],
        [ord(v) - ord('A') for v in 'ABDE'],
        [ord(v) - ord('A') for v in 'ABC'],
        [ord(v) - ord('A') for v in 'BCEF'],
        [ord(v) - ord('A') for v in 'ADG'],
        [ord(v) - ord('A') for v in 'BDEFH'],
        [ord(v) - ord('A') for v in 'CFI'],
        [ord(v) - ord('A') for v in 'DEGH'],
        [ord(v) - ord('A') for v in 'GHI'],
        [ord(v) - ord('A') for v in 'EFHI'],
    ]

    A = []
    for i in range(3):
        row = [int(x) for x in input().split()]
        for j in range(3):
            A.append(row[j]//3-1)


    def tostate(a):
        s = 0
        for v in a:
            s *= 4
            s += v
        return s

    def toa(s):
        a = []
        while s > 0:
            a.append(s%4)
            s //= 4
        while len(a) < 9:
            a.append(0)
        return a[::-1]

    def act(s, a):
        sa = toa(s)
        for i in ops[a]:
            sa[i] = (sa[i] + 1) % 4
        return tostate(sa)


    INF = 10**9+7
    vis = [False for _ in range(4**9+1)]
    pre = [(-1, -1) for _ in range(4**9+1)]
    target = tostate([3 for _ in range(9)])
    start = tostate(A)
    q = [start]
    vis[start] = True
    while q:
        nq = []
        for s in q:
            if s == target:
                cur = target
                ans = []
                while cur != start:
                    ps, pa = pre[cur]
                    ans.append(pa)
                    cur = ps
                print(' '.join(map(str, ans[::-1])))
                exit(0)
            for a in range(1, 10):
                ns = act(s, a)
                if not vis[ns]:
                    vis[ns] = True
                    # nq.append((ns, p+[a]))
                    nq.append(ns)
                    pre[ns] = (s, a)

        q = nq
