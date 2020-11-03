# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    # sys.stdin = open('P1373_1.in', 'r')
    N, M, K = map(int, input().split())
    A = []
    K += 1
    for _ in range(N):
        row = [int(x) % K for x in input().split()]
        A.append(row)
    
    MOD = 1000000007
    
    dp = [[[[0 for _ in range(2)] for _ in range(K)] for _ in range(M)] for _ in range(N)]
    
    ans = 0
    for r in range(N):
        for c in range(M):
            v = A[r][c]
            dp[r][c][v][0] = 1
            if r - 1 >= 0:
                for k in range(K):
                    dp[r][c][k][0] += dp[r - 1][c][(k - v + K) % K][1]
                    dp[r][c][k][0] %= MOD
                    dp[r][c][k][1] += dp[r - 1][c][(k + v) % K][0]
                    dp[r][c][k][1] %= MOD
            
            if c - 1 >= 0:
                for k in range(K):
                    dp[r][c][k][0] += dp[r][c - 1][(k - v + K) % K][1]
                    dp[r][c][k][0] %= MOD
                    dp[r][c][k][1] += dp[r][c - 1][(k + v) % K][0]
                    dp[r][c][k][1] %= MOD
            
            ans += dp[r][c][0][1]
            # if dp[r][c][0][1] > 0:
            #     print(r, c, dp[r][c][0][1])
            ans %= MOD
    
    print(ans)


