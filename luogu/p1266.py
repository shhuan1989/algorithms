# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/14 08:25

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

MAXN = 200
MAXM = 10**5

head = [-1 for _ in range(MAXN)]

to = [-1 for _ in range(MAXM)]
L = [-1 for _ in range(MAXM)]
speed = [-1 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]

tot = [1]


def add(u, v, w, s):
    tot[0] += 1
    i = tot[0]

    to[i] = v
    L[i] = w
    speed[i] = s
    nxt[i] = head[u]
    head[u] = i

def argmin(a):
    t = float('inf')
    ti = -1
    for i, v in enumerate(a):
        if v < t:
            t = v
            ti = i

    return ti


def spfa(start, end, speeds):
    speeds = list(sorted(speeds))
    si = {s: i for i, s in enumerate(speeds)}
    S = len(speeds)

    print(speeds)

    dist = [[float('inf') for _ in range(S)] for _ in range(MAXN)]
    pre = [[-1 for _ in range(S)] for _ in range(MAXN)]

    q = collections.deque([(start, si[70])])
    dist[start][si[70]] = 0


    while q:
        u, s = q.popleft()
        i = head[u]
        while i > 0:
            ns = s if speed[i] == 0 else si[speed[i]]
            v = to[i]
            nt = dist[u][s] + L[i]/ns
            if dist[v][ns] > dist[u][s] + nt:
                dist[v][ns] = dist[u][s] + nt
                pre[v][ns] = u
                q.append((v, ns))
            i = nxt[i]

    print(dist[:N+1])

    s = argmin(dist[end])
    path = []
    u = end
    while u != start:
        path.append(u)
        u = pre[u][s]
        s = argmin(dist[u])

    path.append(start)

    return path[::-1]




if __name__ == '__main__':
    sys.stdin = open('p1266.in', 'r')
    N, M, D = map(int, input().split())
    speeds = {70}
    for i in range(M):
        u, v, s, w = map(int, input().split())
        add(u, v, w, s)
        speeds.add(s)


    print(' '.join(map(str, spfa(0, D, speeds))))