# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/15

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache


def solve(n, M, fixed):
    
    
    def check():
        p = [0 for _ in range(n+1)]
        for u, v in fixed:
            i = v
            find = False
            while i <= n:
                if p[i] == 0:
                    p[i] = u
                    find = True
                    break
                i += 1
            if not find:
                return False
            
        return True
    
    
    if not check():
        print('NO')
        return
    
    fixedmap = {u: v for u, v in fixed}
    
    @lru_cache(maxsize=None)
    def ncr(c, r):
        if r > c:
            return 0
        if c == r or r == 0:
            return 1
        if r > c - r:
            return ncr(c, c - r)
        return ncr(c - 1, r) + ncr(c - 1, r - 1)
    
    @lru_cache(maxsize=None)
    def invalid_place(x):
        if x <= 1:
            return 0
        
        dp = [0 for _ in range(x + 1)]
        # dp[2] = 1
        
        for i in range(2, x + 1):
            dp[i] = dp[i - 1] * (x if i not in fixedmap else 1)
            dp[i] %= MOD
            for c in range(1 if i not in fixedmap else x - fixedmap[i] + 1, i):
                
                # select c nums from previous i-1 nums to put them at end of queue
                # pos in [x-c+1, x]
                
                must = len([1 for u, v in fixed if x-c+1 <= v <= x])
                if must > c:
                    continue
                elif must == c:
                    dp[i] += pow(x - c - 1, i - 1 - c, MOD) * c
                else:
                    rest = i-must-1
                    choose = c-must
                    dp[i] += ncr(rest, choose) * (pow(c, choose, MOD) + MOD - invalid_place(c))
                
                
                # dp[i] += ncr(i - 1, c) * ((pow(c, c, MOD) + MOD - invalid_place(c)) % MOD) * pow(x - c - 1, i - 1 - c,
                #                                                                                  MOD) * c
                dp[i] %= MOD
        
        return dp[-1]
    
    print('YES {}'.format((pow(n, n, M) + M - invalid_place(n)) % M))

if __name__ == '__main__':
    MOD = 10**9+7
    
    T = int(input())
    
    for _  in range(T):
        n, m, M = map(int, input().split())
        fixed = []
        if m > 0:
            row = [int(x) for x in input().split()]
            for i in range(0, len(row), 2):
                fixed.append((row[i], row[i+1]))
        solve(n, M, fixed)
    
