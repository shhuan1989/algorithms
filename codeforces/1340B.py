# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
from functools import lru_cache


NUMS_REP = ['1110111', '0010010', '1011101', '1011011', '0111010', '1101011', '1101111', '1010010', '1111111', '1111011']


def diff(s, t):
    d = 0
    for i in range(7):
        sone = (s & (1 << i)) > 0
        tone = (t & (1 << i)) > 0
        if sone and not tone:
            return -1
        if not sone and tone:
            d += 1
            
    return d


def str2int(s):
    v = 0
    for c in s:
        v <<= 1
        v |= 1 if c == '1' else 0
    
    return v


NUMS = [str2int(s) for s in NUMS_REP]


dist = [[0 for _ in range(10)] for _ in range(128)]
for s in range(128):
    for t in range(10):
        dist[s][t] = diff(s, NUMS[t])



def solve(N, K, A):
    A = [0] + A[::-1]
    dp = [[False for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = True
    for i in range(1, N+1):
        for k in range(min(K, 7 * i)+1):
            for t in range(10):
                d = dist[A[i]][t]
                if 0 <= d <= k and dp[i-1][k-d]:
                    dp[i][k] = True
                    break
                    
    if not dp[N][K]:
        return -1
    
    ans = []
    x, y = N, K
    while x > 0:
        s = A[x]
        for t in range(9, -1, -1):
            d = dist[s][t]
            if 0 <= d <= y and dp[x-1][y-d]:
                ans.append(t)
                x -= 1
                y -= d
                break
        
    return ''.join(map(str, ans))
    


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = []
    for i in range(N):
        A.append(str2int(input()))
        
    print(solve(N, K, A))
