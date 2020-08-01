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
created by shhuan at 2020/7/17 10:02

"""

if __name__ == '__main__':
    N = int(input())
    A = [0] + [int(x) for x in input().strip().split()]

    dpa = [float('-inf') for _ in range(N+1)]
    dpb = [A[i] for i in range(N+1)]

    G = collections.defaultdict(list)
    for i in range(N-1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    def dfs(root, parent):
        if not root:
            return 0, 0

        a, b = 0, 0
        for v in G[root]:
            if v != parent:
                c, d = dfs(v, root)
                a = max(a, c)
                b += max(d, 0)

        dpb[root] = b + A[root]
        dpa[root] = max(a, dpb[root])

        return dpa[root], dpb[root]

    a, b = dfs(1, -1)
    print(a)