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
created by shhuan at 2020/7/24 22:20

"""


if __name__ == '__main__':
    A, B = map(int, input().split())

    edges = []
    for u in range(B):
        row = [int(x) for x in input().split()]
        for v in range(u+1, B):
            if row[v] > 0:
                edges.append((min(A, row[v]), u, v))
    edges.sort()

    parent = [i for i in range(B + 1)]

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
    while edges:
        w, u, v = edges.pop(0)
        if find(u) != find(v):
            merge(u, v)
            cost += w
    cost += A

    print(cost)