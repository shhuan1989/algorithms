# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/6 21:07

"""

N = int(input())
A = [int(x) for x in input().split()]
#
# N = 1000
# A = [random.randint(0, 100) for _ in range(N)]

LP = sum(A) + 1
primes = [True] * LP
primes[0] = False
primes[1] = False
for i in range(LP):
    if primes[i]:
        t = i * 2
        while t < LP:
            primes[t] = False
            t += i

primes = {i for i in range(LP) if primes[i]}


groups = []
others = {(v, i+1) for i, v in enumerate(A)}
while True:
    outupdate = False
    oo = None
    g = []
    for vi in others:
        if vi[0] in primes:
            oo = vi
            outupdate = True
            g = [vi]
            s = vi[0]
            while True:
                o = None
                for ui in others:
                    update = False
                    if s + ui[0] in primes:
                        s += ui[0]
                        g.append(ui)
                        o = ui
                        update = True
                        break
                if not update:
                    break
                others.discard(o)
            break
    if not outupdate:
        break
    others.discard(oo)
    groups.append(g)

# print(A)
# print(groups)
# print(others)

while True:
    updated = False
    a, b = None, None
    for ui in others:
        for vi in others:
            if ui != vi and ui[0] + vi[0] in primes:
                update = True
                a, b = ui, vi
                break
    if updated:
        groups.append([a, b])
        others.discard(a)
        others.discard(b)
    else:
        break

ans = []
root = None
others = list(others)
if others:
    root = others[0]
    for o in others[1:]:
        ans.append((root[1], o[1]))
elif groups:
    g = groups[0]
    root = g[0]

    for i in range(len(g)-1):
        ans.append((g[i][1], g[i+1][1]))

    groups = groups[1:]

for g in groups:
    ans.append((root[1], g[0][1]))
    for i in range(len(g)-1):
        ans.append((g[i][1], g[i+1][1]))

# print(len(ans))

print('\n'.join([' '.join(map(str, edge)) for edge in ans]))