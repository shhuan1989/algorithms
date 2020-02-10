# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/6/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(money):
    ans = money // 100
    money %= 100
    
    if money == 0:
        return ans
    
    dp = [100 for _ in range(money+1)]
    dp[0] = 0
    for i in range(1, money+1):
        for v in [1, 5, 10, 20]:
            if i - v >= 0:
                dp[i] = min(dp[i], dp[i-v]+1)
    
    return ans + dp[money]
    
    
money = int(input())
print(solve(money))