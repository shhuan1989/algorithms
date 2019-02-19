# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/14/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

N, M, P = map(int, input().split())

S = [int(x) for x in input().split()]

A = []
castles = collections.defaultdict(list)
for i in range(N):
    row = [0 if v == '.' else (-1 if v == '#' else int(v)) for v in list(input())]
    A.append(row)
    for j, v in enumerate(row):
        if 1 <= v <= P:
            castles[int(v)].append((i, j))


q = [(p, castles[p]) for p in range(1, P+1)]

# print(q)

while q:
    p, cs = q.pop(0)
    ncs = []
    for r, c in cs:
        nq = [(0, r, c)]
        heapq.heapify(nq)
        while nq:
            s, x, y = heapq.heappop(nq)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = x+dr, y+dc
                if 0 <= nr < N and 0 <= nc < M and A[nr][nc] == 0:
                    A[nr][nc] = p
                    ncs.append((nr, nc))
                    if s+1 < S[p-1]:
                        heapq.heappush(nq, (s+1, nr, nc))
    if ncs:
        q.append((p, ncs))


ans = collections.defaultdict(int)
for row in A:
    # print(row)
    for v in row:
        ans[v] += 1

print(' '.join(map(str, [ans[p] for p in range(1, P+1)])))