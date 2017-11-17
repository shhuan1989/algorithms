# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/5 15:00

"""

N = int(input())
S = ['']
head = [""]
tail = [""]
for i in range(N):
    S.append(input())
    head.append(S[i][:10])
    tail.append(S[i][:-10])


M = int(input())

A = [[set() for _ in range(10)] for _ in range(M+N+1)]
C = collections.defaultdict(tuple)
D = collections.defaultdict(int)

for i in range(1, N+1):
    for j in range(1, 10):
        s = S[i]
        if j > len(s):
            break
        for k in range(len(s)-j+1):
            A[i][j].add(int(s[k:k+j], 2))

        if all(v in A[i][j] for v in range(2**j)):
            D[i] = j

for i in range(M):
    a, b = map(int, input().split())
    s = S[a] + S[b]
    S.append(s)
    head.append(s[:10])
    tail.append(s[:-10])

    ai = i+N+1
    C[ai] = (a, b)

    d = max(D[a], D[b]) + 1
    for dv in range(d, 10):
        if len(S[i]) + len(S[b]) < dv:
            break
        A[ai][dv] = {int(S[a][-i:] + S[b][:dv-i], 2) for i in range(1, dv+1)}

    q = [(ai)]
    oz = set()
    while q:
        x = q.pop()
        if x in C:
            q.append(C[x][0])
            q.append(C[x][1])
        oz |= A[x][d]

    if all(v in oz for v in range(2**d)):
        print(d)
        D[ai] = d
    else:
        print(d-1)
        D[ai] = d-1










