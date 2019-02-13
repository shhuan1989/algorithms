# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/15/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


def pow2(n, mod):
    if n == 0:
        return 1
    if n == 1:
        return 2
    
    h = pow2(n // 2, mod)
    
    if n % 2 == 0:
        return (h * h) % mod
    else:
        return (h * h * 2) % mod
    
    
MOD = 998244353
N = int(input())
A = [int(x) for x  in  input().split()]

S, T = {}, {}
for i, v in enumerate(A):
    if v not in S:
        S[v] = i
    else:
        T[v] = i

segs = [(S[k], v) for k, v in T.items()]
segs.sort()

# print(segs)

if not segs:
    print(pow2(N-1, MOD))
else:
    i = 1
    s, t = segs[0]
    segCount = s
    while i < len(segs):
        seg = segs[i]
        if seg[0] <= t:
            t = max(t, seg[1])
        else:
            segCount += seg[0] - t
            s, t = seg
        i += 1
    segCount += N - t
    print(pow2(segCount-1, MOD))
