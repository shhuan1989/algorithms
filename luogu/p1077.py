# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [0] + [int(x) for x in input().split()]
    MOD = 10000071000007
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 1
    
    for i in range(1, N+1):
        for j in range(M+1):
            for k in range(A[i]+1):
                if k > j:
                    break
                dp[i][j] += dp[i-1][j-k]
                dp[i][j] %= 1000007
    
    print(dp[N][M])