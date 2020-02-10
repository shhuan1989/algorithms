# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/15/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


MAXN = 3 * 10 ** 5 + 5
F = [1 for _ in range(MAXN)]
MOD = 998244353
for i in range(2, MAXN):
    F[i] = (i * F[i-1]) % MOD


def solve(N, A):
    va = [a for a, b in A]
    wa = collections.Counter(va)
    bada = 1
    for c in wa.values():
        bada *= F[c]
        bada %= MOD
    
    vb = [b for a, b in A]
    wb = collections.Counter(vb)
    badb = 1
    for c in wb.values():
        badb *= F[c]
        badb %= MOD
    
    badab = 0
    A.sort()
    if all([A[i][0] <= A[i+1][0] and A[i][1] <= A[i+1][1] for i in range(N-1)]):
        badab = 1
        wab = collections.Counter(A)
        for c in wab.values():
            badab *= F[c]
            badab %= MOD
            
    total = F[N]
    ans = (2 * MOD + total - bada - badb + badab) % MOD
    
    # print(total, bada, badb, badab)
    print(ans)
    

N = int(input())
A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append((a, b))

solve(N, A)