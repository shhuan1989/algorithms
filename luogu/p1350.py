# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    A, B, C, D, K = map(int, input().split())
    MOD = 10**5+3
    
    MAXN = 2010
    
    fac = [1 for _ in range(MAXN)]
    ifac = [1 for _ in range(MAXN)]
    fac[1] = 1
    for i in range(2, MAXN):
        fac[i] = (fac[i-1] * i) % MOD
        
    for i in range(1, MAXN):
        ifac[i] = pow(fac[i], MOD-2, MOD)
        
    
    # print(fac[1:10])
    # print(ifac[1:10])
    
    def perm(n, c):
        return (fac[n] * ifac[n-c]) % MOD
    
    
    def comb(n, c):
        return (((fac[n] * ifac[n-c]) % MOD) * ifac[c]) % MOD
    
    
    # A * B
    ans = 0
    for x in range(min(K, A, B)+1):
        y = K - x
        if 0 <= y <= min(A+C, D):
            a = (comb(A, x) * perm(B, x)) % MOD
            b = (comb(A+C-x, y) * perm(D, y)) % MOD
            
            # if a * b > 0:
            #     print(x, y, a, b)
            ans += a * b
            ans %= MOD
            
    print(ans)
    
        
    