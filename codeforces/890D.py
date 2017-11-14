# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/13 00:56

"""

N = int(input())
A = []
for i in range(N):
    A.append(input())


WC = collections.defaultdict(int)
P = collections.defaultdict(str)
for a in A:
    wc = collections.Counter(a)
    if any([v > 1 for v in wc.values()]):
        print('NO')
        exit(0)
    for c in a:
        WC[c] += 1

    # P[a[0]].append(a)
    if a[0] not in P:
        P[a[0]] = a
    else:
        b = P[a[0]]
        if len(a) < len(b):
            a, b = b, a
        if a.find(b) < 0:
            print('NO')
            exit(0)
        else:
            P[a[0]] = a


def connect(start, vals, pre):
    for v in vals:
        if set(start) & set(v):
            for k in range(max(0, len(start)-len(v)), len(start)):
                l = len(start)-k
                if start[k:] == v[:l]:
                    return connect(start[:k]+v, vals-{v}, pre+v[l:])

    return pre


ps = set(P.values())
vals = [connect(s, ps - {s}, s) for s in ps]

vals = [v for v in vals if all([x.find(v) < 0 for x in vals if x != v])]

# res = []
# for a in vals:
#     f = True
#     for b in vals:
#         if a != b and b.find(a) >= 0:
#             f = False
#             break
#     if not f:
#         res.append(a)

# print(vals)

ans = "".join(sorted(vals))
wc = collections.Counter(ans)
if any([v > 1 for v in wc.values()]):
    print("NO")
else:
    print(ans)


















