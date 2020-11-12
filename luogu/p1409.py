# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/5

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List
from functools import lru_cache

if __name__ == '__main__':
    
    @lru_cache(maxsize=None)
    def dp(n, m, depth):
        # print(n, m)
        if depth > 122:
            return 0
        if m > n:
            return 0
        if n == 1:
            return 1 if m == n else 0
        
        if m == 1:
            return 1/6 + 0.5 * dp(n, n, depth+1)
        
        return 0.5 * dp(n, m-1, depth+1) + 1/3 * dp(n-1, m-1, depth+1)
    
    N, M = map(int, input().split())
    print('{:.9f}'.format(dp(N, M, 1)))
        