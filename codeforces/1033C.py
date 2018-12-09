# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/22/18

"""
import collections

N = int(input())
A = [int(x) for x in input().split()]


grev = collections.defaultdict(set)
g = collections.defaultdict(set)
degree = collections.defaultdict(int)
for i in range(N):
    d = 0
    for j in range(i+A[i], N, A[i]):
        if A[j] > A[i]:
            grev[j].add(i)
            g[i].add(j)
            d += 1
    for j in range(i-A[i], -1, -A[i]):
        if A[j] > A[i]:
            grev[j].add(i)
            g[i].add(j)
            d += 1

    degree[i] = d 

ans = [0] * N


left = {i for i in range(N)}
while left:
    used = set()
    for v in left:
        if degree[v] == 0:
            if all([ans[i] == 2 for i in g[v]] or [True]):
                ans[v] = 1
            else:
                ans[v] = 2
    
            used.add(v)
    for v in used:
        for u in grev[v]:
            degree[u] -= 1
    left -= used

print(''.join(['B' if ans[i] == 1 else 'A' for i in range(N)]))




