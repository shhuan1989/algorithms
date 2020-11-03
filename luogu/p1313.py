# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


sys.setrecursionlimit(2000)
if __name__ == '__main__':
    a, b, k, n, m = map(int, input().split())
    
    MOD = 10007
    memo = {}
    
    def dfs(px, py, pk):
        if pk == 0:
            return 1 if px == 0 and py == 0 else 0
        
        if px < 0 or py < 0 or px > pk or py > pk:
            return 0
        
        if pk == 1:
            if px == 0 and py == 1:
                return b % MOD
            elif py == 0 and px == 1:
                return a % MOD
            else:
                return 0
        
        key = (px, py, pk)
        if key in memo:
            return memo[key]
        
        u = dfs(px-1, py, pk-1)
        v = dfs(px, py-1, pk-1)
        
        memo[key] = (u * a + v * b) % MOD
        return memo[key]
    
    
    print(dfs(n, m, k))