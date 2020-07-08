# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    xb, yb, xh, yh = map(int, input().split())
    
    dp = [[0 for _ in range(yb+1)] for _ in range(xb+1)]
    block = [(xh, yh)]
    for dx, dy in zip([1, 2], [2, 1]):
        block.append((xh + dx, yh + dy))
        block.append((xh - dx, yh + dy))
        block.append((xh + dx, yh - dy))
        block.append((xh - dx, yh - dy))
        
    dp[0][0] = 1
    for x in range(xb+1):
        for y in range(yb+1):
            if (x, y) in block:
                continue
            dp[x][y] += dp[x-1][y] if x-1>=0 else 0
            dp[x][y] += dp[x][y-1] if y-1>=0 else 0
            
    print(dp[xb][yb])
    