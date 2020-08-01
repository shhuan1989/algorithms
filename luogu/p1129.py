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
created by shhuan at 2020/7/18 18:08

"""



MATCH = [-1 for _ in range(1000)]
VIS = [0 for _ in range(1000)]
def dfs(u, graph, tim):
    for v in graph[u]:
        if VIS[v] == tim:
            continue
        if MATCH[v] < 0:
            MATCH[v] = u
            return 1
    for v in graph[u]:
        if VIS[v] == tim:
            continue
        VIS[v] = tim
        if dfs(MATCH[v], graph, tim):
            MATCH[v] = u
            return 1

    return 0



def solve(N, A):
    for i in range(N+1):
        MATCH[i] = -1
        VIS[i] = False
    G = collections.defaultdict(list)
    cs = set()
    for r, row in enumerate(A):
        for c, v in enumerate(row):
            if v == 1:
                G[r].append(c)
                cs.add(c)

    if len(cs) != N:
        return 'No'

    return 'Yes' if sum([dfs(i, G, i+1) for i in range(N)]) == N else 'No'


if __name__ == '__main__':
    T = int(input())
    for ti in range(T):
        N = int(input())
        A = []
        for i in range(N):
            row = [int(x) for x in input().strip().split()]
            A.append(row)

        print(solve(N, A))