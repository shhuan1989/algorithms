# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/11/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


N, M = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

f = False
if N < M:
    f = True
    N, M = M, N
    A, B = B, A

A = [(v, i) for i, v in enumerate(A)]
B = [(v, i) for i, v in enumerate(B)]
A.sort()
B.sort()

ans = [(i, B[0][1]) for i in range(N)]
vals = {a[0]+B[0][0] for a in A}
ai = 0
for bi in range(1, M):
    b = B[bi]
    while A[ai][0] + b[0] in vals:
        ai = (ai+1) % N

    vals.add(A[ai][0] + b[0])
    ans.append((A[ai][1], b[1]))


if f:
    ans = [(j, i) for (i, j) in ans]
    A, B = B, A

# print(ans)
print('\n'.join(['{} {}'.format(i, j) for i, j in ans]))
# print('\n'.join(['{} {} {}'.format(A[i][0]+B[j][0], A[i][1], B[j][1]) for i, j in ans]))