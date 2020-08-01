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
created by shhuan at 2020/7/18 13:53

"""


if __name__ == '__main__':

    N, A, B = map(int, input().split())
    K = [0] + [int(x) for x in input().split()]

    INF = 10**7
    dist = [INF for _ in range(N+1)]
    dist[A] = 0
    q = [(0, A)]
    heapq.heapify(q)
    while q:
        d, u = heapq.heappop(q)
        for v in [u+K[u], u-K[u]]:
            if 0 < v <= N and dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                heapq.heappush(q, (dist[v], v))

    print(dist[B] if dist[B] < INF else -1)


