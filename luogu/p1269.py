# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/14

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

MAXN = 30000
MAXM = 10 ** 5
head = [-1 for _ in range(MAXN)]

to = [-1 for _ in range(MAXM)]
decay = [-1 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]

tot = [1]


def add(u, v, w):
    tot[0] += 1
    i = tot[0]
    to[i] = v
    decay[i] = w
    nxt[i] = head[u]
    head[u] = i


def draw():
    for u in range(MAXN):
        i = head[u]
        while i > 0:
            v = to[i]
            print('{} {}'.format(u, v))
            i = nxt[i]


def dfs(u, p, signal):
    a = 0
    rest = signal
    i = head[u]
    while i > 0:
        v = to[i]
        if v == p:
            i = nxt[i]
            continue
        c = decay[i]
        na, ns = dfs(v, u, signal)
        a += na
        if ns - c <= 0:
            a += 1
            # print('put', v)
            rest = min(rest, ns + signal - c)
        else:
            rest = min(rest, ns - c)
        
        i = nxt[i]
    
    return a, rest


if __name__ == '__main__':
    N = int(input())
    
    maxdist = 0
    for i in range(1, N + 1):
        row = [int(x) for x in input().split()]
        for j in range(1, len(row), 2):
            add(i, row[j], row[j + 1])
            maxdist = max(maxdist, row[j + 1])
    
    signal = int(input())
    if signal <= maxdist:
        print('No solution.')
        exit(0)
    # draw()
    
    add(0, 1, 0)
    add(1, 0, 0)
    a, s = dfs(0, -1, signal)
    print(a)