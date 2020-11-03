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
    p, q, a1, a2, n, m = map(int, input().split())
    
    if n == 1:
        print(a1 % m)
        exit(0)
    
    if n == 2:
        print(a2 % m)
        exit(0)
    
    MOD = m
    
    def mul(a, b):
        c = [[0, 0], [0, 0]]
        
        for i in range(2):
            for j in range(2):
                c[i][j] = sum([x*y for x, y in zip(a[i], [b[br][j] for br in range(2)])]) % MOD
        
        return c
    
    def mypow(a, k):
        ans = [row.copy() for row in a]
        k -= 1
        while k > 0:
            if k & 1:
                ans = mul(ans, a)
            a = mul(a, a)
            k //= 2
        
        return ans
    
    def mypow2(a, k):
        if k == 1:
            return [row.copy() for row in a]
        
        b = mypow2(a, k//2)
        
        b = mul(b, b)
        if k % 2 == 0:
            return b
        return mul(a, b)


    a = [
        [p, 1],
        [q, 0]
    ]
    
    xa = mypow(a, n-2)
    # xb = mypow2(a, n-2)
    # print(xa)
    # print(xb)
    
    ans = a2*xa[0][0] + a1*xa[1][0]
    ans %= MOD
    
    print(ans)