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

MOD = 2 ** 50 + 7
MAXN = 5 * 10 ** 6 + 5
HASH = [0 for _ in range(MAXN)]
HASH[0] = 1
for i in range(1, MAXN):
    # only contains char 'a', 'b', 'c'
    h = HASH[i-1] * 3
    h %= MOD
    HASH[i] = h
    

def polyhash(val):
    h = 0
    for i, v in enumerate(val):
        h += (ord(v) - ord('a') + 1) * HASH[i]
        h %= MOD
    return h


def check(word, hashvals):
    h = polyhash(word)
    for i, w in enumerate(word):
        u = (ord(w) - ord('a') + 1)
        nh = (h + MOD - u * HASH[i]) % MOD
        for v in range(1, 4):
            nh = (nh + HASH[i]) % MOD
            if v != u and nh in hashvals:
                return True
    return False


def solve(N, M, A, B):
    hashvals = {polyhash(w) for w in A}
    ans = []
    for v in B:
        ans.append(check(v, hashvals))
    return ans
    

N, M = map(int, input().split())
A = []
for i in range(N):
    s = input()
    A.append(s)
    
B = []
for i in range(M):
    word = input()
    B.append(word)

ans = solve(N, M, A, B)
print('\n'.join(['YES' if v else 'NO' for v in ans]))
