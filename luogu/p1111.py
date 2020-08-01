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
created by shhuan at 2020/7/16 21:35

"""


if __name__ == '__main__':
    N, M = map(int, input().split())
    # W = [[False for _ in range(N+1)] for _ in range(N+1)]

    fix = []
    for i in range(M):
        u, v, t = map(int, input().split())
        fix.append((t, u, v))

    fix.sort()


    parent = [i for i in range(N+1)]

    def find(u):
        pu = parent[u]
        if pu == u:
            return u

        pu = find(pu)
        parent[u] = pu
        return pu


    def merge(u, v):
        pu, pv = find(u), find(v)
        parent[pu] = pv

    count = N
    for t, u, v in fix:
        if find(u) == find(v):
            continue

        merge(u, v)
        count -= 1
        if count <= 1:
            print(t)
            exit(0)

    print(-1)
