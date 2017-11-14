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
created by shhuan at 2017/11/14 11:20

"""


eps = 1e-5
# N = int(input())
# A = []
# for i in range(N):
#     x, y = map(int, input().split())
#     A.append((x, y))
#

N = 200
A = [(random.randint(-1000, 1000), random.randint(-1000, 1000)) for _ in range(N)]
if N <= 2:
    print(-1)
    exit(0)

t0 = time.time()
center = sum([x for x, _ in A])/N, sum([y for _, y in A])/N


def sym(a, b, c):
    return abs((a[0]+b[0])/2-c[0]) < eps and abs((a[1]+b[1])/2-c[1]) < eps

symed = set()

for i in range(N):
    for j in range(i+1, N):
        a, b = A[i], A[j]
        if sym(a, b, center):
            symed.add(a)
            symed.add(b)

left = [v for v in A if v not in symed]
print(time.time() - t0)
print(len(left))

if not left or len(left) <= 2:
    print(-1)
    exit(0)

ans = 0
lines = set()

for i in range(len(left)):
    for j in range(i+1, len(left)):
        a, b = left[i], left[j]
        if a != b:
            c = (a[0]+b[0])/2, (a[1]+b[1])/2
            line = c[1] - center[1], center[0] - c[0]
            if abs(line[0]) < eps and abs(line[1]) < eps:
                print(-1)
                exit(0)
            if abs(line[0]) > eps and abs(line[1]) > eps:
                k = "%.6f" % (line[1]/line[0])
                lines.add(k)

print(time.time() - t0)
print(len(lines))

def project(point, k):
    x, y = point
    x1 = (k*y+x)/(k**2+1)
    y1 = k*x1

    return (x1, y1)

def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1-x2)**2 + (y1-y2)**2


def check(points, center, k):
    ps = set()
    for a in points:
        b = project(a, k)
        ps.add(b)
    c = project(center, k)
    ds = collections.defaultdict(int)
    for p in ps:
        d = dist(c, p)
        if d > eps:
            d = "%.6f" % d
            ds[d] += 1

    if all(v % 2 == 0 for v in ds.values()):
        return True
    return False

# print(lines)
for k in {float(k) for k in lines}:
    # y = kx
    if check(left, center, k):
        ans += 1

# project to y axis
ps = {v[1] for v in left}
ds = collections.defaultdict(int)
for p in ps:
    d = abs(p-center[1])
    if d > eps:
        d = "%.6f" % (d)
        ds[d] += 1
if ds and all(v % 2 == 0 for v in ds.values()):
    ans += 1

#project to x axis
ps = {v[0] for v in left}
ds = collections.defaultdict(int)
for p in ps:
    d = abs(p-center[0])
    if d > eps:
        d = "%.6f" % (d)
        ds[d] += 1
if ds and all(v % 2 == 0 for v in ds.values()):
    ans += 1

print(ans)












