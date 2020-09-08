# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


from functools import lru_cache
if __name__ == '__main__':
    N, R = map(int, input().split())
    
    
    @lru_cache(maxsize=None)
    def ncr(c, r):
        if c < r:
            return 0
        if r == 0 or r == c:
            return 1
        if r > c-r:
            return ncr(c, c-r)
        
        return ncr(c-1, r-1) + ncr(c-1, r)
    
    
    def dfs(index, perm, rest):
        if index >= R:
            if rest == 0:
                x = 1
                s = 0
                for i in range(R-1):
                    x *= ncr(N-s, perm[i])
                    s += perm[i]
                return x
            else:
                return 0
        
        if rest < R - index:
            return 0
        
        ans = 0
        for curr in range(1, rest+1):
            ans += dfs(index+1, perm+[curr], rest-curr)
        
        return ans
        
    print(dfs(0, [], N))