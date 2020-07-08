# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/5

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


N, M = map(int, input().split())
G = collections.defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

desire = [0] + [int(v) for v in input().split()]

desiredict = collections.defaultdict(list)
maxdesire = max(desire)
for i in range(1, N+1):
    desiredict[desire[i]].append(i)

if maxdesire > N:
    print(-1)
    exit(0)

mark = [0 for _ in range(N+1)]
ans = []
for p in range(1, maxdesire+1):
    for u in desiredict[p]:
        s = set()
        for v in G[u]:
            if desire[v] == p or mark[v] >= p:
                print(-1)
                exit(0)
            if mark[v] > 0:
                s.add(mark[v])

        if len(s) != p-1:
            print(-1)
            exit(0)
            
        mark[u] = p
        ans.append(u)
        
print(' '.join(map(str, ans)))