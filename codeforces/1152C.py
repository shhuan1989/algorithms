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
import math

MAXN = 10 ** 6 + 5
p = [True for _ in range(MAXN)]
p[0] = p[1] = False
for i in range(2, MAXN):
    if p[i]:
        v = i + i
        while v < MAXN:
            p[v] = False
            v += i

PRIMES = [i for i in range(MAXN) if p[i]]


def gcd(x, y):
    while y:
        x, y = y, x % y
    
    return x


def defact(val):
    factors = []
    
    for p in PRIMES:
        if p > val:
            break
        if val % p == 0:
            factors.append(p)
            while val % p == 0:
                val //= p
    if val > 1:
        factors.append(val)
    return factors


def solve(A, B):
    A, B = min(A, B), max(A, B)
    
    lcm = A * B // gcd(A, B)
    ans = 0
    u = B-A
    for v in range(1, min(u, int(math.sqrt(u)) + 1) + 1):
        if u % v == 0:
            for w in [v, u//v]:
                if A % w != 0:
                    k = w - A % w
                    x = (A+k) * (B+k) // gcd(A+k, B+k)
                    if x < lcm:
                        lcm = x
                        ans = k
    return ans
            
    
A, B = map(int, input().split())
print(solve(A, B))