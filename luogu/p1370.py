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
    N = int(input())
    A = [0] + [int(x) for x in input().split()]
    dp = [0 for _ in range(N + 2)]
    dp[N] = 2
    
    MOD = 998244353
    right = {A[N]: N}
    for i in range(N - 1, 0, -1):
        dp[i] = (dp[i + 1] * 2 + 2) % MOD
        if A[i] in right:
            j = right[A[i]]
            dp[i] = (dp[i] + MOD - dp[j + 1] - 1) % MOD
        right[A[i]] = i
        dp[i] %= MOD
    
    # print(dp)
    print(sum(dp) % MOD)