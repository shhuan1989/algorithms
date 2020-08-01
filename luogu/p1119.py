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
created by shhuan at 2020/7/15 20:41

"""




if __name__ == '__main__':

    N, M = map(int, input().split())
    T = [int(x) for x in input().split()]

    W = [[float('inf') for _ in range(N)] for _ in range(N)]
    G = collections.defaultdict(list)
    for i in range(M):
        u, v, w = map(int, input().split())
        W[u][v] = w
        W[v][u] = w
        G[u].append(v)
        G[v].append(u)
    for u in range(N):
            W[u][u] = 0

    Q = int(input())
    queries = []
    for i in range(Q):
        u, v, t = map(int, input().split())
        queries.append((t, u, v, i))

    built = [False for _ in range(N)]
    built_list = []
    ans = [-1 for _ in range(Q)]
    now = 0
    for t, u, v, i in queries:
        while now < N and T[now] <= t:
            for start in range(N):
                for end in range(N):
                    W[start][end] = min(W[start][end], W[start][now] + W[now][end])
            now += 1
        if T[u] > t or T[v] > t:
            ans[i] = -1
        else:
            ans[i] = W[u][v] if W[u][v] < float('inf') else -1

    print('\n'.join(map(str, ans)))









