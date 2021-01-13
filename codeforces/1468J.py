# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2021/1/4

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


MAXN = 2 * 10 ** 5 + 5
parent = [i for i in range(MAXN)]


def find(u):
    pu = parent[u]
    if pu == u:
        return pu
    pu = find(pu)
    parent[u] = pu
    return pu


def merge(u, v):
    pu, pv = find(u), find(v)
    parent[pu] = pv
    return pu != pv


def solve(n, m, k, edges):
    edges.sort()
    for i in range(n+1):
        parent[i] = i
    
    groups = n
    ans = 0
    for i, (s, u, v) in enumerate(edges):
        if s <= k:
            if merge(u, v):
                groups -= 1
        else:
            if groups == 1:
                return min(k - edges[i-1][0], s - k)
            if merge(u, v):
                groups -= 1
                ans += s - k
            if groups == 1:
                return ans
    
    return k - edges[-1][0]


if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        n, m, k = map(int, input().strip().split())
        edges = []
        for _ in range(m):
            u, v, s = map(int, input().split())
            edges.append((s, u, v))
        ans.append(solve(n, m, k, edges))
    
    print('\n'.join(map(str, ans)))
    
    
    