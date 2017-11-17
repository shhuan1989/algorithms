# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/9/24 09:55

"""

N = int(input())

A = []
for i in range(N):
    w = input()
    wc = collections.Counter(w)
    if any(v > 1 for v in wc.values()):
        print("NO")
        exit(0)
    A.append(w)

E = {}
degree = collections.defaultdict(int)
chars = set()
for w in A:
    chars |= set(w)
    for i in range(len(w)-1):
        v = w[i]
        if v not in E:
            E[v] = w[i+1]
            degree[w[i+1]] += 1
        else:
            if E[v] != w[i+1]:
                print("NO")
                exit(0)

ans = ""
for start in [c for c in chars if degree[c] == 0]:
    while start:
        ans += start
        start = E[start] if start in E else ""

print(ans)