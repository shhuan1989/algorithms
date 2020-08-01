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
created by shhuan at 2020/7/17 22:24

"""

if __name__ == '__main__':
    MOD = 100003
    N, M = map(int, input().strip().split())
    G = collections.defaultdict(list)
    for i in range(M):
        u, v = map(int, input().strip().split())
        G[u].append(v)
        G[v].append(u)

    ans = [0 for _ in range(N+1)]
    dist = [N+1 for i in range(N+1)]
    dist[1] = 0
    ans[1] = 1

    q = collections.deque([1])
    while q:
        u = q.popleft()
        for v in G[u]:
            nd = dist[u] + 1
            if dist[v] > nd:
                dist[v] = nd
                ans[v] = ans[u]
                q.append(v)
            elif dist[v] == nd:
                ans[v] += ans[u]
                ans[v] %= MOD


    # print(dist)
    # print(ans)
    print('\n'.join(map(str, [x%100003 for x in ans[1:]])))




