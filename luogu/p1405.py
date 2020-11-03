# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/22

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    while len(A) < N:
        A += [int(x) for x in input().split()]
    
    MAXN = 10010
    phi = [1 for _ in range(MAXN)]
    isp = [True for _ in range(MAXN)]
    primes = []
    for i in range(2, MAXN):
        if isp[i]:
            primes.append(i)
            phi[i] = i - 1
        
        for p in primes:
            x = p * i
            if x >= MAXN:
                break
            isp[x] = False
            if i % p == 0:
                phi[x] = phi[i] * p
            else:
                phi[x] = phi[i] * (p - 1)
                
    def gcd(x, y):
        while y:
            x, y = y, x%y
        return x
    
    # print(phi)
    # print(primes)

    MOD = 10007
    ans = A[-1] % phi[MOD]
    for i in range(N-2, -1, -1):
        ans += 0 if gcd(MOD, A[i]) == 1 else phi[MOD]
        ans = pow(A[i], ans, MOD)
        MOD = phi[MOD]
    
    print(ans)
        