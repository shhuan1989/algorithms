# -*- coding: utf-8 -*-
"""
created by shhuan at 2018/10/20 22:37

"""
import collections
"""
# Definition for a Node.
"""



N, M = map(int, input().split())


A = [[0, 0]]
D = [(float('-inf'), 0, 0, 0)]
for i in range(N):
    x, y = map(int, input().split())
    A.append([x, y])
    D.append((x-y, x, y, i+1))

D.sort()

G = collections.defaultdict(set)
ans = [0 for _ in range(N+1)]
for i in range(M):
    u, v = list(sorted([int(x) for x in input().split()]))
    G[u].add(v)

righty = [0] * (N+2)
leftx = [0] * (N+2)
for i in range(N, -1, -1):
    righty[i] = righty[i+1] + D[i][2]
for i in range(1, N+1):
    leftx[i] = leftx[i-1] + D[i][1]

for id in range(1, N+1):
    d, x, y, i = D[id]
    ans[i] += righty[id+1] + x*(N-id)
    ans[i] += leftx[id-1] + y*(id-1)

    ans[i] -= sum([min(x+A[v][1], y + A[v][0]) for v in G[i]] or [0])

print(' '.join(map(str, ans[1:])))
