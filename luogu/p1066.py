# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def brutal(K, N):
    x = 2**K
    q = [[i] for i in range(1, x)]
    
    for i in range(N-1):
        nq = []
        for v in q:
            for a in range(v[-1]+1, x):
                nq.append(v + [a])
        q = nq
    
    q = [int(''.join(map(str, v))) for v in q]
    print(q)
    print(len(q))
    

def count(K, A, M):
    x = 2 ** K
    y = 2 ** M
    
    N = max(A) + 1
    dp = [[0 for _ in range(x)] for _ in range(N+1)]
    dp[0][0] = 1
    
    for v in range(1, min(x, y)):
        dp[1][v] = 1
    
    for i in range(2, N+1):
        for v in range(x):
            for pv in range(v):
                dp[i][v] += dp[i-1][pv]
    
    return sum([sum(dp[n]) for n in A])


def solve(K, W):
    ans = count(K, [num for num in range(2, W // K + 1)], K)
    
    if W % K != 0:
        ans += count(K, [W//K+1], W % K)
        
    return ans
    

if __name__ == '__main__':
    K, W = map(int, input().split())
    print(solve(K, W))
