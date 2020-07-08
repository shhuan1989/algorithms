# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/1

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

MOD = 998244353

def solve(s, t):
    n, m = len(s), len(t)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[n][0] = 1
    
    for i in range(n-1, 0, -1):
        for j in range(m+1):
            if j == 0:
                if i >= m:
                    dp[i][0] = n - i + 1
                elif s[i] == t[i]:
                    dp[i][0] = dp[i+1][0]
            elif j == m:
                dp[i][m] = 2 * dp[i+1][m] % MOD
                if s[i] == t[m-1]:
                    dp[i][m] = (dp[i][m] + dp[i+1][m-1]) % MOD
            else:
                if i + j >= m or s[i] == t[i+j]:
                    dp[i][j] = dp[i+1][j]
                if s[i] == t[j-1]:
                    dp[i][j] = (dp[i][j] + dp[i+1][j-1]) % MOD
                
    ans = dp[1][m]
    for i in range(m):
        if t[i] == s[0]:
            ans = (ans + dp[1][i]) % MOD
    ans *= 2
    ans %= MOD
    
    return ans


if __name__ == '__main__':
    s = input()
    t = input()
    print(solve(s, t))