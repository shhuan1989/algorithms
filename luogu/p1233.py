# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/30

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
    A = [int(x) for x in input().strip().split()]
    LW = []
    for i in range(N):
        LW.append((A[2*i], A[2*i+1]))
    
    
    def lis(a):
        na = len(a)
        dp = [1 for _ in range(na)]
        for i in range(na):
            for j in range(i):
                if a[j] < a[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    # print(LW)
    LW.sort(reverse=True)
    # print([w for l, w in LW])
    ans = lis([w for l, w in LW])
    
    print(ans)