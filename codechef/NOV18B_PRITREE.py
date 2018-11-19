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


# import random
# N = 1000
# A = [random.randint(0, 100) for _ in range(N)]
# print(A)
# A = [90, 62, 21, 93, 55, 7, 68, 24, 95, 60]

# print('starting')

LP = sum(A) + 1
PRIMES = [True] * LP
PRIMES[0] = False
PRIMES[1] = False
for i in range(LP):
    if PRIMES[i]:
        t = i * 2
        while t < LP:
            PRIMES[t] = False
            t += i


def longestPrimePath(start, indice):
    q = [start]
    total = A[start]
    while True:
        add = float('inf')
        adi = -1
        for v in indice:
            if PRIMES[total+A[v]]:
                if total + A[v] < add:
                    add = total + A[v]
                    adi = v
        if adi < 0:
            break
        q.append(adi)
        total = add
        indice.remove(adi)
    return q


primeIdx = [(A[i], i) for i in range(N) if PRIMES[A[i]]]
primeIdx.sort()
primeIdx = [x[1] for x in primeIdx]

others = {i for i in range(N)}
groups = []
for start in primeIdx:
    if start in others:
        others.remove(start)
        ps = longestPrimePath(start, others)
        groups.append(ps)

idxMap = {}
for g in groups:
    total = sum([A[i] for i in g])
    A.append(total)
    ndi = len(A) - 1
    others.add(ndi)
    idxMap[ndi] = g[-1]

groups2 = []
if others:
    # find other elements that can be make prime
    # if sum of any two elements is prime
    while True:
        found = False
        a, b = -1, -1
        for u in others:
            if found:
                break
            for v in others:
                if u != v and PRIMES[A[u]+A[v]]:
                    a, b = u, v
                    found = True
        if found:
            g = [a, b]
            total = A[a] + A[b]
            others.remove(a)
            others.remove(b)

            while True:
                found = False
                for u in others:
                    if PRIMES[total+A[u]]:
                        g.append(u)
                        found = True
                        break
                if found:
                    others.remove(g[-1])
                else:
                    break
            groups2.append(g)
        else:
            break

    # if sum of any three elements is prime
    while True:
        found = False
        a, b, c = -1, -1, -1
        for x in others:
            if found:
                break
            for y in others:
                if found:
                    break
                if x != y:
                    for z in others:
                        if z != x and z != y and PRIMES[A[x]+A[y]+A[z]]:
                            a, b, c = x, y, z
                            found = True
                            break
        if found:
            g = [a, b, c]
            total = A[a] + A[b] + A[c]
            others.remove(a)
            others.remove(b)
            others.remove(c)
            while True:
                found = False
                for u in others:
                    if PRIMES[total + A[u]]:
                        found = True
                        g.append(u)
                if found:
                    others.remove(g[-1])
                else:
                    break
            groups2.append(g)
        else:
            break

    # if sum of any count of elements is prime
    while others:
        q = [(0, [])]
        g = []
        found = False
        for u in others:
            if found:
                break
            nq = []
            for t, c in q:
                nt = t + A[u]
                nc = c + [u]
                if PRIMES[nt] and len(nc) > 1:
                    g = nc
                    found = True
                    break
                else:
                    nq.append((nt, nc))
            q.extend(nq)
        if found:
            # g.sort()
            groups2.append(g)
            others -= set(g)
        else:
            break
else:
    pass


# connect groups

ans = []
for g in groups:
    for i in range(len(g)-1):
        ans.append((g[i], g[i+1]))

for g in groups2:
    for i in range(len(g)-1):
        a = g[i] if g[i] < N else idxMap[g[i]]
        b = g[i+1] if g[i+1] < N else idxMap[g[i+1]]
        ans.append((a, b))

if others:
    others = list(others)
    for i in range(len(others)-1):
        a = others[i] if others[i] < N else idxMap[others[i]]
        b = others[i+1] if others[i+1] < N else idxMap[others[i+1]]
        ans.append((a, b))

    node = others[-1] if others[-1] < N else idxMap[others[-1]]
    for g in groups2:
        ans.append((g[-1] if g[-1] < N else idxMap[g[-1]], node))
else:
    if groups2:
        if len(groups2) > 1:
            node = groups2[-1][-1] if groups2[-1][-1] < N else idxMap[groups2[-1][-1]]
            for g in groups2[:-1]:
                ans.append((g[-1] if g[-1] < N else idxMap[g[-1]], node))
    else:
        if len(groups) > 1:
            for g in groups[:-1]:
                ans.append((g[-1], groups[-1][-1]))

ans = [(u+1, v+1) for (u, v) in ans]
print('\n'.join(['{} {}'.format(u, v) for u, v in ans]))


# print(len(ans))
