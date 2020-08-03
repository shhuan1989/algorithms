# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
from functools import lru_cache

if __name__ == '__main__':
    # sys.stdin = open('P1156_5.in', 'r')
    D, G = map(int, input().split())
    A = [(0, 10, 0)]
    for i in range(G):
        t, f, h = map(int, input().split())
        A.append((t, f, h))
    
    A.sort()
    
    # dp = [[float('-inf') for _ in range(D+1)] for _ in range(G+1)]
    # dp[0][0] = 10
    #
    # for i in range(1, G+1):
    #     for h in range(D+1):
    #         d = A[i][0] - A[i-1][0]
    #         if dp[i-1][h] >= d:
    #             dp[i][h] = max(dp[i][h], dp[i-1][h] + A[i][1] - d)
    #         if dp[i-1][h-A[i][2]] >= d:
    #             dp[i][h] = max(dp[i][h], dp[i-1][h-A[i][2]] - d)
    
    @lru_cache(maxsize=None)
    def dfs(index, height):
        if index == 0:
            return 10 if height <= 0 else float('-inf')
        
        d = A[index][0] - A[index-1][0]
        a = dfs(index-1, height)
        b = dfs(index - 1, height - A[index][2])
        ans = float('-inf')
        if a >= d:
            ans = max(ans, a+A[index][1]-d)
        if b >= d:
            ans = max(ans, b-d)
        return ans
    
    
    # print(A)
    for i, (t, f, h) in enumerate(A):
        health = dfs(i, D)
        if health >= 0:
            print(t)
            exit(0)
            
    health = 10
    live = 10
    for i in range(1, G+1):
        health -= A[i][0] - A[i-1][0]
        if health < 0:
            break
        
        health += A[i][1]
        live += A[i][1]
    
    print(live)
    