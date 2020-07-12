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
created by shhuan at 2020/7/10 19:24

"""


def build(N, G):
    q = [1]
    vis = {1}
    while True:
        u = q[-1]
        find = False
        for v in G[u]:
            if v not in vis:
                vis.add(v)
                q.append(v)
                find = True
                break
        if not find:
            break

    if len(q) != N:
        return []

    # for i in range(1, N-1):
    #     a, b, c = q[i-1], q[i], q[i+1]
    #     if a not in G[b] or c not in G[b]:
    #         return []
    # if q[1] not in G[q[0]] or q[-1] not in G[q[0]]:
    #     return []
    # if q[-2] not in G[q[-1]] or q[0] not in G[q[-1]]:
    #     return []

    return q


def find(path):
    n = len(path)
    wc = collections.defaultdict(int)

    for i, v in enumerate(path):
        u = i + 1
        d = v - u if v >= u else n-u+v
        wc[d] += 1

    return max(wc.values() or [0])


if __name__ == '__main__':
    N = int(input())
    G = collections.defaultdict(list)
    for i in range(1, N+1):
        a, b = map(int, input().split())
        G[i].append(a)
        G[i].append(b)

    # print(G)
    path = build(N, G)
    if not path or len(path) != N:
        print(-1)
        exit(0)

    # print(path)
    a = find(path)
    b = find(path[::-1])
    ans = N - max(a, b)
    print(ans)

