# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    T, M = map(int, input().split())
    A = []
    for i in range(M):
        t, v = map(int, input().split())
        A.append((t, v))
        
    dp = [[0 for _ in range(T+1)] for _ in range(M+1)]
    
    for i in range(1, M+1):
        t, v = A[i-1]
        for cost in range(1, T+1):
            dp[i][cost] = dp[i-1][cost]
            
            if cost - t >= 0:
                dp[i][cost] = max(dp[i][cost], dp[i-1][cost-t] + v)
    
    print(dp[M][T])
    
    