# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/21

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
    S = input().strip()
    dp = [0 for _ in range(N+1)]
    combo = 0
    for i in range(1, N+1):
        v = S[i-1]
        if v == 'x':
            dp[i] = dp[i-1]
            combo = 0
        elif v == 'o':
            dp[i] = dp[i-1] + 2 * combo + 1
            combo += 1
        else:
            dp[i] = dp[i-1] + combo + 0.5
            combo = (combo + 1) / 2
    
    # print(dp)
    print('{:.4f}'.format(dp[N]))
        