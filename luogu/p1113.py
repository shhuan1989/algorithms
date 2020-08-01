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
created by shhuan at 2020/7/15 22:51

"""


if __name__ == '__main__':
    N = int(input())
    cost = [0 for _ in range(N+1)]

    G = collections.defaultdict(list)
    ind = [0 for _ in range(N+1)]
    for i in range(N):
        a = [int(x) for x in input().split()]
        cost[a[0]] = a[1]
        pre = a[2:-1]
        ind[a[0]] = len(pre)
        for u in pre:
            G[u].append(a[0])

    startime = [0 for _ in range(N+1)]
    endtime = [0 for _ in range(N+1)]
    q = [u for u in range(1, N+1) if ind[u] == 0]
    while q:
        nq = []
        for u in q:
            endtime[u] = startime[u] + cost[u]
            for v in G[u]:
                ind[v] -= 1
                startime[v] = max(startime[v], endtime[u])
                if ind[v] == 0:
                    nq.append(v)
        q = nq

    print(max(endtime))