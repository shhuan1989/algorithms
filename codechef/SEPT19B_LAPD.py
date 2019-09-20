# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/11 21:30

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List

# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/11/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
import math

MOD = 10 ** 9 + 7

def mul(x, y):
    if y == 0:
        return 0
    if y == 1:
        return x

    if y % 2 == 0:
        return (mul(x, y//2)*2) % MOD

    return (mul(x, y // 2) * 2 + x) % MOD

# X = [0 for _ in range(5000)]

# b**2 < (a-1)*(c-1)
def solve(A, B, C):
    if A == 1 or C == 1:
        return 0

    ans = 0
    pc, pa = 0, 0
    pp, pb, pb2 = 0, 0, 0
    for b in range(1, B + 1):
        b2 = b ** 2
        a = max(A - (b + 1), 0)
        c = max(C - (b + 1), 0)
        if a > 0 and c > 0:
            pp += 1
            pb += b+1
            pb2 += (b+1)**2


        # ans += a*c
        # ans %= MOD

        al, ar = max(b2//(C-1)+1, 1), min(A, b + 1)
        if ar > al:
            pc += ar-al
            ans += MOD - sum([b2 // a for a in range(al, min(ar, b2//2+1))]) - max(0, ar-b2//2-1)
            ans %= MOD

        cl, cr = max(b2//(A-1)+1, 1), min(C, b + 1)
        if cr > cl:
            pa += cr-cl
            ans += MOD - sum([b2 // c for c in range(cl, min(cr, b2//2+1))]) - max(0, cr-b2//2-1)
            ans %= MOD

    ans += pc*(C-1)
    ans %= MOD
    ans += pa*(A-1)
    ans %= MOD
    ans += A*C*pp
    ans %= MOD
    ans += pb2
    ans %= MOD
    ans = ans + MOD - pb*(A+C)
    ans %= MOD

    print(pc, pa, B)
    return ans



import random
t0 = time.time()
for i in range(10):
    A, B, C = random.randint(10**8, 10**9), random.randint(4000, 5000), random.randint(10**8, 10**9)
    # A, B, C = random.randint(4000, 5000), random.randint(4000, 5000), random.randint(4000, 5000)


    print(solve(A, B, C))
print(time.time() - t0)


T = int(input())
for ti in range(T):
    A, B, C = map(int, input().split())
    print(solve(A, B, C))