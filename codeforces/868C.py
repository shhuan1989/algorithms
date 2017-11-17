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

N, K = map(int, input().split())

problems = collections.defaultdict(set)
for i in range(N):
    row = tuple([int(x) for x in input().split()])
    k = sum(row)
    if k == 0:
        print('YES')
        exit(0)
    elif k < K:
        for i in range(K):
            if row[i] == 0:
                problems[i].add(row)

if not problems:
    print('NO')
    exit(0)


for p1 in problems[0]:

    idx = [i for i in range(K) if p1[i] == 1]
    if not idx:
        print("YES")
        exit(0)

    p2s = problems[idx[0]]

    for p2 in p2s:
        if all(p2[i] == 0 for i in idx):
            print("YES")
            exit(0)


print("NO")



