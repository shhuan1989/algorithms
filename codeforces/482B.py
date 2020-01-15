# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/14/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, A):
    B = [0] * N

    for k in range(31):
        u = 1 << k
        add = [0 for _ in range(N)]
        for i, (l, r, v) in enumerate(A):
            if v & u > 0:
                add[l] += 1
                if r + 1 < N:
                    add[r + 1] -= 1
        a = 0
        for i, v in enumerate(add):
            a += v
            if a > 0:
                B[i] |= u
    # print(B)
    st = [0] * (N * 4)

    def build(index, nodel, noder):
        if nodel > noder:
            return (1 << 31) - 1
        if nodel == noder:
            st[index] = B[nodel]
            return B[nodel]
        else:
            m = (nodel + noder) // 2
            a = build(index * 2, nodel, m)
            b = build(index * 2 + 1, m + 1, noder)
            c = a & b
            st[index] = c
            return c

    def query(index, nodel, noder, targetl, targetr):
        if targetl > targetr:
            return (1 << 31) - 1

        if nodel == targetl and noder == targetr:
            return st[index]

        m = (nodel + noder) // 2
        a = query(index * 2, nodel, m, targetl, min(m, targetr))
        b = query(index * 2 + 1,m + 1, noder, max(m+1, targetl), targetr)
        c = a & b
        return c

    build(1, 0, N-1)
    for l, r, v in A:
        u = query(1, 0, N-1, l, r)
        if u != v:
            print('NO')
            return
    print('YES')
    print(' '.join(map(str, B)))


N, M = map(int, input().split())
A = []
for i in range(M):
    l, r, v = map(int, input().split())
    # A.append((l, v))
    # A.append((r, -v))
    A.append((l - 1, r - 1, v))

solve(N, M, A)