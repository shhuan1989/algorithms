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
    L, R = map(int, input().split())
    
    
    def gets(x):
        y = 0
        while x > 0:
            y += x % 10
            x //= 10
        
        return y
    
    def dfs(curr):
        ans = 0
        for i in range(4):
            x = curr * 10 + i
            if x == 0 or gets(x) * gets(x) != gets(x**2):
                continue
            if L <= x <= R:
                ans += 1
            if x <= R // 10:
                ans += dfs(x)
        return ans
    
    print(dfs(0))