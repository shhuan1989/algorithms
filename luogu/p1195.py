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
created by shhuan at 2020/7/24 22:15

"""


if __name__ == '__main__':
    N, M, K = map(int, input().split())

    edges = []
    for i in range(M):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()

    parent = [i for i in range(N+1)]
    def find(u):
        pu = parent[u]
        if pu == u:
            return u

        parent[u] = find(pu)
        return parent[u]

    def merge(u, v):
        pu, pv = find(u), find(v)
        parent[pu] = pv


    cost = 0
    while N > K:
        w, u, v = edges.pop(0)
        if find(u) != find(v):
            cost += w
            merge(u, v)
            N -= 1
    print(cost)