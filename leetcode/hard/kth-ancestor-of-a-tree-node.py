# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/17

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class TreeAncestor:
    
    def __init__(self, n: int, parent: List[int]):
        k = 1
        while 2 ** k <= n:
            k += 1
        
        dp = [[-1 for _ in range(k)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = parent[i]
        
        for x in range(1, k):
            for i in range(n):
                if dp[i][x-1] >= 0:
                    dp[i][x] = dp[dp[i][x-1]][x-1]
        
        self.dp = dp
    
    
    
    def getKthAncestor(self, node: int, k: int) -> int:
        if node < 0:
            return node
        dp = self.dp
        
        i = 0
        while 2 ** i <= k:
            i += 1
        i -= 1
        
        if 2 ** i == k:
            return dp[node][i]
        else:
            return self.getKthAncestor(dp[node][i], k-2**i)
        



if __name__ == '__main__':
    ta = TreeAncestor(7, [-1,0,0,1,1,2,2])
    print(ta.getKthAncestor(3, 1))
    print(ta.getKthAncestor(5, 2))
    print(ta.getKthAncestor(6, 3))
    
    ta = TreeAncestor(5, [-1,0,0,0,3])
    print(ta.getKthAncestor(1, 5))
