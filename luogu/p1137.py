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
created by shhuan at 2020/7/17 23:35

"""


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    G = collections.defaultdict(list)
    ind = [0 for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        ind[y] += 1

    ans = [1 for _ in range(N+1)]

    q = collections.deque([i for i in range(1, N+1) if ind[i] == 0])
    inq = [False for _ in range(N+1)]
    while q:
        u = q.popleft()
        inq[u] = False
        for v in G[u]:
            nc = ans[u] + 1
            if nc > ans[v]:
                ans[v] = nc
                if not inq[v]:
                    inq[v] = True
                    q.append(v)
    print('\n'.join(map(str, ans[1:])))