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
tail = set()
chars = set()
for w in A:
    chars |= set(w)
    for i in range(len(w)-1):
        u, v = w[i], w[i+1]
        if u not in E:
            E[u] = v
            tail.add(v)
        else:
            if E[u] != v:
                print("NO")
                exit(0)

ans = ""
for start in sorted(chars - tail):
    while start:
        if start in ans: # cycle
            print("NO")
            exit(0)
        ans += start
        start = E[start] if start in E else ""

if ans:
    wc = collections.Counter(ans)
    # ab, cb
    if any(v > 1 for v in wc.values()) or not all(c in ans for c in chars):
        print("NO")
    else:
        print(ans)
else:
    print("NO")