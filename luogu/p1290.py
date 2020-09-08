# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


from functools import lru_cache

def solve(M, N):
    
    @lru_cache(maxsize=None)
    def dfs(a, b):
        if a % b == 0 or b % a == 0:
            return True
        if a < b:
            return dfs(b, a)
        
        for k in range(1, a // b + 1):
            if not dfs(a-b*k, b):
                return True
        
        return False
    
    return dfs(M, N)
    

if __name__ == '__main__':
    C = int(input())
    
    for _ in range(C):
        M, N = map(int, input().split())
        win = solve(M, N)
        print('Stan wins' if win else 'Ollie wins')